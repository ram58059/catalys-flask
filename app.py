from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Simulate in-memory storage
data_storage = {}

# Function to fetch data from the external API
def fetch_data_from_external_service():
    response = requests.get("https://api.restful-api.dev/objects")
    if response.status_code == 200:
        print(response.json())
        return response.json()  # Return JSON data
    else:
        return {"error": "Failed to fetch data from external service."}

# Data processing function (you can customize this as needed)
def process_data(data):
    # Example processing: Just pass through the data (no transformation)
    for product_data in data:
        product_data["name"] += '- 2024' 
    return data
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    data = fetch_data_from_external_service()
    processed_data = process_data(data)
    # Store the processed data in memory
    global data_storage
    data_storage['processed_data'] = processed_data
    return jsonify({"message": "Data fetched and processed successfully."})

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    # Retrieve the processed data from memory
    global data_storage
    processed_data = data_storage.get('processed_data', "No data available.")
    return jsonify({"processed_data": processed_data})

if __name__ == '__main__':
    app.run(debug=True)
