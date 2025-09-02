import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def crawl_boe():
    today = datetime.now().strftime("%Y%m%d")
    url = f"https://www.boe.es/datosabiertos/api/boe/sumario/{today}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        
        ns = {'ns': 'http://www.boe.es/ns/Sumario/1.0'}
        seccion_ii_b = root.find(".//ns:Seccion[ns:Nombre='II.B']", ns)
        
        boe_links = []
        if seccion_ii_b is not None:
            enlaces = seccion_ii_b.findall(".//ns:Enlace", ns)
            for enlace in enlaces:
                link = enlace.attrib.get('URL')
                if link and "BOE-A-2025" in link:
                    boe_links.append(link)
        
        return boe_links
    except Exception as e:
        print(f"Error crawling BOE: {e}")
        return []

if __name__ == "__main__":
    urls = crawl_boe()
    with open("urls_boe.txt", "w") as f:
        for url in urls:
            f.write(url + "\n")
    print(f"Found {len(urls)} URLs")