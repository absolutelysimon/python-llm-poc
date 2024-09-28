import pyautogui


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
    print("Playing " + song_name)
    pass