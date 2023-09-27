'''Wood Refining module - To be updated'''

from multi_modules_functions import refining_mats_variables
from multi_modules_functions import api_url_csv


wood_items = refining_mats_variables('WOOD','PLANKS')
url = api_url_csv(wood_items)
