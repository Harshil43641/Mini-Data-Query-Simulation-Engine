# Mini Data Query Simulation Engine

This project simulates an AI-powered analytics query system with a simple REST API built using Flask.

## Endpoints

- **/query:** Accepts a natural language query, translates it into a pseudo-SQL statement, and returns simulated results.
- **/explain:** Returns an explanation of how the query was interpreted.
- **/validate:** Checks if the query is valid based on predefined criteria.

## Setup Instructions

1. **Clone the repository or create a new folder:**

   ```bash
   git clone <repository_url>
   cd mini-data-query-engine

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

3. **Run the Application**

   ```bash
   python app.py
The server runs at http://127.0.0.1:5000.


## API Testing

/query Endpoint

🔹 Description:
      Accepts a natural language query, translates it into a pseudo-SQL statement, and returns a simulated response.

🔹 Method: POST

🔹 Headers:
   
   Content-Type: application/json
      
   Authorization: secret-token

🔹 Request Body (JSON):

      {
        "query": "Show all sales records"
      }

🔹 Response (Success - 200 OK):
      
      {
        "original_query": "Show all sales records",
        "translated_query": "SELECT * FROM sales",
        "result": [
           {"id": 1, "item": "Laptop", "price": 1500},
           {"id": 2, "item": "Phone", "price": 800},
           {"id": 3, "item": "Tablet", "price": 500}
        ]
      }


🔹 Error Responses:

400 Bad Request → If the request body is not valid JSON

401 Unauthorized → If authentication is missing


1. PowerShell
    ```bash
   Invoke-RestMethod -Uri "http://127.0.0.1:5000/query" -Method Post `
    -Headers @{ "Content-Type" = "application/json"; "Authorization" = "secret-token" } `
    -Body '{"query": "Show all sales records"}'

  
2. Command Prompt (cmd) or Git Bash
    ```bash
    curl.exe -X POST http://127.0.0.1:5000/query -H "Content-Type: application/json" -H "Authorization: secret-token" -d "{\"query\": \"Show all sales records\"}"


/explain Endpoint

🔹 Description:
      Returns a breakdown of how the natural language query is interpreted.

🔹 Method: POST

🔹 Headers:
   
   Content-Type: application/json
      
   Authorization: secret-token

🔹 Request Body (JSON):

      {
        "query": "Show all sales records"
      }

🔹 Response (Success - 200 OK):
      
      {
        "original_query": "Show all sales records",
        "translated_query": "SELECT * FROM sales",
        "explanation": "The query retrieves all records from the sales database."
      }



🔹 Error Responses:

400 Bad Request → Invalid JSON

401 Unauthorized → Authentication missing

  
1. PowerShell
    ```bash
   Invoke-RestMethod -Uri "http://127.0.0.1:5000/explain" -Method Post `
    -Headers @{ "Content-Type" = "application/json"; "Authorization" = "secret-token" } `
    -Body '{"query": "Show all sales records"}'

  
2. Command Prompt (cmd) or Git Bash
    ```bash
    curl.exe -X POST http://127.0.0.1:5000/explain -H "Content-Type: application/json" -H "Authorization: secret-token" -d "{\"query\": \"Show all sales records\"}"


/validate Endpoint

🔹 Description:
      Checks if the given query is feasible based on predefined rules.

🔹 Method: POST

🔹 Headers:
   
   Content-Type: application/json
      
   Authorization: secret-token

🔹 Request Body (JSON):

      {
        "query": "Delete all sales records"
      }

🔹 Response (Success - 200 OK):
      
      {
        "original_query": "Delete all sales records",
        "valid": false,
        "reason": "Destructive queries like DELETE are not allowed."
      }

🔹 Response for Valid Queries:

      {
        "original_query": "Show all sales records",
        "valid": true,
        "reason": "The query is valid and can be executed."
      }

🔹 Error Responses:

400 Bad Request → Invalid JSON

401 Unauthorized → Authentication missing

  
1. PowerShell
    ```bash
   Invoke-RestMethod -Uri "http://127.0.0.1:5000/validate" -Method Post `
    -Headers @{ "Content-Type" = "application/json"; "Authorization" = "secret-token" } `
    -Body '{"query": "Show all sales records"}'

  
2. Command Prompt (cmd) or Git Bash
    ```bash
    curl.exe -X POST http://127.0.0.1:5000/validate -H "Content-Type: application/json" -H "Authorization: secret-token" -d "{\"query\": \"Show all sales records\"}"

