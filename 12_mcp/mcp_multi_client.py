import asyncio
import os
from dotenv import load_dotenv

from langchain_mcp_adapters.client import MultiServerMCPClient

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

load_dotenv()
SMITHERY_API_KEY = os.getenv('SMITHERY_API_KEY')
SMITHERY_API_PROFILE = os.getenv('SMITHERY_API_PROFILE')

# from urllib.parse import urlencode
# params = urlencode({"api_key": SMITHERY_API_KEY, "profile": SMITHERY_API_PROFILE})

# 실제 실행 파트
async def main():
    
    print("Multi Server MCP Client Setting...")
    
    client = MultiServerMCPClient(
        {
            # "math": {
            #     "command": "python",
            #     "args": ["C:/Potenup/LLM-Study/12_mcp/odd_math_server.py"],
            #     "transport": "stdio"
            # },
            # "local_mcp_weather_server": {
            #     "url": "http://localhost:8100/mcp",
            #     "transport": "streamable_http"
            # },
            # "remote_mcp_weather_server": {
            #     "url": f"https://server.smithery.ai/@isdaniel/mcp_weather_server/mcp?{params}",
            #     "transport": "streamable_http"
            # },
            # "remote_mcp_weather_server": {
            #     "transport": "stdio",
            #     "command": "npx",
            #     "args": [
            #         "-y",
            #         "@smithery/cli@latest",
            #         "run",
            #         "@isdaniel/mcp_weather_server",
            #         "--key",
            #         SMITHERY_API_KEY,
            #         "--profile",
            #         SMITHERY_API_PROFILE
            #     ]
            # },
            "exa_search_mcp": {
                "transport": "stdio",
                "command": "npx",
                "args": [
                    "-y",
                    "@smithery/cli@latest",
                    "run",
                    "exa",
                    "--key",
                    SMITHERY_API_KEY,
                    "--profile",
                    SMITHERY_API_PROFILE
                ]
            },
            "brave_search_mcp": {
                "transport": "stdio",
                "command": "npx",
                "args": [
                    "-y",
                    "@smithery/cli@latest",
                    "run",
                    "@JonyanDunh/brave-search-mcp",
                    "--key",
                    SMITHERY_API_KEY,
                    "--profile",
                    SMITHERY_API_PROFILE
                ]
            },
            "perplexity-search": {
                "transport": "stdio",
                "command": "npx",
                "args": [
                    "-y",
                    "@smithery/cli@latest",
                    "run",
                    "@arjunkmrm/perplexity-search",
                    "--key",
                    SMITHERY_API_KEY,
                    "--profile",
                    SMITHERY_API_PROFILE
                ]
            }
        }
    )

    tools = await client.get_tools()
    
    for tool in tools:
        print(tool.name)
    
    print("=" * 30)

    model = ChatOpenAI(
        model = "gpt-4.1-mini",
        temperature=0
    )
    
    agent_executor = create_react_agent(model=model, tools=tools)

    # # 더하기 도구
    # response = await agent_executor.ainvoke(
    #     {"messages" : [system_message, HumanMessage(content="1+2 는?")]}
    # )
    # print("답변: ", response["messages"][-1].content)

    # # 곱하기 도구
    # response = await agent_executor.ainvoke(
    #     {"messages" : [system_message, HumanMessage(content="2*3 는?")]}
    # )
    # print("답변: ", response["messages"][-1].content)

    response = await agent_executor.ainvoke(
        {"messages" : [HumanMessage(content="삼성전자의 ai 사업 도입 현황에 대해서 조사해줘")]}
    )
    print("답변: ", response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())