# API-Security
Repo for various API testing scripts with descriptions and User prompts for input

# RestTest.py # 

The python script imports the requests module, which allows you to send HTTP requests from your Python code. It defines a list of HTTP methods (GET, POST, PUT, DELETE) and prompts the user to enter the URL of an API endpoint. It then defines the headers that will be sent with each request and a payload that will be sent with POST and PUT requests.

The code then iterates over each method in the list and sends a request to the specified URL using the requests module. It prints the response text for each request.

The code also includes additional tests for sending requests with an invalid access token, without an access token, and with a tampered payload. These tests can help you verify that your API is properly handling these scenarios.

# RestTest.go #

This golang script defines a function called httpRequest() that performs an HTTP request to the specified URL with the specified method and data. The function takes three arguments: the method (as a string), the URL (as a string), and the data to send with the request (as a string). The function returns two values: the response from the server (as a string) and any error that occurred (as an error object).

The httpRequest() function first creates a new HTTP request with the specified method, URL, and data. If the data argument is empty, the request body is set to nil, otherwise it is set to the data argument as a strings.Reader object. The function then sets the content type of the request to "application/x-www-form-urlencoded" and makes the request using the default HTTP client.

After making the request, the function reads the response body, closes the response body, and returns the response as a string.

The main() function prompts the user for the URL of a REST API to test, and then calls the httpRequest() function to test the three common HTTP methods: GET, POST, and PUT. For each method, the function prints the response from the server (or any error that occurred) to the console.
