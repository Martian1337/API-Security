# API-Security
Repo for various API testing scripts with descriptions and User prompts for input

# RestTest.py # 

This script sends HTTP requests to an API using the requests module. The user is prompted to enter the URL of the API endpoint, and the code sends a request using each of the HTTP methods in the methods list (GET, POST, PUT, and DELETE).

For each request, it sets the Content-Type header to application/json and sends an Authorization header with a bearer token. The code also defines a payload that is sent with POST and PUT requests.

The script also includes several tests for handling error cases. It tests sending a request with invalid credentials, without credentials, with an invalid access token, and without an access token. It also tests sending a request with a tampered payload. If an error occurs, the code prints the error message. If the request is successful, it prints the response text.

# RestTest.go #

This golang script defines a function called httpRequest() that performs an HTTP request to the specified URL with the specified method and data. The function takes three arguments: the method (as a string), the URL (as a string), and the data to send with the request (as a string). The function returns two values: the response from the server (as a string) and any error that occurred (as an error object).

The httpRequest() function first creates a new HTTP request with the specified method, URL, and data. If the data argument is empty, the request body is set to nil, otherwise it is set to the data argument as a strings.Reader object. The function then sets the content type of the request to "application/x-www-form-urlencoded" and makes the request using the default HTTP client.

After making the request, the function reads the response body, closes the response body, and returns the response as a string.

The main() function prompts the user for the URL of a REST API to test, and then calls the httpRequest() function to test the three common HTTP methods: GET, POST, and PUT. For each method, the function prints the response from the server (or any error that occurred) to the console.
