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
`docker run thiago977/thiagosilva_consulta_juridica:latest crawl-process


