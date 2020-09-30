from iqoptionapi.stable_api import IQ_Option
import time, json
from datetime import datetime

# ESTABELECENDO CONEXÃO____________________________________________________________________________________________________

API = IQ_Option('ilton.aws@gmail.com', '/ajV@xjzJ-3peBv')

API.connect()
API.change_balance('PRACTICE')  # PRACTICE / REAL

while True:
    if API.check_connect() == False:
        print('Erro ao tentar se conectar!')

        API.connect()
    else:
        print('Conexão estabelecida!')
        break

# DEFININDO VARIÁVEIS________________________________________________________________________________________________________

par = API.get_all_open_time()
payout = API.get_all_profit()
payout_min = int(84)
entrada = int(2)
timeframe = 1
index = 0
# direcao        = 0

# GERANDO OPERAÇÕES___________________________________________________________________________________________________________

for paridade in par['binary']:
    if par['binary'][paridade]['open'] == True:  # and payout[par] >= payout_min:
        check, id = API.buy(entrada, paridade, "call", timeframe)
        if check:
            print("Ordem executada com sucesso!")
        else:
            print("Não foi possível executar a ordem!")
















