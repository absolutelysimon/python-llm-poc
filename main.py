import pyautogui

function_list = {
    "Set an alarm": set_alarm,
    "Pause the music": pause_music,
    "Play the music": play_music,
    "Next song": next_song,
    "Previous song": previous_song,
    "Play a TV show": play_tv_show,
}

prompt = f"Please take the following string and determine which function is most appropriate to deal with its request. The options you have to pick from are "


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
