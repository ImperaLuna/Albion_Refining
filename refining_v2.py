'''Refining calculator run module'''

from multi_modules_functions import generate_variable_name
from multi_modules_functions import strip_variable_name
from multi_modules_functions import create_csv_filename
from multi_modules_functions import show_best_price
from multi_modules_functions import price_calculator
from multi_modules_functions import nr_of_daily_crafts
from multi_modules_functions import show_max_price
from multi_modules_functions import max_price_refined
from multi_modules_functions import calculate_daily_profit

variable_name = generate_variable_name('t7.1', 'hide')

print()
print(f'The list generated for your items is: {variable_name}')
print()

strip_var_name = strip_variable_name(variable_name)
resource_type = create_csv_filename(strip_var_name)

show_price_df = show_best_price(variable_name, resource_type)
print(show_price_df)

mats_price = int(price_calculator(variable_name, show_price_df))
formatted_mats_price = format(mats_price, ',')
print()
print(f'Total price for 1 craft: {formatted_mats_price}')

daily_crafts = int(nr_of_daily_crafts(variable_name))
print(f'Daily number of crafts is: {daily_crafts}')

total_amount = int(mats_price * daily_crafts)
formatted_total_amount = format(total_amount, ',')
print(f'Total amount that needs to be invested into resources is: {formatted_total_amount}')
print()

show_max_price_df = show_max_price(variable_name, resource_type)
print(show_max_price_df)
print()

refined_resource_cost = int(max_price_refined(show_max_price_df) * 0.935) #tax
formatted_refined_resource_cost = format(refined_resource_cost, ',')
print(f'Refined resource cost: {formatted_refined_resource_cost}')

returned_resources = int(calculate_daily_profit(daily_crafts, mats_price))
formatted_returned_resources = format(returned_resources, ',')
print(f'Value of returned resources is: {formatted_returned_resources}')

formatted_max_crafted_resources = format(refined_resource_cost * daily_crafts, ',')
print(f'Max value of crafted resources is: {formatted_max_crafted_resources}')

total_daily_profit = int(returned_resources + (refined_resource_cost * daily_crafts))
total_daily_profit -= total_amount
formatted_total_daily_profit = format(total_daily_profit, ',')
print(f'Total daily profit is: {formatted_total_daily_profit}')

formatted_expected_profit_per_month = format(30 * total_daily_profit, ',')
print(f'Expected profit per month is: {formatted_expected_profit_per_month}')
print()