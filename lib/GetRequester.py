import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        objects = self.get_response_body()
        return json.loads(objects)

# Example usage:
if __name__ == "__main__":
    # Replace 'https://example.com/some_api_endpoint' with your desired API endpoint
    url = 'https://example.com/some_api_endpoint'
    
    requester = GetRequester(url)
    
    try:
        # Get the response body as bytes
        response_body = requester.get_response_body()
        
        # Load and parse the JSON data from the response
        json_data = requester.load_json()
        
        # Now you can work with the JSON data as a Python data structure
        print(json_data)
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
