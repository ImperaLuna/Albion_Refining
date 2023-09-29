'''Refining calculator run module'''

from multi_modules_functions import generate_variable_name
from multi_modules_functions import strip_variable_name
from multi_modules_functions import create_csv_filename
from multi_modules_functions import show_best_price
from multi_modules_functions import price_calculator

# create a variable name to generate the mats price
variable_name = generate_variable_name('t4.4', 'hide')
print(variable_name)

# strip variable in order to find right csv_file
strip_var_name = strip_variable_name(variable_name)
resource_type = create_csv_filename(strip_var_name)

# print data_frame for mats
show_price_df = show_best_price(variable_name, resource_type)
print(show_price_df)

#print total cost for mats used in refining process
mats_price = price_calculator(variable_name, show_price_df)
print(mats_price)
