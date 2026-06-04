from typing import Any
from mcp.server.fastmcp import FastMCP
import requests
import os

# Initialize FastMCP server
mcp = FastMCP("weather", dependencies=["requests"])


@mcp.tool()
def get_weather(city: str) -> dict[str, Any]:
    """Get current weather for a location"""
    # Using https://openweathermap.org/current#geo

    #api_key = os.getenv("OPENWEATHER_API_KEY")
    api_key = "c8ddf7f5f752db3c0c99b9d7d80c1990"
    
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
