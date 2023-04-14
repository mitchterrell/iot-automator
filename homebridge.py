import requests
import json
import sys


class HomeBridge:
    def __init__(self, host='192.168.5.14', port='8581'):
        self.host = host
        self.port = port
        self.username = 'nickwang'
        self.password = '99329063@'
        self.device_name = 'Smart Desk Lamp'
        
    def login(self):
        url = 'http://'+self.host+'/api/auth/login'

        headers = {"accept": "*/*", "Content-Type": "application/json"}

        data = {"username": self.username, "password": self.password}

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200 or response.status_code == 201:
            content = response.json()
            access_token = content.get("access_token")
            token_type = content.get("token_type")
            # print(token_type, " ", access_token)
            result = token_type+" "+access_token
            return result
        else:
            print("Error: Failed to retrieve Meross device status. Status code: {}".format(response.status_code))
            return

    def find_device_unique_id(self):
        url = 'http://'+self.host+'/api/accessories'

        authorization_code = self.login()
        headers = {"accept": "*/*", "Authorization": authorization_code}

        response = requests.get(url, headers=headers)

        if response.status_code == 200 or response.status_code == 201:
            # print(response.json())
            data = response.json()
            for item in data:
                # print(item)
                if item.get("serviceName") == "Smart Desk Lamp":
                    # print(item.get("uniqueId"))
                    # TODO: return the uniqueId of the device
                    return item.get("uniqueId")
        else:
            print("Error: Failed to retrieve Meross device status. Status code: {}".format(response.status_code))
            return

    def lamp_switch_on(self):
        uniqueid = self.find_device_unique_id()
        url = 'http://'+self.host+':'+self.port+'/api/accessories/'+uniqueid

        authorization_code = self.login()
        headers = {"accept": "*/*", "Content-Type": "application/json", "Authorization": authorization_code}

        data = {"characteristicType": "On", "value": '1'}

        response = requests.put(url, headers=headers, json=data)

        if response.status_code == 200 or response.status_code == 201:
            return
            # print(response.content)
        else:
            print("Error: Failed to retrieve Meross device status. Status code: {}".format(response.status_code))

    def lamp_switch_off(self):
        uniqueid = self.find_device_unique_id()
        url = 'http://'+self.host+':'+self.port+'/api/accessories/'+uniqueid

        authorization_code = self.login()
        headers = {"accept": "*/*", "Content-Type": "application/json", "Authorization": authorization_code}

        data = {"characteristicType": "On", "value": '0'}

        response = requests.put(url, headers=headers, json=data)

        if response.status_code == 200 or response.status_code == 201:
            return
            # print(response.content)
        else:
            print("Error: Failed to retrieve Meross device status. Status code: {}".format(response.status_code))


if __name__ == '__main__':
    # print(sys.argv[1], " ", len(sys.argv))
    if len(sys.argv) != 2:
        print("usage: python homebridge.py on/off")

    c = HomeBridge()
    if sys.argv[1] == 'on':
        HomeBridge.lamp_switch_on(c)
    else:
        HomeBridge.lamp_switch_off(c)
    