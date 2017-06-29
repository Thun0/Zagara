import discord
import asyncio
from model import Model

client = discord.Client()
model = Model()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!pollc'):
        await client.send_message(message.channel, model.create_poll(message))
    elif message.content.startswith('!pollend'):
        await client.send_message(message.channel, model.end_poll())
    elif message.content.startswith('!poll'):
        await client.send_message(message.channel, model.get_poll_message())
    elif message.content.startswith('!help'):
        await client.send_message(message.channel, model.get_help_message())
    elif message.content.startswith('!roll'):
        await client.send_message(message.channel, model.roll_dice(message))
    #elif message.content.startswith('!vote'):
    #    await client.send_message(message.channel, model.roll_dice(message))
    # TODO: message user, not channel


client.run('MzI5NTcwODM5NjUxNTQ5MTk0.DDZJzA.vPLeGDPXlY2ChrjGPCf86X6rDog')
