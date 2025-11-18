from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, MessagesState, START, END

# 1. Create a llm
llm_anthropic = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    temperature=0.7,
    max_tokens=1024
)

llm_openai = ChatOpenAI(
    model="gpt-4o",
    temperature=0.8,
    max_tokens=1024*64
)

# 2. call the llm based on the messages
def call_claude(state):
    response = llm_anthropic.invoke(state["messages"])
    return {"messages": [response]}

def call_gpt(state):
    response = llm_openai.invoke(state["messages"])
    return {"messages": [response]}

# 3. build a graph for an agent
def build_graph():
    graph = StateGraph(MessagesState)   # create a stategraph
    graph.add_node("llm_anthropic", call_claude)    # add llm node: name, node(func)

    graph.add_edge(START, "llm_anthropic")  # add edge to build the graph
    graph.add_edge("llm_anthropic", END)

    return graph.compile()  # compile the graph


# 4. run the agent to call llm via state graph
def main():
    # Read pdf document and encode to base64
    import base64
    from pathlib import Path

    pdf_path = Path.home() / "Documents/project/Advanced-Python/test/pdf/DeepSeek_OCR_paper_page_1_demo.pdf"

    with open(pdf_path, "rb") as pdf_file:
        pdf_base64_deepseek_orc_page_1 = base64.b64encode(pdf_file.read()).decode("utf-8")

    messages = {
        "messages": [
            SystemMessage(content="You are an expert in document analysis."),
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
   
    app = build_graph()
    res = app.invoke(messages)
    print(f"User: Summarize the key points from this PDF.")
    print(f"Claude: {res['messages'][-1].content}")


if __name__ == "__main__":
    main()