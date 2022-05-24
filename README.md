# Streamlit Dashboard para análise e visualização de dados
Meu primeiro dashboard Streamlit para analisar dados de viagens Uber na cidade de Nova York em Setembro de 2014.
Interativo, com utilização de alguns filtros para exibição dos dados. Projeto do curso Sigmoidal com algumas poucas alterações feitas por mim.

### URL do banco de dados:
https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz

### Pacotes utilizados:
1. Pandas
2. Numpy
3. Streamlit

### Como instalar o Streamlit e rodar a aplicação:
No Terminal, instalar o Streamlit:
```console
$ pip install streamlit
```
Após a instalação, rodar a aplicação:
```console
$ python -m streamlit run uber.py
```

## Interagindo com a aplicação
Ao rodar a aplicação, uma janela será aberta no navegador.

### Carregando os dados para análise:
Após carregar toda a página, no menu lateral altere o número de linhas a serem analisadas para 1000 ou um número de sua escolha.
![image](https://user-images.githubusercontent.com/25406715/170102173-47814e71-8934-4758-af48-5ccf5487e7d2.png)

### Visualizando os dados:
**Planilha**
Para visualizar os dados gerais, no menu lateral marque a caixa Dados. Será exibido na página principal uma planilha com as primeiras 1000 linhas do banco de dados.
![image](https://user-images.githubusercontent.com/25406715/170102111-f9445aa3-7d3a-470e-8363-118cc90406f1.png)

**Mapa**
Para visualizar os dados no mapa, no menu lateral marque a caixa Mapa e escolha um horário a ser analisado. Será exibido na página principal um mapa com a localização das viagens realizadas no horário definido. A quantidade total de viagens é exibida acima do mapa.
![image](https://user-images.githubusercontent.com/25406715/170102907-57e2faff-1f7c-4610-b192-23a47e05383d.png)

**Histograma**
Para visualizar o histograma dos dados, no menu lateral marque a caixa Histograma. Será exibido na página principal o histograma da quantidade de viagens por hora.
![image](https://user-images.githubusercontent.com/25406715/170103312-b57ceaa8-301b-4072-a597-532dc345da8e.png)
