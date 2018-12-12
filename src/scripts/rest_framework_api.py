import os
import json
import requests

#######################################
# AUTH REGISTER REQUESTS TEST
######################################

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

headers = {
    "Content-Type": "application/json",
    # "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyNywidXNlcm5hbWUiOiJtb2hpbi5uckBnbWFpbC5jb20iLCJleHAiOjE1NDQ0NDc4NTIsImVtYWlsIjoibW9oaW4ubnJAZ21haWwuY29tIn0.ehX6MveqNBOBVd300rpjH52uGKG8GcqOasrPLCEsv0U'
}

data = {
    "first_name": 'First Name',
    "last_name": 'Last Name',
    "email": 'mohin.nr@gmail.com',
    "password": 'SADHIN101119',
    "password2": 'SADHIN101119',
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()  # ['token']
print(token)

#######################################
# AUTH LOGIN REQUESTS TEST
######################################

# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
#
# headers = {
#     "Content-Type": "application/json",
#     # "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwidXNlcm5hbWUiOiJqYWtpQGpxdXJpdHkuY29tIiwiZXhwIjoxNTQ0MzczOTYwLCJlbWFpbCI6Impha2lAanF1cml0eS5jb20ifQ.oGSNVTNw3A4Ke7g8KgsCB-t52ZNHQIbIDuBygkGfJeM'
# }
#
# data = {
#     "username": 'jaki@jqurity.com',
#     "password": 'SADHIN101119',
# }
#
# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json()  # ['token']
# print(token)