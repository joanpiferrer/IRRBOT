import json
import requests 

def make_markdown_table(var):

    markdown = "```" + str("| ")

    for e in var:
        to_add = " " + str(e) + str(" |")
        markdown += to_add
    markdown += "\n"

    markdown += '|'
    for i in range(len(var)):
        markdown += str("-------------- | ")
    markdown += "\n"

    for entry in var:
        markdown += str("| ")
        for e in entry:
            to_add = str(e) + str(" | ")
            markdown += to_add
        markdown += "\n"

    return markdown + "```"

def get_mordrek_ranking(idCompetition,filter):
  URL = "https://www.mordrek.com:666/api/v1/queries?req=%7B%22compStandings%22%3A%7B%22id%22%3A%22compStandings%22%2C%22idmap%22%3A%7B%22idcompetition%22%3A%22"+idCompetition+"%22%7D%2C%22filters%22%3A%7B%22team_name%22%3A%22"+filter+"%22%7D%2C%22ordercol%22%3A%22sorting%22%2C%22order%22%3A%22desc%22%2C%22limit%22%3A300%2C%22from%22%3A0%2C%22group%22%3Anull%2C%22aggr%22%3Anull%7D%7D"

  RACES: [str] = [
        "INDEX0",
        "Humans",
        "Nans",
        "Skaven",
        "Orcs",
        "Homes llangardaix",
        "Goblins",
        "Elfs silvans",
        "Caos",
        "Elfos Oscuros",
        "No morts",
        "Halflings",
        "Norse",
        "Amazones",
        "Elfs pro",
        "Alts elfs",
        "Khemri",
        "Nigromants",
        "Nurgle",
        "Ogres",
        "Vampirs",
        "Nans del Caos",
        "Inframón",
        "EQUIPO23",
        "Bretonia",
        "Kislev"
    ]

  response = requests.get(url = URL) 
  # extracting data in json format 
  data = json.loads(response.text)
  
  #user = await client.fetch_user(247677555170082816)
  headers = f"{'Punts':10}{'Record':10}{'Partides':10}{'Nom Equip':25}{'Raça':20}{'Entrenador':30}\n"

  rankingccl = ''
  for val in data['response']['compStandings']['result']['rows']:
    rankingccl = rankingccl + f"{val[2]:10}{val[6]+'-'+val[7]+'-'+val[8]:10}{val[19]:10}{val[22]:25}{RACES[int(val[21])]:20}{val[27]:30}\n"
  

  return '```' + headers + rankingccl + '```'