from pyrogram import filters
from pyrogram.types import Message

from ImageBot import bot
from ImageBot.decorators.owner_only import admin
from ImageBot import GITHUB_USERNAME, GITHUB_REPO_NAME, GITHUB_BRANCH

import sys
import os
import subprocess
import requests
import pickle


LOCAL_REPO_PATH = os.getcwd()

API_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{GITHUB_REPO_NAME}/branches/{GITHUB_BRANCH}"


def get_latest_remote_commit():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["commit"]["sha"]
    else:
        return None


def get_latest_local_commit():
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=LOCAL_REPO_PATH,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def store_restart_msg(msg: Message):
    with open("msg.dat", "wb") as f:
        pickle.dump(msg, f)


def load_restart_msg():
    if os.path.exists("msg.dat"):
        with open("msg.dat", "rb") as f:
            data = pickle.load(f)
        if data:
            msg: Message = data
            os.remove("msg.dat")
            return msg
        else:
            return False


@bot.on_message(filters.command("restart"))
@admin
async def restart_bot(c: bot, m: Message):
    x = await c.send_message(
        chat_id=m.chat.id,
        text="Starting repository tracking...",
        reply_to_message_id=m.id,
    )

    remote_commit = get_latest_remote_commit()
    local_commit = get_latest_local_commit()

    if remote_commit and remote_commit != local_commit:
        await x.edit_text(text="New commit detected. Fetching updates...")
        subprocess.run(["git", "pull"], cwd=LOCAL_REPO_PATH)
        await x.edit_text(text="Repository updated.")
    else:
        await x.edit_text(text=f"Bot is up to date with branch : {GITHUB_BRANCH}")
    await x.edit_text(text="Bot restarting...")

    store_restart_msg(x)

    os.execv(
        sys.executable,
        [sys.executable.split("\\")[-1].split(".")[0], "-m", "ImageBot", *sys.argv[1:]],
    )
