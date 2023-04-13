<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">API de Extração de Dados Jurídicos</h3>

  <p align="center">
    Api que retorna dados do TJCE e TJAL.
    <br />
    <a href="https://github.com/thiagosilva977/api-extracao-dados-juridicos/issues">Report Bug</a>
    ·
    <a href="https://github.com/thiagosilva977/api-extracao-dados-juridicos/pulls">Request Feature</a>
  </p>
</div>

## Descrição
O desafio é fazer uma API que busque dados de um processo em todos os graus dos Tribunais de Justiça de Alagoas (TJAL) e do Ceará (TJCE).

Geralmente o processo começa no primeiro grau e pode subir para o segundo. 

A aplicação busca o processo em todos os graus e retorna suas informações.
### Exemplos de processos jurídicos

```
0710802-55.2018.8.02.0001 , 0070337-91.2008.8.06.0001
```

### Implementação
Para este processo, foi utilizado:
- **FastAPI** para criação de uma API escalável, de alta performance e fácil desenvolvimento.
- **Scrapy** para crawling dos dados em alta performance de forma assíncrona, aproveitando o bom padrão de estrutura de código e sua boa modularidade. 
- **Docker** para uma boa portabilidade, sendo possível de ser executado em qualquer máquina e mantendo eficiência e escalabilidade.
- **Click** para decorators de funções.
- **Regex e BS4** para parsing dos dados.

### Fluxograma
 <img src="https://user-images.githubusercontent.com/11250089/231607303-b3e14394-6099-4ae8-b95f-041f2fb099e8.png" alt="Logo" width="500" height="300">

## Docker
### Pull 
`docker pull thiago977/thiagosilva_consulta_juridica:latest`
### Run
#### Inicializar API
`docker run -p 8000:8000 -p 5000:5000 thiago977/thiagosilva_consulta_juridica:latest initialize-api --port=5000 --host="0.0.0.0"`

#### Executar uma coleta de teste
`docker run thiago977/thiagosilva_consulta_juridica:latest crawl-process`

## Uso da API
- Usamos o endpoint `/consulta_processo` para realizar a extração dos dados
- Enviamos um json com o seguinte padrão:  {'numero_processo': '0000000-00.yyyy.m.dd.0000'} .
- É possível também solicitar uma lista de números de processos, seja ela uma lista, uma lista em forma de string, ou até mesmo
como um dado não estruturado. 
- Enviar requisição POST ou GET possuem o mesmo efeito.


#### Exemplo de requisição
```
import requests
url = "http://0.0.0.0:5000/consulta_processo"
json_data = {'numero_processo': '0710802-55.2018.8.02.0001'}
response = requests.post(url, json=json_data)

print(response.status_code)
print(response.json())
```  

## Resultados

