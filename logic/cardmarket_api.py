from mkmsdk.mkm import Mkm
from mkmsdk.api_map import _API_MAP
from os import environ

app_token="8E8kK8bxbENRJGBC"
app_secret="hS2A0OJiSxABc41woFSHFoGMiL1yh6JP"
mkm_sandbox = Mkm(_API_MAP["1.1"]["api"], _API_MAP["1.1"]["api_sandbox_root"])


def get_sets_on_mkm():
	response=mkm_sandbox.market_place.expansion(game="1")
	return response.json()


def get_cards_from_set_on_mkm(set_name):
	response=mkm_sandbox.market_place.expansion_singles(game="1", name=set_name)
	return response.json()


def get_card_from_id_on_mkm(product_id):
	response=mkm_sandbox.market_place.product(product=product_id)
	return response.json()


def set_env():
	environ["MKM_APP_TOKEN"]=app_token
	environ["MKM_APP_SECRET"]=app_secret
	environ["MKM_ACCESS_TOKEN"]=""
	environ["MKM_ACCESS_TOKEN_SECRET"]=""
	return