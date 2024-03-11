from fastapi import HTTPException

from schema.customer import CustomerCreate, customers


class CustomerService:
    @staticmethod
    def check_unique_username( payload: CustomerCreate):
        username = payload.username
        existing_usernames = {customer.username for customer in customers}
        if username in existing_usernames:
            raise HTTPException(status_code=409, detail="Username already exists")
        return payload


customer_service = CustomerService()