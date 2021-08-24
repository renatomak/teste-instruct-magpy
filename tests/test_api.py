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
    response = httpx.get(url_base)
    assert response.status_code == 200, "Error when fetching projects"


def test_get_by_name_project():
    initial_delete_for_test(payload_name)
    initial_insert_for_test()

    response = httpx.get(url_base+payload_name)
    assert response.status_code == 200, 'Error when fetching project'

    initial_delete_for_test(payload_name)


def test_create_new_project():
    initial_delete_for_test(payload_name)

    response = httpx.post(url_base, json=payload, headers=headers)
    assert response.status_code == 201, 'Error creating project'

    initial_delete_for_test(payload_name)


def test_create_new_projeto_unnamed():
    payload_unnamed = {
        'name': '',
        'packages': [
            {"name": "Django"},
            {"name": "graphene", "version": "2.0"}
        ]
    }

    response = httpx.post(url_base, json=payload_unnamed, headers=headers)
    assert response.status_code == 400, 'Project created without name'


def test_create_same_project():
    initial_delete_for_test(payload_name)
    initial_insert_for_test()

    response = httpx.post(url_base, json=payload, headers=headers)
    assert response.status_code == 400, 'Duplicate project created'

    initial_delete_for_test(payload_name)


def test_create_project_without_packages():
    payload_without_packages = {
        "name": "Projeto sem pacotes"
    }
    response = httpx.post(
        url_base, json=payload_without_packages, headers=headers)
    assert response.status_code == 400, 'Project create without "packeges" key'

    payload_packages_without_list = {
        "name": "Projeto sem pacotes",
        "packages": ""
    }
    response = httpx.post(
        url_base, json=payload_packages_without_list, headers=headers)
    assert response.status_code == 400, '"packages" with invalid format'


def test_create_package_without_version():
    payload_test_version = {
        'name': 'version',
        'packages': [
            {"name": "Django"}
        ]
    }

    response = httpx.post(url_base, json=payload_test_version, headers=headers)
    django = response.json()['packages'][0]
    assert 'version' in django, 'Version not included in the package'

    initial_delete_for_test('version')


def test_ceate_invalid_package():
    payload_test = {
        'name': 'version',
        'packages': [
            {"name": "Xblau"}
        ]
    }
    response = httpx.post(url_base, json=payload_test, headers=headers)
    assert response.status_code == 400, 'Invalid package name'


def test_create_package_invalid_version():
    payload_test = {
        'name': 'version',
        'packages': [
            {"name": "django", "version": "AAA"}
        ]
    }
    response = httpx.post(url_base, json=payload_test, headers=headers)
    assert response.status_code == 400, 'Package with invalid version'


def test_delete_project():
    initial_delete_for_test(payload_name)
    initial_insert_for_test()

    response = httpx.delete(url_base+payload_name)
    assert response.status_code == 204, 'Error deleting project'


def test_delete_project_nonexistent():
    response = httpx.delete(url_base+"xablau")
    assert response.status_code == 404, 'Error deleting non-existent project'
