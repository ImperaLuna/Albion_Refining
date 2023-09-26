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

    for t in tier:
        # Flag to track if unenchated raw resource has been added for the tier
        UNENCHANTED_RAW_ADDED = False
        UNENCHANTED_PLANK_ADDED = False
        for e in enchantment:
            if not UNENCHANTED_RAW_ADDED:
                raw_resource_items.append(f'{t}_{raw_resource_type}')
                # Set the constant to True after adding the unenchated tier resource
                UNENCHANTED_RAW_ADDED = True
                if not UNENCHANTED_PLANK_ADDED:
                    refined_resource_items.append(f'{t}_{refined_resource_type}')
                UNENCHANTED_PLANK_ADDED = True
            if e > 0:
                raw_resource_items.append(f'{t}_{raw_resource_type}_LEVEL{e}@{e}')
                refined_resource_items.append(f'{t}_{refined_resource_type}_LEVEL{e}@{e}')

    refining_items_required = raw_resource_items + refined_resource_items
    return refining_items_required

