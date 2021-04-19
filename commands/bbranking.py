from utilities import get_mordrek_ranking
import configparser

# Tomamos la info del archivo config
config = configparser.ConfigParser()
config.read('config.ini')

async def run(message , args, utilidad):
  response = get_mordrek_ranking("16950",'',3)
  await message.channel.send('Ranking de la lliga online d\'irregulars de planB\n'+response)

info = {
   "nombre": "bbranking",
   "des": "Ranking de la lliga online d\'irregulars de planB'",
   "uso": config['MAIN']['PREFIJO']+"bbranking"
}