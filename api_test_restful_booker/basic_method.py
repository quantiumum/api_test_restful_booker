import requests
import json

class BasicMethods():
    def get_token(self, login: str, password: str):
        url = 'https://restful-booker.herokuapp.com/auth'
        set_headers = {'Content-Type': 'application/json'}
        set_param = {'username' : login,
                     'password' : password
                    }
        res = requests.post(url, headers = set_headers, json = set_param )
        return res

    def get_all_booking_id(self, filters = dict()):
        url = 'https://restful-booker.herokuapp.com/booking'
        res = requests.get(url, params = filters)
        return res

    def get_booking_on_id(self, id: str):
        url = 'https://restful-booker.herokuapp.com/booking/' + id
        res = requests.get(url)
        return res

    def create_booking(self, set_param: dict):
        url = 'https://restful-booker.herokuapp.com/booking'
        set_headers = {'Content-Type': 'application/json'}
        res = requests.post(url, headers = set_headers, json = set_param )
        return res

    def update_full_booking(self, id: str, set_param: dict, token: str):
        url = 'https://restful-booker.herokuapp.com/booking/' + id
        set_headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json'
        }
        res = requests.put(url, headers = set_headers, json = set_param, cookies = token )
        return res

    #not_worked
    def update_partical_booking(self, id: str, set_param: dict, token: str):
        url = 'https://restful-booker.herokuapp.com/booking/' + id
        set_headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json'
        }
        res = requests.put(url, headers = set_headers, json = set_param, cookies = token )
        return res

    def delete_booking_on_id(self, id: str, token: str):
        url = 'https://restful-booker.herokuapp.com/booking/' + id
        set_headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json'
        }
        res = requests.delete(url, headers = set_headers, cookies = token)
        return res