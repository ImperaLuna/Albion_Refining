'''Store functions used in multiple modules'''
import pandas as pd
import refining_calculator as rc

#! ====================================== Building CSV files ======================================


#! ====================================== Building CSV files ======================================

def show_best_price(item_ids, csv_filename):
    '''
    Reads a CSV file, selects specific columns, and returns a DataFrame 
    grouped by 'item_id' and sorted by 'sell_price_max' in ascending order within each group.

    Args:
        item_ids |list| -- List of item IDs to filter the data.

        csv_filename |str| -- File created using fct save_data_to_csv()

    Returns:
        result_data_frame |DataFrame| -- Grouped and ascended by 'item_id' and 'sell_price_max
    '''

    selected_columns = ['item_id', 'city', 'sell_price_max', 'sell_price_max_date']

    data_frame = pd.read_csv(csv_filename)
    data_frame['sell_price_max'] = data_frame['sell_price_max'].astype(float)
    filtered_data_frame = data_frame[data_frame['item_id'].isin(item_ids)]

    # Group by 'item_id' and sort within each group
    result_data_frame = (filtered_data_frame[selected_columns]
                         .groupby('item_id', as_index=True)
                         .apply(lambda x: x.sort_values(by='sell_price_max', ascending=True)))

    return result_data_frame



def generate_variable_name(tier, raw_resource):
    '''
    Generates variable names based on the input tier and raw resource.

    Args:
        tier |str|: A string representing the item's tier (e.g., 'T4', 'T5').
        raw_resource |str|: A string representing the raw resource (e.g., 'ore', 'fiber', 'hide').

    Returns:
        variable_name |list or None|: A list with variable name(s) if input is invalid.

    Constructs variable based on tier, raw resource, refined resource and enchantment level:
    - For 'T4', appends '_{raw_resource}' or '_{raw_resource}_LEVEL{enchantment}@{enchantment}'.
    - For 'T5' to 'T8', includes '_{raw_resource}' and possibly '_{raw_resource}_LEVEL{e}@{e}'.

    Example:
    >>> generate_variable_name('T4.0', 'ore')
    ['T4_ORE', 'T3_METALBAR']
    '''

    # Dictionary mapping raw resources to refined resources
    resource_type = {
        'WOOD': 'PLANKS',
        'ORE': 'METALBAR',
        'FIBER': 'CLOTH',
        'HIDE': 'LEATHER'
    }

    tiers = ('T4', 'T5', 'T6', 'T7', 'T8')
    tier_str_parts = tier.split('.')

    # Convert the input raw_resource to uppercase
    raw_resource = raw_resource.upper()

    if len(tier_str_parts) == 2 and tier_str_parts[0].upper() in tiers:
        ench = tier_str_parts[1]  # variable to define enchantment levels

        if tier_str_parts[0].upper() == 'T4':
            if ench == '0':
                variable_name = [f'{tier_str_parts[0].upper()}_{raw_resource}',
                                f'T3_{resource_type.get(raw_resource, "")}']
            elif ench in ('1', '2', '3', '4'):
                variable_name = [f'{tier_str_parts[0].upper()}_{raw_resource}_LEVEL{ench}@{ench}',
                                 f'T3_{resource_type.get(raw_resource, "")}']
            else:
                variable_name = None  # Invalid enchantment level
        else:
            if ench == '0':
                variable_name = [
                    f'{tier_str_parts[0].upper()}_{raw_resource}',
                    f'T{int(tier_str_parts[0][1])-1}_{resource_type.get(raw_resource, "")}'
                ]
            elif ench in ('1', '2', '3', '4'):
                variable_name = [
                    f'{tier_str_parts[0].upper()}_{raw_resource}_LEVEL{ench}@{ench}',
                    f'T{int(tier_str_parts[0][1])-1}_{resource_type.get(raw_resource, "")}_LEVEL{ench}@{ench}'
                ]
            else:
                variable_name = None  # Invalid enchantment level

        return variable_name


######

