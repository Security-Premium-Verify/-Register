import requests
import time

token = ""
with open("tokens.txt", "r") as f:
    token = f.readline().strip()

channel_id = input("Enter Channel ID: ")
num_messages = int(input("How many messages to send? "))
delay = float(input("Delay between messages (in seconds): "))
message_content = input("Enter message content: ")

headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

for i in range(num_messages):
    payload = {
        "content": f"{message_content} ({i + 1})"
    }

    response = requests.post(
        f"https://discord.com/api/v9/channels/{channel_id}/messages",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        print(f"Sent message {i + 1}")
    else:
        print(f"Failed to send message {i + 1} | Status Code: {response.status_code} | {response.text}")

    time.sleep(delay)
