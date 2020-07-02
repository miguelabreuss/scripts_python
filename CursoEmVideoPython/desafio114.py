import requests

def url_check(url):
    try:
        r = requests.head(url)
    except:
        print(f'\33[:31mO Site {url} está fora do ar.\33[m')
    else:
        print(f'\33[:32mO Site {url} está online.\33[m')


url_check('http://www.pudim.com.br')