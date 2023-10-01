'''
Albion Online Refining Cost Calculation Module for WOOD, ORE, FIBER, HIDE

This module provides functions for calculating the refining cost of resources in Albion Online.
It provides functions for refining costs at T4, T5, T6, T7, and T8 tiers.

Each function takes a DataFrame containing resource data with 'item_id' and 'sell_price_max'
columns as input and returns the total refining cost based on the specified formula.
'''

from typing import List
import pandas as pd

def calculate_t4_refining_materials_price(data_frame: pd.DataFrame) -> int:
    '''
    Calculates the formula 2 * T4_raw_resource + T3_refined_resource using a DataFrame.

    Args:
        - data_frame |DataFrame| -- DataFrame with 'item_id' and 'sell_price_max' columns.

    Returns:
        - total_cost |float| -- Result of the formula.
    '''
    unique_item_id = data_frame["item_id"].unique()

    t3_refined_resource_data = data_frame[data_frame['item_id'] == unique_item_id[0]]
    t4_raw_resource_data = data_frame[data_frame['item_id'] == unique_item_id[1]]

    min_t3_refined_resource = t3_refined_resource_data['sell_price_max'].min()
    min_t4_raw_resource = t4_raw_resource_data['sell_price_max'].min()

    t4_raw_resource_price = 2 * min_t4_raw_resource

    total_cost = int(t4_raw_resource_price + min_t3_refined_resource)

    return total_cost


def calculate_t5_refining_materials_price(data_frame: pd.DataFrame) -> int:
    '''
    Calculates the formula 3 * T5_raw_resource + T4_refined_resource using a DataFrame.

    Args:
        - data_frame (DataFrame): DataFrame with 'item_id' and 'sell_price_max' columns.

    Returns:
        - total_cost |float| -- Result of the formula.
    '''
    unique_item_id = data_frame["item_id"].unique()

    t4_refined_resource_data = data_frame[data_frame['item_id'] == unique_item_id[0]]
    t5_raw_resource_data = data_frame[data_frame['item_id'] == unique_item_id[1]]

    min_t4_refined_resource = t4_refined_resource_data['sell_price_max'].min()
    min_t5_raw_resource = t5_raw_resource_data['sell_price_max'].min()

    total_cost = int(3 * min_t5_raw_resource + min_t4_refined_resource)
    return total_cost


def calculate_t6_refining_materials_price(data_frame: pd.DataFrame) -> int:
    '''
    Calculates the formula 4 * T6_raw_resource + T5_refined_resource using a DataFrame.

    Args:
        - data_frame |DataFrame| -- DataFrame with 'item_id' and 'sell_price_max' columns.

    Returns:
        - total_cost |float| -- Result of the formula.
    '''
    unique_item_id = data_frame["item_id"].unique()

    t5_refined_resource_data = data_frame[data_frame['item_id'] == unique_item_id[0]]
    t6_raw_resource_data = data_frame[data_frame['item_id'] == unique_item_id[1]]

    min_t5_refined_resource = t5_refined_resource_data['sell_price_max'].min()
    min_t6_raw_resource = t6_raw_resource_data['sell_price_max'].min()

    total_cost = int(4 * min_t6_raw_resource + min_t5_refined_resource)
    return total_cost


def calculate_t7_refining_materials_price(data_frame: pd.DataFrame) -> int:
    '''
    Calculates the formula 5 * T7_raw_resource + T6_refined_resource using a DataFrame.

    Args:
        - data_frame |DataFrame| -- DataFrame with 'item_id' and 'sell_price_max' columns.

    Returns:
        - total_cost |float| -- Result of the formula.
    '''
    unique_item_id = data_frame["item_id"].unique()

    t6_refined_resource_data = data_frame[data_frame['item_id'] == unique_item_id[0]]
    t7_raw_resource_data = data_frame[data_frame['item_id'] == unique_item_id[1]]

    min_t6_refined_resource = t6_refined_resource_data['sell_price_max'].min()
    min_t7_raw_resource = t7_raw_resource_data['sell_price_max'].min()

    total_cost = int(5 * min_t7_raw_resource + min_t6_refined_resource)
    return total_cost


def calculate_t8_refining_materials_price(data_frame: pd.DataFrame) -> int:
    '''
    Calculates the formula 5 * T8_raw_resource + T7_refined_resource using a DataFrame.

    Args:
        - data_frame |DataFrame| -- DataFrame with 'item_id' and 'sell_price_max' columns.

    Returns:
        - total_cost |float| -- Result of the formula.
    '''

    unique_item_id = data_frame["item_id"].unique()

    t7_refined_resource_data = data_frame[data_frame['item_id'] == unique_item_id[0]]
    t8_raw_resource_data = data_frame[data_frame['item_id'] == unique_item_id[1]]

    min_t7_refined_resource = t7_refined_resource_data['sell_price_max'].min()
    min_t8_raw_resource = t8_raw_resource_data['sell_price_max'].min()

    total_cost = int(5 * min_t8_raw_resource + min_t7_refined_resource)
    return total_cost

def calculate__materials_price(variable_name: List[str], data_frame: pd.DataFrame) -> int:
    #todo : this variables most likely will change
    '''
    Calculates the refining materials price based on the provided variables and data frame.

    Args:
        - variable_name |List[str]| -- List of strings generated by generate_variable_name.
        - data_frame |pd.DataFrame| -- DataFrame generated by show_best_price.

    Returns:
        - materials_price |int| -- The calculated refining materials price.
    '''

    extract_tier = variable_name[0].split('_')
    tier = extract_tier[0]

    if tier == 'T4':
        materials_price = calculate_t4_refining_materials_price(data_frame)
    elif tier == 'T5':
        materials_price = calculate_t5_refining_materials_price(data_frame)
    elif tier == 'T6':
        materials_price = calculate_t6_refining_materials_price(data_frame)
    elif tier == 'T7':
        materials_price = calculate_t7_refining_materials_price(data_frame)
    elif tier == 'T8':
        materials_price = calculate_t8_refining_materials_price(data_frame)
    return materials_price
