import requests

def send_message(bot_token: str, chat_id: str, message: str) -> bool:
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.status_code == 200