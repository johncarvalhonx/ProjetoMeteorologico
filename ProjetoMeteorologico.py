import requests
import os
from sklearn.linear_model import LinearRegression
import numpy as np

api_key = "" #API do OpenWeatherAPI (Substitua pela sua ou utilize a minha.)

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def aps():
    print("     ____  ____  ____      __________________")
    print("   / __ \/ __ \/ __ \    / / ____/_  __/ __ \ ")
    print("  / /_/ / /_/ / / / /_  / / __/   / / / / / /")
    print(" / ____/ _, _/ /_/ / /_/ / /___  / / / /_/ /")
    print("/_/   /_/ |_|\____/\____/_____/ /_/  \____/")
    print("")

while True:
    aps()
    print("Bem-vindo ao PyClima!\n")
    location = input("> Digite sua cidade: ")
    clear()
    aps()
    print("> Carregando informações...")
    weather = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&lang=pt_br&units=metric&appid={api_key}')
    if weather.json()['cod'] == '404':
        clear()
        aps()
        print("Local invalido.")
        close = input("\n> Insira qualquer tecla para voltar.\n\n> ")
        clear()
        continue
    break

geoloc = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&appid={api_key}")
getlat = geoloc.json()
lat = getlat[0]['lat']
getlon = geoloc.json()
lon = getlon[0]['lon']

#Temperatura dos ultimos 30 dias: (Alterar conforme necessário para a sua cidade.)
temperatures = np.array([20, 21, 19, 20, 22, 23, 21, 20, 19, 18, 19, 20, 21, 22, 23, 24, 25, 24, 23, 22, 21, 20, 19, 18, 19, 20, 21, 22, 23, 24])
temperatures = temperatures.reshape(-1, 1)

X_train = temperatures[:-1]
y_train = temperatures[1:]

model = LinearRegression()
model.fit(X_train, y_train)

today_temperature = np.array([[25]])
predicted_tomorrow_temperature = model.predict(today_temperature)
predicted_tomorrow_temperature_rounded = round(predicted_tomorrow_temperature[0][0])


clear()
aps()

