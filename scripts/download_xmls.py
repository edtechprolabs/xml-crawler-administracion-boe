import requests
import os
from datetime import datetime

def download_xmls():
    # Crear directorio de descargas
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)
    
    # Descargar XMLs de administracion.gob.es
    try:
        with open("urls_administracion.txt", "r") as f:
            admin_urls = f.read().splitlines()
        
        for idx, url in enumerate(admin_urls):
            try:
                response = requests.get(url, timeout=10)
                filename = f"admin_{datetime.now().strftime('%Y%m%d')}_{idx}.xml"
                with open(os.path.join(download_dir, filename), "wb") as xml_file:
                    xml_file.write(response.content)
                print(f"Downloaded {filename}")
            except Exception as e:
                print(f"Error downloading {url}: {e}")
    except FileNotFoundError:
        print("No administracion URLs found")
    
    # Descargar XMLs del BOE
    try:
        with open("urls_boe.txt", "r") as f:
            boe_urls = f.read().splitlines()
        
        for idx, url in enumerate(boe_urls):
            try:
                response = requests.get(url, timeout=10)
                filename = f"boe_{datetime.now().strftime('%Y%m%d')}_{idx}.xml"
                with open(os.path.join(download_dir, filename), "wb") as xml_file:
                    xml_file.write(response.content)
                print(f"Downloaded {filename}")
            except Exception as e:
                print(f"Error downloading {url}: {e}")
    except FileNotFoundError:
        print("No BOE URLs found")

if __name__ == "__main__":
    download_xmls()