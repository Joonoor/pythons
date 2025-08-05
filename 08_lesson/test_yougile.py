import requests
import pytest


base_url = 'https://ru.yougile.com/api-v2'
key = 'bSa1TYBkDv5ygL-nn+zt8yEIvaAmY+TZ7f5jaaV93VD2775Qwrr8tJpqlwxGNPMW'

headers = {
    "Content-Type": "application/json",
    "Authorization":
    "Bearer bSa1TYBkDv5ygL-nn+zt8yEIvaAmY+TZ7f5jaaV93VD2775Qwrr8tJpqlwxGNPMW"
    }


@pytest.mark.positive
def test_create_project():
    body = {
        "title": "Новый проектище",
        "users": {
            "43958489-89f9-41c4-af40-856a02f3057c": "admin"
        }
    }
    res = requests.post(base_url + '/projects', headers=headers, json=body)

    assert res.status_code == 201


@pytest.mark.positive
def test_edit_project():
    body = {
        "title": "Новый проектище",
        "users": {
            "43958489-89f9-41c4-af40-856a02f3057c": "admin"
        }
    }
    res = requests.post(base_url + '/projects', headers=headers, json=body)
    project_id = res.json()['id']

    body_req = {
        "deleted": False,
        "title": "Новая доска"
        }

    requests.put(base_url + '/projects/' + project_id, headers=headers,
                 json=body_req)
    res_3 = requests.get(base_url + '/projects/' + project_id, headers=headers)

    assert res_3.json()['title'] == "Новая доска"


@pytest.mark.positive
def test_get_project():
    body = {
        "title": "Новый проектище",
        "users": {
            "43958489-89f9-41c4-af40-856a02f3057c": "admin"
        }
    }
    res = requests.post(base_url + '/projects/', headers=headers, json=body)
    project_id = res.json()['id']

    res_3 = requests.get(base_url + '/projects/' + project_id, headers=headers)

    assert res_3.status_code == 200


@pytest.mark.negative
def test_create_project_fail():
    body = {
        "title": "Новый проектище",
        "users": {
            "43958489-89f9-41c4-af40-856a02f3057c": "admin"
        }
    }
    res = requests.post(base_url + '/projects', json=body)

    assert res.status_code == 401


@pytest.mark.negative
@pytest.mark.negative
def test_get_project_fail():
    fake_id = "not-existed-project-id"
    res = requests.get(base_url + '/projects/' + fake_id, headers=headers)
    assert res.status_code == 404


@pytest.mark.negative
def test_edit_project_fail():
    body = {
        "title": "",
        "users": {
            "43958489-89f9-41c4-af40-856a02f3057c": "admin"
        }
    }
    res = requests.post(base_url + '/projects', headers=headers, json=body)
    assert res.status_code == 400
