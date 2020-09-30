from iqoptionapi.stable_api import IQ_Option
import time, json
from datetime import datetime

# ESTABELECENDO CONEXÃO____________________________________________________________________________________________________

API = IQ_Option('ilton.aws@gmail.com', '/ajV@xjzJ-3peBv')

API.connect()
API.change_balance('PRACTICE')  # PRACTICE / REAL

con_tests = 0
max_con_test = 10

while True:
    con_tests = con_tests + 1
    if API.check_connect() is False:
        print('Erro ao tentar se conectar!')
        API.connect()
    elif con_tests == max_con_test:
        print('(error)Número máximo de tentativas excedidas!')
        break
    else:
        print('Conexão estabelecida!')
        break

# DEFININDO VARIÁVEIS________________________________________________________________________________________________________

pairs = API.get_all_open_time()
payouts = API.get_all_profit()
min_payout = int(84)
spend_bid = int(2)
timeframe = 1
index = 0
# direcao = 0

# GERANDO OPERAÇÕES___________________________________________________________________________________________________________

for pair in pairs['binary']:
    if pairs['binary'][pair]['open'] is True:# and payout[par] >= payout_min:
        check, id = API.buy(spend_bid,pair,"call",timeframe)
        if check:
            print("Ordem executada com sucesso!")
        else:
            print("Não foi possível executar a ordem!")
