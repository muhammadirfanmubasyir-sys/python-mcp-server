VENV
====
D:\PROJECTS\python\mcp-python-weather>python -m venv .venv

D:\PROJECTS\python\mcp-python-weather>.venv\Scripts\activate

(.venv) D:\PROJECTS\python\mcp-python-weather>pip install -r requirements.txt
 

Python MCP Server SDK:  https://github.com/modelcontextprotocol/python-sdk
Open Weather API Key: https://home.openweathermap.org/api_keys

pip install "mcp[cli]"
pip install requests
pip install uv 

INSTALL uv in windows (https://docs.astral.sh/uv/)
==================================================
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"

RESULT: [uv.exe, uvw.exe, uvx.exe] IN C:\Users\LENOVO L13 YOGA\.local\bin
========================
RUN
===
mcp dev src/mcp_weather.py

uv run mcp dev src/mcp_weather.py
========================
FROM CMD OUTSIDE VS CODE
===============================================================================
D:\PROJECTS\python\mcp-python-weather>python -m venv .venv
D:\PROJECTS\python\mcp-python-weather>.venv\Scripts\activate

(.venv) D:\PROJECTS\python\mcp-python-weather>uv run mcp dev src/mcp_weather.py
Starting MCP inspector...
⚙️ Proxy server listening on localhost:6277
🔑 Session token: 7fabc3796e69a1b84d23a1684f48f5e810501e0065db116525160d74f676846c
   Use this token to authenticate requests or set DANGEROUSLY_OMIT_AUTH=true to disable auth

🚀 MCP Inspector is up and running at:
   http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=7fabc3796e69a1b84d23a1684f48f5e810501e0065db116525160d74f676846c

🌐 Opening browser...
New STDIO connection request
(see mcp-weather.png)

{
location:
"jakarta"

temperature:
33.43

description:
"Clouds"

}