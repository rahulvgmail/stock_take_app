# app/services/customer_service.py
from app.models import __execute_sql as db, queries

def create_customer(customer_data):
    query = queries.insert_customer_query()
    params = (customer_data['name'], customer_data['email'], customer_data['phone'])
    customer_id = db.execute_query(query, params, commit=True)
    return customer_id

def get_all_customers():
    query = queries.select_all_customers_query()
    customers = db.execute_query(query)
    return customers

def get_customer_by_id(customer_id):
    query = queries.select_customer_by_id_query()
    params = (customer_id,)
    customer = db.execute_query(query, params)
    return customer

def update_customer(customer_id, customer_data):
    query = queries.update_customer_query()
    params = (customer_data['name'], customer_data['email'], customer_data['phone'], customer_id)
    result = db.execute_query(query, params, commit=True)
    return result

def delete_customer(customer_id):
    query = queries.delete_customer_query()
    params = (customer_id,)
    result = db.execute_query(query, params, commit=True)
    return result
