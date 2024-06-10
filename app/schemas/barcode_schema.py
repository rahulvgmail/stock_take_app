from pydantic import BaseModel

class BarcodeBase(BaseModel):
    barcode: str

class BarcodeCreate(BarcodeBase):
    sku_id: int

class BarcodeUpdate(BarcodeBase):
    sku_id: int

class BarcodeInDB(BarcodeBase):
    id: int
    sku_id: int

    class Config:
        orm_mode = True
