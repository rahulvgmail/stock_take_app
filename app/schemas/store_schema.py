from typing import Annotated, Optional
from pydantic import BaseModel, constr

# Define constraints for name and address
NameStr = Annotated[str, constr(strip_whitespace=True, min_length=1, max_length=100)]
AddressStr = Annotated[str, constr(strip_whitespace=True, min_length=1, max_length=300)]

class StoreBase(BaseModel):
    """
    Base model for store, includes all common fields.
    """
    name: NameStr
    address: AddressStr

class StoreCreate(StoreBase):
    """
    Schema for creating a new store. Inherits all fields from StoreBase.
    """
    # Additional fields or validations can be added here if necessary.

class StoreUpdate(BaseModel):
    """
    Schema for updating an existing store. All fields are optional to allow partial updates.
    """
    name: Optional[NameStr] = None
    address: Optional[AddressStr] = None

class StoreInDB(StoreBase):
    """
    Schema for returning a store from the database, includes the store's ID.
    """
    id: int
