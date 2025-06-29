from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two integers"""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two integers"""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> int:
    """Divide two integers"""
    return a // b

@mcp.tool()
def power(a: int, b: int) -> int:
    """Raise a to the power of b"""
    return a ** b


if __name__ == "__main__":
    mcp.run(transport="stdio") 