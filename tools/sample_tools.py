# Copyright (c) Microsoft. All rights reserved.

"""Sample tool definitions for the agent.

Add your custom tools here. Each tool is a function decorated with @tool
from agent_framework. Tools are automatically exposed to the LLM.
"""

from datetime import datetime, timezone

from agent_framework import tool


@tool(approval_mode="never_require")
def get_current_time() -> str:
    """Get the current UTC time."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
