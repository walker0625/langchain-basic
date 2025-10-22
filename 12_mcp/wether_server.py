from mcp.server.fastmcp import FastMCP

# 외부에서 접속할 수 있도록 end-point 제공
mcp = FastMCP(
    "Weather",
    host="0.0.0.0",
    port=8100
    )

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location"""
    return "석촌역의 날씨는 맑음입니다"

if __name__ == '__main__':
    mcp.run(transport='streamable-http') # 클라이언트는 streamable_http이라고 적어야 동작함