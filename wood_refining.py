'''Wood Refining module - To be updated'''
import os
from multi_modules_functions import refining_mats_variables
from multi_modules_functions import api_url_csv
from multi_modules_functions import save_data_to_csv
from multi_modules_functions import show_best_price
from multi_modules_functions import refining_calculator
from multi_modules_functions import generate_variable_name

wood_items = refining_mats_variables('WOOD', 'PLANKS')
wood_url = api_url_csv(wood_items)

script_directory = os.path.dirname(os.path.abspath(__file__))
csv_filename = os.path.join(script_directory, 'wood_refining.csv')

# TODO: add a function that executes this either on a timer or on specific request
save_data_to_csv(wood_url, csv_filename)

ITEM_IDS = ['T3_PLANKS','T4_WOOD']
show_price = show_best_price(ITEM_IDS, csv_filename)
print(show_price)

ref_total_price = refining_calculator(show_price)
print()
print(f'Price for resources is {ref_total_price} silver')


variable_name = generate_variable_name('t4')
print(variable_name)
