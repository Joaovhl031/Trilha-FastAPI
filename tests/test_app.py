from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')

    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'user': 'Joao',
            'email': 'joaohenrique@example.com',
            'password': '123',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'user': 'Joao',
        'email': 'joaohenrique@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'user': 'Joao',
                'email': 'joaohenrique@example.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'user': 'Joaozinho',
            'email': 'joaozinho@novoemail.com',
            'password': 'novasenha',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'user': 'Joaozinho',
        'email': 'joaozinho@novoemail.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'user': 'Joaozinho',
        'email': 'joaozinho@novoemail.com',
        'id': 1,
    }
