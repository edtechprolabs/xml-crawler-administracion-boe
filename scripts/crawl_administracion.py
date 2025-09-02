import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
from datetime import datetime

def crawl_administracion():
    base_url = "https://administracion.gob.es"
    today = datetime.now().strftime("%d/%m/%Y")
    search_url = f"https://administracion.gob.es/pagFront/ofertasempleopublico/resultadosEmpleo.htm?referencia=&tipoConvocatoria=2&_ambitoGeografico=1&_comunidadAutonoma=1&_provincia=1&_tipoPlazo=1&_discapacidadGeneral=on&_discapacidadIntelectual=on&_tipoPersonal=1&tipoFechas=default&fechaPublicacionDesde={today.replace('/', '%2F')}&fechaPublicacionHasta=&tipoPlazaPublicacion=&_tipoBusqueda=on&_administracionConvocante=1&_nivelTitulacion=1&orders=id&sort=desc&desde=1&tam=&txtClaveE=&viaAcceso=2&buscar=true"
    
    try:
        response = requests.get(search_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        pattern = re.compile(r'detalleEmpleo\.htm\?idConvocatoria=\d+')
        links = soup.find_all('a', href=pattern)
        
        xml_urls = []
        for link in links:
            full_url = urljoin(base_url, link['href'])
            xml_urls.append(full_url)
        
        return xml_urls
    except Exception as e:
        print(f"Error crawling administracion.gob.es: {e}")
        return []

if __name__ == "__main__":
    urls = crawl_administracion()
    with open("urls_administracion.txt", "w") as f:
        for url in urls:
            f.write(url + "\n")
    print(f"Found {len(urls)} URLs")