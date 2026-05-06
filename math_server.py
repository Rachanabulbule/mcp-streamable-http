from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings


# mcp = FastMCP(name="MathServer", stateless_http=True)

mcp = FastMCP(
    "MathServer",
    stateless_http=True,
    json_response=True,
    transport_security=TransportSecuritySettings(
    enable_dns_rebinding_protection=True,
    allowed_hosts=["localhost:*", "127.0.0.1:*"],
    allowed_origins=["http://localhost:*"]
    )
    # TransportSecuritySettings(
    #     enable_dns_rebinding_protection=False
    # )
)

@mcp.tool(description="Adds two to a number")
def add_two(n: int) -> int:
    return n + 2