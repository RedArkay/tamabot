import requests
import json
import discord
import config
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('tamamo, '):
		content = message.content.lower()
		if 'master mission' in content:
			r = requests.get('https://raw.githubusercontent.com/RedArkay/tamabot/master/missions.json')
			parsed = json.loads(r.text, strict=False)
			await message.channel.send(parsed['missions'])
		if 'stop' in content:
			await client.close()
client.run(config.token)
