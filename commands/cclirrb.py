import requests 

# api-endpoint  https://www.mordrek.com/gspy/comp/16941?filter={%22compStandings%22:{%22filters%22:{%22team_name%22:%22IRRB%22},%22limit%22:300,%22from%22:0}}

URL = "https://www.mordrek.com:666/api/v1/queries?req=%7B%22compStandings%22%3A%7B%22id%22%3A%22compStandings%22%2C%22idmap%22%3A%7B%22idcompetition%22%3A%2216941%22%7D%2C%22filters%22%3A%7B%22team_name%22%3A%22IRRB%22%7D%2C%22ordercol%22%3A%22sorting%22%2C%22order%22%3A%22desc%22%2C%22limit%22%3A30%2C%22from%22%3A0%2C%22group%22%3Anull%2C%22aggr%22%3Anull%7D%7D"
#{"compStandings":{"id":"compStandings","idmap":{"idcompetition":"16941"},"filters":{"team_name":"IRRB"},"ordercol":"sorting","order":"desc","limit":30,"from":0,"group":null,"aggr":null}}

# location given here 
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API 
PARAMS = {'compStandings':{'id':"compStandings","idmap":{"idcompetition":"16941"}}}

async def run(message , args, utilidad):
  # sending get request and saving the response as response object 
  r = requests.get(url = URL) 
  # extracting data in json format 
  data = r.json()
  
  # extracting latitude, longitude and formatted address  
  # of the first matching location 
  
  # printing the output 
  print(data)
  await message.channel.send(data)

info = {
   "nombre": "cclirrb",
   "des": "Ranking dels socis participants a les CCL que hagin posat al seu equip la tag IRRB",
   "uso": "$cclirrb"
}