# 🌦️ PyClima - Consulta de Clima e Qualidade do Ar 🌦️

Desenvolvido por **João Pedro Villas Boas de Carvalho**

Uma ferramenta de linha de comando em Python para consultar informações meteorológicas atuais, qualidade do ar, previsões básicas e avaliação de riscos para uma cidade específica, utilizando a API **OpenWeatherMap**. Insira o nome da cidade e navegue por um menu interativo para obter dados detalhados sobre temperatura, condições do ar, e possíveis riscos associados.

**IMPORTANTE**

Criei este programa sozinho para um projeto da faculdade, com prazo apertado. Por isso, algumas partes podem ser mais conceituais ou focadas em cumprir requisitos específicos. Fique à vontade para explorar, modificar e usar o código como quiser! :D

---

## 🔧 Funcionalidades

- ✅ **Consulta de Tempo Atual:** Exibe temperatura atual, sensação térmica, máxima, mínima, descrição do clima (ex: céu limpo, chuva) e umidade.
- ✅ **Qualidade do Ar:** Mostra os níveis de poluentes como CO, SO2, O3, NO2 e fornece um status qualitativo (Bom, Ruim, etc.) com base em limiares padrão.
- ✅ **Previsão Simples para Amanhã:** Utiliza Regressão Linear (com dados históricos *hardcoded* no script) para estimar a temperatura do dia seguinte. **Nota:** A precisão depende dos dados históricos fornecidos no código.
- ✅ **Previsão Estendida (5 dias):** Busca e exibe a previsão do tempo em intervalos de 3 horas para os próximos 5 dias.
- ✅ **Informações Adicionais:** Inclui dados sobre pressão atmosférica, velocidade e direção do vento.
- ✅ **Avaliação de Riscos:** Fornece alertas e recomendações básicas com base na temperatura (muito baixa/alta), condições climáticas (chuva forte, tempestade, névoa) e níveis de qualidade do ar.
- ✅ **Interface de Console Clara:** Interação via terminal com menu de fácil navegação e feedback visual usando cores.
- ✅ **Tabelas Informativas:** Apresenta tabelas que explicam o Índice de Qualidade do Ar (AQI) e os limiares para diferentes poluentes.

---

## 🚀 Tecnologias Utilizadas

- **Linguagem Principal:** Python 3.x
- **Requisições HTTP:** `requests` (para consumir a API OpenWeatherMap)
- **Manipulação Numérica:** `numpy` (usado na parte de previsão de temperatura)
- **Machine Learning (Básico):** `scikit-learn` (especificamente `LinearRegression` para a previsão)
- **Interação com SO:** `os` (para limpar a tela do console - `cls`/`clear`)
- **API Externa:** OpenWeatherMap API (para dados de clima e qualidade do ar)

---

## ⚙️ Configuração e Uso

### 🔹 Passo 1: Pré-requisitos

- Garanta que você tem o **Python 3** instalado. Verifique com `python --version` ou `python3 --version`.
- Você precisará do `pip` (gerenciador de pacotes do Python), que geralmente acompanha o Python.

### 🔹 Passo 2: Obter o Código

- Faça o download ou clone o arquivo Python (`.py`) contendo o script.

### 🔹 Passo 3: Chave da API OpenWeatherMap

