import requests

HOST_URL = "http://127.0.0.1:5000/"

def test_train_get_200():
    response = requests.get(HOST_URL + "trains")
    assert response.status_code == 200

def test_train_post_200():
    parms = {'Train': "NYCD", 'Times': "[19:00, 18:00]"}
    response = requests.post(HOST_URL + "/trains", params=parms)
    assert response.status_code == 200

def test_times_post_200():
    parms = {'Time': "08:00"}
    response = requests.post(HOST_URL + "/times", params=parms)
    assert response.status_code == 200

def test_train_post_400():
    parms = {'Train': "NYC1", 'Times': "[19:00, 18:00]"}
    response = requests.post(HOST_URL + "/trains", params=parms)
    assert response.status_code == 400

def test_times_post_400():
    parms = {'Time': "8:00"}
    response = requests.post(HOST_URL + "/times", params=parms)
    assert response.status_code == 400