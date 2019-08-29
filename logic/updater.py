import requests
import wget
from json import loads
from logic.db import save_card, find_card
from os import remove


pickle_file_path = "store/environment.pickle"
definition_path = "store/scryfall-default-cards.json"



def check_card_definitions():
	path="https://api.scryfall.com/bulk-data"
	response=requests.get(path).json()
	for elem in response["data"]:
		if elem["type"]=="default_cards":
			last_definition=elem["updated_at"]
			card_definition=retrieve_card_definition()
			print("Last definitions is %s, deployed definition is %s" % (last_definition,card_definition))
			if last_definition!=card_definition:
				print("Old definitions")
				print("Downloading new definitions")
				remove(definition_path)
				wget.download(response["data"][0]["permalink_uri"], definition_path)
				store_card_definition(last_definition)
				print("Updating definitions")
				update_card_definitions()
			else:
				print("Definitions up to date")
			return


def update_card_definitions():
	with open(definition_path, encoding="utf-8") as def_file:
		for line in def_file:
			if len(line)>10:
				entry=loads(line[2:].strip(",\n"))
				if entry["object"]=="card" :
					name=entry["name"]
					set_name=entry["set_name"]
					if not (find_card(name, set_name) or entry["rarity"]=="common"):
						print("Saving %s from set %s" % (name,set_name))
						if "image_uris" in entry.keys():
							save_card(name, set_name, entry["image_uris"]["large"])
						else:
							save_card(name, set_name, entry["card_faces"][0]["image_uris"]["large"])





def store_card_definition(card_definition):
	from pickle import dump
	with open(pickle_file_path, "wb") as pickle_file:
		dump(card_definition, pickle_file)
	return


def retrieve_card_definition():
	from pickle import load
	with open(pickle_file_path, "rb") as pickle_file:
		card_definition=load(pickle_file)
	return card_definition