def menu():
    print("")
    print("============== Menu Principal ==============")
    print("")
    print(f"> Local escolhido: {location}")
    print("")
    print("> Escolha uma opção:                     ")
    print("> [1] Temperatura                        ")
    print("> [2] Qualidade de Ar                    ")
    print("> [3] Tabelas de Informação")
    print("> [4] Lista Completa de Riscos")
    print("> [5] Creditos")
    print("> [6] Sair")
    print("")
    print("============================================")
    choice = input("\n> ")
    if choice == "1":
        clear()
        aps()
        print("> Carregando informações...")
        description = weather.json()['weather'][0]['description']
        temperature = round(weather.json()['main']['temp'])
        feels_like = round(weather.json()['main']['feels_like'])
        high = round(weather.json()['main']['temp_max'])
        low = round(weather.json()['main']['temp_min'])
        humi = round(weather.json()['main']['humidity'])
        clear()
        aps()
        print("=============== Temperatura =============")
        print("")
        print(f"> Local: {location[0].upper()}{location[1:]}")
        print(f"> Temperatura: {temperature}° C")
        print(f"> O clima está: {description} com {humi}% de umidade.")
        print(f"> Sensação térmica de {feels_like}° C.")
        print(f"> Máxima de {high}° C e mínima de {low}° C.")
        print("")
        print(f"A temperatura prevista para amanhã é {predicted_tomorrow_temperature_rounded}° C.")
        print("=============== Temperatura =============")
        print("")
        print(">>> Possíveis Riscos e/ou Acontecimentos <<<")
        if temperature <= 0:
            print("> Atenção: Alerta de temperatura extremamente baixa")
            print("> Recomendação: Utilize roupas de frio extremo e evite exposição prolongada.")
            print("> Riscos: Risco de Hipotermia")
        elif temperature <= 10:
            print("> Atenção: Temperatura baixa")
            print("> Recomendação: Utilize roupas de frio.")
            print("> Riscos: Risco de Perniosis")
        elif temperature <= 15:
            print("> Atenção: Temperatura ligeiramente baixa")
            print("> Recomendação: Utilize roupas de frio.")
        elif temperature >= 50:
            print("> Atenção: Inferno na Terra")
            print("> Recomendação: Não saia de casa!")
        elif temperature >= 40:
            print("> Atenção: Temperatura extremamente alta")
            print("> Recomendação: Evite ao máximo exposição ao Sol.")
            print("> Riscos: Risco de Hipertermia")
        elif temperature > 30 and description == "céu limpo":
            print("> Atenção: Temperatura alta com céu limpo")
            print("> Recomendação: Use protetor solar.")
        elif temperature > 30 and description == "nublado":
            print("> Atenção: Temperatura alta com céu nublado")
            print("> Recomendação: Use protetor solar.")
        elif description == "tempestade":
            print("> Atenção: Alerta de Tempestade")
            print("> Recomendação: Evite áreas alagadas e busque abrigo.")
        elif description == "chuva":
            print("> Atenção: Risco de chuva")
            print("> Recomendação: Use guarda-chuva e/ou capa de chuva.")
        elif description == "névoa":
            print("> Atenção: Alerta de névoa.")
            print("> Recomendação: Evite exposição prolongada.")
        elif description == "chuva leve":
            print("> Atenção: Alerta de chuva leve.")
            print("> Recomendação: Use guarda-chuva.")
        elif description == "chuva moderada":
            print("> Atenção: Alerta de chuva moderada.")
            print("> Recomendação: Use guarda-chuva.")
        elif description == "chuva forte":
            print("> Atenção: Alerta de chuva forte.")
            print("> Recomendação: Use guarda-chuva e/ou busque abrigo.")
            print("> Riscos: Risco de alagamento.")
        else:
            print("> Nenhum, é seguro sair.")
        choicetemp = input("\n[1] Previsão 5 dias\n[2] Informações extras\n[3] Voltar\n\n> ")
        if choicetemp == "1":
            clear()
            aps()
            print("> Carregando informações...")
            forecast = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&lang=pt_br&appid={api_key}")
            forecast_data = forecast.json()
            list_of_forecasts = forecast_data['list']
            clear()
            aps()
            print("=============== Previsão =============")
            print("")
            for forecast in list_of_forecasts:
                date = forecast['dt_txt']
                temp_max = round(forecast['main']['temp_max'] - 273.15)
                temp_min = round(forecast['main']['temp_min'] - 273.15)
                weather_description = forecast['weather'][0]['description']
                print(f"Data: {date}, Máxima de: {temp_max}°C - Mínima de {temp_min}°C, Clima: {weather_description}")
            print("")
            print("=============== Previsão =============")
            close = input("\n> Insira qualquer tecla para voltar ao menu.\n\n> ")
            clear()
            aps()
            menu()
        elif choicetemp == "2":
            clear()
            aps()
            print("> Carregando informações...")
            pressure = round(weather.json()['main']['pressure'])
            wind = round(weather.json()['wind']['speed']) #m/s
            winddirect = round(weather.json()['wind']['deg']) #graus
            clear()
            aps()
            print("=============== Ar/Vento =============")
            print("")
            print("Pressão Atmosférica: {} HPA".format(pressure))
            print("Velocidade do Vento: {} m/s".format(wind))
            print("Direção do Vento: {}º".format(winddirect))
            print("")
            print(">>> Riscos de Exposição ao Vento <<<")
            if wind > 10:
                print("> Atenção: Vento forte")
                print("> Recomendação: Evite áreas abertas.")
            elif wind > 5:
                print("> Atenção: Vento moderado")
                print("> Recomendação: Evite áreas abertas.")
            else:
                print("> Nenhum, é seguro sair.")
            print("")
            print("=============== Ar/Vento =============")
            close = input("\n> Insira qualquer tecla para voltar ao menu.\n\n> ")
            clear()
            aps()
            menu()
        elif choicetemp == "3":
            clear()
            aps()
            menu()
        else:
            clear()
            print("Opção invalida.")
            close = input("\n> Insira qualquer tecla para voltar ao menu.\n\n> ")
            clear()
            aps()
            menu()
    elif choice == "2":
        clear()
        aps()
        print("> Carregando informações...")
        air = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}')
        co = air.json()['list'][0]['components']['co']
        so2 = air.json()['list'][0]['components']['so2']
        o3 = air.json()['list'][0]['components']['o3']
        no2 = air.json()['list'][0]['components']['no2']
        aqi = air.json()['list'][0]['main']['aqi']
        clear()
        aps()
        print("")
        print("=========== Qualidade de Ar ============")
        print(f"> Local: {location[0].upper()}{location[1:]}")
        print(f"> CO: {co} (Monóxido de Carbono)")
        if co <= 4400:
            costats = f"{GREEN}Bom{RESET}"
        elif 4400 <= co <= 9900:
            costats = f"{GREEN}Decente{RESET}"
        elif 9900 <= co <= 12400:
            costats = f"{YELLOW}Moderado{RESET}"
        elif 12400 <= co <= 15400:
            costats = f"{RED}Ruim{RESET}"
        elif co > 15400:
            costats = f"{RED}Extremamente ruim{RESET}"
        print("> Status:", costats)
        print(f"> SO2: {so2} (Dióxido de Enxofre)")
        if so2 <= 20:
            so2stats = f"{GREEN}Bom{RESET}"
        elif 20 <= so2 <= 80:
            so2stats = f"{GREEN}Decente{RESET}"
        elif 80 <= so2 <= 250:
            so2stats = f"{YELLOW}Moderado{RESET}"
        elif 250 <= so2 <= 350:
            so2stats = f"{RED}Ruim{RESET}"
        elif so2 > 350:
            so2stats = f"{RED}Extremamente ruim{RESET}"
        print("> Status:", so2stats)
        print(f"> O3: {o3} (Ozônio)")
        if o3 <= 60:
            o3stats = f"{GREEN}Bom{RESET}"
        elif 60 <= o3 <= 100:
            o3stats = f"{GREEN}Decente{RESET}"
        elif 100 <= o3 <= 140:
            o3stats = f"{YELLOW}Moderado{RESET}"
        elif 140 <= o3 <= 180:
            o3stats = f"{RED}Ruim{RESET}"
        elif o3 > 180:
            o3stats = f"{RED}Extremamente ruim{RESET}"
        print("> Status:", o3stats)
        print(f"> NO2: {no2} (Dióxido de Nitrogênio)")
        if no2 <= 40:
            no2stats = f"{GREEN}Bom{RESET}"
        elif 40 <= no2 <= 70:
            no2stats = f"{GREEN}Decente{RESET}"
        elif 70 <= no2 <= 150:
            no2stats = f"{YELLOW}Moderado{RESET}"
        elif 150 <= no2 <= 200:
            no2stats = f"{RED}Ruim{RESET}"
        elif no2 > 200:
            no2stats = f"{RED}Extremamente ruim{RESET}"
        print("> Status:", no2stats)
        print("\n>>> Riscos de Exposição ao Ar <<<")
        if co > 15400 or so2 > 350 or o3 > 180 or no2 > 200:
            print("> Risco: Evite ao máximo exposição ao ar.")
        elif co > 12400 or so2 > 250 or o3 > 140 or no2 > 150:
            print("> Risco: Reduza a exposição ao ar.")
        else:
            print("> Risco: Nenhum, é seguro ficar exposto ao ar.")
        print("")
        print("=========== Qualidade de Ar ============")
        close = input("\n> Insira qualquer tecla para voltar ao menu.\n\n> ")
        clear()
        aps()
        menu()
    elif choice == "3":
        clear()
        aps()
        print("=============== Tabelas de Informação =============")
        print("\n> Índice de Qualidade do Ar (AQI):")
        print("\n> O Índice de Qualidade do Ar (AQI) é um indicador que informa a qualidade do ar em uma determinada região. Ele é calculado com base em diversos poluentes atmosféricos, como o CO, SO2, NO2, PM10, PM2.5, O3 e NH3. O AQI varia de 0 a 500, sendo que quanto maior o valor, pior a qualidade do ar. O AQI é dividido em 6 categorias, que são:\n")
        print(f"{'Qualidade':<12} {'Index':<6} {'SO2':<10} {'NO2':<10} {'PM10':<10} {'PM2.5':<10} {'O3':<10} {'CO':<10}")
        print(f"{'Bom':<12} {'1':<6} {'[0; 20)':<10} {'[0; 40)':<10} {'[0; 20)':<10} {'[0; 10)':<10} {'[0; 60)':<10} {'[0; 4400)':<10}")
        print(f"{'Decente':<12} {'2':<6} {'[20; 80)':<10} {'[40; 70)':<10} {'[20; 50)':<10} {'[10; 25)':<10} {'[60; 100)':<10} {'[4400; 9400)':<10}")
        print(f"{'Moderado':<12} {'3':<6} {'[80; 250)':<10} {'[70; 150)':<10} {'[50; 100)':<10} {'[25; 50)':<10} {'[100; 140)':<10} {'[9400-12400)':<10}")
        print(f"{'Ruim':<12} {'4':<6} {'[250; 350)':<10} {'[150; 200)':<10} {'[100; 200)':<10} {'[50; 75)':<10} {'[140; 180)':<10} {'[12400; 15400)':<10}")
        print(f"{'Muito Ruim':<12} {'5':<6} {'⩾350':<10} {'⩾200':<10} {'⩾200':<10} {'⩾75':<10} {'⩾180':<10} {'⩾15400':<10}")
        print("")
        print("=============== Tabelas de Informação =============")
        print("\n> Outros parâmetros que não afetam o cálculo do Índice de Qualidade do Ar (AQI):")
        print("\nNH3: valor min 0.1 - valor max 200")
        print("NO: valor min 0.1 - valor max 100")
        close = input("\n> Insira qualquer tecla para voltar ao menu.\n\n> ")
        clear()
        aps()
        menu()
    elif choice == "4":
        clear()
        aps()
        print("=============== Riscos de Temperatura/Clima =============")
        print("")
        print("> Riscos de Temperatura:")
        print("> Temperatura <= 0: Risco de Hipotermia")
        print("> Temperatura <= 10: Risco de Perniosis")
        print("> Temperatura > 30 e Céu Limpo: Risco de Queimadura Solar")
        print("> Temperatura > 30 e Nublado: Risco de Queimadura Solar")
        print("> Temperatura >= 40: Risco de Hipertermia")
        print("--------------------")
        print("> Névoa: Risco de Visibilidade")
        print("> Chuva Leve: Risco de Molhar-se")
        print("> Chuva Moderada: Risco de Molhar-se")
        print("> Chuva Forte: Risco de Alagamento")
        print("> Tempestade: Risco de Raios")
        print("")
        print("=============== Riscos de Temperatura/Clima =============")
        print("")
        choicerisk = input("\n[1] Riscos de Qualidade do Ar\n[2] Voltar ao menu\n\n> ")
        if choicerisk == "1":
            clear()
            aps()
            print("=============== Riscos de Qualidade do Ar =============")
            print("")
            print("> Riscos de Qualidade do Ar:")
            print("> CO > 15400: Evite ao máximo exposição ao ar")
            print("> SO2 > 350: Evite ao máximo exposição ao ar")
            print("> O3 > 180: Evite ao máximo exposição ao ar")
            print("> NO2 > 200: Evite ao máximo exposição ao ar")
            print("--------------------")
            print("> CO > 12400: Reduza a exposição ao ar")
            print("> SO2 > 250: Reduza a exposição ao ar")
            print("> O3 > 140: Reduza a exposição ao ar")
            print("> NO2 > 150: Reduza a exposição ao ar")
            print("")
            print("=============== Riscos de Qualidade do Ar =============")
            close = input("\n> Insira qualquer tecla para voltar ao menu.\n\n> ")
            clear()
            aps()
            menu()
        elif choicerisk == "2":
            clear()
            aps()
            menu()
    elif choice == "5":
        clear()
        aps()
        print("=============== Creditos =============")
        print("")
        print("> Desenvolvido por:")
        print("> João Pedro Villas Boas de Carvalho")
        print("")
        print("> API utilizada:")
        print("> OpenWeatherMap")
        print("")
        print("=============== Creditos =============")
        close = input("\n> Insira qualquer tecla para voltar ao menu.\n\n> ")
        clear()
        aps()
        menu()
    elif choice == "6":
        exit()
    else:
        clear()
        print("Opção invalida.")
        close = input("\n> Insira qualquer tecla para voltar ao menu.\n\n> ")
        clear()
        aps()
        menu()
menu()
