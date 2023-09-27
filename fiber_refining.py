'''Cloth Refining module - To be updated'''

from multi_modules_functions import refining_mats_variables
from multi_modules_functions import api_url_csv


cloth_items = refining_mats_variables('FIBER','CLOTH')
url_cloth = api_url_csv(cloth_items)
