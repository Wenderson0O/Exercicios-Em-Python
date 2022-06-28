import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O Site Não esta acessivel no momento.')
else:
    print('Site acessado com Sucesso!')
