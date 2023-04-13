import glob
import json
import logging
import multiprocessing
import os
import random
import re
import string
import subprocess
from pathlib import Path

import click
import nest_asyncio
from fastapi import FastAPI
from scrapy.crawler import CrawlerProcess
from uvicorn import run

from project_scraper.spiders.tj_al_and_ce import TjalSpider

nest_asyncio.apply()

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
app = FastAPI()


@app.post("/consulta_processo")
@app.get("/consulta_processo")
async def consulta_processo(data: dict):
    print('data_received: ', data)
    data_to_return = {'search_status': 'notfound',
                      'description': '',
                      'data': []}
    pattern = r'\d{7}-\d{2}\.\d{4}\.\d{1,2}\.\d{1,2}\.\d{4}'
    matches = re.findall(pattern, data['numero_processo'])
    print(matches)
    if not matches:
        data_to_return['search_status'] = 'value_error'
        data_to_return['description'] = str(f"Value {data['numero_processo']} doesnt match the pattern.")
    else:
        if len(matches) == 1:
            instance_code = generate_random_code()
            mp = multiprocessing.Process(target=main_scraper,
                                         args=(data['numero_processo'], '.',
                                               instance_code))
            mp.start()
            mp.join()
            output_path = Path.cwd()
            file_to_found = glob.glob(str(f"{output_path}/*{instance_code}.json"))
            with open(file_to_found[0], 'r') as file:
                data = json.load(file)
        else:
            data_to_return['description'] = f'Collected {len(matches)} values.'
            all_instance_code = []
            all_mps = []
            all_results = []
            for item in matches:
                instance_code = generate_random_code()
                all_instance_code.append(instance_code)
                mpx = multiprocessing.Process(target=main_scraper,
                                              args=(item, '.',
                                                    instance_code))
                all_mps.append(mpx)

            for mp in all_mps:
                mp.start()
            for mp in all_mps:
                mp.join()

            output_path = Path.cwd()
            for current_instance in all_instance_code:
                files_to_found = glob.glob(str(f"{output_path}/*{current_instance}.json"))
                with open(files_to_found[0], 'r') as file:
                    data = json.load(file)
                    all_results.append(data)
            data_to_return['search_status'] = 'success'
            data_to_return['data'] = all_results
            data = data_to_return

    result = data
    
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
def main_scraper_click(process_number: str, output_path: str):
    main_scraper(process_number=process_number, output_path=output_path,
                 instance_code='testfile')


def main_scraper(process_number: str, output_path: str, instance_code: str):
    """
    Main program execution.
    https://www.randomlists.com/urls

    bash to output docker files
    docker run -it -v /path/to/local/folder:/data scrapy-image scrapy crawl spider_name -o /data/output.json


    :param instance_code:
    :param process_number:
    :param output_path:
    :return: .json file
    """
    output_path = Path.cwd()
    feed_uri = str(f"{output_path}/collected_website_data_{generate_random_code()}.json")

    logging.debug(str(f"Initializing data collector"))
    logging.info(str(f"Searching: {process_number}"))
    logging.info(str(f"Output path: {output_path}"))

    data_to_return = {'search_status': 'notfound',
                      'description': str(f"Value not found for {process_number}"),
                      'data': []}
    try:
        os.remove(feed_uri)
    except FileNotFoundError:
        pass
    """empty_dict = {}
    to_save_file = str(''+str(feed_uri))
    with open(to_save_file, 'w') as f:
        json.dump(empty_dict, f)"""

    pattern = r'\d{7}-\d{2}\.\d{4}\.\d{1,2}\.\d{1,2}\.\d{4}'
    matches = re.findall(pattern, process_number)
    print(matches)
    if not matches:
        data_to_return['search_status'] = 'value_error'
        data_to_return['description'] = str(f"Value {process_number} doesnt match the pattern.")
    else:
        for item in matches:
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
            # prevent error: https://stackoverflow.com/questions/74380442/
            # error-twisted-internet-error-reactornotrestartable
            results = []
            process.crawl(TjalSpider, item)
            process.start()
            """subprocess.call([f'scrapy crawl tjal -a input_process=' + item + ''], shell=True,
                            cwd=str(''))"""

    try:
        with open(feed_uri, 'r') as file:
            data = json.load(file)

        print(data)
        data_to_return['search_status'] = 'success'
        data_to_return['description'] = str(f"Value found for {process_number}")
        data_to_return['data'] = data
        # Save final result file

    except json.decoder.JSONDecodeError:
        pass

    except FileNotFoundError:
        pass

    print(data_to_return, 'xxsdfsdfsdfsdfs')
    to_save_file = str(f"{output_path}/resultfile_{instance_code}.json")
    with open(to_save_file, 'w') as f:
        json.dump(data_to_return, f)
    return data_to_return


def generate_random_code(length=4):
    # Define the set of characters to choose from
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits

    # Use random.choices to generate a list of random characters of the specified length
    code_list = random.choices(characters, k=length)

    # Convert the list to a string and return it
    code = ''.join(code_list)
    return code


if __name__ == '__main__':
    # main_scraper_click()
    main_fastapi()
