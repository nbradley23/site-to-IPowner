from ipwhois import IPWhois
import dns.resolver
import pandas as pd
import openpyxl

# Empty dict where results will go
site_and_cdn = {}

# Converting Excel sites column to Python list
sites = pd.read_excel('sites.xlsx')
column_name = 'Sites'
column_data = sites[column_name]

# List of sites
site_list = column_data.tolist()

for site in site_list:
    # Removes trailing / to avoid lookup errors
    if site[-1] == '/':
        site = site[:-1]
    # For any URL's containing subpages
    if '/' in site:
        site_and_cdn[site] = 'Subpage, please check root entry'
    else:
        resolver = dns.resolver.Resolver()
        try:
            # Resolves URL to IP adress
            results = list(resolver.resolve(f'{site}', "A"))[0]
            obj = IPWhois(results)
            # Saves the name of the owner of the IP address
            ip_results = obj.lookup_rdap(depth=1)['asn_description']
            # Adds the results to the dict with the URL as the key and owner as the value
            site_and_cdn[site] = ip_results
        except:
            site_and_cdn[site] = 'Unable to process'


# print(site_and_cdn)


# Export to excel spreadsheet
# df = pd.DataFrame(data=site_and_cdn, index=[0])
# df = (df.T)
# df.to_excel('sites-and-cdns.xlsx')
