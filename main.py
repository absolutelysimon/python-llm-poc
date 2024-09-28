import pyautogui
import requests
import http.client
import urllib.parse  # For URL encoding
import re  # For regex parsing
from gpt_api_call import call_gpt
import pprint
import json
import os

# Define headers for the Streaming Availability API
STREAMING_API_HEADERS = {
    'x-rapidapi-key': "955c435d11msh91de3c80eedefb7p17a38bjsnea85402fba7d",
    'x-rapidapi-host': "streaming-availability.p.rapidapi.com"
}
COUNTRY_CODE = "ca"  # Example country code, update as needed

def get_llm_response(prompt):
    try:
        # Call GPT API to interpret the user's prompt
        response = call_gpt(
            f"You are an AI assistant whose job is to identify which functions you should call based on a natural language prompt. The functions you can call are: play_song(song_name), play_album(album_name), play_artist(artist_name), set_alarm(datetime), set_timer(time), get_weather(), lower_volume(), raise_volume(), mute(), play_music(), pause_music(), next_song(), previous_song(), play_tv_show(show_name), play_movie(), read_the_news(). Your response from now on should be only a function name and the arguments you think are most appropriate, if any arguments are needed. Try to fully qualify the names of any TV shows and songs. The string for this request is: '{prompt}'"
        )
        return response

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

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

# Improved regex to handle both parentheses and single/double quotes
def extract_quoted_content(response):
    """Extract content inside single or double quotes or parentheses."""
    # Handle cases with both quotes and parentheses
    match = re.search(r'["\'\(]([^"\')]+)["\'\)]', response)
    if match:
        return match.group(1)
    return None

# Example list of prompts
prompt_list = [
    "Play BoJack.",
]

# Process each prompt and call appropriate functions
strre = ''
for prompt in prompt_list:
    response = get_llm_response(prompt)
    print(f"Response for prompt '{prompt}': {response}")

    if response is None:
        continue  # Skip if there's no valid response

    # Extract the quoted or parenthesized content (song, movie, or show names)
    extracted_content = extract_quoted_content(response)

    # Call appropriate function based on GPT response
    if "play_tv_show" in response and extracted_content:
        strre = play_tv_show(extracted_content)
    elif "play_movie" in response and extracted_content:
        strre = play_movie(extracted_content)        
        print (f'setting strre to {strre}')

    else:
        print(f"Error parsing content from response: {response}")

strre = json.loads(strre)
streaming_options = strre[0]['streamingOptions']['ca']
streaming_links = []
for option in streaming_options:
    streaming_links.append(option['videoLink'])

print(f"Liks: {streaming_links}")
os.system(f'start {streaming_links[0]}')
# Sample media control functions
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

def set_alarm(time):
    """Sets an alarm."""
    pass

def play_song(song_name):
    """Plays a song."""
    pass

def play_album(album_name):
    """Plays an album."""
    pass

def play_artist(artist_name):
    """Plays an artist."""
    pass

def get_weather():
    """Fetches weather information."""
    pass
