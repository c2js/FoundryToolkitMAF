* Implement both the Responses API and InvokeAPI.
* Always use the latest Microsoft Agent Framework.
* Ensure the generated code can run locally in VS Code with Agent Inspector and is also ready for deployment on Foundry Hosted Agent.
* For any officially defined environment variables that start with `FOUNDRY_` or `AGENT_`, add a prefix of `MY_` (e.g., `MY_FOUNDRY_AI_PROJECT`). The `FOUNDRY_` or `AGENT_` prefixes are reserved for the hosted agent environment.
* Separate tool and workflow implementations from the main application files. If the task is complex, organize them into dedicated folders for better maintainability.
