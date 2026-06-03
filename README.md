# Test Driven Development (TDD) na Prática

## Uma demonstração com uso do framework Django

Apresentação no Caypira 2026



No ambiente Linux:

```console
git clone https://github.com/orlandosaraivajr/caypira26.git
cd caypira26/
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd estagios/
python manage.py makemigrations
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py runserver
```

No ambiente Windows:

```console
git clone https://github.com/orlandosaraivajr/caypira26.git
cd caypira26/
virtualenv venv
cd venv
cd scripts
activate.bat
cd ..
cd ..
pip install -r requirements.txt
cd estagios/
python manage.py makemigrations
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py runserver

```

### Sprint 1

O projeto apresenta um cadastro de vagas de estágio. 

Na rota index (/index), se apresenta quatro botões, conforme imagem abaixo:
<img src="img/index.png">

Ao acessar a rota cadastro (/create), é possível cadastrar o contato, que armazena as seguintes informações:

- Título
- Empresa
- Telefone

<img src="img/create.png">

Ao acessar a rota read (/read), Nenhum contato está cadastrado:

<img src="img/read_1.png">
Após cadastrar uma vaga, rota listar (/read), lista todas as vagas cadastradas:
<img src="img/read_2.png">
<img src="img/read_3.png">

Ao acessar a rota update (/update), é possível selecionar e atualizar uma vaga:

<img src="img/update_1.png">
<img src="img/update_2.png">
<img src="img/update_3.png">

Ao acessar a rota delete (/delete), é possível remover um contato:

<img src="img/delete_1.png">

