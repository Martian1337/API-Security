import requests

# Define the list of HTTP methods to test
methods = ['GET', 'POST', 'PUT', 'DELETE']

# Prompt the user for the URL of the API endpoint
url = input('Enter the URL of the API endpoint (or type "list" to test a list of URLs from a text file): ')

# Prompt the user for the value of the Authorization header
auth_header = input('Enter the value for the Authorization header: ')

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

# Prompt the user for which HTTP method(s) to test
print('Enter the number(s) of the HTTP method(s) to test:')
print('1: GET')
print('2: POST')
print('3: PUT')
print('4: DELETE')
print('5: Test all methods')
print('Enter multiple numbers separated by spaces (e.g. "1 3 4" for GET, PUT, and DELETE)')
selected_methods = input('Selection: ')

# Parse the user's selection and create a list of the selected HTTP methods
selected_methods = selected_methods.split()
selected_methods = [methods[int(x) - 1] for x in selected_methods]

# Prompt the user to enter a proxy (optional)
use_proxy = input('Use a proxy? (y/n) ')

if use_proxy.lower() == 'y':
    # Prompt the user for the proxy URL
    proxy_url = input('Enter the proxy URL: ')
    proxies = {'http': proxy_url, 'https': proxy_url}
else:
    proxies = None

# Test a single URL if the user entered one
# Iterate over each method and send a request to the API
if url != 'list':
    for method in selected_methods:
        try:
            # Send request with specified method
            if method == 'GET':
                response = requests.get(url, headers=headers, proxies=proxies, verify=False)
            elif method == 'POST':
                response = requests.post(url, json=payload, headers=headers, proxies=proxies, verify=False)
            elif method == 'PUT':
                response = requests.put(url, json=payload, headers=headers, proxies=proxies, verify=False)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers, proxies=proxies, verify=False)
            else:
                raise ValueError('Invalid HTTP method')

            # Print the response text
            print(method + ':', response.text)
        except requests.exceptions.RequestException as e:
            # Print the error message if the request failed
            print(method + ':', e)

# Read the list of URLs from the text file and test them if the user entered "list"
else:
    # Read the list of URLs from the text file
    with open('urls.txt', 'r') as f:
        urls = f.readlines()

    # Iterate over each URL and test each HTTP method
    for url in urls:
        for method in selected_methods:
            try:
                # Send request with specified method
                if method == 'GET':
                    response = requests.get(url, headers=header, proxies=proxies, verify=False)
                elif method == 'POST':
                    response = requests.post(url, json=payload, headers=headers, proxies=proxies, verify=False)
                elif method == 'PUT':
                    response = requests.put(url, json=payload, headers=headers, proxies=proxies, verify=False)
                elif method == 'DELETE':
                    response = requests.delete(url, headers=headers, proxies=proxies, verify=False)
                else:
                    raise ValueError('Invalid HTTP method')

                # Print the response text
                print(method + ':', response.text)
            except requests.exceptions.RequestException as e:
                # Print the error message if the request failed
                print(method + ':', e)

# GET testing

# Test sending a request with an invalid username and password
try:
    response = requests.get(url, auth=('invalid_username', 'invalid_password'), headers=headers, proxies=proxies, verify=False)
    print('GET with invalid credentials:', response.text)
except requests.exceptions.RequestException as e:
    print('GET with invalid credentials:', e)

# Test sending a request without a username and password
try:
    response = requests.get(url, headers=headers, proxies=proxies, verify=False)
    print('GET without credentials:', response.text)
except requests.exceptions.RequestException as e:
    print('GET without credentials:', e)
    
    # Test sending a request with an invalid access token
try:
    headers_invalid_token = headers.copy()
    headers_invalid_token['Authorization'] = 'Bearer <INVALID_ACCESS_TOKEN>'
    response = requests.get(url, headers=headers_invalid_token, proxies=proxies, verify=False)
    print('GET with invalid token:', response.text)
except requests.exceptions.RequestException as e:
    print('GET with invalid token:', e)

# Test sending a request without an access token
try:
    headers_no_token = headers.copy()
    headers_no_token.pop('Authorization', None)
    response = requests.get(url, headers=headers_no_token, proxies=proxies, verify=False)
    print('GET without token:', response.text)
except requests.exceptions.RequestException as e:
    print('GET without token:', e)



# POST Testing

# Test sending a request with a tampered payload
try:
    payload_tampered = payload.copy()
    payload_tampered['key1'] = 'tampered value'
    response = requests.post(url, json=payload_tampered, headers=headers, proxies=proxies, verify=False)
    print('POST with tampered payload:', response.text)
except requests.exceptions.RequestException as e:
    print('POST with tampered payload:', e)

