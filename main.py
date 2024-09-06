import requests
import datetime

USERNAME = "kosana"
TOKEN = "njknjkfduiewlwpmdsakl"
graph_id = "readinginenglish"

pixela_endpoint = "https://pixe.la/v1/users"

new_user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
create_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
new_graph_params = {
    "id": graph_id,
    "name": "Reading",
    "unit": "pages",
    "type": "int",
    "color": "ajisai",
}

headers_params = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=pixela_endpoint, json=new_user_params)
# print(response.text)
# print(response)

# create_graph_req = requests.post(url=create_graph_endpoint, json=new_graph_params, headers=headers_params)
# print(create_graph_req.text)

monday = datetime.datetime(2024, 9, 2)
monday_str = monday.strftime("%Y%m%d")

# post_pixel_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
# new_pixel_params = {
#     "date": monday_str,
#     "quantity": "30",
# }
# response = requests.post(url=post_pixel_end_point, json=new_pixel_params, headers=headers_params)
# print(response.text)

# update monday data
update_pixel_params = {
    "quantity": "3",
}
# response = requests.put(f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{monday_str}", json=update_pixel_params,
#                         headers=headers_params)
response = requests.delete(f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{monday_str}", headers=headers_params)
print(response.text)
