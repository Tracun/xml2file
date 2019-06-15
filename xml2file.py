import os
import xmltodict
from datetime import datetime

# Get the current date
now = datetime.now()

DAY = now.day
MONTH = now.month
YEAR = now.year

# Folder path
# Open output file
OUTPUT = open('./saida/xml_{}_{}_{}.txt'.format(DAY, MONTH, YEAR), 'w')

for root, dirs, files in os.walk('./xml'):

    for filename in files:
        with open('./XML/'+filename, 'rb') as arq:
            doc = xmltodict.parse(arq)
            print(filename)
            products = doc["nfeProc"]["NFe"]['infNFe']['det']

            print(type(products))
            
            if(not type(products) is list):
                prodName = products['prod']['xProd']
                prodQuant = products['prod']['qCom'].replace('.', ',')
                prodValue = products['prod']['vProd'].replace('.', ',')

                # Write on file
                OUTPUT.write('{};{};{}\n'.format(prodName, prodQuant, prodValue))
                print('Nome:{}, Quant:{}, Valor:{}'.format(prodName, prodQuant, prodValue))
            else:
                for prod in products:
                    prodName = prod['prod']['xProd']
                    prodQuant = prod['prod']['qCom'].replace('.', ',')
                    prodValue = prod['prod']['vProd'].replace('.', ',')

                    # Write on file
                    OUTPUT.write('{};{};{}\n'.format(prodName, prodQuant, prodValue))
                    print('Nome:{}, Quant:{}, Valor:{}'.format(prodName, prodQuant, prodValue))

        # Delete file
        #os.remove('./XML/'+filename)

OUTPUT.close()