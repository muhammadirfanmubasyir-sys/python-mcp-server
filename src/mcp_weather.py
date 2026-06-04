from typing import Any
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import requests
import os

# Initialize FastMCP server
mcp = FastMCP("weather", dependencies=["requests"])

@mcp.tool()
def get_weather(city: str) -> dict[str, Any]:
    """Get current weather for a location"""
    # Using https://openweathermap.org/current#geo

    # Load environment variables. Assumes that project contains .env file with API keys
    load_dotenv()
    #---- Set OpenAI API key 
    # Change environment variable name from "OPENAI_API_KEY" to the name given in 
    # your .env file.

    api_key = os.getenv("OPEN_WEATHER_API_KEY")
    print(f"OPEN_WEATHER_API_KEY : {api_key}")
    
    # Get the latitude and longitude of the city.
    geo_url = (
        f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    )
    geo_data = requests.get(geo_url).json()
    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

    # Get the current weather for the city.
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    weather_data = requests.get(weather_url).json()
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["main"]

    return {
        "location": city,
        "temperature": temperature,
        "description": description,
    }


if __name__ == "__main__":
    mcp.run()
