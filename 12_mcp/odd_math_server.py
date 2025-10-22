from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Math')

@mcp.tool()
def add(x: int, y: int) -> int:
    """Add two numbers + 1"""
    return x + y + 1

@mcp.tool()
def multiply(x: int, y: int) -> int:
    """Multiply two numbers * 2"""
    return x * y * 2

if __name__ == '__main__':
    mcp.run(transport='stdio') # local 방식