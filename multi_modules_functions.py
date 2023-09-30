'''Store functions used in multiple modules'''
import pandas as pd
import requests
from bs4 import BeautifulSoup
import refining_calculator as rc

#! ====================================== Building CSV files ======================================

def refining_mats_variables(raw_resource_type : str, refined_resource_type : str):
    '''
    Use args in order to generate the correct variables for the api

    ARGS:
        raw_resource |str| -- WOOD, ORE, FIBER, HIDE

        refined_resource |str| -- PLANKS, METALBAR, CLOTH, LEATHER
    Return:
        refining_mats_variables |str| -- Variables to generate url for api
    
    '''

    # Define the tiers and enchantments
    tier = ('T4', 'T5', 'T6', 'T7', 'T8')
    enchantment = (0, 1, 2, 3, 4)
    raw_resource_items = []
    refined_resource_items = []
    refined_resource_items.append(f'T3_{refined_resource_type}') # add T3 refined resource

    for t_level in tier:
        # Flag to track if unenchated raw resource has been added for the tier
        unenchanted_raw_added = False
        unenchanted_refined_added = False
        for e_level in enchantment:
            if not unenchanted_raw_added:
                raw_resource_items.append(f'{t_level}_{raw_resource_type}')
                # Set the constant to True after adding the unenchated tier resource
                unenchanted_raw_added = True
                if not unenchanted_refined_added:
                    refined_resource_items.append(f'{t_level}_{refined_resource_type}')
                unenchanted_refined_added = True
            if e_level > 0:
                raw_resource_items.append(
                    f'{t_level}_{raw_resource_type}_LEVEL{e_level}@{e_level}')
                refined_resource_items.append(
                    f'{t_level}_{refined_resource_type}_LEVEL{e_level}@{e_level}')

    refining_items_required = raw_resource_items + refined_resource_items
    return refining_items_required

def api_url_csv(refining_items_required: str):
    '''
    Create the api url based on function refining_mats_variables() return
    ARGS:
        refining_items_required |STR| -- variable for the url        
    Return:
        url |STR| -- final url
    '''

    table_base_url = 'https://west.albion-online-data.com/api/v2/stats/view/'
    locations = 'Martlock,Fort%20Sterling,Thetford,Lymhurst,Bridgewatch'

    api_url = f'{table_base_url}{",".join(refining_items_required)}?locations={locations}'

    return api_url

def save_data_to_csv(api_url: str, csv_filename: str, timeout: int = 10):
    '''
    Fetch data from an API and save it to a CSV file.

    Args:
        api_url |str| -- The URL of the API to fetch data from, obtained via api_url_csv fct

        csv_filename |str| -- Set the CSV file name (with .csv extension and path) for data storage.

        timeout |int, optional| -- Maximum response wait time in seconds (default: 10 seconds).

    Result:
        Creates a CSV file with the specified data.
    '''

    # Define the selected columns here
    selected_columns = ['item_id', 'city',
        'sell_price_min', 'sell_price_min_date',
        'sell_price_max', 'sell_price_max_date']

    try:
        response = requests.get(api_url, timeout=timeout)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table')

            if table:
                data_frame  = pd.read_html(str(table))[0]
                data_frame  = data_frame [selected_columns]
                data_frame .to_csv(csv_filename, index=False, encoding='utf-8')

                print(f'Data has been saved to {csv_filename}')
            else:
                print('No table is found in the API response')
        else:
            print(f'Failed to fetch data from the API. Status code: {response.status_code}')

    except requests.exceptions.Timeout:
        print('The request to the API timed out.')

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
        variable_name |list or None|: A list with variable name(s) or None if input is invalid.

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
