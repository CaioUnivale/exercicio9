def ler_valores():
    tempo_gasto = float(input("Digite o tempo gasto na viagem (em horas): "))
    velocidade_media = float(input("Digite a velocidade média durante a viagem (em Km/h): "))
    return tempo_gasto, velocidade_media
def calcular_distancia(tempo_gasto, velocidade_media):
    distancia_percorrida = tempo_gasto * velocidade_media
    return distancia_percorrida
def calcular_litros(distancia_percorrida):
    litros_usados = distancia_percorrida / 12
    return litros_usados
def apresentar_resultado(tempo_gasto, velocidade_media, distancia_percorrida, litros_usados):
    print("Velocidade média: ", velocidade_media, "Km/h")
    print("Tempo gasto na viagem: ", tempo_gasto, "horas")
    print("Distância percorrida: ", distancia_percorrida, "Km")
    print("Litros de combustível utilizados: ", litros_usados, "litros")
tempo_gasto, velocidade_media = ler_valores()
distancia_percorrida = calcular_distancia(tempo_gasto, velocidade_media)
litros_usados = calcular_litros(distancia_percorrida)
apresentar_resultado(tempo_gasto, velocidade_media, distancia_percorrida, litros_usados)