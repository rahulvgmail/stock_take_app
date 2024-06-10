

'''
repository for storing SQL queries

When your application needs to interact with the database,
 it can import these queries into data access or service layers, 
 which then use these strings to execute operations via a database driver 
 or a connection utility like the previously discussed __execute_sql.py.
EXAMPLES:
def create_location():
    return """
    INSERT INTO locations (store_id, description, zone_id)
    VALUES (%s, %s, %s) RETURNING location_id;
    """

def read_location():
    return """
    SELECT location_id, store_id, description, zone_id
    FROM locations
    WHERE location_id = %s;
    """

def update_location():
    return """
    UPDATE locations
    SET description = %s, zone_id = %s
    WHERE location_id = %s;
    """

def delete_location():
    return """
    DELETE FROM locations
    WHERE location_id = %s;
    """


'''

# app/models/queries.py

def get_store_query():
    return "SELECT id, name, address FROM stores WHERE id = %s;"

def insert_store_query():
    return "INSERT INTO stores (name, address) VALUES (%s, %s) RETURNING id;"

def update_store_query():
    return "UPDATE stores SET name = %s, address = %s WHERE id = %s;"

def delete_store_query():
    return "DELETE FROM stores WHERE id = %s;"
