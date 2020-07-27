import discord
from discord import File
from os.path import dirname, abspath
from os import listdir
from random import choice
import json
import asyncio

client = discord.Client()

path = dirname(abspath(__file__))

def JSONLoader() -> dict:
    with open(path + "/config.json") as Json:
        json_data: dict = json.load(Json)
        return json_data

async def sendReminder() -> None:
    if(not client.get_user(jsondata["user"]).dm_channel):
        await client.get_user(jsondata["user"]).create_dm()
    channel: discord.DMChannel = client.get_user(jsondata["user"]).dm_channel

    content: str = path + "/content/" + choice(listdir(path) + "/content"))
    image_filetype: list = [
        "png",
        "bmp",
        "gif",
        "jpg",
        "jpeg",
        "webm",
        "mp4",
        "mp3"
    ]
    filetype = content.rsplit(".", 1)[1]
    if(content.rsplit(".", 1)[1] in image_filetype):
        await channel.send(file=File(content))
    else:
        with open(content) as f:
            await channel.send(content=f.read())


@client.event
async def on_ready():
    await sendReminder()
    await client.close()

if __name__ == "__main__":
    jsondata: dict = JSONLoader()
    client.run(jsondata["token"])
