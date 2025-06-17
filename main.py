import os
import base64
import random
import requests
import threading
from colorama import Fore, init
from os.path import isfile, join

init(autoreset=True)

TOKENS_FILE = 'tokens.txt'
AVATAR_FOLDER = 'avatars/'
DISCORD_API_URL = 'https://discord.com/api/v9/users/@me'

def get_random_token():
    if not isfile(TOKENS_FILE):
        print(f"{Fore.RED}[ERROR]{Fore.RESET} Missing 'tokens.txt'")
        return None

    with open(TOKENS_FILE, 'r') as f:
        tokens = [t.strip() for t in f.readlines() if t.strip()]
    
    return random.choice(tokens) if tokens else None

def get_random_avatar():
    if not os.path.exists(AVATAR_FOLDER):
        print(f"{Fore.RED}[ERROR]{Fore.RESET} Missing avatars folder.")
        return None

    pictures = [f for f in os.listdir(AVATAR_FOLDER) if isfile(join(AVATAR_FOLDER, f))]
    return random.choice(pictures) if pictures else None

def change_profile_picture():
    token = get_random_token()
    if not token:
        return

    avatar_file = get_random_avatar()
    if not avatar_file:
        return

    with open(join(AVATAR_FOLDER, avatar_file), "rb") as img:
        b64_avatar = base64.b64encode(img.read()).decode('utf-8')

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'DiscordBot (https://github.com/OxksTools, 1.0)',
    }

    payload = {
        'avatar': f"data:image/png;base64,{b64_avatar}"
    }

    response = requests.patch(DISCORD_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"{Fore.GREEN}[SUCCESS]{Fore.RESET} Profile updated for token: {token[:25]}...")
    else:
        print(f"{Fore.RED}[FAIL]{Fore.RESET} Status Code: {response.status_code}")

def main():
    try:
        count = int(input("Enter number of profiles to change > "))
    except ValueError:
        print(f"{Fore.RED}[ERROR]{Fore.RESET} Please enter a valid number.")
        return

    threads = []
    for _ in range(count):
        thread = threading.Thread(target=change_profile_picture)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"{Fore.CYAN}[DONE]{Fore.RESET} All profile changes attempted.")

if __name__ == "__main__":
    main()
