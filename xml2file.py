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
OUTPUT = open('C:\\Users\\55119\\Documents\\Automation Anywhere Files\\TaskBots\\NotaFiscal\\Arquivos TXT\\xml_{}_{}_{}.txt'.format(DAY, MONTH, YEAR), 'w')
countItems = 0

for root, dirs, files in os.walk('./xml'):

    for filename in files:
        with open('./XML/'+filename, 'rb') as arq:
            doc = xmltodict.parse(arq)
            print(filename)
            products = doc["nfeProc"]["NFe"]['infNFe']['det']

            print(type(products))
            
            if(not type(products) is list):
                prodCode = products['prod']['cProd']
                prodName = products['prod']['xProd']
                prodNCM = products['prod']['NCM']
                prodQuant = products['prod']['qCom'].replace('.', ',')
                prodValue = products['prod']['vUnCom']
                prodTotalOrto = products['prod']['vProd']
                prodLote = products[countItems]['infAdProd']
                prodTotal = float(prodQuant) * float(prodValue)
                prodUnidCom = products['prod']['uCom']
                prodUnidTrib = products['prod']['uTrib']
                
                prodQuant = prodQuant.replace('.', ',')
                prodValue = prodValue.replace('.', ',')
                prodTotal = str(prodTotal).replace('.', ',')
                prodTotalOrto = str(prodTotalOrto).replace('.', ',')

                # Write on file
                OUTPUT.write('{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n'.format(prodCode, prodName, prodNCM, prodQuant, prodValue, prodTotal, prodTotalOrto, prodLote, prodUnidCom, prodUnidTrib))
                print('Codigo:{}, Nome:{}, NCM:{}, Quant:{}, Valor:{}, Valor total:{}, Valor Total Orto:{}, lote:{}'.format(prodCode, prodName, prodNCM, prodQuant, prodValue, prodTotal, prodTotalOrto, prodLote))
            else:
                for prod in products:
                    prodCode = prod['prod']['cProd']
                    prodName = prod['prod']['xProd']
                    prodNCM = prod['prod']['NCM']
                    prodQuant = prod['prod']['qCom']
                    prodValue = prod['prod']['vUnCom']
                    prodTotalOrto = prod['prod']['vProd']
                    prodLote = products[countItems]['infAdProd']
                    prodTotal = float(prodQuant) * float(prodValue)
                    prodUnidCom = prod['prod']['uCom']
                    prodUnidTrib = prod['prod']['uTrib']
                    
                    prodQuant = prodQuant.replace('.', ',')
                    prodValue = prodValue.replace('.', ',')
                    prodTotal = str(prodTotal).replace('.', ',')
                    prodTotalOrto = str(prodTotalOrto).replace('.', ',')

                    # Write on file
                    OUTPUT.write('{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n'.format(prodCode, prodName, prodNCM, prodQuant, prodValue, prodTotal, prodTotalOrto, prodLote, prodUnidCom, prodUnidTrib))
                    print('Codigo:{}, Nome:{}, NCM:{}, Quant:{}, Valor:{}, Valor Total:{}, Valor Total Orto:{}, lote:{}'.format(prodCode, prodName, prodNCM, prodQuant, prodValue, prodTotal, prodTotalOrto, prodLote))
                    countItems += 1

        # Delete file
        #os.remove('./XML/'+filename)

OUTPUT.close()