from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# -------------------------------------------------------------------
# In-memory "database" simulation
# -------------------------------------------------------------------
# This dictionary acts as a simple data store. In our example, we only
# have one table called "sales" which contains a list of sales records.
mock_db = {
    "sales": [
        {"id": 1, "item": "Laptop", "price": 1500},
        {"id": 2, "item": "Phone", "price": 800},
        {"id": 3, "item": "Tablet", "price": 600},
    ]
}

# -------------------------------------------------------------------
# Lightweight Authentication Setup
# -------------------------------------------------------------------
# We use a simple token-based authentication. In real-world projects,
# you might integrate OAuth, JWT, or another authentication mechanism.
API_TOKEN = "secret-token"

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token != API_TOKEN:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

# -------------------------------------------------------------------
# Query Translation and Explanation Functions
# -------------------------------------------------------------------

def translate_to_sql(natural_query):
    """
    Convert a natural language query to a pseudo-SQL statement.
    For example, if the query mentions 'sales', we convert it to:
    'SELECT * FROM sales'
    """
    if "sales" in natural_query.lower():
        sql = "SELECT * FROM sales"
    else:
        sql = "SELECT * FROM unknown_table"
    return sql

def explain_query(natural_query):
    """
    Provide a simple breakdown of the query.
    This function simulates how an AI might interpret parts of the query.
    """
    explanation = {
        "original_query": natural_query,
        "detected_table": "sales" if "sales" in natural_query.lower() else "unknown",
        "translated_query": translate_to_sql(natural_query)
    }
    return explanation

def validate_query(natural_query):
    """
    Validate whether the query is feasible.
    For this simulation, we only consider queries that reference 'sales' as valid.
    """
    if "sales" in natural_query.lower():
        return True, ""
    else:
        return False, "Query does not reference any known table."

# -------------------------------------------------------------------
# API Endpoints
# -------------------------------------------------------------------

@app.route('/query', methods=['POST'])
@require_auth
def query():
    """
    Endpoint: /query
    Method: POST
    Description: Accepts a natural language query, translates it to pseudo-SQL,
                 and returns simulated results from the mock database.
    Expected JSON payload: {"query": "Show all sales records"}
    """
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    natural_query = data['query']
    pseudo_sql = translate_to_sql(natural_query)
    
    # Retrieve simulated data based on the query.
    # If the query references 'sales', return the sales data.
    result = mock_db.get("sales", []) if "sales" in natural_query.lower() else []

    return jsonify({
        "original_query": natural_query,
        "translated_query": pseudo_sql,
        "result": result
    })

@app.route('/explain', methods=['POST'])
@require_auth
def explain():
    """
    Endpoint: /explain
    Method: POST
    Description: Returns an explanation/breakdown of the natural language query.
    Expected JSON payload: {"query": "Show all sales records"}
    """
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    natural_query = data['query']
    explanation = explain_query(natural_query)
    return jsonify(explanation)

@app.route('/validate', methods=['POST'])
@require_auth
def validate():
    """
    Endpoint: /validate
    Method: POST
    Description: Validates the natural language query.
    Expected JSON payload: {"query": "Show all sales records"}
    """
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    natural_query = data['query']
    is_valid, error_message = validate_query(natural_query)
    
    if is_valid:
        return jsonify({"valid": True, "message": "Query is feasible"})
    else:
        return jsonify({"valid": False, "error": error_message}), 400

# -------------------------------------------------------------------
# Main Entry Point
# -------------------------------------------------------------------
if __name__ == '__main__':
    # Run the Flask app in debug mode on localhost:5000
    app.run(debug=True)
