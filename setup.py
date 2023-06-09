from setuptools import setup, find_packages

setup(
    name='extracao_dados_juridicos',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/thiagosilva977/api-extracao-dados-juridicos',
    license='',
    author='Thiago Silva',
    author_email='thiagosilva977@hotmail.com',
    description='Inicializa uma api para extrair processos juridicos.',
    setup_requires=['wheel'],
    install_requires=[
        "click>=8.1.3",
        "setuptools>=62.1.0",
        "urllib3>=1.26.15",
        "nest-asyncio>=1.5.6",
        "requests>=2.27.1",
        "bs4>=0.0.1",
        "Shapely>=1.8.1.post1",
        "pymongo>=4.1.1",
        "pandas>=1.4.2",
        "fastparquet>=0.8.1",
        "pyarrow>=10.0.1",
        "scrapy>=2.8.0",
        "fastapi>=0.95.0",
        "uvicorn>=0.21.1",
        "pydantic>=1.10.7",

    ],
    entry_points={
        'console_scripts': [
            "crawl-process=project_scraper.main:main_scraper_click",
            "initialize-api=project_scraper.main:main_fastapi",
        ]
    },
    include_package_data=True

)
