import pyautogui
import requests
import http.client
import urllib.parse  # For URL encoding
import re  # For regex parsing
from gpt_api_call import call_gpt
import pprint
import json
import os
#install python-dotenv (pip install)
# from dotenv import load_dotenv
import base64
#install requests (pip install)
from requests import post, get
import json

# Define headers for the Streaming Availability API
STREAMING_API_HEADERS = {
    'x-rapidapi-key': "955c435d11msh91de3c80eedefb7p17a38bjsnea85402fba7d",
    'x-rapidapi-host': "streaming-availability.p.rapidapi.com"
}
COUNTRY_CODE = "ca"  # Example country code, update as needed


def get_streaming_availability(title):
    """Fetches streaming availability for a given show or movie title."""
    try:
        encoded_title = urllib.parse.quote(title)  # Safely encode the title
        conn = http.client.HTTPSConnection("streaming-availability.p.rapidapi.com")
        conn.request("GET", f"/shows/search/title?title={encoded_title}&country={COUNTRY_CODE}&output_language=en", headers=STREAMING_API_HEADERS)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
    except Exception as e:
        print(f"An error occurred while fetching streaming info: {e}")
        return None



def pause_music():
    """Pauses the music."""
    pyautogui.press("playpause")


def play_music():
    """Plays the music."""
    pyautogui.press("playpause")


def next_song():
    """Plays the next song."""
    pyautogui.press("nexttrack")


def previous_song():
    """Plays the previous song."""
    pyautogui.press("prevtrack")


def play_tv_show(tv_show_name):
    """Handles the request to play a TV show by fetching its streaming availability."""
    print(f"Fetching streaming availability for the TV show: {tv_show_name}")
    streaming_info = get_streaming_availability(tv_show_name)
    print(f"Streaming info for '{tv_show_name}': {streaming_info}")
    return (streaming_info)


def play_movie(movie_name):
    """Handles the request to play a movie by fetching its streaming availability."""
    print(f"Fetching streaming availability for the movie: {movie_name}")
    streaming_info = get_streaming_availability(movie_name)
    print(f"Streaming info for '{movie_name}': ")

    pprint.PrettyPrinter(streaming_info)
    return streaming_info


def set_alarm(time):
    """Sets an alarm."""
    pass


def play_song(song_name):
    """Plays the music."""
    print("Playing " + song_name)
    pass

