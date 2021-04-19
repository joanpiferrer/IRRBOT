import configparser

# Tomamos la info del archivo config
config = configparser.ConfigParser()
config.read('config.ini')

async def run(message, args, utilidad):
   await message.channel.send(" ".join(args))
   await message.delete()


info ={
   "nombre": "say",
   "des": "El bot repeteix el que dius",
   "uso": config['MAIN']['PREFIJO']+"say [texto]"
}