import discord
import os
from discord.utils import get

intents = discord.Intents(members=True)
client=discord.Client(intents=intents)
newUserMessage = """
Benvingut al canal de discord d'Irregulars de PlanB!
Si no ets soci i necessites preguntar quelcom pots comunicarte mitjançant el canal de text public
Si ets soci comunica-ho a en Folldelturó i encantats et donarem permisos per que puguis accedir a la resta de canals.
"""


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(
      f'Hola {member.name}, ' + newUserMessage
  )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send('Hola!')

client.run(os.getenv('TOKEN'))