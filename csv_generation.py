'''Module that creates the csv files'''

import os
from multi_modules_functions import refining_mats_variables
from multi_modules_functions import api_url_csv
from multi_modules_functions import save_data_to_csv

# TODO: add a function that executes this either on a timer or on specific request

script_directory = os.path.dirname(os.path.abspath(__file__))

wood_items = refining_mats_variables('WOOD', 'PLANKS')
ore_items = refining_mats_variables('ORE', 'METALBAR')
cloth_items = refining_mats_variables('FIBER', 'CLOTH')
hide_items = refining_mats_variables('HIDE', 'LEATHER')

wood_url = api_url_csv(wood_items)
ore_url = api_url_csv(ore_items)
cloth_url = api_url_csv(cloth_items)
hide_url = api_url_csv(hide_items)

csv_filename_wood = os.path.join(script_directory, 'wood_refining.csv')
csv_filename_ore = os.path.join(script_directory, 'ore_refining.csv')
csv_filename_cloth = os.path.join(script_directory, 'cloth_refining.csv')
csv_filename_fiber = os.path.join(script_directory, 'hide_refining.csv')

save_data_to_csv(wood_url, csv_filename_wood)
save_data_to_csv(ore_url, csv_filename_ore)
save_data_to_csv(cloth_url, csv_filename_cloth)
save_data_to_csv(hide_url, csv_filename_fiber)
