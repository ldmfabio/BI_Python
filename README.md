# Como _brincar_ com o repositório

> Este repositório foi criado seguindo os passos disponíveis no vídeo [É o fim do Power BI? Criando Dashboard com Python em 15 minutos](https://www.youtube.com/watch?v=P6E_Kts9pxE)

_Alguns filtros adicionais foram colocados para dinamizar o dashboard._

**Libs utilizadas:** *streamlit, pandas, plotly.express*

## Criando o ambiente virtual
```
python3 -m venv venv
```
Este comando cria um ambiente virtual, chamado venv, na pasta atual. O nome do ambiente virtual pode ser alterado, porém é recomendado que seja mantido o nome venv.

## Habilitando o ambiente virtual
```
source venv/bin/activate
```

## Instalando as dependências
```
pip install -r requirements.txt
```
O arquivo requirements foi gerado com o comando `pip freeze > requirements.txt` e contém todas as dependências instaladas no ambiente virtual.

## Executando o streamlit
```
streamlit run dashboards.py
```
O streamlit é uma ferramenta que permite a criação de dashboards de forma simples e rápida. Para mais informações, acesse o [site oficial](https://streamlit.io/).

## Desabilitando o ambiente virtual
```
deactivate
```