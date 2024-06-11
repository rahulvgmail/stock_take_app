

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

### User Queries

def get_user_by_login():
    return """
    SELECT user_id, username, email, password_hash, role
    FROM Users
    WHERE email = %s OR username = %s;
    """
def get_user_by_id():
    return """
    SELECT user_id, username, email, role
    FROM Users
    WHERE user_id = %s;
    """    
def create_user():
    return """
    INSERT INTO Users (email, password_hash, name, role)
    VALUES (%s, %s, %s, %s)
    RETURNING user_id;
    """
def update_user_password():
    return """
    UPDATE Users
    SET password_hash = %s
    WHERE user_id = %s;
    """
def update_user_role():
    return """
    UPDATE Users
    SET role = %s
    WHERE user_id = %s
    RETURNING user_id;
    """