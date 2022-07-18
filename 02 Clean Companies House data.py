################################################################################
# 02 CLEAN COMPANIES HOUSE DATA
# AUTHOR: RORY CREEDON
################################################################################

################################################################################
# 0. Import relevant packages and set paths
################################################################################

import pandas as pd

path = r"H:\companies_house_scraping"

################################################################################
# 1. Clean data
################################################################################
data = pd.read_csv(path + "\data\companies_house_data.csv")

# Remove part of names in brackets
data['company_name_clean'] = data['CompanyName']
data['company_name_clean'].replace("[\(\[].*?[\)\]]","",regex=True, inplace = True)

# Clean company names
phrases = ["!", "LTD", "?", '"', "LIMITED", "", "GROUP", "INC", "(", ")", ".", "COMPANY", "PLC", "HODLINGS", "LLP", ]
for p in phrases:
    data['company_name_clean'] = data['company_name_clean'].str.replace(p,"", regex=False)

# 