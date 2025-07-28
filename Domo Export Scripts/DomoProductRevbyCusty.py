import requests
import csv
import http.client

# Define the URL for the API request to generate the access token
token_url = "https://api.domo.com/oauth/token?grant_type=client_credentials&scope=data"

# Define your credentials
client_id = "bfe74062-ee7e-42a5-910f-1f4790366c22"
client_secret = "e3fc5b2f9cbb27c2a1e38f03c91d3807affa0fb43cd0b4f586433c4a51903cef"

# Make the API request using Basic Authentication
response = requests.get(token_url, auth=(client_id, client_secret))
# Define the file name
file_name = "All Product By Month by Custy.csv"

# URL encode the file name
file_name_encoded = requests.utils.quote(file_name)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()

    # Extract the access token
    access_token = json_data["access_token"]

    # Define the file path where you want to save the exported dataset
    output_file_path = "G:/Shared drives/Confidential.Finance/Finance.Squad/Confidential Finance/FP&A/PowerBi/1. Datasets and Uploads/All Product By Month by Custy.csv"

    conn = http.client.HTTPSConnection("api.domo.com")

    headers = {
        'Accept': "text/csv",
        'Authorization': f"Bearer {access_token}"
    }
    conn.request("GET", "/v1/datasets/09879ff4-d497-4c0d-9379-b7ff2df8a0a7/data?includeHeader=true&fileName={file_name_encoded}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # Save the data to the specified file path, overwriting if it exists
    with open(output_file_path, 'wb') as output_file:
        output_file.write(data)

    print(f"Dataset exported to '{output_file_path}'")
else:
    print(f"Error: {response.status_code} - {response.text}")


