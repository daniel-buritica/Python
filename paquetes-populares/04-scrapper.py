import requests
from bs4 import BeautifulSoup

url = "https://www.farmatodo.com.co/destacados/50998?categoria=50998%3Futm_source%3Dcms%26utm_medium%3Dbanner_home%26utm_campaign%3Dfolleto%26utm_content%3Dcuidadopersonal%26utm_term%3Dgeneral05oct"
header_request = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-encoding': 'gzip, deflate, br',
    'Accept-language': 'en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7',
    'Connection': 'keep-alive',
    'Sec-ch-ua': 'Google Chrome;v=117, Not;A=Brand;v=8, Chromium;v=117',
    'Sec-ch-ua-mobile': '?0',
    'Sec-ch-ua-platform': 'Windows',
    'Sec-fetch-dest': 'image',
    'Sec-fetch-mode': 'no-cors',
    'Sec-fetch-site': 'same-origin',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

repuesta = requests.get(url, headers=header_request)
texto = repuesta.text
print(repuesta.request.headers)

print(texto)
soup = BeautifulSoup(texto, "html.parser")

productos = soup.select(".card-ftd")

for producto  in productos:
    print(producto)