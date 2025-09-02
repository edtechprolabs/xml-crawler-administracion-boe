# XML Crawler para Administración.gob.es y BOE

Herramienta automatizada para crawling y descarga de archivos XML de ofertas de empleo público y sumarios del BOE.

## Funcionalidades
- Crawling diario de administracion.gob.es
- Descarga de sumarios XML del BOE
- Ejecución automatizada con GitHub Actions

## Configuración
1. Clona este repositorio
2. Instala dependencias: `pip install -r requirements.txt`
3. Ejecuta los scripts manualmente o configura GitHub Actions

## Estructura
/scripts
├── crawl_administracion.py
├── crawl_boe.py
└── download_xmls.py
/.github/workflows
└── crawl.yml
requirements.txt
.gitignore