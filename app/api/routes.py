
from fastapi import APIRouter
from . import customer_api, stock_event_api, user_api, report_api, audit_api

router = APIRouter()

router.include_router(customer_api.router, prefix="/customers", tags=["customers"])
router.include_router(stock_event_api.router, prefix="/stock-events", tags=["stock-events"])
router.include_router(user_api.router, prefix="/users", tags=["users"])
router.include_router(report_api.router, prefix="/reports", tags=["reports"])
router.include_router(audit_api.router, prefix="/audits", tags=["audits"])
#sku
#location
#admin user
#admin interface to upload bulk data
# existing quantity  of stock while upload