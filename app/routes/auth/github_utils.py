import requests
import json

from urllib.parse import parse_qs

from config import Config

app_id = Config.CLIENT_ID
app_secret = Config.CLIENT_SECRET

def generate_link(url_redirect):
    params = dict(client_id=app_id,  # the client ID you received from GitHub when you registered
                  redirect_uri=url_redirect,  # the URL in your application where users will be sent after authorization
                  # scope="",  # type of access
                  response_type="code")  # request the code
    endpoint = "https://github.com/login/oauth/authorize"
    response = requests.get(endpoint, params=params)
    return response.url

def get_token_by_code(code, url_redirect):
    params = dict(client_id=app_id,
                  client_secret=app_secret,
                  redirect_uri=url_redirect,
                  code=code)

    endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(endpoint, json=params)

    data = parse_qs(response.content.decode('utf-8'))
    print(data)
    token = data.get("access_token")[0]

    return token

def get_user_info(access_token) -> dict:
    # read the GitHub manual about headers
    headers = {"Authorization": f"token {access_token}"}
    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint, headers=headers)

    data = response.json()

    return data