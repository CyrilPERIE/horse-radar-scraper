import asyncio
import logging
import schedule
import time
from .api_client import send_data_to_api
from .scrapers.instagram import instagram
from .scrapers.leboncoin import leboncoin
from .scrapers.marketplace import marketplace

logging.getLogger().setLevel(logging.INFO)

def main():

    logging.info("[scheduler] > Starting...")
    
    schedule.every().hour.at(":00").do(scrap_and_store, scrap_fn=instagram)
    schedule.every().hour.at(":20").do(scrap_and_store, scrap_fn=leboncoin)
    schedule.every().hour.at(":40").do(scrap_and_store, scrap_fn=marketplace)

    logging.info("[scheduler] > Running !")

    while True:
        schedule.run_pending()
        time.sleep(1)

def scrap_and_store(scrap_fn):
    logging.info(f"[scheduler] > Starting {scrap_fn.__name__}...")
    data = asyncio.run(scrap_fn())
    logging.info(f"[scheduler] > Ending {scrap_fn.__name__}...")
    if data:
        logging.info(f"[scheduler] > Storing data for {scrap_fn.__name__}...")
        send_data_to_api(data)
    else:
        logging.info(f"[scheduler] > No data for {scrap_fn.__name__}...")

if __name__ == "__main__":
    main()
