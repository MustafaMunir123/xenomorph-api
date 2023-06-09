import requests
import os
from xenomorph_api.apps.tracking.constants import CITY_HOTELS
from dotenv import load_dotenv

load_dotenv("config/.env")

X_RAPIDAPI_WEATHER_KEY = os.getenv("X_RAPIDAPI_WEATHER_KEY")
X_RAPIDAPI_NEWS_KEY = os.getenv("X_RAPIDAPI_NEWS_KEY")


class TrackingService:
    @staticmethod
    def get_aggregated_weather(city):
        url = "https://open-weather13.p.rapidapi.com/city/" + city
        headers = {
            "X-RapidAPI-Key": X_RAPIDAPI_WEATHER_KEY,
            "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        weather_data = response.json()
        return {"description": weather_data["weather"][0]["description"],
                "temp": weather_data["main"]["temp"],
                "humidity": weather_data["main"]["humidity"],
                "wind_speed": weather_data["wind"]["speed"]}

    @staticmethod
    def get_aggregated_hotels(city):
        if city in CITY_HOTELS.keys():
            return CITY_HOTELS[city]

    @staticmethod
    def get_aggregated_news(city):
        url = "https://bing-news-search1.p.rapidapi.com/news/search"
        query = city + ", Pakistan"
        count = 4
        headers = {
            "X-BingApis-SDK": "true",
            "X-Search-Location": city,
            "X-RapidAPI-Key": X_RAPIDAPI_NEWS_KEY,
            "X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
        }
        params = {
            "q": query,
            "count": count,
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        articles = data.get("value", [])
        news_list = []
        for article in articles:
            news_dict = {"name": article["name"], "description": article["description"],
                         "article_url": article["url"], "source": article["provider"][0]["name"]}
            if "image" in article:
                news_dict["image"] = article["image"]["thumbnail"]["contentUrl"]
            news_list.append(news_dict)
        return news_list
