from dataclasses import dataclass, field
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, MessagesState, START, END
from typing import TypedDict, List, Any

# 1. Create a llm
llm_anthropic = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    temperature=0.7,
    max_tokens=1024*4
)

llm_openai = ChatOpenAI(
    model="gpt-4o",
    temperature=0.8,
    max_tokens=1024*4
)


# 2. Define a custom state to handle both image and PDF messages
class MultiModalState(TypedDict):
    """A custom state to handle both image and PDF messages.

    Use list types for the incoming message sequences (e.g. a list of
    `SystemMessage`/`HumanMessage` objects) and optional strings for
    extracted/derived content. Fields use sensible defaults so the
    dataclass can be instantiated without arguments.
    """
    image_messages: List[Any] 
    pdf_messages: List[Any]
    image_content: str
    pdf_content: str
    final_summary: str
    


# 3. call the llm based on the messages
def call_claude(state):
    response = llm_anthropic.invoke(state["messages"])
    return {"messages": [response]}

def call_gpt(state):
    response = llm_openai.invoke(state["messages"])
    return {"messages": [response]}


def extract_image(state):
    """Extract image content from the image message"""
    response = llm_openai.invoke(state["image_messages"])
    return {"image_content": response.content}

def summarize_pdf(state):
    """Summarize the PDF content from the document message"""
    response = llm_anthropic.invoke(state["pdf_messages"])
    return {"pdf_content": response.content}

def process_image_and_pdf(state):
    """Process both image and PDF content"""
    combined_content = f"Image Content: {state['image_content']}\n\nPDF Content: {state['pdf_content']}"
    response = llm_openai.invoke([SystemMessage(content="You are an expert in analyzing images and documents."),
                                  HumanMessage(content=f"Combine and analyze the following content:\n"\
                                               f"{combined_content}" \
                                               "Then provide a combined summary combining insights from both." \
                                               )])
    return {"final_summary": response.content}



# 4. build a graph for an agent
def build_graph():
    graph = StateGraph(MultiModalState)   # create a stategraph

    # START -> image_extractor -> 
    #       -> pdf_extractor ->  combined_summerizor -> END
    graph.add_node("image_extractor", extract_image)   
    graph.add_node("pdf_extractor", summarize_pdf)
    graph.add_node("combined_summerizor", process_image_and_pdf)

    graph.add_edge(START, "image_extractor") 
    graph.add_edge(START, "pdf_extractor") 

    graph.add_edge("image_extractor", "combined_summerizor")
    graph.add_edge("pdf_extractor", "combined_summerizor")

    graph.add_edge("combined_summerizor", END)

    return graph.compile()  # compile the graph


# 5. run the agent to call llm via state graph
def main():
    # Read pdf document and encode to base64
    import base64
    from pathlib import Path

    pdf_path = Path.home() / "Documents/project/Advanced-Python/test/pdf/DeepSeek_OCR_paper_page_1_demo.pdf"
    img_path = Path.home() / "Documents/project/Advanced-Python/test/image/gemini_3_deepthink.png"


    with open(pdf_path, "rb") as pdf_file:
        pdf_base64_deepseek_orc_page_1 = base64.b64encode(pdf_file.read()).decode("utf-8")

    with open(img_path, "rb") as image_file:
        image_base64_gemini_3_deepthink = base64.b64encode(image_file.read()).decode("utf-8")

    pdf_messages = {
        "pdf_messages": [
            SystemMessage(content="You are an expert in pdf document analysis."),
            HumanMessage(
                content=[
                    {"type": "text", "text": "Summarize the key points from this PDF."},
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data" : pdf_base64_deepseek_orc_page_1
                    }
                }
                ]
            )
        ]
    }

    image_messages = {
        "image_messages": [
            SystemMessage(content="You are an expert in image analysis."),
            HumanMessage(
                content=[
                    {"type": "text", "text": "Extract the insights from the image."},
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data" : image_base64_gemini_3_deepthink
                    }
                }
                ]
            )
        ]
    }

    init_messages = {
        "image_messages": image_messages["image_messages"],
        "pdf_messages": pdf_messages["pdf_messages"]
    }
   
    app = build_graph()
    res = app.invoke(init_messages)
    print(f"User: Summarize the key points from uploaded image and PDF.")
    print(f"Claude: {res['final_summary']}")


if __name__ == "__main__":
    main()