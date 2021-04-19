import discord
import configparser

# Tomamos la info del archivo config
config = configparser.ConfigParser()
config.read('config.ini')

async def run(message, args, utilidad):
    embed = discord.Embed(title="Ajuda", description="Llista de totes les comandes disponibles", color=0x00ff00)
    for cmds in utilidad:
      if cmds['nombre'] != 'say':
        embed.add_field(name=cmds['nombre'], value= '`Descripció`: ' + cmds['des'] + '\n`Ús`: ' + cmds['uso'], inline=False)
    await message.channel.send(embed=embed)


info = {
   "nombre": "ajuda",
   "des": "Et mostra totes les comandes disponibles",
   "uso": config['MAIN']['PREFIJO']+"ajuda"
}