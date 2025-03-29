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
  
1. PowerShell
    ```bash
   Invoke-RestMethod -Uri "http://127.0.0.1:5000/query" -Method Post `
    -Headers @{ "Content-Type" = "application/json"; "Authorization" = "secret-token" } `
    -Body '{"query": "Show all sales records"}'

  
3. Command Prompt (cmd) or Git Bash
    ```bash
    curl.exe -X POST http://127.0.0.1:5000/query -H "Content-Type: application/json" -H "Authorization: secret-token" -d "{\"query\": \"Show all sales records\"}"

/explain Endpoint
  
1. PowerShell
    ```bash
   Invoke-RestMethod -Uri "http://127.0.0.1:5000/explain" -Method Post `
    -Headers @{ "Content-Type" = "application/json"; "Authorization" = "secret-token" } `
    -Body '{"query": "Show all sales records"}'

  
3. Command Prompt (cmd) or Git Bash
    ```bash
    curl.exe -X POST http://127.0.0.1:5000/explain -H "Content-Type: application/json" -H "Authorization: secret-token" -d "{\"query\": \"Show all sales records\"}"


/validate Endpoint
  
1. PowerShell
    ```bash
   Invoke-RestMethod -Uri "http://127.0.0.1:5000/validate" -Method Post `
    -Headers @{ "Content-Type" = "application/json"; "Authorization" = "secret-token" } `
    -Body '{"query": "Show all sales records"}'

  
3. Command Prompt (cmd) or Git Bash
    ```bash
    curl.exe -X POST http://127.0.0.1:5000/validate -H "Content-Type: application/json" -H "Authorization: secret-token" -d "{\"query\": \"Show all sales records\"}"
