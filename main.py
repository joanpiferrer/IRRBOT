# Importando dependencias
from keep_alive import keep_alive
import configparser
import discord
import requests 
from discord.ext import commands
import sys
import os
from os import walk
import json

# Tomamos la info del archivo config
config = configparser.ConfigParser()
config.read('config.ini')

newUserMessage = """
Benvingut al canal de discord d'Irregulars de PlanB!
Si no ets soci i necessites preguntar qualsevol cosa, pots comunicar-te mitjançant aquest xat de text.
Si ja ets soci comunica-ho a <@247677555170082816> i et donarem permisos perquè puguis accedir a la resta de canals.
"""
columnsAccepted = [3,4,5,6,7,8,16,18,19,22,23,27]

URL = "https://www.mordrek.com:666/api/v1/queries?req=%7B%22compStandings%22%3A%7B%22id%22%3A%22compStandings%22%2C%22idmap%22%3A%7B%22idcompetition%22%3A%2216941%22%7D%2C%22filters%22%3A%7B%22team_name%22%3A%22IRRB%22%7D%2C%22ordercol%22%3A%22sorting%22%2C%22order%22%3A%22desc%22%2C%22limit%22%3A300%2C%22from%22%3A0%2C%22group%22%3Anull%2C%22aggr%22%3Anull%7D%7D"

if not 'MAIN' in config:
    raise ValueError('No se encontro la secccion MAIN en el archivo config')

prefix = config['MAIN']['PREFIJO']

# Poder obtener los modulos de la carpeta comandos
sys.path.append('./commands')

# Array vacio para poner los nombres de los comandos
f = []

# Usando la funcion walk de operating system Buscamos los archivos
for (dirpath, dirnames, filenames) in walk('./commands'):
    # Array con los nombres
    for x in filenames:
        # Nos aseguramos que todos los archivos que tomemos sean de pyhton
        if not x[-3:] == '.py':
            break
        # Guardamos en nuestro array el nombre, pero sin la extension
        f.append(x[:-3])
    break

intents = discord.Intents.default()
intents.members = True

# Client de Discord.py
client = commands.Bot(command_prefix='!',intents=intents)


# Simple evento ready para avisar cuando el Bot esta listo
@client.event
async def on_ready():
    print('Iniciado como ' + client.user.name)
    response = requests.get(url = URL) 
    # extracting data in json format 
    data = json.loads(response.text)
    # extracting latitude, longitude and formatted address  
    # of the first matching location 
    message = ''
    user = await client.fetch_user(247677555170082816)
    for idx, val in enumerate(data['response']['compStandings']['result']['cols']):
      if idx in columnsAccepted:
        message = message + f"{str(val):15}"
      #message = message +  idx
    await user.send('```' + message + '```') 
    message = ''
    for idx, val in enumerate(data['response']['compStandings']['result']['rows']):
      message = ''
      print(val)
      for idx2,val2 in enumerate(val):
        if idx2 in columnsAccepted:
          message = message + f"{str(val2):15}"
      await user.send('```' + message + '```')
    
    
    
    #message = message + '```'
    # printing the output 

# Un Array para poner la info de cada comando
utilidad = []

# Parecido a lo que hicimos arriba, pero esta vez guardaremos el objeto que creamos en cada comando en un array (Para luego usarlo)
for (dirpath, dirnames, filenames) in walk('./commands'):
    for x in filenames:
        if not x[-3:] == '.py':
            break
        util = __import__(x[:-3])
        if hasattr(util, 'info'):
            utilidad.append(util.info)
        else:
            print('El comando ' + x + ' no tiene el objeto de información')

# Evento mensaje que va a a ser la raiz de nuestro handler
@client.event
async def on_message(message):
    # Ignoremos todos los mensajes que son de otros Bots
    if message.author.bot is True:
        return

    # Vemos si el mensaje comienza con el prefijo
    if message.content[0] == prefix:

        # Si lo hace separamos el comando
        command = message.content.split(' ')[0][1:]
        # Obtenemos los argumentos
        args = message.content.split(' ')
        # Borramos el primer elemento de los Argumentos (El comando)
        del args[0]

        # Buscamos en nuestro array de comandos si el comando ese esta
        if command in f:

            # Si esta, lo importamos y lo ejecutamos
            comando = __import__(command)
            # Pasando como parametros el mensaje , los argumentos, y la ulilidad
            await comando.run(message, args, utilidad)

@client.event
async def on_member_join(member):
    channel = member.guild.get_channel(808624631581376522)

    await channel.send(f'Hola <@{member.id}>, ' + newUserMessage)

keep_alive()
client.run(os.getenv('TOKEN'))

