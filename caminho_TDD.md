# Test Driven Development (TDD) na Prática

## Uma demonstração com uso do framework Django

Apresentação no Caypira 2026


### O que temos até aqui ?

Nesta sprint, temos um CRUD simples sem testes. 
Nossa primeira missão é aumentar a cobertura de testes do projeto:


### Primeiros testes

Editar o arquivo <b>estagios/core/tests</b>

```console
from django.test import TestCase

class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/index')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Vagas de estágio')
```

Após inserir o código acima, execute o comando:

```console
python manage.py test
coverage run --source='.' manage.py test 
coverage report
```

O que aconteceu ?


### Testes para GET

Editar o arquivo  <b>estagios/core/tests</b>. Insira os novos testes:

```console
class CreateTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/create')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Cadastrar vaga')

    def test_form_presente(self):
        self.assertContains(self.resp, '<form')

    def test_csrf_presente(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


class ReadTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/read')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Listar vagas')


class UpdateTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/update')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Gerencie e atualize as vagas cadastradas abaixo')


class ConfirmUpdateTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/confirm_update')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Ver todas as vagas')

    def test_form_presente(self):
        self.assertContains(self.resp, '<form')


class DeleteTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/delete')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Remover vaga')
```

Após inserir o código acima, execute o comando:

```console
python manage.py test
coverage run --source='.' manage.py test 
coverage html
```

O que aconteceu ?

### Testes para POST

Editar o arquivo  <b>estagios/core/tests</b>. Insira os novos testes:

```console
from core.models import VagaModel


class CreatePostTest(TestCase):
    def setUp(self):
        self.dados_validos = {
            'titulo': 'Desenvolvedor back-end',
            'empresa': 'Acme Tecnologia',
            'telefone': '19 99999-0000',
        }

    def test_post_valido_redireciona(self):
        resp = self.client.post('/create', self.dados_validos)
        self.assertEqual(302, resp.status_code)

    def test_post_valido_cria_registro(self):
        self.client.post('/create', self.dados_validos)
        self.assertEqual(1, VagaModel.objects.count())

    def test_post_invalido_retorna_200(self):
        resp = self.client.post('/create', {})
        self.assertEqual(200, resp.status_code)

    def test_post_invalido_nao_cria_registro(self):
        self.client.post('/create', {})
        self.assertEqual(0, VagaModel.objects.count())

    def test_post_invalido_exibe_form_com_erros(self):
        resp = self.client.post('/create', {})
        self.assertContains(resp, 'form')


class ReadPostTest(TestCase):
    def setUp(self):
        self.vaga = VagaModel.objects.create(
            titulo='Analista de dados',
            empresa='Acme Tecnologia',
            telefone='(19) 99999-0000',
        )

    def test_post_com_id_valido_retorna_200(self):
        resp = self.client.post('/read', {'id': self.vaga.pk})
        self.assertEqual(200, resp.status_code)

    def test_post_com_id_valido_exibe_vaga(self):
        resp = self.client.post('/read', {'id': self.vaga.pk})
        self.assertContains(resp, 'Analista de dados')

    def test_post_com_id_invalido_retorna_200(self):
        resp = self.client.post('/read', {'id': 'abc'})
        self.assertEqual(200, resp.status_code)

    def test_post_sem_id_retorna_200(self):
        resp = self.client.post('/read', {})
        self.assertEqual(200, resp.status_code)


class UpdatePostTest(TestCase):
    def setUp(self):
        self.vaga = VagaModel.objects.create(
            titulo='Designer UX/UI',
            empresa='Acme Tecnologia',
            telefone='(19) 99999-0000',
        )

    def test_post_com_id_valido_retorna_200(self):
        resp = self.client.post('/update', {'id': self.vaga.pk})
        self.assertEqual(200, resp.status_code)

    def test_post_com_id_valido_exibe_form_preenchido(self):
        resp = self.client.post('/update', {'id': self.vaga.pk})
        self.assertContains(resp, 'Designer UX/UI')

    def test_post_com_id_invalido_retorna_200(self):
        resp = self.client.post('/update', {'id': 'abc'})
        self.assertEqual(200, resp.status_code)

    def test_post_sem_id_retorna_200(self):
        resp = self.client.post('/update', {})
        self.assertEqual(200, resp.status_code)


class ConfirmUpdatePostTest(TestCase):
    def setUp(self):
        self.vaga = VagaModel.objects.create(
            titulo='Desenvolvedor front-end',
            empresa='Acme Tecnologia',
            telefone='19 99999-0000',
        )
        self.dados_validos = {
            'id': self.vaga.pk,
            'titulo': 'Desenvolvedor full-stack',
            'empresa': 'Nova Empresa',
            'telefone': '19 98888-1111',
        }

    def test_post_valido_retorna_200(self):
        resp = self.client.post('/confirm_update', self.dados_validos)
        self.assertEqual(200, resp.status_code)

    def test_post_valido_atualiza_registro(self):
        self.client.post('/confirm_update', self.dados_validos)
        self.vaga.refresh_from_db()
        self.assertEqual('DESENVOLVEDOR FULL-STACK', self.vaga.titulo)

    def test_post_invalido_retorna_200(self):
        resp = self.client.post('/confirm_update', {'id': self.vaga.pk})
        self.assertEqual(200, resp.status_code)

    def test_post_invalido_nao_atualiza_registro(self):
        self.client.post('/confirm_update', {'id': self.vaga.pk})
        self.vaga.refresh_from_db()
        self.assertEqual('Desenvolvedor front-end', self.vaga.titulo)

    def test_post_id_inexistente_retorna_404(self):
        self.dados_validos['id'] = 9999
        resp = self.client.post('/confirm_update', self.dados_validos)
        self.assertEqual(404, resp.status_code)


class DeletePostTest(TestCase):
    def setUp(self):
        self.vaga = VagaModel.objects.create(
            titulo='Desenvolvedor back-end',
            empresa='Acme Tecnologia',
            telefone='(19) 99999-0000',
        )

    def test_post_com_id_valido_retorna_200(self):
        resp = self.client.post('/delete', {'id': self.vaga.pk})
        self.assertEqual(200, resp.status_code)

    def test_post_com_id_valido_remove_registro(self):
        self.client.post('/delete', {'id': self.vaga.pk})
        self.assertEqual(0, VagaModel.objects.count())

    def test_post_com_id_invalido_retorna_200(self):
        resp = self.client.post('/delete', {'id': 9999})
        self.assertEqual(200, resp.status_code)

    def test_post_com_id_invalido_nao_remove_registro(self):
        self.client.post('/delete', {'id': 9999})
        self.assertEqual(1, VagaModel.objects.count())

    def test_post_sem_id_retorna_200(self):
        resp = self.client.post('/delete', {})
        self.assertEqual(200, resp.status_code)
```

