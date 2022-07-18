################################################################################
# 01 DOWNLOAD COMPANIES HOUSE DATA
# AUTHOR: RORY CREEDON
################################################################################

################################################################################
# 0. Import relevant packages and set paths
################################################################################

import pandas as pd
import requests
from bs4 import BeautifulSoup as beautifulsoup

path = r"H:\companies_house_scraping"

################################################################################
# 1. Download relevant files
################################################################################

# Extract the HTML file from Companies House website
url = "http://download.companieshouse.gov.uk/en_output.html"
r = requests.get(url)
soup = beautifulsoup(r.text, 'html.parser')

# Parse HTML file for relevant links
links = []
for i in range(0, len(soup.find_all("li"))):
    if "AsOneFile" in str(soup.find_all("li")[i]).split('"')[1]: 
        next
    else:
        str_to_append = "http://download.companieshouse.gov.uk/" + str(soup.find_all("li")[i]).split('"')[1]
        links.append(str_to_append)

# Download data, keeping only relevant columns
required_columns = ['CompanyName', 'CompanyNumber', 'RegAddress.PostCode', 'CompanyCategory', 'CompanyStatus', 'IncorporationDate', 'Accounts.AccountCategory', 'Returns.LastMadeUpDate', 'SICCode.SicText_1', 'SICCode.SicText_2', 'SICCode.SicText_3', 'SICCode.SicText_4']
data = pd.read_csv(links[0], usecols=required_columns, skipinitialspace=True)

for i in range(1, len(links)):
    data_to_append = pd.read_csv(links[i], usecols=required_columns, skipinitialspace=True)
    data.append(data_to_append)

# Save as a CSV file
data.to_csv(path + r'\data\companies_house_data.csv', index=False)


#temp

import zipfile
from urllib.request import urlopen
import shutil
import os

url = 'http://download.companieshouse.gov.uk/BasicCompanyData-2022-07-01-part7_7.zip'
file_name = 'BasicCompanyData-2022-07-01-part7_7.zip'

# extracting zipfile from URL
with urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

    # extracting required file from zipfile
    with zipfile.ZipFile(file_name) as zf:
        zf.extract(path + r'\data\all_matches.csv')

# deleting the zipfile from the directory
os.remove('BasicCompanyData-2022-07-01-part7_7.zip')

# loading data from the file
data = pd.read_csv(path + r'\data\all_matches.csv')