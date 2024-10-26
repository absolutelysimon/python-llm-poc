import pyautogui
import inspect


def _execute_func(module, function_name, *args, **kwargs):
        if hasattr(module, function_name) and callable(func := getattr(module, function_name)): # noqa
            try:
                inspect.signature(func).bind(*args, **kwargs)
                return func(*args, **kwargs)
            except TypeError:
                return func()


def pause_music():
    """Pauses the music."""
    print("pause_music")
    try:
        pyautogui.press("playpause")
    except:
        pass


def play_music():
    """Plays the music."""
    print("play_music")
    try:
        pyautogui.press("playpause")
    except:
        pass


def next_song():
    """Plays the next song."""
    print("next_song")
    try:
        pyautogui.press("nexttrack")
    except:
        pass


def previous_song():
    """Plays the previous song."""
    print("previous_song")
    try:
        pyautogui.press("prevtrack")
    except:
        pass


def play_tv_show(tv_show_name):
    """Plays a TV show."""
    print("Play show")
    pass


def set_alarm(time):
    """Sets an alarm."""
    print("Set alarm")
    pass


def play_song(song_name):
    """Plays the music."""
    print("Playing " + song_name)
    pass


def default():
    """Greetings"""
    print("Hello")
    return "Hi"
