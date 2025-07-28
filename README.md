# Domo-API-Implementation
A simple Python script to authenticate with the Domo API, retrieve a dataset in CSV format, and export it to a specified local or shared file path.

# Domo Dataset Exporter

This Python script connects to the Domo API, authenticates using OAuth 2.0 client credentials, and exports a specified dataset as a CSV file to a target directory. 
It's designed for easy integration into FP&A or analytics workflows where scheduled or automated data pulls from Domo are required.

---

## 🔧 Features

- Authenticates securely with Domo using client credentials
- Retrieves data from a specified Domo dataset ID
- Saves output as a CSV file with headers
- Automatically overwrites existing exports

---

## 📦 Requirements

- Python 3.x
- `requests` module (for HTTP API calls)

Install dependencies with:

```bash
pip install requests
```
# Usage
## 1. Set your credentials and dataset ID
```shell
client_id = "your-client-id"
client_secret = "your-client-secret"
dataset_id = "your-domo-dataset-id"
output_file_path = "your/local/or/network/path/DomoExport.csv"
```
## 2. Run the script
```shell
python domo_export.py
```
