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

#### Exemplo de resposta

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
