from flask import Flask, render_template, request
from logic.helpers import extract_parameter
from logic.updater import check_card_definitions, update_card_definitions
from logic.db import search_cards, check_db
from threading import Thread

app = Flask(__name__)


@app.route('/')
def hello():
	return "Hello World!"


@app.route("/admin")
def admin():
	return render_template("admin.html")


@app.route("/check_definitions")
def check_definitions():
	update = Thread(target=check_card_definitions, args=())
	update.setDaemon(True)
	update.start()
	return render_template("message.html", message="Definitions check launched")


@app.route("/update_definitions")
def update_definitions():
	check = Thread(target=update_card_definitions, args=())
	check.setDaemon(True)
	check.start()
	return render_template("message.html", message="Definitions update launched")


@app.route("/check_database")
def check_database():
	check = Thread(target=check_db, args=())
	check.setDaemon(True)
	check.start()
	return render_template("message.html", message="Database check launched")


@app.route("/search")
def search():
	return render_template("search.html")


@app.route("/search_results")
def search_results():
	card_name = extract_parameter(request, 'card_name')
	set_name = extract_parameter(request, 'set_name')
	min_price = extract_parameter(request, 'min_price')
	max_price = extract_parameter(request, 'max_price')
	results = search_cards(card_name, set_name, min_price, max_price)
	return render_template("search_results.html", cards=results)


if __name__ == '__main__':
	from logic.cardmarket_api import set_env
	set_env()
	app.run()
