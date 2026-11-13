# test-mcp-server

Testing out FastMCP.

- `my_server.py` — FastMCP server (`greet` tool). Run with HTTP transport:
  `uv run fastmcp run my_server.py:mcp --transport http --port 8000`
- `my_client.py` — example client that calls the server at `http://localhost:8000/mcp`.
