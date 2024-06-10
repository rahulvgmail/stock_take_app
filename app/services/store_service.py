
# store_service.py
from app.models import queries, __execute_sql as db

def create_store(store_data):
    sql = queries.create_store_query()
    params = (store_data['name'], store_data['address'], store_data['client_id'])
    store_id = db.execute_query(sql, params, commit=True)
    return store_id

def get_store(store_id):
    sql = queries.get_store_by_id_query()
    store = db.execute_query(sql, (store_id,), commit=False)
    return store

def list_stores():
    sql = queries.list_stores_query()
    stores = db.execute_query(sql, commit=False)
    return stores

def update_store(store_id, store_data):
    sql = queries.update_store_query()
    params = (store_data['name'], store_data['address'], store_id)
    updated = db.execute_query(sql, params, commit=True)
    return updated

def delete_store(store_id):
    sql = queries.delete_store_query()
    result = db.execute_query(sql, (store_id,), commit=True)
    return result
