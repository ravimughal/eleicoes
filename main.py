import requests
import json
import pandas as pd
import time

while True:

    data = requests.get(
        "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json")

    json_data = json.loads(data.content)

    candidato = []
    partido = []
    votos = []
    porcentagem = []

    for inf in json_data['cand']:

        
        candidato.append(inf['nm'])
        votos.append(inf['vap'])
        porcentagem.append(inf['pvap'])

    df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=['Candidato', 'Votos', 'Porcentagem'])

    print(df_eleicao)
    print("\n\r")

    time.sleep(60)