import pyautogui
import requests
from gpt_api_call import call_gpt

# function_list = {
#     "Set an alarm": set_alarm,
#     "Pause the music": pause_music,
#     "Play the music": play_music,
#     "Next song": next_song,
#     "Previous song": previous_song,
#     "Play a TV show": play_tv_show,
# }


def get_llm_response(prompt):
    try:
        response = call_gpt(
            f"You are an AI assistant whose job is to identify which functions you should call based on a natural language prompt. The functions you can all are: play_song(song_name), play_album(album_name), play_artist(artist_name), set_alarm(datetime), set_timer(time), get_weather(), lower_volume(), raise_volume(), mute(), play_music(), pause_music(), next_song(), previous_song(), play_tv_show(show name), play_movie(), read_the_news(). Your response from now on should be only a function name and the arguments you think are most appropriate, if any arguments are needed. Try to fully qualify the names of any TV shows and songs. For example, when you are asked to play 'BoJack' you should return play_tv_show('BoJack Horseman'). The string for this request is: '{prompt}'"
        )
        # Check if the request was successful
        # print("Response from the server:")
        # print(response)  # Assuming the response is in JSON format
        return response

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


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

for prompt in prompt_list:
    response = get_llm_response(prompt)
    print(f"Response for prompt '{prompt}': {response}")


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
    """Plays a TV show."""
    pass


def set_alarm(time):
    """Sets an alarm."""
    pass


def play_song(song_name):
    """Plays the music."""
    pass
