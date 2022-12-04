# API-Security
Repo for various API testing scripts with descriptions and User prompts for input

RestTest.py - 
The python script imports the requests module, which allows you to send HTTP requests from your Python code. It defines a list of HTTP methods (GET, POST, PUT, DELETE) and prompts the user to enter the URL of an API endpoint. It then defines the headers that will be sent with each request and a payload that will be sent with POST and PUT requests.

The code then iterates over each method in the list and sends a request to the specified URL using the requests module. It prints the response text for each request.

The code also includes additional tests for sending requests with an invalid access token, without an access token, and with a tampered payload. These tests can help you verify that your API is properly handling these scenarios.
