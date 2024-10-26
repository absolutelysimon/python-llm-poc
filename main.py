import pyautogui
import requests
import http.client
import urllib.parse  # For URL encoding
import re  # For regex parsing
from gpt_api_call import call_gpt
import pprint
import json
import os

# install python-dotenv (pip install)
import base64

# install requests (pip install)
from requests import post, get
import json

# Define headers for the Streaming Availability API
STREAMING_API_HEADERS = {
    "x-rapidapi-key": "955c435d11msh91de3c80eedefb7p17a38bjsnea85402fba7d",
    "x-rapidapi-host": "streaming-availability.p.rapidapi.com",
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
        # print(f"An error occurred: {e}")
        return None


def get_streaming_availability(title):
    """Fetches streaming availability for a given show or movie title."""
    try:
        encoded_title = urllib.parse.quote(title)  # Safely encode the title
        conn = http.client.HTTPSConnection("streaming-availability.p.rapidapi.com")
        conn.request(
            "GET",
            f"/shows/search/title?title={encoded_title}&country={COUNTRY_CODE}&output_language=en",
            headers=STREAMING_API_HEADERS,
        )
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
    except Exception as e:
        # print(f"An error occurred while fetching streaming info: {e}")
        return None


def play_tv_show(tv_show_name):
    """Handles the request to play a TV show by fetching its streaming availability."""
    # print(f"Fetching streaming availability for the TV show: {tv_show_name}")
    streaming_info = get_streaming_availability(tv_show_name)
    # print(f"Streaming info for '{tv_show_name}': {streaming_info}")
    return streaming_info


def play_movie(movie_name):
    """Handles the request to play a movie by fetching its streaming availability."""
    # print(f"Fetching streaming availability for the movie: {movie_name}")
    streaming_info = get_streaming_availability(movie_name)
    # print(f"Streaming info for '{movie_name}': ")

    # pprint.PrettyPrinter(streaming_info)
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
    "Play the Matrix Soundtrack.",
    "Pause the music.",
    "Play the music.",
    "Play the next song.",
    "Play the previous song.",
    "Play BoJack.",
    "Set an alarm for 7:30 AM.",
    "Play the song 'Bohemian Rhapsody'.",
    "Play the album 'Dark Side of the Moon'.",
    "Play the artist 'The Beatles'.",
    "What's the weather like?",
    "Lower the volume.",
    "Raise the volume.",
    "Mute the music.",
    "Play the 'Breaking Bad'.",
    "Be quiet.",
]

# Process each prompt and call appropriate functions
strre = ""
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
        strre = json.loads(strre)
        streaming_options = strre[0]["streamingOptions"]["ca"]
        streaming_links = []
        for option in streaming_options:
            streaming_links.append(option["videoLink"])
        os.system(f"start {streaming_links[0]}")

    elif "play_movie" in response and extracted_content:
        strre = play_movie(extracted_content)
        streaming_options = strre[0]["streamingOptions"]["ca"]
        streaming_links = []
        for option in streaming_options:
            streaming_links.append(option["videoLink"])
        # print(f"setting strre to {strre}")
        os.system(f"start {streaming_links[0]}")

    elif "play_song" in response and extracted_content:
        song_name = input("Put the song that you want to hear: ")
        play_music(token, extracted_content)

    else:
        # print(f"Error parsing content from response: {response}")
        pass


#########################################
# Load client IDs
# load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


# Create function for authorization
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


# Function to get authorization header
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


# putting a variable to get the token of the user
token = get_token()


# Sample media control functions
def pause_music():
    """Pauses the music."""
    pyautogui.press("playpause")


# token to get the user profile using client_id and client_secret
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)

    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


# Function to get authorization header
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


# Function to search for a song
def play_music(token, song_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    params = {
        "q": song_name,
        "type": "track",
        "limit": 1,  # Number of results to return currently most played in spotify
    }

    result = get(url, headers=headers, params=params)
    if result.status_code == 200:
        json_result = result.json()
        tracks = json_result["tracks"]["items"]

        if len(tracks) > 0:
            track = tracks[0]  # Get the first track in the list
            track_name = track["name"]
            artist_name = track["artists"][0]["name"]
            album_name = track["album"]["name"]
            spotify_url = track["external_urls"]["spotify"]

            os.system(f"start {spotify_url}")
            # print(
            #     f"Playing '{track_name}' by {artist_name}. Listen here: {spotify_url}"
            # )
        else:
            # print("No results found.")
            pass
    else:
        pass
        # print(f"Failed to search for the song: {result.status_code}")


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


# user interaction where they have to put the name of the song and call the function
