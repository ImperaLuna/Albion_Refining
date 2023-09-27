'''Store functions used in multiple modules'''
import pandas as pd
import requests
from bs4 import BeautifulSoup


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
