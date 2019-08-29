# MTG Gold Comparison

## Use case
Check which MTG cards cost more (per gram) than gold

## Logic
* MTG card database is build pulling bulk data from Scryfall website
* MTG cards prices will be pulled daily from MKM (if they approve my token request)
* Gold (and other valuables TBD) will be pulled daily from some finance website

All functions will be available via web GUI built

## Technologies
* App is written in Python 3.6
* Web app is built with Flask
* DB logic is built with SQLAlchemy
* Web pages are built with Jinja2
* MKM API mapping has been built by [Evonove](https://github.com/evonove/mkm-sdk)

## Endpoints
* `/` index dummy page (will host the comparison page)
* `/admin` administration page (will host the check db/check definitions links)
* `/check_definitions` updates card database from Scryfall
* `/update_definitions` updates card database from local file
* `/check_database` checks if db exists and if not creates it
* `/search` search page with simple form
* `/search_results` result page to show cards in db matching filters


## Author
[@KouranDarkhand](https://twitter.com/KouranDarkhand)