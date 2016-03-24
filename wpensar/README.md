# Desafio WPensar
reference: [https://bitbucket.org/wpensar/querotrabalharnawpensar]

Tasks:

- Cadastro de produtos (Nome) OK! -> Product(name, price, average_price)
- Compra de produtos (Produto, quantidade e preço de compra) OK! -> Purchase(product, cart_uuid, quantity, total_price)
- Listagem dos produtos comprados separados por compra (Nome, quantidade, preço de compra, preço médio)
Exibição da fila de processamento das tarefas de calculo de preço médio (Aguardando, Em execução, Executados) - O processamento é - feito em tempo real
- Ser fácil de configurar e rodar em ambiente Unix (Linux ou Mac OS X) - Linux OK! OSX faltam alguns testes
- Ser WEB - OK!
- Ser escrita em Python 2.7+ OK! -> python --version # Python 2.7.10
- Só deve utilizar biliotecas livres e gratuitas OK! -> OK! Django REST framework e AngularJS

Bonus:

- Autenticação e autorização (se for com OAuth, melhor ainda) - Cheguei a fazer um branch com oauth mas iria perder muito tempo estruturando um passo a passo de como usar através da api pois não há login no front
- Ter um design bonito OK! - Skeleton + SweetAlert + Ionic Icons
- Testes automatizados OK! - Teste de metodos da API + ambiente configurado de testes front com karma sem testes :/

---

### Step-by-step

OBS: The app assumes that you are consuming the api on 'localhost',
if isn't the case, change the path on 'www/js/app.js':

	'apiPath' : 'http://localhost:8000',

then:

	$ git clone https://bitbucket.org/aj07mm/querotrabalharnawpensar
	$ cd querotrabalharnawpensar

	$ sudo bash install.sh # install dependencies
	$ sudo bash startup.sh # startup application

Run Api tests:

	$ python api/manage.py test

Run Frontend tests: (make sure you have Chrome installed, otherwise create a new config file)

	$ npm install
	$ cd www/
	$ npm test

Then check the console after the browser open.

---

Demo:

- application: http://192.241.203.151:8080/
- api: http://192.241.203.151:8000/