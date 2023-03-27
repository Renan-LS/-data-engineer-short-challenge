# Resolução desafio de engenheria de dados da REFERA #
- Segue resolução do desafio de Engenharia de dados da REFERA no qual foram criados 02(dois) scripts em *python* que realizam o trabalho de EL(Extract and Load).
  - No script **main_local.py**, é realizado a rotina de extração total de todas as tabelas do banco de dados `transactional` e carregadas para o banco de dados `analytics`. [Objetivo do desafio - **Solução 1**]
  
  - Já o script **main.py** é usado em conjunto com docker-compose.yml[modificado]. Este compose é responsável não só por upar os containers contendo os bancos de dados `transactional` e `analytics`. Ele também upa um serviço contendo `Python 3.9` e todas as dependencias necessárias para rodar o script main.py, realizando assim o pipeline de Extração e Carregamento dos dados totalmente via DOCKER. [Diferencial na implementação - **Solução 2**]

*PS: Tanto para solução 1, quanto para solução 2, é necessário que seja realizado os passos descritos ao fim desta página: realização do Git Clone com a posterior execução do Compose.*




## Seja bem vindo ao desafio de engenharia de dados da Refera!


O objetivo desse desafio é ser algo rápido para exemplificar alguns desafios do dia a dia de quem trabalha com dados. Queremos com esse desafio avaliar o seu conhecimento básico em programação, banco de dados e entender mais quais as boas práticas você segue para construção de código.


## O desafio

Pensando em não sobrecarregar nosso banco de dados transacional, precisamos ter um ambiente separado para analisar nossos dados sem grandes problemas. Assim, escreva um código local que faça uma extração total de todas as tabelas do banco de dados `transactional` e as carregue para o banco de dados `analytics`.

O arquivo [docker-compose.yml](docker-compose.yml) ativa containers com os bancos de dados `transactional` e `analytics`.

![Infra dos banco de dados](fluxo.png)

Diferenciais na implementação:
- script rodando dentro do docker

## Configuração do Ambiente

Os banco de dados podem ser configurados usando o docker compose. Você pode instalá-lo seguindo as instruções em https://docs.docker.com/compose/install/.

Clone o repositório:


```bash
git clone https://github.com/Renan-LS/-refera-data-engineer-short-challenge
```

Com o docker compose instalado, basta executar:

```bash
cd -refera-data-engineer-short-challenge
docker-compose up
```
