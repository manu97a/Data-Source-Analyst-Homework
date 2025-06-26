from getpass import getpass
from datetime import datetime
import requests #just for check if You can get results from the api 

token = getpass("Enter yout Github Token :")

headers = {
    "Authorization": f"Bearer {token}"
}

# function for test the connection and auth for github API
def test_connection():
  response = requests.get("https://api.github.com/user", headers=headers)
  if response.status_code == 200:
    user = response.json()
    print(f"Succesful opperation. Authenticated user: {user['login']}")
  else:
    print("Connection failed. Check your token !")
def rate_limit(headers):
  api_url = "https://api.github.com/rate_limit"
  res = requests.get(api_url, headers=headers)
  if res.status_code == 200:
    data = res.json()
    remaining_limit = data['rate']['remaining']
    reset_time = data['rate']['reset']
    reset_datetime = datetime.utcfromtimestamp(reset_time).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Remaining requests: {remaining_limit}")
    print(f"Reset datetime: {reset_datetime}")
  else:
    print(f"Error {res.status_code}:{res.json()}")
test_connection()