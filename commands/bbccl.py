from utilities import get_mordrek_ranking

async def run(message , args, utilidad):
  response = get_mordrek_ranking("16941","IRRB|IRREGULAR|IRRPB|VINICULTORES")
  await message.channel.send('Ranking d\'equips IRRB a les CCL\n'+response)

info = {
   "nombre": "bbccl",
   "des": "Ranking dels socis participants a les CCL que hagin posat al seu equip la tag IRRB",
   "uso": "$bbccl"
}