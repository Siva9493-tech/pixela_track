import requests
from datetime import datetime

TOKEN="qwertyasdfgh123456"
USER_NAME="sivabalu123"
pixela_endpoint="https://pixe.la/v1/users"



pixela_params={
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixela_endpoint,json=pixela_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs"
headers={
    "X-USER-TOKEN":TOKEN
}

graph_id="graph1"

graph_params={
    "id":"graph1",
    "name":"sprint_sec",
    "unit":"Km",
    "type":"float",
    "color":"sora",
}

# response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)

pixel_create_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}"

today=datetime.today()

pixel_create_params={
    "date":today.strftime("%Y%m%d"),
    "quantity":"20"
}
pixel_date=pixel_create_params["date"]

# print(pixel_create_params["date"])
# response=requests.post(url=pixel_create_endpoint,json=pixel_create_params,headers=headers)
# print(response.json())

update_pixel_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_params["id"]}/{pixel_date}"

# update_pixel_params={
#     "quantity":input("how many kms did you run today: ")
# }
# response=requests.put(url=update_pixel_endpoint,json=update_pixel_params,headers=headers)
# print(response.text)

delete_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}/{pixel_create_params["date"]}"
response=requests.delete(url=delete_endpoint,headers=headers)
print(response.text)