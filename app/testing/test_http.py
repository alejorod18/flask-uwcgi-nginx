import json


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))

def test_resource01(app, client):
    res = client.get('/test01')
    assert res.status_code == 200
    expected = {'hello': 'test01'}
    assert expected == json.loads(res.get_data(as_text=True))

def test_resource02(app, client):
    res = client.get('/test02')
    assert res.status_code == 200
    expected = {'hello': 'test02'}
    assert expected == json.loads(res.get_data(as_text=True))
