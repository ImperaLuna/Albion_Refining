'''Store functions used in multiple modules'''

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

def api_url_csv(refining_items_required):
    '''
    Create the api url based on function refining_mats_variables() return
    ARGS:
        refining_items_required |STR| -- variable for the url        
    Return:
        url |STR| -- final url
    '''

    table_base_url = 'https://west.albion-online-data.com/api/v2/stats/view/'
    locations = 'Martlock,Fort%20Sterling,Thetford,Lymhurst,Bridgewatch'

    url = f'{table_base_url}{",".join(refining_items_required)}?locations={locations}'

    return url
