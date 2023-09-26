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

print(refining_mats_variables('WOOD','PLANKS'))
