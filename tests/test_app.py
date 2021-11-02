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
    test_test1 = {'message': "NYC1 already exists."}
    response = requests.post(HOST_URL + "/trains", params=parms)
    assert response.status_code == 400, response.text == test_test1

def test_times_post_400():
    parms = {'Time': "8:00"}
    test_test2 = {"message": "Please make sure '8:00' is in correct HH:MM 24 hr format."}
    response = requests.post(HOST_URL + "/times", params=parms)
    assert response.status_code == 400, response.text == test_text2