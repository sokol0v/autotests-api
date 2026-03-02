import httpx

ENDPOINT = {
    "URL": "http://localhost:8000",
    "POST": "/api/v1/authentication/login",
    "GET": "/api/v1/users/me"
}
# Данные для входа в систему
login_payload = {
    "email": "dyein@bk.ru",
    "password": "S0kolov!"
}

def authenticate_user(login_json):
    login_response = httpx.post(ENDPOINT["URL"]+ENDPOINT["POST"], json=login_json)
    login_token = login_response.json()
    if login_response.status_code == 200:
        print(f"Успешная авторизация, статус-код {login_response.status_code}")
        print(f"Получен JSON с токенами - {login_token}")
    else:
        print(f"Ошибка авторизации, статус-код {login_response.status_code}")
    return login_token["token"]["accessToken"]

def get_user_me(login_token):
    get_user_response = httpx.get(ENDPOINT["URL"]+ENDPOINT["GET"], headers={"Authorization": f"Bearer {login_token}"})
    if get_user_response.status_code == 200:
        print(f"Пользователь получен, данные пользователя {get_user_response.json()}")
    else:
        print(f"Ошибка авторизации, статус-код {get_user_response.status_code}")

authentication = authenticate_user(login_payload)
get_user_me(authentication)