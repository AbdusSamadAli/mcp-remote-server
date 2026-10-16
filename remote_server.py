from fastmcp import FastMCP

mcp = FastMCP("remote calculator server")

@mcp.tool()
def add(a:float, b:float) -> float:
    """add 2 numbers"""
    return a+b

@mcp.tool()
def multiply(a:float, b:float) -> float:
    """multiply 2 numbers"""
    return a*b

@mcp.tool()
def get_server_info() -> str:
    """return information about this server"""
    return "remote calculator mcp server is running"

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )