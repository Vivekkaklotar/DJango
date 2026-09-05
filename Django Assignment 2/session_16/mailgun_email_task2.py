import requests

def send_mailgun_welcome(user_email, username):
    api_key = "YOUR_MAILGUN_API_KEY"
    domain = "YOUR_MAILGUN_DOMAIN"
    
    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
            "from": f"Welcome Team <mailgun@{domain}>",
            "to": [user_email],
            "subject": f"Welcome aboard, {username}!",
            "text": f"Hi {username},\n\nThank you for signing up on our platform!"
        }
    )