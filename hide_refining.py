'''Hide Refining module - To be updated'''

from multi_modules_functions import refining_mats_variables
from multi_modules_functions import api_url_csv


hide_items = refining_mats_variables('HIDE','LEATHER')
url_hide = api_url_csv(hide_items)

print(url_hide)