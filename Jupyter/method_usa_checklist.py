#!/usr/bin/env python
# coding: utf-8
import pandas as pd
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#input file could be in excel or csv format
try:
    df = pd.read_csv('Files/am.csv')
except:
    df = pd.read_excel('Files/am.xlsx')

counts = df.count()


#checklist 1: SKU count must match with that of  description #1 
if(counts['SKU'] != counts['Description #1']):
    print('ERR: Description #1 count do not match')
else:
    print('Description #1 checklist passed')


#checklist 2: SKU count must match with that of Manufacturer part #  
if(counts['SKU'] != counts['MFRPart #']):
    print('ERR: MRFPart# count do not match')
else:
    print('MRFPart# checklist passed')


#checklist 3: SKU count must match with that of Manufacturer  
if(counts['SKU'] != counts['Manufacturer']):
    print('ERR: Manufacturer count do not match')
else:
    print('Manufacturer checklist passed')


# checklist 4: SKU count must match with that of Price Date  
if(counts['SKU'] != counts['Price Date']):
    print('ERR: Price Date count do not match')
else:
    print('Price Date checklist passed')

# because product page url is written in so many different ways 
try:
    product_page_url = counts['ProductPageURL']
except: 
    try:
        product_page_url = counts['Product Page URL']
    except:
        try:
            product_page_url = counts['ProductPage URL']
        except:
            product_page_url = counts['ProductPage Url']


#checklist 5: SKU count must match with that of ProductPageURL
if(counts['SKU'] != product_page_url):
    print('ERR: ProductPageURL count do not match')
else:
    print('ProductPageURL checklist passed')


# checklist 6: Category #1 must match with SKU count
if(counts['SKU'] != counts['Category #1']):
    print('{}ERR: Category #1 count do not match{}'.format(bcolors.FAIL, bcolors.ENDC))
else:
    print('Category #1 checklist passed')

