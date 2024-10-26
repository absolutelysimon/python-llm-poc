import requests
from flask import Flask, jsonify, request
from gpt_api_call import call_gpt
import functions
from get_functions import get_list_of_functions

app = Flask(__name__)


def get_function_name(input_str):
    try:
        response = call_gpt(
            f"""You are an AI assistant whose job is to identify which functions 
            you should call based on a natural language prompt. 
            The functions you can all are: {get_list_of_functions()}. 
            Your response from now on should be only a function name and the arguments 
            you think are most appropriate, if any arguments are needed. 
            Try to fully qualify the names of any TV shows and songs. 
            For example, when you are asked to play 'BoJack' you should return play_tv_show('BoJack Horseman'). 
            The string for this request is: '{input_str}'"""
        )

        # Todo: Hacky, find another way to do this
        responselist = response.split("(")
        function_name = responselist[0]
        function_param = None
        if len(function_name) > 1:
            function_param = responselist[1].strip(")")
        return (function_name, function_param)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


@app.route('/', methods=['GET', 'POST'])
def execute_request():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing input string'}), 400

    input_str = data['text']
    function_name, function_param = get_function_name(input_str)

    return jsonify({'status': 'success', 'result': f"Executed {function_name}"})

    # functions_status = getattr(functions, function_name)


if __name__ == '__main__':
    app.run(debug=True)
