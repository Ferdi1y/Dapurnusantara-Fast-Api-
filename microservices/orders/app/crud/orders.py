from sqlalchemy.orm import Session
from app.models.orders import *
from app.schemas.orders import *

def get_orders(db: Session, item_id: int):
    return db.query(Orders).filter(Orders.id == item_id).first()

def create_orders(db: Session, item: OrdersCreate):
    db_item = Orders(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_orders(db: Session, db_item: Orders, item: OrdersCreate):
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_orders(db: Session, item_id: int):
    db_item = db.query(Orders).filter(Orders.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item
