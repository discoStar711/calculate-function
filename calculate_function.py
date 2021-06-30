import requests

wolfram_api_url = 'https://api.wolframalpha.com/v2/query'
request_params = {
    'format': 'image,plaintext',
    'output': 'JSON',
    'appid': 'EEK9JE-ALEXGXEXR4',
}

def calculate(input):
    request_params['input'] = input
    response = requests.get(wolfram_api_url, params=request_params)
    return response.json()