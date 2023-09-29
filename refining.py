'''Wood Refining module - To be updated'''

from multi_modules_functions import show_best_price
from multi_modules_functions import refining_calculator
from multi_modules_functions import generate_variable_name
from multi_modules_functions import strip_variable_name
from multi_modules_functions import create_csv_filename


variable_name = generate_variable_name('t5.1', 'wood')
print(variable_name)

strip_var_name = strip_variable_name(variable_name)
print(strip_var_name)

resource_type = create_csv_filename(strip_var_name)
print(resource_type)

show_price = show_best_price(variable_name, resource_type)
print(show_price)

ref_total_price = refining_calculator(show_price)
print()
print(f'Price for resources is {ref_total_price} silver')




