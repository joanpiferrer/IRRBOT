from utilities import get_upcoming_events
import configparser

# Tomamos la info del archivo config
config = configparser.ConfigParser()
config.read('config.ini')

async def run(message, args, utilidad):
  response = get_upcoming_events()
  if response is not None:
    if type(message).__name__ == 'TextChannel':
      channel = message
    else:
      channel = message.channel
    await channel.send(response)

info = {
   "nombre": "reserves",
   "des": "Mostrar els pròxims esdeveniments al local",
   "uso": config['MAIN']['PREFIJO']+"reserves"
}