'''Store functions used in multiple modules'''

from typing import List
import pandas as pd


def show_buy_price_df(item_ids: List[str], csv_filename: str) -> pd.DataFrame:
    '''
    Reads a CSV file, selects specific columns, and returns a DataFrame 
    grouped by 'item_id' and sorted by 'sell_price_max' in ascending order within each group.

    Args:
        - item_ids |list of strings| -- Item IDs for filtering data from generate_variable_name()
        - csv_filename |str| -- File created using fct create_csv_file()

    Returns:
        - buy_materials_df |DataFrame| -- Grouped and ascended by 'item_id' and 'sell_price_max'
    '''

    columns_to_select = ['item_id', 'city', 'sell_price_max', 'sell_price_max_date']

    data = pd.read_csv(csv_filename)
    data['sell_price_max'] = data['sell_price_max'].astype(float)
    filtered_data = data[data['item_id'].isin(item_ids)]

    # Group by 'item_id' and sort within each group
    buy_materials_df = (
        filtered_data[columns_to_select].groupby('item_id', as_index=True)
        .apply(lambda x: x.sort_values(by='sell_price_max', ascending=True))
    )

    return buy_materials_df

def show_sell_price_df(item_ids: List[str], csv_filename: str) -> pd.DataFrame:
    '''
    Extract the item_id and edit it to matchT for final refining process product.

    Reads a CSV file, selects specific columns, and returns a DataFrame, 
    sorted by 'sell_price_max' in descending.

    Args:
        - item_ids |list of strings|| -- List's [1] holds ID from generate_variable_name()
        - csv_filename |str| -- File created using fct create_csv_file()

    Returns:
        sell_refined_resource_df |DataFrame| -- Descended 'sell_price_max
    '''

    required_item_id = item_ids[1]
    next_tier = f"{required_item_id[0]}{int(required_item_id[1]) + 1}{required_item_id[2:]}"

    selected_columns = ['item_id', 'city', 'sell_price_max', 'sell_price_max_date']

    data_frame = pd.read_csv(csv_filename)
    data_frame['sell_price_max'] = data_frame['sell_price_max'].astype(float)

    filtered_data_frame = data_frame[data_frame['item_id'] == next_tier]

    sell_refined_resource_df = (
        filtered_data_frame[selected_columns]
        .sort_values(by='sell_price_max', ascending=False)
    )

    return sell_refined_resource_df


def generate_variable_name(tier: str, raw_resource: str) -> List[str]:
    '''
    Generates variable names based on the input tier and raw resource.

    Args:
        - tier |str|: A string representing the item's tier (e.g., 't4.0', 'T5.2').
        - raw_resource |str|: A string representing the raw resource (e.g., 'ore', 'fiber', 'hide').

    Returns:
        - variable_name |list or None|: A list with variable name(s) if input is invalid.

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
            elif ench in ['1' , '2' , '3', '4']:
                variable_name = [f'{tier_str_parts[0].upper()}_{raw_resource}_LEVEL{ench}@{ench}',
                                 f'T3_{resource_type.get(raw_resource, "")}']
            else:
                variable_name = None  # Invalid enchantment level
        else:
            if ench == '0':
                variable_name = [
                    f'{tier_str_parts[0].upper()}_{raw_resource}',
                    f'T{int(tier_str_parts[0][1]) - 1}'
                    f'_{resource_type.get(raw_resource, "")}'
                ]
            elif ench in ['1' , '2' , '3', '4']:
                variable_name = [
                    f'{tier_str_parts[0].upper()}_{raw_resource}_LEVEL{ench}@{ench}',
                    f'T{int(tier_str_parts[0][1]) - 1}'
                    f'_{resource_type.get(raw_resource, "")}_LEVEL{ench}@{ench}'
                ]
            else:
                variable_name = None  # Invalid enchantment level

        return variable_name


def strip_variable_name(variable_names: List[str]) -> List[str]:
    '''
    Extracts and formats the resource types from a list of variable names.
    Used in generate_resource_csv_filename()

    Args:
        - variable_names |List[str]| -- A list of variable names from generate_variable_name().

    Returns:
        - stripped_type |List[str]| -- contains 1 resource type ('wood', 'ore', 'cloth', 'hide').
    '''
    stripped_type = []

    for name in variable_names:
        # Remove any extra characters and split by underscores
        parts = name.strip().split('_')

        if len(parts) >= 2:
            # Get the resource type and convert to lowercase
            resource_type = parts[1].lower()

            # Check if it's a valid resource type
            if resource_type in ('wood', 'ore', 'cloth', 'hide'):
                stripped_type.append(resource_type)

    return stripped_type


def generate_resource_csv_filename(stripped_type: List[str]) -> str:
    '''
    Generate CSV filename based on resource names.

    Args:
        - stripped_type |List[str]| -- contains 1 resource type ('wood', 'ore', 'cloth', 'hide')

    Returns:
        - filename |str|: Formatted CSV filename, e.g., 'wood_refining.csv'.
    '''
    if stripped_type:
        first_resource_name = stripped_type[0]

    filename = f'{first_resource_name}_refining.csv'
    return filename


def calculate_daily_crafts(variable_name: List[str]) -> int:
    '''
    Calculates and returns the number of daily crafts based on the item's tier and enchantment.

    Args:
        variable_name |List[str]| -- List generated by generate_variable_name() , item_id[0] req.

    Returns:
        - daily_crafts |int| -- The number of daily crafts for the specified tier.
    '''
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


def find_maximum_sell_price(data_frame: pd.DataFrame) -> int:
    '''
    Finds and returns the maximum sell price from a DataFrame.

    Args:
        - data_frame |pd.DataFrame| -- The item data DataFrame from show_sell_price_df(

    Returns:
        - max_sell_price |int| -- The maximum sell price of the final product.
    '''
    unique_item_id = data_frame["item_id"].unique()

    item_id = data_frame[data_frame['item_id'] == unique_item_id[0]]
    max_sell_price = int(item_id['sell_price_max'].max())

    return max_sell_price



def calculate_returned_resources_value(daily_crafts: int, resource_value: float) -> float:
    '''
    Calculates and returns the value of resources returned from daily crafts.

    Args:
        - daily_crafts |int| -- The number of daily crafts from calculate_daily_crafts()
        - resource_value |float| -- The value of each resource from find_maximum_sell_price()

    Returns:
        - value_returned_resources |float| -- The value of resources returned.
    '''
    # Updated logic
    value_returned_resources = daily_crafts * resource_value * 0.539
    return value_returned_resources
