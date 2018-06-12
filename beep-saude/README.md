# Beep Saude

![](https://s3-us-west-2.amazonaws.com/aj07mm-public-files/Screenshot+from+2018-05-21+14-58-51.png)

*demo:* http://ec2-18-237-179-106.us-west-2.compute.amazonaws.com/

# How to run

	make run

	try: http://localhost:80/

*Obs:* _Make sure you have docker and docker-compose installed_



# Requirements

Preciso que em meu site tenha uma página com um gráfico que apresente a cotação dos últimos sete dias para real versus dólar, euro e pesos argentinos. 
A página deve ter três botões (um para cada uma das moedas) e, ao clicar nos botões, apareceria o gráfico de linha com os valores abaixo dos botões. 
Parecido com esse site aqui: http://economia.uol.com.br/cotacoes/cambio/euro-uniao-europeia/

### Existem algumas restrições que devem ser seguidas:

    - Os dados das cotações devem ser coletados utilizando a api do http://jsonrates.com/;
    - O código deve ser desenvolvido utilizando um repositório git público no seu perfil do Github ou BitBucket;
    - Backend: pode ser implementando em qualquer linguagem.
    - Frontend: o único requisito é usar o highcharts para apresentação dos dados. 
    - Não precisa de login, usuário, autenticação ou qualquer coisa. Só a página carregando o gráfico.

    Bônus:

    - deploy no heroku ou em outro servidor de sua preferência

### O que será avaliado?

    - a clareza do código escrito
    - o uso de Orientação a Objetos
    - o entendimento de práticas de desenvolvimento como testes automatizados, utilização correta do controle de versão conhecimento do framework escolhido
