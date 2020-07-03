import asyncio
import discord
import json
import random
import os

client = discord.Client()

jsondata: dict = {}

#########################################
#   JSONLoader:                         #
#       Loads the config.json file      #
#   Returns:                            #
#       The JSON data in a dict format  #
#########################################
def JSONLoader() -> dict:
    try:
        with open(os.path.dirlist(os.path.abspath(__file__)) + "/config.json") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error, file 'config.json' doesn't exist")
    except:
        print("Unknown error in JSONLoader")

#############################################
#   sendReminder:                           #
#       Sends our target user a reminder    #
#   Returns:                                #
#       Nothing                             #
#############################################
async def sendReminder() -> None:
    global jsondata
    msgs: list = [
        "this",
        "is",
        "filler",
        "text"
    ]
    # These two if statements aren't really important after the first run of our bot, opens DM channel with our users
    if(not client.get_user(jsondata["user"]).dm_channel):
        await client.get_user(jsondata["user"]).create_dm()
    if(not client.get_user(jsondata["debug_user"]).dm_channel):
        await client.get_user(jsondata["debug_user"]).create_dm()
    # Try/except incase our target user decides to block the bot
    try:
        channel: discord.DMChannel = client.get_user(jsondata["user"]).dm_channel
        await channel.send(content=random.choice(msgs))
    except:
        channel: discord.DMChannel = client.get_user(jsondata["debug_user"]).dm_channel
        await channel.send(content="an error occured sending the message to " + str(client.get_user(jsondata["user"])))


@client.event
async def on_ready():
    await sendReminder()
    await client.close()

jsondata = JSONLoader()
client.run(jsondata["token"])
