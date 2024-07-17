from neo4j import GraphDatabase

# Connect to the Neo4j database
uri = "bolt://localhost:7687"
username = "your_username"
password = "your_password"
driver = GraphDatabase.driver(uri, auth=(username, password))

# Define a function to execute a query
def execute_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result

# Example usage
query = "MATCH (n) RETURN n LIMIT 10"
result = execute_query(query)
for record in result:
    print(record)

# Close the driver when you're done
driver.close()