import unittest

class TestStringMethods(unittest.TestCase):

    def test_200():
        response = requests.get("http://127.0.0.1:5000/trains")
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()