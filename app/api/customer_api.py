from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.schemas.customer_schema import CustomerCreate, CustomerUpdate, CustomerInDB
from app.services.customer_service import (
    create_customer,
    update_customer,
    get_customer,
    delete_customer,
    list_customers
)

router = APIRouter()

@router.post("/customers/", response_model=CustomerInDB, status_code=201)
def create_customer_endpoint(customer: CustomerCreate):
    """Create a new customer and return the customer data."""
    new_customer = create_customer(customer.dict())
    if not new_customer:
        raise HTTPException(status_code=400, detail="Failed to create customer")
    return new_customer

@router.get("/customers/{customer_id}", response_model=CustomerInDB)
def get_customer_endpoint(customer_id: int):
    """Retrieve a customer by their ID."""
    customer = get_customer(customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.get("/customers/", response_model=List[CustomerInDB])
def list_customers_endpoint():
    """List all customers."""
    return list_customers()

@router.put("/customers/{customer_id}", response_model=CustomerInDB)
def update_customer_endpoint(customer_id: int, customer: CustomerUpdate):
    """Update an existing customer."""
    updated_customer = update_customer(customer_id, customer.dict())
    if updated_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found or update failed")
    return updated_customer

@router.delete("/customers/{customer_id}", status_code=204)
def delete_customer_endpoint(customer_id: int):
    """Delete a customer."""
    success = delete_customer(customer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Customer not found or delete failed")
    return {"message": "Customer deleted successfully"}
