# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "mcp",
#     "httpx",
# ]
# ///

import os
import httpx
from mcp.server.fastmcp import FastMCP

# This file implements the open-source MCP proxy server for Mdtero.
# It can be used by Claude Code, Cursor, or OpenClaw.
# Users must provide MDTERO_API_KEY environment variable.

BASE_URL = os.environ.get("MDTERO_API_URL", "https://api.mdtero.com")
API_KEY = os.environ.get("MDTERO_API_KEY")

mcp = FastMCP("Mdtero", dependencies=["httpx"])

@mcp.tool()
async def parse_paper(url_or_doi: str) -> str:
    """
    Parse a scientific paper (Elsevier DOI or URL) into a clean Markdown bundle.
    
    Args:
        url_or_doi: The DOI or URL of the paper to parse.
    """
    if not API_KEY:
        return "Error: MDTERO_API_KEY environment variable is not set. Please generate one at https://mdtero.com/account"
        
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{BASE_URL}/tasks/parse",
                headers={"ApiKey": API_KEY},
                json={"input": url_or_doi},
                timeout=60.0
            )
            if response.status_code == 200:
                data = response.json()
                task_id = data.get("task_id")
                return f"Successfully initiated parse task. Task ID: {task_id}\nCheck your Mdtero dashboard to download the parsed artifacts."
            else:
                return f"Failed to parse paper: {response.text}"
        except Exception as e:
            return f"Error connecting to Mdtero API: {str(e)}"

@mcp.tool()
async def get_task_status(task_id: str) -> str:
    """
    Check the status and get artifacts of a parsed task.
    
    Args:
        task_id: The ID of the task to check (returned by parse_paper).
    """
    if not API_KEY:
        return "Error: MDTERO_API_KEY environment variable is not set."
        
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{BASE_URL}/tasks/{task_id}",
                headers={"ApiKey": API_KEY},
            )
            if response.status_code == 200:
                data = response.json()
                return f"Task Status: {data.get('status')}\nResults: {data.get('result', 'None yet')}"
            else:
                return f"Failed to get task status: {response.text}"
        except Exception as e:
            return f"Error connecting to Mdtero API: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport='stdio')
