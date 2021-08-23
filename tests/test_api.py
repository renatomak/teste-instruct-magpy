import httpx
url_base = 'http://localhost:8000/api/projects/'
headers = {'Content-Type': 'application/json'}

payload_name = 'django-titan'
payload = {
    'name': payload_name,
    'packages': [
        {"name": "Django"},
        {"name": "graphene", "version": "2.0"}
    ]
}


def initial_delete_for_test(package_name):
    if httpx.get(url_base+package_name).status_code == 200:
        httpx.delete(url_base+package_name)


def initial_insert_for_test():
    httpx.post(url_base, json=payload, headers=headers)


def test_get_list_projects():
    request = httpx.get(url_base)
    assert request.status_code == 200, 'Código da resposta diferente de 200'


def test_get_by_name_project():
    initial_delete_for_test(payload_name)
    initial_insert_for_test()

    request = httpx.get(url_base+payload_name)
    assert request.status_code == 200, 'Código da resposta diferente de 200'

    initial_delete_for_test(payload_name)


def test_post_new_project():
    initial_delete_for_test(payload_name)

    request = httpx.post(url_base, json=payload, headers=headers)
    assert request.status_code == 201, 'Código da resposta diferente de 201'

    initial_delete_for_test(payload_name)


def test_post_some_project():
    initial_delete_for_test(payload_name)
    initial_insert_for_test()

    request = httpx.post(url_base, json=payload, headers=headers)
    assert request.status_code == 400, 'Código da resposta diferente de 400'

    initial_delete_for_test(payload_name)


def test_post_inclusion_key_version():
    payload_test_version = {
        'name': 'version',
        'packages': [
            {"name": "Django"}
        ]
    }

    request = httpx.post(url_base, json=payload_test_version, headers=headers)
    django = request.json()['packages'][0]
    assert 'version' in django, 'Versão não incluída no pacote'

    initial_delete_for_test('version')
