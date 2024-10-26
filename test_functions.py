import functions
import json


sample_functions = ["play_song", "null_function", "pause_music", "default"]
for name in sample_functions:
    func = functions._execute_func(functions, name, "Baby by blues")
    if func:
        print(f"{json.dumps(func)} response returned")
    else:
        print("No response returned")
