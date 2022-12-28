# Import the requests module
import requests

# Define the list of HTTP methods to test
methods = ['GET', 'POST', 'PUT', 'DELETE']

# Prompt the user for the URL of the API endpoint
url = input('Enter the URL of the API endpoint: ')

# Define the headers that will be sent with each request
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer <ACCESS_TOKEN>',
}

# Define the payload that will be sent with POST and PUT requests
payload = {
    'key1': 'value1',
    'key2': 'value2',
}

# Iterate over each method and send a request to the API
for method in methods:
    try:
        # Send request with specified method
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, json=payload, headers=headers)
        elif method == 'PUT':
            response = requests.put(url, json=payload, headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError('Invalid HTTP method')

        # Print the response text
        print(method + ':', response.text)
    except requests.exceptions.RequestException as e:
        # Print the error message if the request failed
        print(method + ':', e)

# Test sending a request with an invalid username and password
try:
    response = requests.get(url, auth=('invalid_username', 'invalid_password'), headers=headers)
    print('GET with invalid credentials:', response.text)
except requests.exceptions.RequestException as e:
    print('GET with invalid credentials:', e)

# Test sending a request without a username and password
try:
    response = requests.get(url, headers=headers)
    print('GET without credentials:', response.text)
except requests.exceptions.RequestException as e:
    print('GET without credentials:', e)# Test sending a request with an invalid access token
try:
    headers_invalid_token = headers.copy()
    headers_invalid_token['Authorization'] = 'Bearer <INVALID_ACCESS_TOKEN>'
    response = requests.get(url, headers=headers_invalid_token)
    print('GET with invalid token:', response.text)
except requests.exceptions.RequestException as e:
    print('GET with invalid token:', e)

# Test sending a request without an access token
try:
    headers_no_token = headers.copy()
    headers_no_token.pop('Authorization', None)
    response = requests.get(url, headers=headers_no_token)
    print('GET without token:', response.text)
except requests.exceptions.RequestException as e:
    print('GET without token:', e)

# Test sending a request with a tampered payload
try:
    payload_tampered = payload.copy()
    payload_tampered['key1'] = 'tampered value'
    response = requests.post(url, json=payload_tampered, headers=headers)
    print('POST with tampered payload:', response.text)
except requests.exceptions.RequestException as e:
    print('POST with tampered payload:', e)


