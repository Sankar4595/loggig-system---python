import requests

NODE_API_URL = "http://localhost:5000/api/logs"

def send_log(employee):
    payload = {
        "empId": employee["empId"],
        "name": employee["name"],
        "department": employee["department"],
        "source": "CAMERA_1"
    }
    requests.post(NODE_API_URL, json=payload)