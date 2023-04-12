import re
import ssl

import requests
import scrapy
import urllib3
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

        """urls_to_scrape = [str(f'https://www2.tjal.jus.br/cposg5/show.do?'
                              f'processo.numero={self._input_url}'),
                          str(f'https://www2.tjal.jus.br/cpopg/show.do?'
                              f'processo.numero={self._input_url}')
                          ]"""

        urls_to_scrape = [str(f'https://esaj.tjce.jus.br/cpopg/show.do?'
                              f'processo.numero={self._input_url}'),
                          str(f'https://esaj.tjce.jus.br/cposg5/show.do?'
                              f'processo.numero={self._input_url}')
                          ]

        urls_to_scrape = [str(f'https://esaj.tjce.jus.br/cposg5/show.do?'
                              f'processo.numero={self._input_url}')

                          ]

        for url in urls_to_scrape:
            if 'cposg5' in url:

                year_digit_unified = str(re.search(r"\d{7}-\d{2}\.\d{4}", self._input_url).group())
                number_unified = self._input_url.split('.')[-1]

                if 'esaj.tjce' in url:
                    yield scrapy.Request(str(f'https://esaj.tjce.jus.br/cposg5/search.do;?conversationId=&'
                                             f'paginaConsulta=0'
                                             f'&cbPesquisa=NUMPROC&numeroDigitoAnoUnificado={year_digit_unified}&'
                                             f'foroNumeroUnificado={number_unified}&'
                                             f'dePesquisaNuUnificado={self._input_url}&'
                                             f'dePesquisaNuUnificado=UNIFICADO&dePesquisa=&tipoNuProcesso=UNIFICADO'),
                                         callback=self.get_tjce_request)

                else:

                    yield scrapy.Request(str(f'https://www2.tjal.jus.br/cposg5/search.do;?conversationId=&'
                                             f'paginaConsulta=0'
                                             f'&cbPesquisa=NUMPROC&numeroDigitoAnoUnificado={year_digit_unified}&'
                                             f'foroNumeroUnificado={number_unified}&'
                                             f'dePesquisaNuUnificado={self._input_url}&'
                                             f'dePesquisaNuUnificado=UNIFICADO&dePesquisa=&tipoNuProcesso=UNIFICADO'),
                                         callback=self.get_tjce_request)



            else:

                if 'esaj.tjce' in url:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'none',
                        'Sec-Fetch-User': '?1',
                    }
                    yield scrapy.Request(url=url,
                                         headers=headers, callback=self.parse)
                else:
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

                    yield scrapy.Request(url=url,
                                         headers=headers, callback=self.parse)

    def get_tjce_request(self, response, **kwargs):

        print(response)
        if 'esaj.tjce.jus.br' in str(response.url):
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Referer': 'https://esaj.tjce.jus.br/cposg5/open.do',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
            }
            soup = BeautifulSoup(response.text, 'html.parser')

            process_code = soup.find('input', {'id': 'processoSelecionado'})['value']

            scrape_url = str(f"https://esaj.tjce.jus.br/cposg5/show.do?processo.codigo={process_code}")

            yield scrapy.Request(url=scrape_url,
                                 headers=headers, callback=self.parse)

        else:
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
            soup = BeautifulSoup(response.text, 'html.parser')

            process_code = soup.find('input', {'id': 'processoSelecionado'})['value']

            scrape_url = str(f"https://www2.tjal.jus.br/cposg5/show.do?processo.codigo={process_code}")
            yield scrapy.Request(url=scrape_url,
                                 headers=headers, callback=self.parse)

    def parse(self, response, **kwargs):
        doc = {
            'process_number': self._input_url,
            'classe': None,
            'area': None,
            'foro': None,
            'vara': None,
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
            doc['classe'] = data_classe
        except AttributeError:
            pass
        except TypeError:
            try:
                data_classe = soup.find('div', {'id': 'classeProcesso'}).find_next('span')['title']
                print(data_classe)
                doc['classe'] = data_classe
            except TypeError:
                pass
            except AttributeError:
                pass
        try:
            data_assunto = soup.find('span', {'id': 'assuntoProcesso'})['title']
            print(data_assunto)
            doc['assunto'] = data_assunto
        except AttributeError:
            pass
        except TypeError:
            try:
                data_assunto = soup.find('div', {'id': 'assuntoProcesso'}).find_next('span')['title']
                print(data_assunto)
                doc['assunto'] = data_assunto
            except TypeError:
                pass
            except AttributeError:
                pass

        try:
            data_foro = soup.find('span', {'id': 'foroProcesso'})['title']
            print(data_foro)
            doc['foro'] = data_foro
        except AttributeError:
            pass
        except TypeError:
            try:
                data_foro = soup.find('div', {'id': 'foroProcesso'}).find_next('span')['title']
                print(data_foro)
                doc['foro'] = data_foro
            except TypeError:
                pass
            except AttributeError:
                pass

        try:
            data_vara = soup.find('span', {'id': 'varaProcesso'})['title']
            print(data_vara)
            doc['vara'] = data_vara
        except AttributeError:
            pass
        except TypeError:
            try:
                data_vara = soup.find('div', {'id': 'varaProcesso'}).find_next('span')['title']
                print(data_vara)
                doc['vara'] = data_vara
            except TypeError:
                pass
            except AttributeError:
                pass

        try:
            data_juiz = soup.find('span', {'id': 'juizProcesso'})['title']
            print(data_juiz)
            doc['juiz'] = data_juiz
        except AttributeError:
            pass
        except TypeError:
            try:
                data_juiz = soup.find('div', {'id': 'juizProcesso'}).find_next('span')['title']
                print(data_juiz)
                doc['juiz'] = data_juiz
            except TypeError:
                pass
            except AttributeError:
                pass

        try:
            data_area = soup.find('div', {'id': 'areaProcesso'}).find_next('span').text
            print(data_area)
            doc['area'] = data_area
        except TypeError:
            pass
        except AttributeError:
            pass

        try:
            data_distribuicao = soup.find('div', {'id': 'dataHoraDistribuicaoProcesso'}).text
            print(data_distribuicao)
            doc['data_distribuicao'] = data_distribuicao
        except TypeError:
            pass
        except AttributeError:
            pass

        try:
            data_valor = soup.find('div', {'id': 'valorAcaoProcesso'}).text
            print(data_valor)
            doc['valor_acao'] = data_valor
        except AttributeError:
            pass
        except TypeError:
            try:
                data_valor = soup.find('div', {'id': 'valorAcaoProcesso'}).find_next('span')['title']
                print(data_valor)
                doc['valor_acao'] = data_valor
            except TypeError:
                pass
            except AttributeError:
                pass

        try:
            table_partes = soup.find('table', {'id': 'tableTodasPartes'})

            processos = []
            for tr in table_partes.find_all("tr", class_="fundoClaro"):
                tipo_autor = tr.find("td", class_="label").text.strip()
                nome_parte = tr.find("td", class_="nomeParteEAdvogado").text.split('Advogado:')[0].strip()
                advogados = []

                list_split = tr.text.split('Advogado:')
                # print(list_split)
                # print(len(list_split))
                for i in range(len(list_split)):
                    if i == 0:
                        pass
                    else:
                        current_text = list_split[i].replace('\n', '').replace('\t', '').replace('\xa0', '').strip()
                        if 'Advogada:' in current_text:
                            current_text = current_text.split('Advogada:')
                            for item in current_text:
                                advogados.append(item.strip())
                        else:
                            advogados.append(current_text)

                processo = {
                    "tipo_autor": tipo_autor,
                    "nome_parte": nome_parte,
                    "nome_advogados": advogados
                }
                processos.append(processo)

            doc['partes_processo'] = processos
        except TypeError:
            pass
        except AttributeError:
            pass
        try:
            movimentacoes = soup.find('h2', text='Movimentações').find_next('table').find_all('tr', {
                'class': 'fundoClaro containerMovimentacao'})
            lista_movimentacoes = []
            for movimentacao in movimentacoes:
                data_movimentacao = movimentacao.find('td', {'class': 'dataMovimentacao'}).text.strip()
                descricao = movimentacao.find('td', {'class': 'descricaoMovimentacao'})

                italic_text = descricao.find('span', {'style': 'font-style: italic;'}).text.strip()
                if italic_text == '':
                    descricao_movimento = None
                    status_movimento = descricao.text.strip()
                else:
                    descricao_movimento = italic_text.replace('\n', ' ').replace('\r', '').strip()

                    status_movimento = str(descricao).split('">')[1].split('<br/>')[0].strip()

                    if '<a' in status_movimento:
                        status_movimento = descricao.find('a', {'class': 'linkMovVincProc'}).text.strip()

                dicionario_movimentacao = {'data_movimento': data_movimentacao,
                                           'descricao_movimento': descricao_movimento,
                                           'status_movimento': status_movimento}
                lista_movimentacoes.append(dicionario_movimentacao)
            doc['lista_movimentacoes'] = lista_movimentacoes
        except TypeError:
            pass
        except AttributeError:
            pass
        yield doc


class CustomHttpAdapter(requests.adapters.HTTPAdapter):
    # "Transport adapter" that allows us to use custom ssl_context.

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)


def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
    session = requests.session()
    session.mount('https://', CustomHttpAdapter(ctx))
    return session