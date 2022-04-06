import requests
import json
from urllib.request import urlopen
nome = input("NOME:")

cpf = input("CPF: ") # 00011122233
if len(cpf) < 11:
    cpf = cpf.zfill(11)
cpf_cl = ('{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:]))

cnpj = input("CNPJ: ") # 00111222333344
if len(cnpj) < 14:
    cnpj = cnpj.zfill(14)
cnpj_ven = ('{}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:]))

cep = input("CEP: ")
if len(cep) != 8:
    print("Quantidade de digitos inválida")
    exit()

busca_ceps = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))

busca_er = busca_ceps.json()
rua = input("RUA: ")
numero = input("NUMERO: ")
bairro = input("BAIRRO: ")
print("CADASTRO CONCLUÍDO COM SUCESSO!")

print("NOME:" +nome)
print("CPF:" +cpf_cl)
print("CNPJ:" +cnpj_ven)
print("ENDEREÇO:" + "{}, {}, {}".format(rua, numero, bairro))

if "erro" not in busca_er:
    print('CEP: {}'.format(busca_er['cep']))
    print('Cidade: {}'.format(busca_er['localidade']))
    print('Estado: {}'.format(busca_er['uf']))
else:
    print("{}: Digite um CEP válido. ".format(cep))