Após inserir o código acima, execute o comando:

```console
python manage.py test
coverage run --source='.' manage.py test 
coverage report
```

O que aconteceu ?

### O caminho do TDD

No TDD, o ciclo segue três etapas: escreve-se um teste que falha (pois o código ainda não existe), implementa-se o mínimo de código necessário para fazê-lo passar e, por fim, refatora-se o código mantendo os testes verdes. 

Aqui, como as views já estavam prontas e com comportamento definido, os testes foram moldados ao que o código já faz, o que pode criar um viés: em vez de especificar o comportamento desejado, os testes acabam documentando o comportamento existente — inclusive eventuais falhas de design que passariam despercebidas num processo TDD.

Após inserir o código abaixo no arquivo de testes:

```console

class RootTest(TestCase):
    def test_200_response(self):
        self.resp = self.client.get('/', follow=True)
        self.assertEqual(200, self.resp.status_code)

    def test_302_response(self):
        self.resp = self.client.get('/')
        self.assertEqual(302, self.resp.status_code)
```

Execute os testes

```console
python manage.py test
coverage run --source='.' manage.py test 
coverage report
```

O que aconteceu ?


Editar o arquivo <b>estagios/core/urls.py</b>

```console
urlpatterns = [
    ...
    path('', views.root, name='root'),
    ...
]
```


Editar o arquivo <b>estagios/core/views.py</b>

```console

def root(request):
    return HttpResponseRedirect(reverse('core:index'))

```

Após inserir os códigos, execute os comandos:

```console
python manage.py test
coverage run --source='.' manage.py test 
coverage report
```

O que aconteceu ?