import json
import logging
import os

import click
from scrapy.crawler import CrawlerProcess
from fastapi import FastAPI
from pydantic import BaseModel
from project_scraper.spiders.my_spider import MySpiderSpider
from project_scraper.spiders.tj_al_and_ce import TjalSpider
from uvicorn import run

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
app = FastAPI()


@app.post("/consulta_processo")
async def consulta_processo(data: dict):
    print('data_received: ', data)
    result = {"mensagem": "Processo consultado com sucesso", "numero_processo": data['numero_processo']}

    return result


@click.command("initialize-api")
@click.option("--port", default=5000, help="Port number to use.")
@click.option("--host", default='0.0.0.0', help="Host number to use.")
def main_fastapi(port, host):
    run(app, port=port, host=host)


@click.command("crawl-process")
@click.option("--process-number", type=click.STRING, help="Process number to scrape data",
              default='0070337-91.2008.8.06.0001')
@click.option("--output-path", type=click.STRING, help="Your local path to save files", default=".")
def main_scraper(process_number: str, output_path: str):
    """
    Main program execution.
    https://www.randomlists.com/urls

    bash to output docker files
    docker run -it -v /path/to/local/folder:/data scrapy-image scrapy crawl spider_name -o /data/output.json


    :param process_number:
    :param output_path:
    :type url: url to search
    :return: .json file
    """
    logging.debug(str(f"Initializing data collector"))
    logging.info(str(f"Searching: {process_number}"))
    logging.info(str(f"Output path: {output_path}"))
    data_to_return = {'search_status':'notfound',
    'description':str(f"Value not found for {process_number}"),
                      'data':[]}
    try:
        os.remove('collected_website_data.json')
    except FileNotFoundError:
        pass

    feed_uri = str(f"{output_path}/collected_website_data.json")

    process = CrawlerProcess(settings={'BOT_NAME': 'project_scraper',
                                       'ROBOTSTXT_OBEY': False,
                                       'CONCURRENT_ITEMS': 32,
                                       'CONCURRENT_REQUESTS_PER_DOMAIN': 16,
                                       'CONCURRENT_REQUESTS_PER_IP': 16,
                                       'DOWNLOAD_TIMEOUT': 6,
                                       'FEED_EXPORT_ENCODING': 'utf-8',
                                       'NEWSPIDER_MODULE': 'project_scraper.spiders',
                                       'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
                                       'RETRY_ENABLED': False,
                                       'RETRY_HTTP_CODES': [500, 502, 503, 504, 522, 524, 408],
                                       'RETRY_TIMES': 5,
                                       'FEED_FORMAT': 'json',
                                       'FEED_URI': feed_uri,
                                       'SPIDER_MODULES': ['project_scraper.spiders'],
                                       'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor',
                                       'ITEM_PIPELINES': {
                                           'project_scraper.pipelines.ProjectScraperPipeline': 300,
                                       }
                                       }

                             )

    process.crawl(TjalSpider, process_number)
    process.start()

    try:
        with open(feed_uri, 'r') as file:
            data = json.load(file)
        data_to_return['search_status'] = 'success'
        data_to_return['description'] = str(f"Value found for {process_number}")
        data_to_return['data'] = data
    except json.decoder.JSONDecodeError:
        pass

    return data_to_return


if __name__ == '__main__':
    """import requests

    url = "http://localhost:8000/consulta_processo"
    json_data = {'numero_processo': '0x4a555'}

    response = requests.post(url, json=json_data)
    print(response.json())"""

    main_scraper()
