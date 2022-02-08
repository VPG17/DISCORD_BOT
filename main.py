import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    string1 = message.content;

    if string1.lower().startswith('hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))