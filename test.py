import requests
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from gpt_api_call import call_gpt
from get_functions import get_list_of_functions


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@cross_origin()

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

        return response


    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

@app.route('/', methods=['GET', 'POST'])
def execute_request():
    # {'text': 'user text'}
    data = request.get_json()

    input_str = data['text']
    function_name = get_function_name(input_str)
    print(function_name)


    # return jsonify(function_name), 200
    return jsonify("Test"), 200


if __name__ == '__main__':
    app.run(debug=True)
