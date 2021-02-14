from utilities import get_mordrek_ranking

async def run(message , args, utilidad):
  response = get_mordrek_ranking("16950",'')
  await message.channel.send('Ranking de la lliga online d\'irregulars de planB\n'+response)

info = {
   "nombre": "bbranking",
   "des": "Ranking de la lliga online d\'irregulars de planB'",
   "uso": "$bbranking"
}