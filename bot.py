import discord
import requests

api_key = "Sports_Data_Io_Api_Key_Here"

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("The bot is ready!")

@client.event
async def on_message(message):
    if message.content.startswith("!odds"):
        event_id = message.content.split(" ")[1]
        response = requests.get("https://api.sportsdata.io/v3/ufc/odds/json/Fights/" + event_id + "?key=" + api_key)
        data = response.json()
        for fight in data['Fights']:
            await message.channel.send(f"Fight: {fight['Description']} Odds: {fight['Odds']}")

client.run("Discord_Bot_Token")
