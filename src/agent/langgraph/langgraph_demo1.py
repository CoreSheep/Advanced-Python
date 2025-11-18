from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
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

def call_claude(state):
    response = llm_anthropic.invoke(state["messages"])
    return {"messages": [response]}


def build_graph():
    graph = StateGraph(MessagesState)   # create a stategraph
    graph.add_node("llm_anthropic", call_claude)    # add llm node

    graph.add_edge(START, "llm_anthropic")  # add edge to build the graph
    graph.add_edge("llm_anthropic", END)

    return graph.compile()  # compile the graph



def main():
    messages = {
        "messages": [
            SystemMessage(content="You are an expert in langchain and langgraph."),
            HumanMessage(content="Show me a coding demo of how to use langchain and langgraph to call a claude model.")
        ]
    }
   
    app = build_graph()
    res = app.invoke(messages)
    print(f"User: Show me a coding demo of how to use langchain and langgraph to call a claude model.")
    print(f"Claude: {res['messages'][-1].content}")


if __name__ == "__main__":
    main()