#### Exemplo de resposta TJAL
```
200
{
   "search_status":"success",
   "description":"Value found for 0710802-55.2018.8.02.0001",
   "data":[
      {
         "process_number":"0710802-55.2018.8.02.0001",
         "classe":"Procedimento Comum Cível",
         "area":"Cível",
         "foro":"Foro de Maceió",
         "vara":"4ª Vara Cível da Capital",
         "assunto":"Dano Material",
         "data_distribuicao":"02/05/2018 às 19:01 - Sorteio",
         "juiz":"José Cícero Alves da Silva",
         "valor_acao":"R$         281.178,42",
         "partes_processo":[
            {
               "tipo_autor":"Autor",
               "nome_parte":"José Carlos Cerqueira Souza Filho",
               "nome_advogados":[
                  "Vinicius Faria de Cerqueira"
               ]
            },
            {
               "tipo_autor":"Autora",
               "nome_parte":"Livia Nascimento da Rocha",
               "nome_advogados":[
                  "Vinicius Faria de Cerqueira"
               ]
            },
            {
               "tipo_autor":"Ré",
               "nome_parte":"Cony Engenharia Ltda.",
               "nome_advogados":[
                  "Carlos Henrique de Mendonça Brandão",
                  "Guilherme Freire Furtado",
                  "Maria Eugênia Barreiros de Mello",
                  "Vítor Reis de Araujo Carvalho"
               ]
            },
            {
               "tipo_autor":"Réu",
               "nome_parte":"Banco do Brasil S A",
               "nome_advogados":[
                  "Nelson Wilians Fratoni Rodrigues"
               ]
            }
         ],
         "lista_movimentacoes":[
            {
               "data_movimento":"22/02/2021",
               "descricao_movimento":"None",
               "status_movimento":"Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso"
            },
            {
               "data_movimento":"06/01/2021",
               "descricao_movimento":"Relação :0003/2021 Data da Publicação: 21/01/2021 Número do Diário: 2738",
               "status_movimento":"Ato Publicado"
            },
            {
               "data_movimento":"06/01/2021",
               "descricao_movimento":"Relação :0003/2021 Data da Publicação: 21/01/2021 Número do Diário: 2738",
               "status_movimento":"Ato Publicado"
            },
            {
               "data_movimento":"22/02/2021",
               "descricao_movimento":"None",
               "status_movimento":"Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso"
            },
            {
               "data_movimento":"06/01/2021",
               "descricao_movimento":"Relação :0003/2021 Data da Publicação: 21/01/2021 Número do Diário: 2738",
               "status_movimento":"Ato Publicado"
            },
            {
               "data_movimento":"06/01/2021",
               "descricao_movimento":"Relação :0003/2021 Data da Publicação: 21/01/2021 Número do Diário: 2738",
               "status_movimento":"Ato Publicado"
            },
            {
               "data_movimento":"06/01/2021",
               "descricao_movimento":"Relação :0003/2021 Data da Publicação: 21/01/2021 Número do Diário: 2738",
               "status_movimento":"Ato Publicado"
            },
            {
               "data_movimento":"05/01/2021",
               "descricao_movimento":"Relação: 0003/2021 Teor do ato: Ato Ordinatório: Interposto recurso de apelação pelos réus (Banco do Brasil e Cony Engenharia), intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 04 de janeiro de 2021. Fernanda Patrícia Belo Marques Técnico Judiciário Advogados(s): Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)",
               "status_movimento":"Disponibilização no Diário da Justiça Eletrônico"
            },
            {
               "data_movimento":"18/12/2020",
               "descricao_movimento":"Nº Protocolo: WMAC.20.70269584-0 Tipo da Petição: Juntada de Instrumento de Procuração Data: 18/12/2020 17:23",
               "status_movimento":"Juntada de Documento"
            },
            {
               "data_movimento":"15/12/2020",
               "descricao_movimento":"Nº Protocolo: WMAC.20.70265228-8 Tipo da Petição: Recurso de Apelação Data: 15/12/2020 13:26",
               "status_movimento":"Juntada de Documento"
            },
            {
               "data_movimento":"24/11/2020",
               "descricao_movimento":"Relação :0912/2020 Data da Publicação: 25/11/2020 Número do Diário: 2711",
               "status_movimento":"Ato Publicado"
            },
            {
               "data_movimento":"24/11/2020",
               "descricao_movimento":"Relação :0912/2020 Data da Publicação: 25/11/2020 Número do Diário: 2711",
               "status_movimento":"Ato Publicado"
            },
            {
               "data_movimento":"23/11/2020",
               "descricao_movimento":"Forte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a data da efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em donos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como colorário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se.Vencimento: 16/12/2020",
               "status_movimento":"Julgado procedente em parte do pedido"
            },
            {
               "data_movimento":"16/08/2020",
               "descricao_movimento":"Despacho Visto em Autoinspeção",
               "status_movimento":"Visto em Autoinspeção"
            },
            {
               "data_movimento":"10/12/2019",
               "descricao_movimento":"None",
               "status_movimento":"Conclusos"
            },
            {
               "data_movimento":"12/07/2019",
               "descricao_movimento":"Nº Protocolo: WMAC.19.70150828-9 Tipo da Petição: Petição Data: 11/07/2019 23:50",
               "status_movimento":"Juntada de Petição"
            },
            {
               "data_movimento":"11/02/2019",
               "descricao_movimento":"Nº Protocolo: WMAC.19.70032532-6 Tipo da Petição: Petição Data: 11/02/2019 09:13",
               "status_movimento":"Juntada de Petição"
            },
            {
               "data_movimento":"05/12/2018",
               "descricao_movimento":"Nº Protocolo: WMAC.18.70259903-1 Tipo da Petição: Petição Data: 05/12/2018 16:46",
               "status_movimento":"Juntada de Petição"
            },
            {
               "data_movimento":"28/11/2018",
               "descricao_movimento":"Relação :0499/2018 Data da Publicação: 29/11/2018 Número do Diário: 2233",
               "status_movimento":"Ato Publicado"
            },
            {
               "data_movimento":"27/11/2018",
               "descricao_movimento":"ATO ORDINATÓRIO Em cumprimento ao disposto no art. 152,VI do CPC, procedo à intimação das partes para especificarem e justificarem as provas que ainda pretendem produzir, fundamentamente, pelo prazo comum de 5(cinco) dias. Maceió, 27 de novembro de 2018",
               "status_movimento":"Ato ordinatório praticado"
            },
            {
               "data_movimento":"26/11/2018",
               "descricao_movimento":"Nº Protocolo: WMAC.18.70251511-3 Tipo da Petição: Impugnação à Contestação Data: 26/11/2018 15:35",
               "status_movimento":"Juntada de Documento"
            },
            {
               "data_movimento":"08/11/2018",
               "descricao_movimento":"Relação: 0456/2018 Teor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Ordinário Autor: José Carlos Cerqueira Souza Filho e outro Réu: Conaço Engenharia Ltda. e outro ATO ORDINATÓRIO Intimo a parte autora a apresentar, querendo, no prazo de 15 (quinze) dias, impugnação às contestações. Maceió, 06 de novembro de 2018 Hallph Sá de Araújo Analista Judiciário Advogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)",
               "status_movimento":"Disponibilização no Diário da Justiça Eletrônico"
            },
            {
               "data_movimento":"16/10/2018",
               "descricao_movimento":"Nº Protocolo: WMAC.18.70221617-5 Tipo da Petição: Contestação Data: 16/10/2018 14:43",
               "status_movimento":"Juntada de Documentos"
            },
            {
               "data_movimento":"24/09/2018",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de Documento"
            },
            {
               "data_movimento":"24/09/2018",
               "descricao_movimento":"Assentada - Genérico",
               "status_movimento":"Audiência Realizada"
            },
            {
               "data_movimento":"21/09/2018",
               "descricao_movimento":"Nº Protocolo: WMAC.18.70203544-8 Tipo da Petição: Petição Data: 21/09/2018 18:07",
               "status_movimento":"Juntada de Petição"
            },
            {
               "data_movimento":"21/09/2018",
               "descricao_movimento":"Nº Protocolo: WMAC.18.70203260-0 Tipo da Petição: Petição Data: 21/09/2018 13:58",
               "status_movimento":"Juntada de Petição"
            },
            {
               "data_movimento":"06/06/2018",
               "descricao_movimento":"Em 06  de  junho  de  2018 é juntado a estes autos o aviso de recebimento (AR803969759TJ - Cumprido), referente  ao  ofício  n. 0710802-55.2018.8.02.0001-0002, emitido para Conaço Engenharia Ltda.. Usuário:",
               "status_movimento":"Juntada de AR - Cumprido"
            },
            {
               "data_movimento":"15/05/2018",
               "descricao_movimento":"Relação :0220/2018 Data da Publicação: 16/05/2018 Número do Diário: 2105",
               "status_movimento":"Ato Publicado"
            },
            {
               "data_movimento":"11/05/2018",
               "descricao_movimento":"Relação: 0220/2018 Teor do ato: DECISÃOTrata-se de ação ordinária de indenização por danos morais e materias c/c obrigação de fazer c/c declaração de nulidade de contrato de financiamento bancário c/c pedido de tutela antecipada proposta por JOSÉ CARLOS CERQUEIRA SOUZA FILHO e LIVIA NASCIMENTO DA ROCHA, qualificados na inicial, em face de a CONY ENGENHARIA LTDA. e BANCO DO BRASIL, igualmente qualificados.Narra a exordial que os autores adquiriram o apartamento residencial de nº 502, da Torre I, do Empreendimento Residencial Dellavia Park Club, situado na Ladeira Murilo Monteiro Valente, n.º 375, no bairro do Barro Duro, Maceió/AL, cuja vendedora foi a ré CONY ENGENHARIA LTDA., pelo valor de R$ 232.000,00 (duzentos e trinta e dois mil reais).Segue narrando que o instrumento celebrado em 02/12/2013 previa a entrega do imóvel no prazo de 36 (trinta e seis) meses contados do início da obra, sendo admitida uma tolerância de no máximo 18 (dezoito) meses. Dentro dessa perspectiva, foi prometido que a obra seria iniciada em no máximo 60 (sessenta) dias da assinatura do contrato, ou seja seria iniciada em 02/02/2014 com previsão de entrega para 02/02/2017, porém, até a presente data a obra não foi concluída.Aduz que os demandantes ainda sendo cobrados ilegalmente pelo BANCO DO BRASIL, também réu da ação, numa suposta \"taxa de obra\", que decorre de financiamento bancário.Requer, em sede de tutela de urgência, que seja determinado ao BANCO DO BRASIL a SUSPENSÃO da cobrança de taxa de Obra.É o relatório. Decido.Ab initio, concedo aos Demandantes as benesses da assistência judiciária gratuita, em respeito as determinações contidas no art. 98 e art. 99 da Lei nº. 13.105/2015 (Código de Processo Civil - CPC/2015).O Código de Defesa do Consumidor, em seu art. 6.º, VIII, assegura como direito básico do consumidor a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiência. Busca-se, assim assegurar a igualdade material.Em que pese bastar apenas um dos requisitos para a inversão, o caso em tela preenche as duas condições. Assim com fulcro no art. 6.º, VIII, do CDC DECIDO POR INVERTER O ÔNUS DA PROVA.Passo a apreciar o pedido de tutela provisória de urgência.Segundo o art. 300 do CPC/15, a tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo. O dispositivo deixa evidentes os requisitos da tutela antecipada de urgência, quais sejam, a probabilidade do direito, doutrinariamente conhecida como fumus boni iuris, e o perigo de dano ou risco ao resultado útil do processo, chamado periculum in mora.Nesse trilhar, importa esclarecer que a tutela de urgência antecipada se funda em um Juízo de cognição sumária, de modo que a medida, quando concedida, será precária, haja vista ser fundamental a necessidade de ser reversível (300, §3º, do CPC/2015).Portanto, a antecipação provisória dos efeitos finais da tutela definitiva, permite o gozo antecipado e imediato dos efeitos próprios da tutela definitiva pretendida, mas não se funda em um juízo de valor exauriente, de modo que pode ser desconstituída a qualquer tempo.Nessa esteira de pensamento, passa-se a analisar o caso concreto e o preenchimento dos requisitos necessários à concessão da tutela provisória pretendida.No caso em tela, pretende a parte autora a suspensão da cobrança da \"taxa de obra\", em razão do suposto descumprimento contratual por parte da demandada no tocante ao prazo estabelecido para a entrega do imóvel.Conforme se extrai dos autos, as partes firmaram um contrato de compra e venda de um apartamento, tendo sido estipulada o prazo para sua entrega em 36 (trinta e seis) meses, com um prazo de tolerância de 18 (dezoito) meses, consoante cláusula quarta do contrato (fls.39). Logo o prazo final para entrega do imóvel se encerra em 02/08/2018, levando em consideração o prazo de tolerância estabelecido no contrato.É cediço que a taxa de evolução de obra é devida desde a aprovação do financiamento até o término da obra.\\xa0Portanto, se a obra atrasar, é devido o pagamento da referida taxa ao banco que financiou o imóvel, no caso, o Banco do Brasil, até a sua conclusão. Sendo certo que ocorrendo a mora da construtora requerida em relação à entrega do imóvel, a parte autora não pode ser penalizada com o pagamento de tal encargo.\\xa0No entanto, no caso em deslinde, ainda não houve mora da construtora, haja vista que ainda não fora encerrado o prazo estimado para entrega do imóvel. Nesse ponto impende destacar que é legal a cláusula contratual que prevê a prorrogação do prazo razoável para entrega do imóvel, considerando o princípio pacta sunt servanda.\\xa0Desta feita, verifica-se a ausência de probabilidade do direito da parte autora, haja vista que, consoante dito alhures, a taxa de evolução de obra é devida até a conclusão da obra, bem como que não houve mora por parte da construtora demandada, haja vista que não houve, ainda, atraso na entrega do imóvel, tendo em vista a cláusula que prevê prazo de tolerância para entrega do imóvel.Ante o exposto, por considerar ausente a probabilidade do direito (art. 300 do CPC/15), INDEFIRO o pedido de tutela de urgência requestado.Inclua-se o feito em pauta de audiência de conciliação. Cite-se a parte ré eintime-a desta decisão, bem como para que compareça à audiência na data designada pelo Cartório, o que deve ser feito com antecedência mínima de 20 dias.Intime-se os autores por advogado constituído (art. 334, §3º, CPC/15).Deverá a parte ré ser advertida da possibilidade do art. 334, §5º, bem como do termo inicial do prazo de contestação (art. 335).Fiquem as partes advertidas, ainda, de que o não comparecimento injustificado à audiência de conciliação é considerado ato atentatório à dignidade da justiça e será sancionado com multa de até dois por cento da vantagem econômica pretendida ou do valor da causa (art. 334, §8º).Publique-se. Intime-seMaceió, 10 de maio de 2018.Henrique Gomes de Barros TeixeiraJuiz de Direito Advogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)",
               "status_movimento":"Disponibilização no Diário da Justiça Eletrônico"
            },
            {
               "data_movimento":"11/05/2018",
               "descricao_movimento":"AR DIGITAL - Citação e Intimação - Audiência de Instrução e Julgamento - Juizado",
               "status_movimento":"Carta Expedida"
            },
            {
               "data_movimento":"11/05/2018",
               "descricao_movimento":"Conciliação Data: 24/09/2018 Hora 14:00 Local: Sala de Audiência Situacão: Realizada",
               "status_movimento":"Audiência Designada"
            },
            {
               "data_movimento":"03/05/2018",
               "descricao_movimento":"None",
               "status_movimento":"Conclusos"
            },
            {
               "data_movimento":"02/05/2018",
               "descricao_movimento":"None",
               "status_movimento":"Distribuído por Sorteio"
            }
         ],
         "url_processo":"https://www2.tjal.jus.br/cpopg/show.do?processo.numero=0710802-55.2018.8.02.0001"
      },
      {
         "process_number":"0710802-55.2018.8.02.0001",
         "classe":"Apelação Cível",
         "area":"Cível",
         "foro":"None",
         "vara":"None",
         "assunto":"Obrigações",
         "data_distribuicao":"None",
         "juiz":"None",
         "valor_acao":"281.178,42",
         "partes_processo":[
            {
               "tipo_autor":"Apelante:",
               "nome_parte":"Cony Engenharia Ltda.",
               "nome_advogados":[
                  "Carlos Henrique de Mendonça Brandão",
                  "Guilherme Freire Furtado",
                  "Maria Eugênia Barreiros de Mello",
                  "Vítor Reis de Araujo Carvalho"
               ]
            },
            {
               "tipo_autor":"Apelante:",
               "nome_parte":"Banco do Brasil S A",
               "nome_advogados":[
                  "Nelson Wilians Fratoni Rodrigues"
               ]
            },
            {
               "tipo_autor":"Apelado:",
               "nome_parte":"José Carlos Cerqueira Souza Filho",
               "nome_advogados":[
                  "Vinicius Faria de Cerqueira"
               ]
            },
            {
               "tipo_autor":"Apelada:",
               "nome_parte":"Livia Nascimento da Rocha",
               "nome_advogados":[
                  "Vinicius Faria de Cerqueira"
               ]
            }
         ],
         "lista_movimentacoes":[
            
         ],
         "url_processo":"https://www2.tjal.jus.br/cposg5/show.do?processo.codigo=P00006BXP0000"
      }
   ]
}
```

