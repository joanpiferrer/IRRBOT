from keep_alive import keep_alive
import discord
import os

newUserMessage = """
Benvingut al canal de discord d'Irregulars de PlanB!
Si no ets soci i necessites preguntar quelcom pots comunicarte mitjançant el canal de text public
Si ets soci comunica-ho a en Folldelturó i encantats et donarem permisos per que puguis accedir a la resta de canals.
"""

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    user = await client.fetch_user(247677555170082816)

    await channel.send(f'Hola <@{member.id}>, ' + newUserMessage)

keep_alive()
client.run(os.getenv('TOKEN'))