def strip_variable_name(variable_names):
    '''
    Extracts and formats the resource types from a list of variable names.

    Args:
        variable_names |list of str|: A list of variable names ex:['T4_WOOD', 'T5_ORE_']).

    Returns:
        resource_types |list of str|: A list resource types ('wood', 'ore', 'cloth', 'hide').
    '''
    resource_types = []

    for variable_name in variable_names:
        # Remove any extra characters and split by underscores
        parts = variable_name.strip().split('_')

        if len(parts) >= 2:
            # Get the resource type and convert to lowercase
            resource_type = parts[1].lower()

            # Check if it's a valid resource type
            if resource_type in ('wood', 'ore', 'cloth', 'hide'):
                resource_types.append(resource_type)

    return resource_types

def create_csv_filename(resource_names):
    '''
    Create a CSV filename based on resource name(s).

    Args:
        resource_names |list of str|: (e.g., ['wood'], ['ore'], ['cloth', 'hide']).

    Returns:
        csv_filename |str|: The formatted CSV filename ('{}_refining.csv').
    '''
    # Get the first element of the list (assuming it contains only one element)
    resource_name = resource_names[0] if resource_names else 'unknown'

    return f'{resource_name}_refining.csv'

#####

def price_calculator(variable_name,data_frame):
    '''
    Args:
        - variable_name |list of strings| - generated by generate_variable_name
        - data_frame |data_frame| - generated by show_best_price
    '''

    extract_tier = variable_name[0].split('_')
    tier = extract_tier[0]

    if tier == 'T4':
        mats_price = rc.refining_calculator_t4(data_frame)
    elif tier == 'T5':
        mats_price = rc.refining_calculator_t5(data_frame)
    elif tier == 'T6':
        mats_price = rc.refining_calculator_t6(data_frame)
    elif tier == 'T7':
        mats_price = rc.refining_calculator_t7(data_frame)
    elif tier == 'T8':
        mats_price = rc.refining_calculator_t8(data_frame)
    return mats_price

def nr_of_daily_crafts(variable_name):

    if variable_name[0][-1] not in ['1', '2', '3', '4']:
        tier = f'{variable_name[0][1]}.0'
    else:
        tier = f'{variable_name[0][1]}.{variable_name[0][-1]}'
        
    focus_cost_max_spec = {
        '4.0': 3, '4.1': 6, '4.2': 10, '4.3': 18, '4.4': 503,
        '5.0': 6, '5.1': 10, '5.2': 18, '5.3': 31, '5.4': 880,
        '6.0': 10, '6.1': 18, '6.2': 31, '6.3': 55, '6.4': 1539,
        '7.0': 18, '7.1': 31, '7.2': 53, '7.3': 96, '7.4': 2694,
        '8.0': 31, '8.1': 55, '8.2': 96, '8.3': 168, '8.4': 4714
    }

    daily_focus = 10000

    focus_per_craft = focus_cost_max_spec.get(tier)
    daily_crafts = daily_focus / focus_per_craft

    return daily_crafts

def show_max_price(item_ids, csv_filename):

    #TODO: clean this shit up

    refined_item_id = item_ids[1]
    tier_refined_item = int(refined_item_id[1])
    tier_refined_item += 1
    updated_tier_number = str(tier_refined_item)
    updated_tier = refined_item_id[0] + updated_tier_number + refined_item_id[2:]

    selected_columns = ['item_id', 'city', 'sell_price_max', 'sell_price_max_date']

    data_frame = pd.read_csv(csv_filename)
    data_frame['sell_price_max'] = data_frame['sell_price_max'].astype(float)
    filtered_data_frame = data_frame[data_frame['item_id'] == updated_tier]

    # Group by 'item_id' and sort within each group
    result_data_frame = (filtered_data_frame[selected_columns]
                         .groupby('item_id', as_index=True)
                         .apply(lambda x: x.sort_values(by='sell_price_max', ascending=False)))

    return result_data_frame

def max_price_refined(data_frame):
    #todo clean this shit
    unique_item_id = data_frame["item_id"].unique()

    item_id = data_frame[data_frame['item_id'] == unique_item_id[0]]
    item_id_price = item_id['sell_price_max'].min()

    return item_id_price

def calculate_daily_profit(daily_crafts, resource_value):
    #todo this logic is shit
    resource_returned = daily_crafts * resource_value * 0.539
    return resource_returned