- **Importante:** Este script requer uma chave de API (API Key) da OpenWeatherMap.
    1. Registre-se gratuitamente em [https://openweathermap.org/](https://openweathermap.org/) para obter sua chave.
    2. Abra o arquivo Python em um editor de texto.
    3. Encontre a linha: `api_key = ""`
    4. Substitua as aspas vazias pela sua chave de API: `api_key = "SUA_CHAVE_API_AQUI"`
    5. Salve o arquivo.

### 🔹 Passo 4: Instalar Dependências

1.  Navegue até o diretório onde você salvou o script usando seu terminal ou prompt de comando:
    ```bash
    cd /caminho/para/o/diretorio/do/script
    ```
2.  Instale as bibliotecas Python necessárias:
    ```bash
    pip install requests scikit-learn numpy
    ```
    * `requests`: Para fazer as chamadas à API.
    * `scikit-learn` e `numpy`: Para a funcionalidade de previsão de temperatura.

### 🔹 Passo 5: (Opcional/Importante) Atualizar Dados Históricos de Temperatura para Previsão

- A previsão de temperatura para o dia seguinte usa um array `numpy` chamado `temperatures` que está **hardcoded** no script:
    ```python
    #Temperatura dos ultimos 30 dias: (Alterar conforme necessário para a sua cidade.)
    temperatures = np.array([20, 21, ..., 23, 24])
    ```
- Esses dados são estáticos e podem não ser relevantes para a sua cidade ou para o período atual. Para uma previsão minimamente significativa (dentro das limitações do método usado), você **deve** substituir esses valores por dados históricos de temperatura reais da sua localidade.
- A linha `today_temperature = np.array([[25]])` também está hardcoded e influencia a previsão. Idealmente, deveria usar a temperatura atual real.

### 🔹 Passo 6: Executar o Script

- Execute o programa a partir do seu terminal:
    ```bash
    python nome_do_seu_script.py
    ```
    *(Substitua `nome_do_seu_script.py` pelo nome real do arquivo)*

### 🔹 Passo 7: Interagir com o Console

1.  Você verá um banner de boas-vindas e o prompt inicial:
    ```
        ____  ____  ____     __________________
       / __ \/ __ \/ __ \   / / ____/_  __/ __ \
      / /_/ / /_/ / / / /_ / / __/   / / / / / /
     / ____/ _, _/ /_/ / /_/ / /___  / / / /_/ /
    /_/   /_/ |_|\____/\____/_____/ /_/  \____/

    > Digite sua cidade:
    ```
2.  Digite o nome da cidade desejada (ex: `São Paulo`) e pressione Enter.
3.  Após carregar os dados, o menu principal será exibido:
    ```
    ============== Menu Principal ==============

    > Local escolhido: São Paulo

    > Escolha uma opção:
    > [1] Temperatura
    > [2] Qualidade de Ar
    > [3] Tabelas de Informação
    > [4] Lista Completa de Riscos
    > [5] Creditos
    > [6] Sair

    ============================================

    >
    ```
4.  Digite o número da opção desejada e pressione Enter para ver as informações correspondentes.
5.  Siga as instruções em cada submenu. Geralmente, você precisará pressionar Enter ou digitar um número para voltar ao menu principal ou sair.
6.  Escolha a opção `6` para sair do programa.

---

## 🌐 Acessando as Funcionalidades

- **Console / Terminal:** Toda a interação com o script ocorre diretamente no terminal onde ele foi executado.
- **Menu Principal:** Use os números de 1 a 6 para navegar entre as diferentes seções de informação (Temperatura, Qualidade do Ar, Tabelas, Riscos, Créditos, Sair).
- **Submenus:** Algumas seções (como Temperatura e Riscos) possuem submenus para informações mais detalhadas ou relacionadas.

---

## 🧠 Exemplos de Limitações e Possíveis Melhorias Futuras

- 💾 **Previsão de Temperatura Simplista:** A previsão atual usa dados históricos *hardcoded* e um modelo `LinearRegression` básico. A precisão é limitada e depende fortemente da atualização manual desses dados. Melhorias: buscar dados históricos reais via API, usar modelos de séries temporais mais adequados (como ARIMA ou Prophet), ou simplesmente confiar na previsão da própria API OpenWeatherMap.
- ⚙️ **Configuração da API Key:** A chave da API está diretamente no código. Seria melhor movê-la para um arquivo de configuração (`.env`, `.ini`) ou variável de ambiente para segurança e facilidade de alteração.
- 🏙️ **Validação de Cidades:** Embora verifique o '404', poderia haver tratamento para cidades homônimas em países diferentes (a API `geo/1.0/direct` pode retornar múltiplas opções).
- 📊 **Visualização:** Adicionar gráficos simples (talvez usando `matplotlib` ou `rich`) para visualizar a previsão de 5 dias ou os níveis de poluição poderia ser útil.
- 🛡️ **Tratamento de Erros:** Adicionar mais blocos `try-except` para lidar com possíveis falhas na conexão com a API ou dados inesperados.
- 🌐 **Internacionalização:** Facilitar a tradução dos textos da interface para outros idiomas.

---

## 👨‍💻 Autor

**João Pedro Villas Boas de Carvalho**
