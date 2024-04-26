"""
CONSTANTE = "variáveis" que não vão mudar
Evitar muitas condições no mesmo if
Diminuir o máximo possível a complexidade do código
código simples de ler = código bom
    <- Contagem de complexidade (indentações)
"""
velocidade = 60 # velocidade atual do carro

local_carro = 100 # local em que o carro está localizado

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local aonde o primeiro radar está
RADAR_RANGE = 1  # A distância que o radar alcança

velocidade_do_carro_passou_do_radar_1 = velocidade > RADAR_1
carro_passou_do_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_do_radar_1 and velocidade_do_carro_passou_do_radar_1

if carro_passou_do_radar_1:
    print('Carro passou no radar 1.')

if velocidade_do_carro_passou_do_radar_1:
    print('Velocidade do carro passou do radar 1.')
