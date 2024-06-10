# app/schemas/location_schema.py
from typing import Optional
from pydantic import BaseModel

class LocationBase(BaseModel):
    description: str
    zone_id: int

class LocationCreate(LocationBase):
    barcode: Optional[str] = None  # Include barcode in creation schema

class LocationUpdate(LocationBase):
    barcode: Optional[str] = None  # Allow updating of barcode

class LocationInDB(LocationBase):
    id: int
    barcode: Optional[str] = None

    class Config:
        orm_mode = True
