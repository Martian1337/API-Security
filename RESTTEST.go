package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
	"strings"
)

// Function to perform an HTTP request to the specified URL with the specified method and data
func httpRequest(method string, url string, data string) (response string, err error) {
	var req *http.Request
	var resp *http.Response

	// Create a new request with the specified method, URL, and data
	if data == "" {
		req, err = http.NewRequest(method, url, nil)
	} else {
		req, err = http.NewRequest(method, url, strings.NewReader(data))
	}
	if err != nil {
		return "", err
	}

	// Set the content type of the request to application/x-www-form-urlencoded
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")

	// Make the request
	resp, err = http.DefaultClient.Do(req)
	if err != nil {
		return "", err
	}

	// Read the response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	// Close the response body
	defer resp.Body.Close()

	// Return the response as a string
	return string(body), nil
}

func main() {
	// Prompt the user for the URL of the REST API to test
	var url string
	fmt.Print("Enter the URL of the REST API to test: ")
	fmt.Scanln(&url)

	// Test the GET method
	fmt.Println("\nTesting GET method...")
	response, err := httpRequest("GET", url, "")
	if err != nil {
		fmt.Println("Error:", err)
		// Continue to the next test even if there is an error
	} else {
		fmt.Println("GET request successful")
		fmt.Println("Response:", response)
	}

	// Test the POST method
	fmt.Println("\nTesting POST method...")
	response, err = httpRequest("POST", url, "data=test")
	if err != nil {
		fmt.Println("Error:", err)
		// Continue to the next test even if there is an error
	} else {
		fmt.Println("POST request successful")
		fmt.Println("Response:", response)
	}

	// Test the PUT method
	fmt.Println("\nTesting PUT method...")
	response, err = httpRequest("PUT", url, "data=test")
	if err != nil {
		fmt.Println("Error:", err)
		// Continue to the next test even if there is an error
	} else {
		fmt.Println("PUT request successful")
		fmt.Println("Response:", response)
	}
