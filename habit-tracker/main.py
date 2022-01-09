import requests
from datetime import datetime
USERNAME = "munish"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
GRAPH_ID = "test-graph"

today = datetime.now()
TODAY = today.strftime("%Y%m%d")

pixela_endpoints = "https://pixe.la/v1/users"

user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
# response = requests.post(url=pixela_endpoints, json=user_params)
# print(response.text)

graph_endpoints = f"{pixela_endpoints}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "Graph",
    "type": "int",
    "color": "shibafu",
    "timezone": "Asia/Kolkata"
}

post_pixel = f"{graph_endpoints}/{GRAPH_ID}"

# today = datetime.now()


post_data = {
    "date": TODAY,
    "quantity": input("How many coding problems you solved today?\n")


}

update_pixel = f"{post_pixel}/{TODAY}"

update_data = {
    "quantity": "15",


}

response = requests.post(url=update_pixel,
                         json=update_data, headers=headers)
print(response.text)
