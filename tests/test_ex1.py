from pytest_django.asserts import assertTemplateUsed
import pytest

def test_rota_admin(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200

def test_rota_index(admin_client):
    response = admin_client.get('/')
    assert response.status_code == 200

def test_rota_adicionar_contatos(admin_client):
    response = admin_client.get('/accounts/dashboard/')
    assert response.status_code == 200


def test_criar_novo_usuario(django_user_model):
    django_user_model.objects.create(username="teste", password="teste",
    )

def test_login_com_novo_usuario(client, django_user_model):
    username = "usuario-teste"
    password = "teste"

    user = django_user_model.objects.create_user(username=username, password=password)

    client.force_login(user)
    
    