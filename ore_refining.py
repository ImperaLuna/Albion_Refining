'''Ore Refining module - To be updated'''

from multi_modules_functions import refining_mats_variables
from multi_modules_functions import api_url_csv


ore_items = refining_mats_variables('ORE','METALBAR')
url_ore = api_url_csv(ore_items)
