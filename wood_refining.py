'''Wood Refining module - To be updated'''
import os
from multi_modules_functions import refining_mats_variables
from multi_modules_functions import api_url_csv
from multi_modules_functions import save_data_to_csv

wood_items = refining_mats_variables('WOOD', 'PLANKS')
wood_url = api_url_csv(wood_items)

script_directory = os.path.dirname(os.path.abspath(__file__))
csv_filename = os.path.join(script_directory, 'wood_refining.csv')

save_data_to_csv(wood_url, csv_filename)
