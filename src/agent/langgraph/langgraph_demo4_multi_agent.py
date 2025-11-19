import base64
from pathlib import Path
from typing import TypedDict, List, Any, Dict

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from langgraph.graph import StateGraph, START, END

# 1. Create LLM instances
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


# 2. Define a custom state
class MultiModalState(TypedDict):
    """
    A custom state to handle both image and PDF messages.

    Attributes:
        image_messages: List of messages related to image processing.
        pdf_messages: List of messages related to PDF processing.
        image_content: Extracted content from the image.
        pdf_content: Summarized content from the PDF.
        final_summary: The final combined summary.
    """
    image_messages: List[BaseMessage]
    pdf_messages: List[BaseMessage]
    image_content: str
    pdf_content: str
    final_summary: str


# 3. Define node functions
def extract_image(state: MultiModalState) -> Dict[str, str]:
    """
    Extract image content from the image message using OpenAI.

    Args:
        state: The current graph state containing image_messages.

    Returns:
        A dictionary with the extracted image_content.
    """
    response = llm_openai.invoke(state["image_messages"])
    return {"image_content": response.content}


def summarize_pdf(state: MultiModalState) -> Dict[str, str]:
    """
    Summarize the PDF content from the document message using Anthropic.

    Args:
        state: The current graph state containing pdf_messages.

    Returns:
        A dictionary with the summarized pdf_content.
    """
    response = llm_anthropic.invoke(state["pdf_messages"])
    return {"pdf_content": response.content}


def process_image_and_pdf(state: MultiModalState) -> Dict[str, str]:
    """
    Combine and analyze both image and PDF content to generate a final summary.

    Args:
        state: The current graph state containing image_content and pdf_content.

    Returns:
        A dictionary with the final_summary.
    """
    combined_content = f"Image Content: {state['image_content']}\n\nPDF Content: {state['pdf_content']}"
    response = llm_openai.invoke([
        SystemMessage(content="You are an expert in analyzing images and documents."),
        HumanMessage(content=(
            f"Combine and analyze the following content:\n{combined_content}\n"
            "Then provide a combined summary combining insights from both."
        ))
    ])
    return {"final_summary": response.content}


# 4. Build the graph
def build_graph() -> StateGraph:
    """
    Build and compile the state graph for the multi-modal agent.

    Returns:
        The compiled StateGraph.
    """
    graph = StateGraph(MultiModalState)

    # Add nodes
    graph.add_node("image_extractor", extract_image)
    graph.add_node("pdf_extractor", summarize_pdf)
    graph.add_node("combined_summerizor", process_image_and_pdf)

    # Define edges
    graph.add_edge(START, "image_extractor")
    graph.add_edge(START, "pdf_extractor")

    graph.add_edge("image_extractor", "combined_summerizor")
    graph.add_edge("pdf_extractor", "combined_summerizor")

    graph.add_edge("combined_summerizor", END)

    return graph.compile()


# 5. Helper functions for main execution
def encode_file_to_base64(file_path: Path) -> str:
    """
    Read a file and encode its content to a base64 string.

    Args:
        file_path: Path to the file.

    Returns:
        Base64 encoded string of the file content.
    """
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")


def create_pdf_messages(pdf_base64: str) -> Dict[str, List[BaseMessage]]:
    """Create the message structure for PDF analysis."""
    return {
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
                            "data": pdf_base64
                        }
                    }
                ]
            )
        ]
    }


def create_image_messages(image_base64: str) -> Dict[str, List[BaseMessage]]:
    """Create the message structure for image analysis."""
    return {
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
                            "data": image_base64
                        }
                    }
                ]
            )
        ]
    }


def main():
    """Main execution function."""
    # Define paths
    base_path = Path.home() / "Documents/project/Advanced-Python/test"
    pdf_path = base_path / "pdf/DeepSeek_OCR_paper_page_1_demo.pdf"
    img_path = base_path / "image/gemini_3_deepthink.png"

    # Encode files
    try:
        pdf_base64 = encode_file_to_base64(pdf_path)
        image_base64 = encode_file_to_base64(img_path)
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        return

    # Create messages
    pdf_messages = create_pdf_messages(pdf_base64)
    image_messages = create_image_messages(image_base64)

    init_messages = {
        "image_messages": image_messages["image_messages"],
        "pdf_messages": pdf_messages["pdf_messages"]
    }

    # Run graph
    app = build_graph()
    print("Running multi-modal agent...")
    res = app.invoke(init_messages)
    
    print(f"\nUser: Summarize the key points from uploaded image and PDF.")
    print(f"Claude: {res['final_summary']}")


if __name__ == "__main__":
    main()