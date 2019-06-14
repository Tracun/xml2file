import os
import getpass
import xmltodict
from datetime import datetime

# Get User
USERNAME = getpass.getuser()

# Get the current date
now = datetime.now()

DAY = now.day
MONTH = now.month
YEAR = now.year

# Folder path
DIR = 'C:\\Users\\{}\\Desktop\\arquivos_XML\\XML'.format(USERNAME)
# Open output file
OUTPUT = open('./saida/xml_{}_{}_{}.txt'.format(DAY, MONTH, YEAR), 'w')

for root, dirs, files in os.walk(DIR):
    for filename in files:

        with open('./XML/'+filename, 'rb') as arq:
            doc = xmltodict.parse(arq)

            products = doc["nfeProc"]["NFe"]['infNFe']['det']['prod']
            for prod in products:
                prodName = prod['xProd']
                prodQuant = prod['qCom'].replace('.', ',')
                prodValue = prod['vProd'].replace('.', ',')

                # Write on file
                OUTPUT.write('{};{};{}\n'.format(prodName, prodQuant, prodValue))
                print('Nome:{}, Quant:{}, Valor:{}'.format(prodName, prodQuant, prodValue))

        # Delete file
        os.remove('./XML/'+filename)

OUTPUT.close()