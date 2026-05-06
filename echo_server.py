from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

# mcp = FastMCP(name="EchoServer", stateless_http=True)

mcp = FastMCP(
    "EchoServer",
    stateless_http=True,
    json_response=True,
    transport_security=TransportSecuritySettings(
    enable_dns_rebinding_protection=True,
    allowed_hosts=["localhost:*", "127.0.0.1:*"],
    allowed_origins=["http://localhost:*"]
    )
    # TransportSecuritySettings(
    #     enable_dns_rebinding_protection=False  # for local dev / inspector
    # )
)

@mcp.tool(description="A simple echo tool")
def echo(message: str) -> str:
    return f"Echo: {message}"