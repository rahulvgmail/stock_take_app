from typing import Annotated, Optional
from pydantic import BaseModel, EmailStr, constr

NameStr = Annotated[str, constr(min_length=1, max_length=100)]
PhoneStr = Annotated[str, constr(min_length=10, max_length=15, regex=r'^\+?\d[\d -]{8,14}\d$')]

class CustomerBase(BaseModel):
    name: NameStr
    email: EmailStr  # Assuming email is required

class CustomerCreate(CustomerBase):
    phone: PhoneStr  # Phone number required on creation

class CustomerUpdate(BaseModel):
    name: Optional[NameStr] = None  # Name optional for updates
    email: Optional[EmailStr] = None  # Email optional for updates
    phone: Optional[PhoneStr] = None  # Phone optional for updates

class CustomerInDB(CustomerBase):
    id: int
    phone: PhoneStr
