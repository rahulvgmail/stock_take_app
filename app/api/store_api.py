# store_api.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.schemas.store_schema import StoreCreate, StoreUpdate, StoreInDB
from app.services import store_service

router = APIRouter()

@router.post("/stores/", response_model=StoreInDB, status_code=201)
def create_store(store: StoreCreate):
    store_id = store_service.create_store(store.dict())
    if not store_id:
        raise HTTPException(status_code=400, detail="Failed to create store")
    return {**store.dict(), "id": store_id}

@router.get("/stores/{store_id}", response_model=StoreInDB)
def get_store(store_id: int):
    store = store_service.get_store(store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store

@router.get("/stores/", response_model=List[StoreInDB])
def get_stores():
    stores = store_service.list_stores()
    return stores

@router.put("/stores/{store_id}", response_model=StoreInDB)
def update_store(store_id: int, store: StoreUpdate):
    updated = store_service.update_store(store_id, store.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Failed to update store")
    return {**store.dict(), "id": store_id}

@router.delete("/stores/{store_id}", status_code=204)
def delete_store(store_id: int):
    success = store_service.delete_store(store_id)
    if not success:
        raise HTTPException(status_code=404, detail="Failed to delete store")
    return {"message": "Store deleted successfully"}
