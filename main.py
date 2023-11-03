'''Refining calculator run module'''

import multi_modules_functions as fc
from refining_calculator import calculate__materials_price
import user_input as uin


def main():
      user_input_tier = uin.get_tier_input()
      user_input_enchantment = uin.get_enchantment_input()
      user_input_resource_type = uin.get_resource_input()

      uin_tier_enchantment, uin_resource_type = uin.convert_user_input(user_input_tier, user_input_enchantment, user_input_resource_type)

      variable_name = fc.generate_variable_name(uin_tier_enchantment, uin_resource_type)


      print()
      print(f'The list generated for your items is: {variable_name}')
      print()

      strip_var_name = fc.strip_variable_name(variable_name)
      resource_type = fc.generate_resource_csv_filename(strip_var_name)

      show_price_df = fc.show_buy_price_df(variable_name, resource_type)
      print(show_price_df)

      refining_materials_price = int(calculate__materials_price(variable_name, show_price_df))
      formatted_refining_materials_price = format(refining_materials_price, ',')
      print()
      print(f'Total price for 1 craft: {formatted_refining_materials_price}')

      daily_crafts = int(fc.calculate_daily_crafts(variable_name))
      print(f'Daily number of crafts is: {daily_crafts}')

      total_price_bought_mats = int(refining_materials_price * daily_crafts)
      formatted_total_price_bought_mats = format(total_price_bought_mats, ',')
      print(f'Total amount that needs to be invested into resources is:'
            f'{formatted_total_price_bought_mats}')
      print()

      show_sell_price_df = fc.show_sell_price_df(variable_name, resource_type)
      print(show_sell_price_df)
      print()

      refined_resource_cost = int(fc.find_maximum_sell_price(show_sell_price_df) * 0.935) #tax
      formatted_refined_resource_cost = format(refined_resource_cost, ',')
      print(f'Refined resource cost: {formatted_refined_resource_cost}')

      returned_resources = int(fc.calculate_returned_resources_value(daily_crafts, refined_resource_cost))
      formatted_returned_resources = format(returned_resources, ',')
      print(f'Value of returned resources is: {formatted_returned_resources}')

      formatted_max_crafted_resources = format(refined_resource_cost * daily_crafts, ',')
      print(f'Max value of crafted resources is: {formatted_max_crafted_resources}')

      total_daily_profit = int(returned_resources + (refined_resource_cost * daily_crafts))
      total_daily_profit -= total_price_bought_mats
      formatted_total_daily_profit = format(total_daily_profit, ',')
      print(f'Total daily profit is: {formatted_total_daily_profit}')

      formatted_expected_profit_per_month = format(30 * total_daily_profit, ',')
      print(f'Expected profit per month is: {formatted_expected_profit_per_month}')
      print()

if __name__ == "__main__":
      main()