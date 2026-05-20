# foundrytoolkitmaf — Agent Framework Starter

A skeleton template for building AI agents and workflows with the **Microsoft Agent Framework (MAF)**, deployable to **Microsoft Foundry** as a Hosted Agent. Clone this repo and fill in your own tools, workflows, and environment configuration.

## Features

- **Responses API** — OpenAI-compatible Responses protocol (`ResponsesHostServer`)
- **Invocations API** — Azure AI Invocations protocol (`InvocationsHostServer`)
- **Separate tool definitions** — `tools/` folder for custom tool functions
- **Separate workflow code** — `workflows/` folder for multi-agent orchestration
- **VS Code debugging** — Pre-configured `launch.json` / `tasks.json` with AI Toolkit Agent Inspector
- **Foundry-ready Dockerfile** — Container image for deployment

## Quick Start

### 1. Clone & setup environment

```bash
git clone <this-repo-url>
cd foundrytoolkitmaf
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

```bash
cp .env.sample .env
# Edit .env with your Foundry project endpoint and model deployment name
```

### 4. Run locally

```bash
# Responses API mode (default)
python main.py --mode responses

# Invocations API mode
python main.py --mode invocations
```

### 5. Debug with AI Toolkit Agent Inspector

Press **F5** in VS Code → select **"Debug Agent (HTTP Server + Inspector)"**.

## Project Structure

```
├── main.py                  # Entry point (supports both Responses & Invocations API)
├── tools/                   # Custom tool definitions
│   ├── __init__.py
│   └── sample_tools.py     # get_weather, get_current_time (replace with your tools)
├── workflows/               # Multi-agent workflow definitions
│   ├── __init__.py
│   └── sample_workflow.py   # Researcher → Summarizer → Formatter pipeline
├── .env.sample              # Template env file (copy to .env)
├── .gitignore
├── requirements.txt         # Python dependencies
├── Dockerfile               # For Foundry hosted deployment
├── Agents.md                # Agent development guidelines
└── .vscode/
    ├── launch.json          # Debug configurations
    └── tasks.json           # Task definitions
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `MY_FOUNDRY_PROJECT_ENDPOINT` | Your Foundry project endpoint (local dev) |
| `MY_AZURE_AI_MODEL_DEPLOYMENT_NAME` | Model deployment name, e.g. `gpt-4o` |

> **Note:** The `MY_` prefix is for local development. In Foundry Hosted Agent, the platform injects `FOUNDRY_PROJECT_ENDPOINT` and `AZURE_AI_MODEL_DEPLOYMENT_NAME` automatically. The code handles both.

## Adding Tools

1. Create a new file in `tools/` or add functions to `tools/sample_tools.py`
2. Decorate with `@tool(approval_mode="never_require")`
3. Import and add to the `tools=[]` list in `main.py`

## Adding Workflows

1. Create a new file in `workflows/`
2. Use `WorkflowBuilder` + `AgentExecutor` to chain agents
3. Call `.as_agent()` to get a single agent for hosting

See `workflows/sample_workflow.py` for an example.

## Deployment to Foundry

The included `Dockerfile` follows the Foundry Hosted Agent container spec (port 8088). Deploy via Microsoft Foundry portal or CLI.

## Next Steps

- **Debug / F5** — Quickly test locally with Agent Inspector
- **Add tracing** — Integrate OpenTelemetry for observability
- **Deploy** — `Deploy Agent to Foundry` when ready for production
