# Nanodegree Desenvolvedor Web Full-Stack Udacity
## Projeto: Site de Trailer de Filmes

### Instalação

Este projeto requer **Python 2.7** que pode ser baixado e instalado através desse link: [Python 2.7](https://www.python.org/download/releases/2.7/)

Também foi utilizada a API [tmdbsimple 2.2.0] (https://pypi.org/project/tmdbsimple/#description) que pode ser instalado usando **pip install tmdbsimple**

### Código

O arquivo `entertainment_center.py` armazena a chave da API *tmdbsimple* que irá se comunicar com o IMDB e obter as informações dos filmes.
Também nesse arquivo consta uma matriz com o código dos 6 filmes que farão parte do carrousel.
Utilizando da classe declarada no arquivo `media.py` os filmes tem suas informações obtidas.
Por fim, é chamada a função que monta dinamicamente o html, que está no arquivo `fresh_tomatoes.py`.

### Execução
O resultado do processamento acima é o arquivo fresh_tomatoes.html que implementa a página de trailer de filmes.

### Dados
Os filmes escolhidos foram selecionados no IMDB.

