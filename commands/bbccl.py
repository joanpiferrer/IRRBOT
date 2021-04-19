from utilities import get_mordrek_ranking
import configparser

# Tomamos la info del archivo config
config = configparser.ConfigParser()
config.read('config.ini')

async def run(message , args, utilidad):
  response = get_mordrek_ranking("19856","IRRB|IRREGULAR|IRRPB|VINICULTORES")
  await message.channel.send('Ranking d\'equips IRRB a les CCL\n'+response)

info = {
   "nombre": "bbccl",
   "des": "Ranking dels socis participants a les CCL que hagin posat al seu equip la tag IRRB",
   "uso": config['MAIN']['PREFIJO']+"bbccl"
}