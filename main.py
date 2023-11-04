'''Main module used to run the albion refining project'''

import argparse
from typing import Dict
import multi_modules_functions as fc
from refining_calculator import calculate__materials_price
import user_input as uin
import csv_generation


def main() -> None:
    '''Main Function'''
    parser = argparse.ArgumentParser(description="Update CSV data")
    parser.add_argument("--update", action="store_true", help="Update CSV data")

    args = parser.parse_args()

    if args.update:
        update_csv()
    else:
        variables = calculate_and_store_variables()
        print_variables(variables)


def calculate_and_store_variables() -> Dict:
    """
    Calculate and store various variables related to refining items.

    Returns:
        - Dict: A dictionary containing the calculated variables.
    """
    variable_name = user_input()

    strip_var_name = fc.strip_variable_name(variable_name)
    resource_type = fc.generate_resource_csv_filename(strip_var_name)

    show_price_df = fc.show_buy_price_df(variable_name, resource_type)

    refining_materials_price = int(calculate__materials_price(variable_name, show_price_df))

    daily_crafts = int(fc.calculate_daily_crafts(variable_name))

    total_price_bought_mats = int(refining_materials_price * daily_crafts)

    show_sell_price_df = fc.show_sell_price_df(variable_name, resource_type)

    refined_resource_cost = int(fc.find_maximum_sell_price(show_sell_price_df) * 0.935)

    returned_resources = int(fc.calculate_returned_resources_value(
                                daily_crafts, refined_resource_cost))


    max_crafted_resources = int(refined_resource_cost * daily_crafts)

    total_daily_profit = int(returned_resources + max_crafted_resources)
    total_daily_profit -= total_price_bought_mats

    expected_profit_per_month = 30 * total_daily_profit

    return {
        "variable_name": variable_name,
        "strip_var_name": strip_var_name,
        "resource_type": resource_type,
        "show_price_df": show_price_df,
        "refining_materials_price": refining_materials_price,
        "daily_crafts": daily_crafts,
        "total_price_bought_mats": total_price_bought_mats,
        "show_sell_price_df": show_sell_price_df,
        "refined_resource_cost": refined_resource_cost,
        "returned_resources": returned_resources,
        "max_crafted_resources": max_crafted_resources,
        "total_daily_profit": total_daily_profit,
        "expected_profit_per_month": expected_profit_per_month,
    }

def print_variables(variables: Dict) -> None:
    """
    Print the calculated variables to the console.

    Args:
        - variables |Dict| -- A dictionary containing the calculated variables.

    """
    print()
    print(f'The list generated for your items is: {variables["variable_name"]}')
    print()
    print(variables["show_price_df"])
    print()
    print(f'Total price for 1 craft: {format(variables["refining_materials_price"], ",")}')
    print(f'Daily number of crafts is: {variables["daily_crafts"]}')
    print('Total amount that needs to be invested into resources is:'
                                     f'{format(variables["total_price_bought_mats"], ",")}')
    print()
    print(variables["show_sell_price_df"])
    print()
    print(f'Refined resource cost: {format(variables["refined_resource_cost"], ",")}')
    print(f'Value of returned resources is: {format(variables["returned_resources"], ",")}')
    print(f'Max value of crafted resources is: {format(variables["max_crafted_resources"], ",")}')
    print(f'Total daily profit is: {format(variables["total_daily_profit"], ",")}')
    print(f'Expected profit per month is: {format(variables["expected_profit_per_month"], ",")}')
    print()

def update_csv() -> None:
    """
    Update CSV data.
    """
    csv_generation.main()

def user_input() -> str:
    """
    Get user input for refining item details.

    Returns:
        - variable_name |str| -- The generated variable name for the refining item.
    """
    user_input_tier = uin.get_tier_input()
    user_input_enchantment = uin.get_enchantment_input()
    user_input_resource_type = uin.get_resource_input()

    uin_tier_enchantment, uin_resource_type = uin.convert_user_input(
                                            user_input_tier,
                                            user_input_enchantment,
                                            user_input_resource_type)

    variable_name = fc.generate_variable_name(uin_tier_enchantment, uin_resource_type)
    return variable_name

if __name__ == "__main__":
    main()
