import requests
import os

# Retrieve secrets from GitHub environment
api_key = os.getenv("OPENAI_API_KEY")
github_token = os.getenv("GH_TOKEN")  # Ensure this matches GitHub Secrets
repo = os.getenv("GITHUB_REPOSITORY")

# Define Qodo AI API endpoint
qodo_ai_url = "https://api.qodo.ai/review"

# Validate API Key and Token
if not api_key or not github_token:
    raise ValueError("Missing API key or GitHub token. Check GitHub Secrets.")

# Make the API request
try:
    response = requests.post(
        qodo_ai_url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "GH_TOKEN": github_token  # Corrected header key
        },
        json={"repo": repo}
    )

    # Print status and response data
    if response.status_code == 200:
        print("Qodo AI Review Response:", response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
