# Copyright (c) Microsoft. All rights reserved.

"""Sample multi-step workflow using Agent Framework WorkflowBuilder.

This demonstrates a linear pipeline: Researcher → Summarizer → Formatter.
Customize or replace with your own workflow logic.
"""

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient


def build_workflow_agent(client: FoundryChatClient) -> Agent:
    """Build a sample multi-agent workflow and return it as a single agent.

    The workflow chains three agents:
    1. Researcher - gathers information
    2. Summarizer - condenses the research
    3. Formatter  - produces a polished final output
    """
    pass
