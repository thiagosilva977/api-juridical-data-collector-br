import time

import scrapy
from bs4 import BeautifulSoup


class TjalSpider(scrapy.Spider):
    def __init__(self, input_process=None, **kwargs):
        super().__init__(**kwargs)
        self._input_url = input_process

    name = "tjal"
    start_urls = ["https://www2.tjal.jus.br/cpopg/open.do",
                  "https://www2.tjal.jus.br/cposg5/open.do"]

    def start_requests(self):
        print(self._input_url)

        urls_to_scrape = [str(f'https://www2.tjal.jus.br/cpopg/show.do?'
                              f'processo.numero={self._input_url}'),
                          str(f'https://www2.tjal.jus.br/cposg5/show.do?'
                              f'processo.numero={self._input_url}')
                          ]

        urls_to_scrape = [str(f'https://www2.tjal.jus.br/cpopg/show.do?'
                              f'processo.numero={self._input_url}'),
                          ]

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www2.tjal.jus.br/cpopg/open.do',
            'Connection': 'keep-alive',
            # 'Cookie': 'JSESSIONID=EB24AC9E02F1B0D2992C53E9510786DB.cpopg3',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
        }

        for url in urls_to_scrape:
            yield scrapy.Request(url=url,
                                 headers=headers, callback=self.parse)

    def parse(self, response, **kwargs):
        doc = {
            'classe': None,
            'area': None,
            'assunto': None,
            'data_distribuicao': None,
            'juiz': None,
            'valor_acao': None,
            'partes_processo': None,
            'lista_movimentacoes': None
        }

        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            data_classe = soup.find('span', {'id': 'classeProcesso'})['title']
            print(data_classe)
        except TypeError:
            pass
        try:
            data_assunto = soup.find('span', {'id': 'assuntoProcesso'})['title']
            print(data_assunto)
        except TypeError:
            pass

        try:
            data_foro = soup.find('span', {'id': 'foroProcesso'})['title']
            print(data_foro)
        except TypeError:
            pass
        try:
            data_vara = soup.find('span', {'id': 'varaProcesso'})['title']
            print(data_vara)
        except TypeError:
            pass
        try:
            data_juiz = soup.find('span', {'id': 'juizProcesso'})['title']
            print(data_juiz)
        except TypeError:
            pass
        try:
            data_area = soup.find('div', {'id': 'areaProcesso'}).find_next('span').text
            print(data_area)
        except TypeError:
            pass

        try:
            data_distribuicao = soup.find('div', {'id': 'dataHoraDistribuicaoProcesso'}).text
            print(data_distribuicao)
        except TypeError:
            pass
        try:
            data_valor = soup.find('div', {'id': 'valorAcaoProcesso'}).text
            print(data_valor)
        except TypeError:
            pass

        table_partes = soup.find('table', {'id': 'tableTodasPartes'})

        processos = []
        for tr in table_partes.find_all("tr", class_="fundoClaro"):
            tipo_autor = tr.find("td", class_="label").text.strip()
            nome_parte = tr.find("td", class_="nomeParteEAdvogado").text.split('Advogado:')[0].strip()
            advogados = []
            # test = tr.find_all('span', {'class': 'mensagemExibindo'})

            list_split = tr.text.split('Advogado:')
            print(list_split)
            print(len(list_split))
            for i in range(len(list_split)):
                if i == 0:
                    pass
                else:
                    current_text = list_split[i].replace('\n', '').replace('\t', '').replace('\xa0', '').strip()
                    if 'Advogada:' in current_text:
                        current_text = current_text.split('Advogada:')
                        for item in current_text:

                            advogados.append(item)
                    else:
                        advogados.append(current_text)

            processo = {
                "tipo_autor": tipo_autor,
                "nome_parte": nome_parte,
                "nome_advogados": advogados
            }
            processos.append(processo)


        print('finishh')
        time.sleep(1212)
