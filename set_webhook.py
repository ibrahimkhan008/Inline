import os
import requests
from config import BOT_TOKEN  # Import the bot token from config.py

# Vercel project URL endpoint
vercel_project_url = "https://api.vercel.com/v8/projects/{PROJECT_ID}"


# Fetch the project URL (replace `YOUR_VERCEL_TOKEN` with your Vercel token)
def fetch_vercel_url(project_id, vercel_token):
    headers = {
        'Authorization': f'Bearer {vercel_token}'
    }
    response = requests.get(vercel_project_url.replace("{PROJECT_ID}", project_id), headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["url"]
    else:
        raise Exception("Error fetching Vercel URL")


# Function to set the webhook
def set_webhook(vercel_url):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"  # Use BOT_TOKEN from config
    webhook_url = f"{vercel_url}/webhook"
    response = requests.post(telegram_url, data={'url': webhook_url})

    if response.status_code == 200:
        print("Webhook set successfully!")
    else:
        print("Failed to set webhook")


if __name__ == "__main__":
    project_id = "your-vercel-project-id"
    vercel_token = os.getenv('VERCEL_TOKEN', 's81gjxJ84XSTlOwfVoH63EKw')

    # Fetch Vercel URL and set webhook
    vercel_url = fetch_vercel_url(project_id, vercel_token)
    set_webhook(vercel_url)
