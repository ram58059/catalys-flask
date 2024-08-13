# Flask Data Retrieval and Processing Application

## Overview
This Flask application simulates a simplified data retrieval and processing system. It includes endpoints to fetch and process data and to retrieve the processed data from temporary in-memory storage.

## Features
1. **/fetch-data**: Simulates fetching data from an external service, processes it, and stores it in memory.
2. **/get-processed-data**: Returns the processed data stored in memory.

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
2. **Set Up Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
4. **Run the Flask Application**
    ```bash
    python app.py
5. **Access the Application**
    1. Open your browser and go to http://127.0.0.1:5000/fetch-data to fetch and process data.
    2. Go to http://127.0.0.1:5000/get-processed-data to view the processed data.