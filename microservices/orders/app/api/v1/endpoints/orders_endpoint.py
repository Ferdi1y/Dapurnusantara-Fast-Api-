from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.orders import *
from app.schemas.orders import *
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Orders)
def create_orders(item: OrdersCreate, db: Session = Depends(get_db)):
    return create_orders(db=db, item=item)

@router.get("/{item_id}", response_model=Orders)
def read_orders(item_id: int, db: Session = Depends(get_db)):
    db_item = get_orders(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Orders not found")
    return db_item

@router.put("/{item_id}", response_model=Orders)
def update_orders(item_id: int, item: OrdersCreate, db: Session = Depends(get_db)):
    db_item = get_orders(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Orders not found")
    return update_orders(db=db, db_item=db_item, item=item)

@router.delete("/{item_id}", response_model=Orders)
def delete_orders(item_id: int, db: Session = Depends(get_db)):
    db_item = get_orders(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Orders not found")
    return delete_orders(db=db, item_id=item_id)

# Add more routes as needed
