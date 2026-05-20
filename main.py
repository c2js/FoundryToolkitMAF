# Copyright (c) Microsoft. All rights reserved.

"""Main entry point for the agent application.

Supports two hosting modes (selectable via --mode flag):
  - responses  : OpenAI Responses API (default) — for Foundry Hosted Agent
  - invocations: Azure AI Invocations API — for Foundry Hosted Agent

Run locally:
  python main.py --mode responses
  python main.py --mode invocations

For Foundry deployment the mode is typically 'responses' (default).
"""

import argparse
import asyncio
import os

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from agent_framework_foundry_hosting import InvocationsHostServer, ResponsesHostServer
from azure.identity import AzureCliCredential
from dotenv import load_dotenv

from tools import get_current_time

# Load environment variables from .env file (no-op when injected by Foundry)
load_dotenv()


def _get_env(name: str) -> str:
    """Get environment variable with MY_ prefix fallback for local dev.

    In hosted Foundry, the platform injects vars like FOUNDRY_PROJECT_ENDPOINT.
    For local development, use MY_FOUNDRY_PROJECT_ENDPOINT in your .env file.
    """
    value = os.environ.get(name) or os.environ.get(f"MY_{name}")
    if not value:
        raise EnvironmentError(
            f"Environment variable '{name}' (or 'MY_{name}') is not set. "
            f"Please configure it in your .env file."
        )
    return value


def create_agent() -> Agent:
    """Create and return the main agent instance."""
    credential = AzureCliCredential()

    client = FoundryChatClient(
        project_endpoint=_get_env("FOUNDRY_PROJECT_ENDPOINT"),
        model=_get_env("AZURE_AI_MODEL_DEPLOYMENT_NAME"),
        credential=credential,
    )

    agent = Agent(
        client=client,
        instructions="You are a helpful assistant. Keep your answers brief and accurate.",
        tools=[get_current_time],
        # History managed by hosting infrastructure for Foundry deployment.
        # https://developers.openai.com/api/reference/resources/responses/methods/create
        default_options={"store": False},
    )

    return agent


async def run_responses(agent: Agent) -> None:
    """Host the agent via the OpenAI Responses API protocol."""
    server = ResponsesHostServer(agent)
    await server.run_async()


def run_invocations(agent: Agent) -> None:
    """Host the agent via the Azure AI Invocations API protocol."""
    server = InvocationsHostServer(agent)
    server.run()


def main() -> None:
    parser = argparse.ArgumentParser(description="Agent Host")
    parser.add_argument(
        "--mode",
        choices=["responses", "invocations"],
        default="responses",
        help="Hosting protocol: 'responses' (OpenAI Responses API) or 'invocations' (Azure AI Invocations API)",
    )
    args = parser.parse_args()

    agent = create_agent()

    if args.mode == "responses":
        asyncio.run(run_responses(agent))
    else:
        run_invocations(agent)


if __name__ == "__main__":
    main()
