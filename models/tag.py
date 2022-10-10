from sqlalchemy import UniqueConstraint
from db import db

class TagModel(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    store = db.relationship("StoreModel", back_populates="tags")
    items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")
    # https://stackoverflow.com/questions/26895207/how-is-a-unique-constraint-across-three-columns-defined
    __table_args__ = (UniqueConstraint(name, store_id, name='tag_store_uc'),)