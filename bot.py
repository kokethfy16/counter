import discord
from discord.ext import commands
from discord.utils import get
import json

prefix = '/'
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=prefix, case_insensitive=True, intents = intents)
client.remove_command('help')


@client.event
async def on_ready():
	print('Bot connected')


@client.event
async def on_message(message):
	channel = client.get_channel(ваш_канал)
	with open('/Users/kirilllavrinenko/Documents/message_bot/output.json', 'r') as f:
		output = json.load(f)


	async def update_data(output, member):
		if not member in output:
				output[member] = {}
				output[member]['name'] = member
				output[member]['count'] = 0
				output[member]['symbols'] = 0
				output[member]['symbols_without_space'] = 0

	async def add_count(output, member, channel: discord.TextChannel):
		if message.channel == channel:
			output[member]['count'] += 1
	async def add_symbol_with_space(output, member, channel: discord.TextChannel):
		if message.channel == channel:
			lenth = len(message.content)
			output[member]['symbols'] += lenth
	async def add_symbol_without_space(output, member, channel: discord.TextChannel):
		if message.channel == channel:
			lenth_spc = len(message.content.replace(" ", ""))
			output[member]['symbols_without_space'] += lenth_spc


	await update_data(output, str(message.author))
	await add_count(output, str(message.author), channel)
	await add_symbol_with_space(output, str(message.author), channel)
	await add_symbol_without_space(output, str(message.author), channel)

	with open('/Users/kirilllavrinenko/Documents/message_bot/output.json', 'w') as f:
		json.dump(output, f)
	await client.process_commands(message)


#Connecting
token = open("token.txt", "r").readline()
client.run(token)
