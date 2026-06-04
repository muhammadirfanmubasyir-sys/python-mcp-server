# Python Simple MCP Tutorial

This project demonstrates a simple weather server using the `mcp` library. It exposes a tool that returns real weather data for a given location using the OpenWeatherMap API.

MCP (Model Context Protocol) is a universal standard that enables AI agents (LLMs) to access data, tools and services. In this case, we will build a "server" that fetches real weather data for an LLM to interact with.

## Setting Up

This project uses `uv` for package management. Go here for [instructions on how to install uv](https://docs.astral.sh/uv/getting-started/installation/).

```sh
uv venv
```

Activate the virtual environment:

```sh
source .venv/bin/activate
```

Install dependencies.

```sh
uv sync
```

## API Key Setup

This project uses the OpenWeatherMap API to fetch real weather data. You'll need to:

1. Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your API key from the dashboard
3. Set the environment variable:

```sh
export OPENWEATHER_API_KEY=your_api_key_here
```

## How To Run

To test the weather MCP server, execute the following command:

```sh
mcp dev src/mcp_weather.py
```

Then wait a while for to load, and click the link to "open inspector with token pre-filled". This will give you a UI you can use to test the MCP server right in your browser.

## Deep Dive

How does our AI agent know how to use this MCP tool? Well, in short, it gets serialized into a JSON schema.

FastMCP automatically registers the get_weather function as a tool, extracting the schema from the function signature and docstring.

```json
{
  "name": "get_weather",
  "description": "Get current weather for a location",
  "inputSchema": {
    "type": "object",
    "properties": {
      "location": { "type": "string" }
    },
    "required": ["location"]
  }
}
```

Then, the AI agent that we use (e.g. Claude Desktop, Cursor, or our own implementation) will know about these tools and know how to invoke them via prompt engineering. It will be turned into a prompt similar to this:

```text
You have access to these tools:
- get_weather: Get current weather for a location

To use: <tool_call>{"name": "get_weather", "parameters": {"location": "Tokyo"}}</tool_call>
```

## MCP Clients: Interacting with MCP Servers

If you want your AI agent to interact with MCP servers, you need an MCP client. Some UI tools (Claude Desktop and Cursor) have this built-in for you already. But you can do this programmatically via code as well.

What it usually boils down to is declaring your MCP server in a config file with instructions on how to access it. In the case of [Claude Desktop](https://claude.ai/download), it looks something like this:

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": ["run", "[...]", "/[PATH_TO_PROJECT]/src/mcp_weather.py"],
      "env": {
        "OPENWEATHER_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

(This example is simplified — refer to https://modelcontextprotocol.io/quickstart/user for more details)

And this will live inside the `claude_desktop_config.json` file which you can access via the Developer settings. But you can also take a shortcut and install it right away by running this command (which will just create the entry in the config file for you):

```sh
mcp install server.py
```

You will need to restart Claude desktop to see the tool in your "search and tools" section.

For options on implementing MCP clients in code:

- https://modelcontextprotocol.io/quickstart/client
- https://github.com/mcp-use/mcp-use

## Using Third-Party MCP Servers (Google Sheets Example)

If your goal is to build powerful and useful AI agents, then you're probably more interested in using existing MCP servers rather than creating your own. There's a huge list of available servers here from both first-party and third-party developers: https://github.com/modelcontextprotocol/servers

It's also really easy to use in Claude Desktop. For this example, let's try integrating Google Sheets access (not just to read, but to create and modify).

- Follow the instructions on https://github.com/xing5/mcp-google-sheets.
- Set up Google access:
  - Create a Google Cloud account and project.
  - Create a service role and save the JSON to disk somewhere.
  - Create a folder in Google drive, and share its permission to the service account email.
  - Enable Drive and Sheets API in the GCP project.

Then set up the MCP server in Claude desktop (replace the environment variables):

```json
{
  "google-sheets": {
    "command": "uvx",
    "args": ["mcp-google-sheets@latest"],
    "env": {
      "SERVICE_ACCOUNT_PATH": "[...]/keys/service-account-xxx.json",
      "DRIVE_FOLDER_ID": "XXX"
    }
  }
}
```

This will now make Google Sheets available as a tool. The `uvx` command also lets you run it without having to clone the Github project or install any dependencies/environments.

## Setting Up uv and uvx commands

On MacOS/Linux, Claude desktop might complain that it can't find `uv` or `uvx` when you try to start the server. You might just have to create a symlink to the binary.

```sh
sudo ln -s ~/.local/bin/uv /usr/local/bin/uv
sudo ln -s ~/.local/bin/uvx /usr/local/bin/uvx
```