# Test sending a request with an invalid access token
try:
    headers_invalid_token = headers.copy()
    headers_invalid_token['Authorization'] = 'Bearer <INVALID_ACCESS_TOKEN>'
    response = requests.post(url, json=payload, headers=headers_invalid_token, proxies=proxies, verify=False)
    print('POST with invalid token:', response.text)
except requests.exceptions.RequestException as e:
    print('POST with invalid token:', e)

# Test sending a request without an access token
try:
    headers_no_token = headers.copy()
    headers_no_token.pop('Authorization', None)
    response = requests.post(url, json=payload, headers=headers_no_token, proxies=proxies, verify=False)
    print('POST without token:', response.text)
except requests.exceptions.RequestException as e:
    print('POST without token:', e)

# Test sending a request with an invalid payload
try:
    payload_invalid = {'invalid_key': 'invalid_value'}
    response = requests.post(url, json=payload_invalid, headers=headers, proxies=proxies, verify=False)
    print('POST with invalid payload:', response.text)
except requests.exceptions.RequestException as e:
    print('POST with invalid payload:', e)

# Test sending a request with a missing required field in the payload
try:
    payload_missing_field = {'key1': 'value1'}
    response = requests.post(url, json=payload_missing_field, headers=headers, proxies=proxies, verify=False)
    print('POST with missing field in payload:', response.text)
except requests.exceptions.RequestException as e:
    print('POST with missing field in payload:', e)

# Test sending a request with an invalid URL
try:
    response = requests.post('http://invalid.url', json=payload, headers=headers, proxies=proxies, verify=False)
    print('POST with invalid URL:', response.text)
except requests.exceptions.RequestException as e:
    print('POST with invalid URL:', e)

# Test sending a request with a XSS payload in key value
try:
    payload_malicious = {'key1': '<SCRIPT>alert("XSS")</SCRIPT>'}
    response = requests.post(url, json=payload_malicious, headers=headers, proxies=proxies, verify=False)
    print('POST with malicious payload:', response.text)
except requests.exceptions.RequestException as e:
    print('POST with malicious payload:', e)

# Test sending a request with a payload that has been padded to try and bypass input validation
try:
    payload_padded = payload.copy()
    payload_padded['key1'] = payload_padded['key1'] + 'a' * 100
    response = requests.post(url, json=payload_padded, headers=headers, proxies=proxies, verify=False)
    print('POST with padded payload:', response.text)
except requests.exceptions.RequestException as e:
    print('POST with padded payload:', e)

# Test sending a request with a payload that has been truncated to try and bypass input validation
try:
    payload_truncated = payload.copy()
    payload_truncated['key1'] = payload_truncated['key1'][:5]
    response = requests.post(url, json=payload_truncated, headers=headers, proxies=proxies, verify=False)
    print('POST with truncated payload:', response.text)
except requests.exceptions.RequestException as e:
    print('POST with truncated payload:', e)



# PUT Testing

# Test sending a request with an invalid access token
try:
    headers_invalid_token = headers.copy()
    headers_invalid_token['Authorization'] = 'Bearer <INVALID_ACCESS_TOKEN>'
    response = requests.put(url, json=payload, headers=headers_invalid_token, proxies=proxies, verify=False)
    print('PUT with invalid token:', response.text)
except requests.exceptions.RequestException as e:
    print('PUT with invalid token:', e)

# Test sending a request without an access token
try:
    headers_no_token = headers.copy()
    headers_no_token.pop('Authorization', None)
    response = requests.put(url, json=payload, headers=headers_no_token, proxies=proxies, verify=False)
    print('PUT without token:', response.text)
except requests.exceptions.RequestException as e:
    print('PUT without token:', e)

# Test sending a request with an invalid payload
try:
    payload_invalid = {'invalid_key': 'invalid_value'}
    response = requests.put(url, json=payload_invalid, headers=headers, proxies=proxies, verify=False)
    print('PUT with invalid payload:', response.text)
except requests.exceptions.RequestException as e:
    print('PUT with invalid payload:', e)

#Test sending a request with a missing required field in the payload
try:
    payload_missing_field = {'key1': 'value1'}
    response = requests.put(url, json=payload_missing_field, headers=headers, proxies=proxies, verify=False)
    print('PUT with missing field in payload:', response.text)
except requests.exceptions.RequestException as e:
    print('PUT with missing field in payload:', e)

# Test sending a request with an invalid URL
try:
    response = requests.put('http://invalid.url', json=payload, headers=headers, proxies=proxies, verify=False)
    print('PUT with invalid URL:', response.text)
except requests.exceptions.RequestException as e:
    print('PUT with invalid URL:', e)
