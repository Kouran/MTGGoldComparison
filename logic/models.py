from sqlalchemy import Integer, String, Column, UniqueConstraint, Float
from logic.db import Base


class Card(Base):
	__tablename__ = "card"

	id = Column(Integer, autoincrement=True, primary_key=True)
	name = Column(String(64), nullable=False)
	set_name = Column(String(64), nullable=False)
	image_uri = Column(String(256), nullable=False)
	price = Column(Float)
	UniqueConstraint("name", "set_name")

	def __init__(self, name, set_name, image_uri):
		self.name = name
		self.set_name = set_name
		self.image_uri = image_uri
		self.price=0

	def __repr__(self):
		return "<Card(name=%s, set_name=%s, image_uri=%s, price=%s)>" % (self.name, self.set_name, self.image_uri, str(self.price))


class Valuable(Base):
	__tablename__ = "valuable"

	id = Column(Integer, autoincrement=True, primary_key=True)
	name = Column(String(64), nullable=False)
	price = Column(Float)
	price_adjusted = Column(Float)
	UniqueConstraint("name")

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "<Valuable(name=%s, price=%s, price_adjusted=%s)>" % (self.name, str(self.price), str(self.price_adjusted))

	def store_price(self, price):
		self.price=price
		self.price_adjusted=price*1.814
