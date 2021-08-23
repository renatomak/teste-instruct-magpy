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