#### Exemplo de resposta TJCE

```
200
{
   "search_status":"success",
   "description":"Value found for 0070337-91.2008.8.06.0001",
   "data":[
      {
         "process_number":"0070337-91.2008.8.06.0001",
         "classe":"Ação Penal - Procedimento Ordinário",
         "area":"Criminal",
         "foro":"Fortaleza - Fórum Clóvis Beviláqua",
         "vara":"1ª Vara Criminal (SEJUD 1º Grau)",
         "assunto":"Crimes de Trânsito",
         "data_distribuicao":"02/05/2018 às 09:13 - Sorteio",
         "juiz":"None",
         "valor_acao":"None",
         "partes_processo":[
            {
               "tipo_autor":"Vítima",
               "nome_parte":"G. de O. C.",
               "nome_advogados":[
                  
               ]
            },
            {
               "tipo_autor":"Vítima",
               "nome_parte":"A. S. F.",
               "nome_advogados":[
                  
               ]
            },
            {
               "tipo_autor":"Autor",
               "nome_parte":"Ministério Público do Estado do Ceará",
               "nome_advogados":[
                  
               ]
            },
            {
               "tipo_autor":"Terceiro",
               "nome_parte":"Departamento de Tecnologia da Informação e Comunicação - DETIC (Polícia Civil)",
               "nome_advogados":[
                  
               ]
            },
            {
               "tipo_autor":"Testemunha",
               "nome_parte":"M. L. S. I.",
               "nome_advogados":[
                  
               ]
            }
         ],
         "lista_movimentacoes":[
            {
               "data_movimento":"16/08/2022",
               "descricao_movimento":"Nº Protocolo: WEB1.22.02299977-0 Tipo da Petição: Ofício Data: 16/08/2022 12:49",
               "status_movimento":"Juntada de Ofício"
            },
            {
               "data_movimento":"10/09/2021",
               "descricao_movimento":"None",
               "status_movimento":"Expedição de Certidão de Arquivamento"
            },
            {
               "data_movimento":"06/09/2021",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"16/08/2022",
               "descricao_movimento":"Nº Protocolo: WEB1.22.02299977-0 Tipo da Petição: Ofício Data: 16/08/2022 12:49",
               "status_movimento":"Juntada de Ofício"
            },
            {
               "data_movimento":"10/09/2021",
               "descricao_movimento":"None",
               "status_movimento":"Expedição de Certidão de Arquivamento"
            },
            {
               "data_movimento":"06/09/2021",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"27/08/2021",
               "descricao_movimento":"None",
               "status_movimento":"Expedição de Ofício"
            },
            {
               "data_movimento":"26/08/2021",
               "descricao_movimento":"None",
               "status_movimento":"Certidão emitida"
            },
            {
               "data_movimento":"25/08/2021",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de Carta Precatória/Rogatória"
            },
            {
               "data_movimento":"26/05/2021",
               "descricao_movimento":"None",
               "status_movimento":"Expedição de Certidão de Arquivamento"
            },
            {
               "data_movimento":"26/05/2021",
               "descricao_movimento":"None",
               "status_movimento":"Certidão emitida"
            },
            {
               "data_movimento":"19/04/2021",
               "descricao_movimento":"None",
               "status_movimento":"Remessa dos autos à Vara de Origem"
            },
            {
               "data_movimento":"19/04/2021",
               "descricao_movimento":"None",
               "status_movimento":"Certidão emitida"
            },
            {
               "data_movimento":"07/04/2021",
               "descricao_movimento":"None",
               "status_movimento":"Certidão emitida"
            },
            {
               "data_movimento":"07/04/2021",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de Ofício"
            },
            {
               "data_movimento":"31/03/2021",
               "descricao_movimento":"None",
               "status_movimento":"Expedida carta precatória"
            },
            {
               "data_movimento":"29/03/2021",
               "descricao_movimento":"Vistos em conclusão. I - Considerando o teor do decisório de págs. 544/550, que transitou em julgado em 12/05/2020 (pág. 553), atualize-se o histórico do apenado WILLIAM AZEVEDO DOS SANTOS no sistema SAJPG. II - Comunique-se ao T.R.E (artigo 71, § 2º, do Código Eleitoral, c/c o art. 15, III, da Constituição Federal), através do Sistema Pólis. III Intime-se o sentenciado, por mandado, para entregar a carteira de habilitação no Gabinete deste Juízo, no prazo de 05 (cinco) dias, após o retorno do atendimento presencial no Fórum. Após a entrega da CNH, oficie-se o DETRAN comunicando a proibição imposta ao réu para dirigir veículo automotor no período assinalado, bem como para encaminhar o documento retido. IV- Expeça-se Carta de Guia à Vara de Execução de Penas Alternativas. V Após o cumprimento das providências acima ordenadas, arquivem-se os presentes autos. Expedientes necessários.",
               "status_movimento":"Proferido despacho de mero expediente"
            },
            {
               "data_movimento":"14/05/2020",
               "descricao_movimento":"Processo devolvido do SG.",
               "status_movimento":"Certificação de Processo Julgado"
            },
            {
               "data_movimento":"02/05/2018",
               "descricao_movimento":"res 06/2018",
               "status_movimento":"Processo Redistribuído por Sorteio"
            },
            {
               "data_movimento":"01/05/2018",
               "descricao_movimento":"None",
               "status_movimento":"Certidão emitida"
            },
            {
               "data_movimento":"17/04/2018",
               "descricao_movimento":"None",
               "status_movimento":"Certidão emitida"
            },
            {
               "data_movimento":"14/09/2016",
               "descricao_movimento":"None",
               "status_movimento":"Certidão emitida"
            },
            {
               "data_movimento":"01/09/2016",
               "descricao_movimento":"None",
               "status_movimento":"Remetido Recurso Eletrônico ao Tribunal de Justiça"
            },
            {
               "data_movimento":"01/09/2016",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"25/08/2016",
               "descricao_movimento":"None",
               "status_movimento":"Expedição de Ofício"
            },
            {
               "data_movimento":"23/08/2016",
               "descricao_movimento":"None",
               "status_movimento":"Concluso para Despacho"
            },
            {
               "data_movimento":"18/08/2016",
               "descricao_movimento":"Nº Protocolo: WEB1.16.10377382-2 Tipo da Petição: Pedido de Juntada de Documento Data: 17/08/2016 18:29",
               "status_movimento":"Juntada de Petição"
            },
            {
               "data_movimento":"28/06/2016",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"23/06/2016",
               "descricao_movimento":"Visto em inspeção ordinária - Portaria nº 01/2016.Oficie-se ao Juízo deprecado solicitando o cumprimento da carta precatória, no prazo de trinta(30) dias..",
               "status_movimento":"Proferido despacho de mero expediente"
            },
            {
               "data_movimento":"26/04/2016",
               "descricao_movimento":"None",
               "status_movimento":"Certidão emitida"
            },
            {
               "data_movimento":"14/04/2016",
               "descricao_movimento":"Recebo a apelação de pág. 301/320 no efeito suspensivo. Dê-se vista dos autos à representante ministerial para apresentar suas contrarrazões, no prazo de 08 (oito) dias.Apresentadas ou transcorrido o prazo, e devolvido o mandado de intimação do réu, sigam os autos ao TJ/CE.",
               "status_movimento":"Recebido o recurso Com efeito suspensivo"
            },
            {
               "data_movimento":"13/04/2016",
               "descricao_movimento":"Nº Protocolo: WEB1.16.10158782-7 Tipo da Petição: RECURSO DE APELAÇÃO Data: 13/04/2016 20:11",
               "status_movimento":"Juntada de Petição"
            },
            {
               "data_movimento":"09/04/2016",
               "descricao_movimento":"None",
               "status_movimento":"Certidão emitida"
            },
            {
               "data_movimento":"29/03/2016",
               "descricao_movimento":"None",
               "status_movimento":"Certidão emitida"
            },
            {
               "data_movimento":"29/03/2016",
               "descricao_movimento":"Cuida-se de embargos declaratórios manejados pela defesa do réu WILLIAM AZEVEDO DOS SANTOS, respaldado no artigo 382 do CPP. Conforme previsão do artigo 620 do CPP os embargos de declaração serão deduzidos em requerimento onde constem os pontos em que a sentença é ambígua, obscura, contraditória ou omissa, de modo a distingui-los do inconformismo próprio da apelação.Da petição que interpõe o embargo não há como identificar quais os argumentos que o postulante reputa vícios da sentença, pois ora narra que houve problemas de formação, acreditando tratar-se de arquivo corrompido, ora alega ausência de fundamentação e de justificativa na prolação do decreto condenatório. A sentença apresentada é sintética, abandona a disposição analítica, sem que isso represente afronta à indicação do CPP. A apresentação sintética, dividida por tópicos, reproduz a complexidade própria dos crimes de trânsito, sem comprometer qualquer dos seus requisitos essenciais. A solução do processo volta-se prioritariamente para agilidade e objetividade na exposição dos fatos, fundamento e dispositivo. No presente caso não há qualquer argumento de acusação, ou defesa, que tenha deixado de ser mencionado e apreciado circunstanciadamente. A vinculação a fórmulas não é capaz de oferecer resposta consentânea com as modernas exigências a que o Judiciário é desafiado: agilidade, clareza e segurança. O protagonismo desse processo deve ser compartilhado por todos que integram o sistema de justiça. Nesse sentido, é muito importante a crítica que surge da iniciativa recursal, desde que hábil a indicar que as deficiências da nova fórmula que merecem aprimoramento. O artigo 381 do CPP indica o conteúdo obrigatório da sentença como sendo: nomes das partes; exposição sucinta da acusação e da defesa; a indicação dos motivos de fato e de direito em que se fundar a decisão; a indicação dos artigos de lei aplicados; o dispositivo; data e a assinatura do juiz. O embargo não identifica a omissão ou insuficiência de qualquer deles, limita-se a imputar falta fundamentação, sem indicar qual argumento da acusação ou defesa que não foi apreciado fundamentadamente, para que a omissão possa ser suprida.Os embargos de declaração excepcionam a regra geral dos recursos, pois a sua interposição não visa necessariamente a reforma da decisão recorrida, mas à supressão de vício ou defeito que comprometa a compreensão do ato decisório.Desse modo, não havendo omissão capaz de admitir a oposição de embargos declaratórios, cumpre reconhecer a inadequação da pretensão veiculada pelo embargante, ante a ausência de pressuposto recursal, sendo impróprio o seu uso como sucedâneo da apelação ou como forma de exercitar efeito regressivo estranho à modalidade recursal eleita, contrariando à logica processual e os fins pretendidos pela norma vigente.Ante o exposto, rejeito os embargos declaratórios manejados pela defesa, em razão da ausência de pressuposto processual intrínseco ao recebimento do recurso, previsto no art. 620 do Código de Processo Penal, não há obscuridade, ambigüidade, contradição ou omissão a ser suprida.Intimem-se as partes. Prazo recursal interrompido apenas para a defesa. Intime-se para recontagem.",
               "status_movimento":"Embargos de Declaração Não-acolhidos"
            },
            {
               "data_movimento":"22/03/2016",
               "descricao_movimento":"None",
               "status_movimento":"Concluso para Decisão Interlocutória"
            },
            {
               "data_movimento":"22/03/2016",
               "descricao_movimento":"Entranhado o processo 0070337-91.2008.8.06.0001/01 - Classe: Embargos de Declaração em Ação Penal - Procedimento Ordinário - Assunto principal: Crimes de Trânsito",
               "status_movimento":"Processo entranhado"
            },
            {
               "data_movimento":"17/03/2016",
               "descricao_movimento":"None",
               "status_movimento":"Expedida carta precatória"
            },
            {
               "data_movimento":"14/03/2016",
               "descricao_movimento":"None",
               "status_movimento":"Certidão emitida"
            },
            {
               "data_movimento":"03/03/2016",
               "descricao_movimento":"None",
               "status_movimento":"Concluso para Sentença"
            },
            {
               "data_movimento":"19/11/2015",
               "descricao_movimento":"None",
               "status_movimento":"Certidão emitida"
            },
            {
               "data_movimento":"01/04/2015",
               "descricao_movimento":"None",
               "status_movimento":"Certidão com o Recebimento da Intimação Pessoal do Defensor"
            },
            {
               "data_movimento":"10/10/2014",
               "descricao_movimento":"Nº Protocolo: PROT.14.01353297-0 Tipo da Petição: Retorno de Carta Precatória Data: 06/10/2014 12:54 Complemento: Acompanha mídia original(CD).",
               "status_movimento":"Juntada de Carta Precatória/Rogatória"
            },
            {
               "data_movimento":"13/06/2014",
               "descricao_movimento":"None",
               "status_movimento":"Decorrido prazo"
            },
            {
               "data_movimento":"15/04/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de Aviso de Recebimento (AR)"
            },
            {
               "data_movimento":"20/02/2014",
               "descricao_movimento":"None",
               "status_movimento":"Expedida carta precatória"
            },
            {
               "data_movimento":"10/02/2014",
               "descricao_movimento":"None",
               "status_movimento":"Expedição de Termo"
            },
            {
               "data_movimento":"30/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de mandado"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de Petição"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de mandado"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de Aviso de Recebimento (AR)"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de Petição"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de Denúncia"
            },
            {
               "data_movimento":"28/01/2014",
               "descricao_movimento":"None",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"29/07/2013",
               "descricao_movimento":"JUNTADA DE DOCUMENTO TIPO DE DOCUMENTO: DESPACHO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"24/07/2013",
               "descricao_movimento":"JUNTADA DE DOCUMENTO TIPO DE DOCUMENTO: PARECER MP - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"11/07/2013",
               "descricao_movimento":"AUTOS ENTREGUES COM CARGA/VISTA AO MINISTÉRIO PÚBLICO NOME DO DESTINATÁRIO: DRA. MARIA DO CARMO  FUNCIONARIO: NEHYSE LIMA  NO. DAS FOLHAS: 00  DATA INICIAL DO PRAZO: 11/07/2013 - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Autos entregues com carga/vista ao ministério público"
            },
            {
               "data_movimento":"20/05/2013",
               "descricao_movimento":"JUNTADA DE DOCUMENTO TIPO DE DOCUMENTO: DESPACHO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"17/05/2013",
               "descricao_movimento":"JUNTADA DE DOCUMENTO TIPO DE DOCUMENTO: PARECER DEFENSOR PUBLICO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"17/05/2013",
               "descricao_movimento":"JUNTADA DE DOCUMENTO TIPO DE DOCUMENTO: PARECER DEFENSOR PUBLICO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Juntada de documento"
            },
            {
               "data_movimento":"14/05/2013",
               "descricao_movimento":"AUTOS ENTREGUES COM CARGA/VISTA AO DEFENSOR PÚBLICO NOME DO DESTINATÁRIO: DR. ATHILA BEZERRA   FUNCIONARIO: NEHYSE LIMA  NO. DAS FOLHAS: 00  DATA INICIAL DO PRAZO: 14/05/2013  DATA FINAL DO PRAZO: 19/05/2013 - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Autos entregues com carga/vista ao defensor público"
            },
            {
               "data_movimento":"23/08/2012",
               "descricao_movimento":"CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO COM RESPOSTA Á ACUSAÇÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Concluso ao juiz"
            },
            {
               "data_movimento":"21/08/2012",
               "descricao_movimento":"AUTOS ENTREGUES COM CARGA/VISTA AO DEFENSOR PÚBLICO NOME DO DESTINATÁRIO: Dr Lino  FUNCIONARIO: alberto  NO. DAS FOLHAS: 95  DATA INICIAL DO PRAZO: 22/08/2012  DATA FINAL DO PRAZO: 26/08/2012 - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Autos entregues com carga/vista ao defensor público"
            },
            {
               "data_movimento":"19/12/2011",
               "descricao_movimento":"EXPEDIÇÃO DE DOCUMENTO TIPO DE DOCUMENTO: CARTA PRECATÓRIA ENVIAR - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Expedição de documento"
            },
            {
               "data_movimento":"28/11/2011",
               "descricao_movimento":"EXPEDIÇÃO DE DOCUMENTO TIPO DE DOCUMENTO: MANDADO DE CITAÇÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Expedição de documento"
            },
            {
               "data_movimento":"31/10/2011",
               "descricao_movimento":"CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO COM DENÚNCIA - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Concluso ao juiz"
            },
            {
               "data_movimento":"31/10/2011",
               "descricao_movimento":"RECEBIDA A DENÚNCIA Inquerito transformado em Processo - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Recebida a denúncia"
            },
            {
               "data_movimento":"23/09/2011",
               "descricao_movimento":"CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Concluso ao juiz"
            },
            {
               "data_movimento":"23/05/2011",
               "descricao_movimento":"CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO DILIGÊNCIAS - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Concluso ao juiz"
            },
            {
               "data_movimento":"16/03/2011",
               "descricao_movimento":"ENTRADA DE PETIÇÃO DE ACOMPANHAMENTO Objeto Peticao :  - Local Entrada :SERVIÇO DE PORTARIA DOS FEITOS JUDICIAIS DA COMARCA DE FORTALEZA ( COMARCA DE FORTALEZA ) - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Entrada de petição de acompanhamento"
            },
            {
               "data_movimento":"18/06/2010",
               "descricao_movimento":"REMESSA DOS AUTOS DESTINO: À DELEGACIA 8º DP - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Remessa dos autos"
            },
            {
               "data_movimento":"27/05/2010",
               "descricao_movimento":"CONCLUSO AO JUIZ TIPO DE CONCLUSÃO: DESPACHO/DECISÃO - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Concluso ao juiz"
            },
            {
               "data_movimento":"27/05/2010",
               "descricao_movimento":"RECEBIDOS OS AUTOS DE QUEM: MP  PROVENIENTE DE : CARGA/VISTA - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Recebidos os autos"
            },
            {
               "data_movimento":"17/05/2010",
               "descricao_movimento":"AUTOS ENTREGUES COM CARGA/VISTA AO MINISTÉRIO PÚBLICO NOME DO DESTINATÁRIO: DR. BRUNO JORGE  FUNCIONARIO: MARTA ESDRAS  NO. DAS FOLHAS: 2  DATA INICIAL DO PRAZO: 17/05/2010 - Local: VARA ÚNICA DE TRÂNSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Autos entregues com carga/vista ao ministério público"
            },
            {
               "data_movimento":"10/03/2009",
               "descricao_movimento":"ENTRADA DE PETIÇÃO DE ACOMPANHAMENTO Objeto Peticao :  - Local Entrada :SERVIÇO DE PORTARIA DOS FEITOS JUDICIAIS DA COMARCA DE FORTALEZA ( COMARCA DE FORTALEZA ) - Local: 1ª VARA DE TRANSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Entrada de petição de acompanhamento"
            },
            {
               "data_movimento":"20/02/2009",
               "descricao_movimento":"REMESSA DOS AUTOS DESTINO: 8º DP. p/ diligências - Local: 1ª VARA DE TRANSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Remessa dos autos"
            },
            {
               "data_movimento":"19/01/2009",
               "descricao_movimento":"AUTOS ENTREGUES COM CARGA/VISTA AO MINISTÉRIO PÚBLICO NOME DO DESTINATÁRIO: DR. BRUNO JORGE  FUNCIONARIO: MARTA ESDRAS  NO. DAS FOLHAS: 31  DATA INICIAL DO PRAZO: 19/01/2009 - Local: 1ª VARA DE TRANSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Autos entregues com carga/vista ao ministério público"
            },
            {
               "data_movimento":"27/11/2008",
               "descricao_movimento":"AUTOS ENTREGUES COM CARGA/VISTA AO MINISTÉRIO PÚBLICO NOME DO DESTINATÁRIO: DR. BRUNO JORGE  FUNCIONARIO: MARTA ESDRAS  NO. DAS FOLHAS: 18  DATA INICIAL DO PRAZO: 27/11/2008 - Local: 1ª VARA DE TRANSITO DA COMARCA DE FORTALEZA",
               "status_movimento":"Autos entregues com carga/vista ao ministério público"
            },
            {
               "data_movimento":"14/07/2008",
               "descricao_movimento":"ENTREGUE AO PROMOTOR DE JUSTIÇA PROMOTOR: DRA. MORGANA - Local: CENTRAL DE INQUERITOS",
               "status_movimento":"Entregue ao promotor de justiça"
            },
            {
               "data_movimento":"11/07/2008",
               "descricao_movimento":"PERMITIR DISTRIBUIÇÃO - Local: SERVIÇO DE DISTRIBUIÇAO DOS FEITOS JUDICIAIS DA COMARCA DE FORTALEZA",
               "status_movimento":"Permitir distribuição"
            },
            {
               "data_movimento":"10/07/2008",
               "descricao_movimento":"PROTOCOLADO - Local: SERVIÇO DE PORTARIA DOS FEITOS JUDICIAIS DA COMARCA DE FORTALEZA",
               "status_movimento":"Protocolado"
            }
         ],
         "url_processo":"https://esaj.tjce.jus.br/cpopg/show.do?processo.numero=0070337-91.2008.8.06.0001"
      },
      {
         "process_number":"0070337-91.2008.8.06.0001",
         "classe":"None",
         "area":"None",
         "foro":"None",
         "vara":"None",
         "assunto":"None",
         "data_distribuicao":"None",
         "juiz":"None",
         "valor_acao":"None",
         "partes_processo":"None",
         "lista_movimentacoes":"None",
         "url_processo":"https://www2.tjal.jus.br/cpopg/show.do?processo.numero=0070337-91.2008.8.06.0001"
      },
      {
         "process_number":"0070337-91.2008.8.06.0001",
         "classe":"Apelação Criminal",
         "area":"Criminal",
         "foro":"None",
         "vara":"None",
         "assunto":"Crimes de Trânsito",
         "data_distribuicao":"None",
         "juiz":"None",
         "valor_acao":"None",
         "partes_processo":"None",
         "lista_movimentacoes":[
            
         ],
         "url_processo":"https://esaj.tjce.jus.br/cposg5/show.do?processo.codigo=P000020AM0000"
      }
   ]
}

```  
#### Exemplo de formato inválido de número de processo
```
200
{'search_status': 'value_error', 'description': 'Value 007fff7-91.2008.8.06.0001 doesnt match the pattern.', 'data': []} 
```
#### Exemplo de documento não encontrado
```
200
{'search_status': 'notfound', 'description': 'Value not found for 0070337-91.2008.8.06.0001', 'data': []}
```
