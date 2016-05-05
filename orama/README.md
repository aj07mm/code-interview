# Orama
Prova para admissão na Orama
---

O banco AMARO gostaria de implementar um sistema de depósitos e saques em contas de clientes

### Estorias:

#### Client (cliente)

Visitante se torna um cliente do banco ao se registrar em `/accounts/register/`

- Como visitante, gostaria de abrir uma conta no banco

   cliente tem o poder de criar contas e adicionar valores na criação da mesma em `/account/create/`

- Como correntista do banco, gostaria de fazer uma operação de depósito de uma quantia em dinheiro;

   cliente faz depositos clicando em 'deposit' na tela `/account/` de acordo com a conta

- Como correntista do banco, gostaria de fazer uma operação de saque de uma quantia em dinheiro;

   cliente faz depositos clicando em 'withdraw' na tela `/account/` de acordo com a conta

- Como correntista do banco, gostaria de ver meu saldo disponível;

   cliente pode ver o total de cada conta em `/account/` ou ver detalhes em `/account/:id`

   cliente pode ver o total de balanço de todas as suas contas no canto superior esquerdo da tela

---

#### Manager (administrador do banco)

Administrador do banco é criado somente pelo `superuser` em `/admin`

Administrador do banco pode acessar a lista de relatórios por `/report/`

- Como administrador do banco, gostaria de ver um relatório que me apresentasse o código do cliente, o nome do cliente, o CPF do cliente, o tipo de operação, data da operação e o valor;

   Administrador do banco pode ver este relatório em `/report/account/transaction/`

- Como administrador do banco, gostaria de saber o saldo em conta de todos os clientes;

   Administrador do banco pode ver este relatório em `/report/account/balance/`

- Como administrador do banco, gostaria de ver quanto dinheiro foi depositado no banco em cada dia;

   Administrador do banco pode ver este relatório em `/report/account/transaction/deposit/`

- Como administrador do banco, gostaria de ver quanto dinheiro foi sacado no banco em cada dia;

   Administrador do banco pode ver este relatório em `/report/account/transaction/withdraw/`

---

#### superuser info:

	login: root
	password: 123123

----

## How to run:


### Prepare environment:

#####installing virutalenv

	$ pip install virtualenv
	$ virtualenv orama_env
	$ source orama_env/bin/activate

#####install bower:

	$ npm install -g bower

### Install dependencies:

#####Loading Dependencies, Migrations and Fixtures

	$ pip install -r requirements.txt

	$ python manage.py migrate
	$ python manage.py loaddata initial_data.json

#####Loading frontend stuff

	$ python manage.py bower install

if you are root:

	$ python manage.py bower_install -- --allow-root --no-input

then:

	$ python manage.py collectstatic

#####Running server

	$ python manage.py runserver 0.0.0.0:8000

---

### How to run tests:

	$ python manage.py test

--

### Links:

	http://localhost:8000/      # bank app
	http://localhost:8000/admin # superuser admin area

--

### Demo:

- [http://159.203.89.204:8000/](http://159.203.89.204:8000/)