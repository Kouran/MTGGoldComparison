from sqlalchemy import create_engine, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from logic.helpers import is_float


DATABASE = 'store/db.db'

engine = create_engine('sqlite:///' + DATABASE)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

from logic.models import Card, Valuable


def init_db():
	Base.metadata.create_all(engine, checkfirst=True)
	return


def check_db():
	import os.path
	if not os.path.isfile(DATABASE):
		print("Database does not exist. Creating")
		init_db()


def save_card(name, set, image_uri):
	card = Card(name, set, image_uri)
	db_session.add(card)
	db_session.commit()
	return


def save_valuable(name):
	valuable = Valuable(name)
	db_session.add(valuable)
	db_session.commit()
	return


def find_card(name, set_name):
	return Card.query.filter_by(name=name, set_name=set_name).first()


def search_cards(name, set_name, min_price, max_price):
	if is_float(min_price):
		min_price=float(min_price)
	else:
		min_price=0
	if is_float(max_price):
		max_price = float(max_price)
	else:
		max_price=9999999
	return Card.query.filter(and_(Card.name.ilike("%"+name+"%"),Card.set_name.ilike("%"+set_name+"%"),Card.price>=min_price),Card.price<=max_price).limit(500).all()


def find_valuable(name):
	return Valuable.query.filter_by(name=name).first()


def update_price_card(name, set_name, price):
	card = find_card(name, set_name)
	if card:
		card.price = price
		db_session.commit()


def update_price_valuable(name, price):
	valuable = find_valuable(name)
	if valuable:
		valuable.price = price
		db_session.commit()
