'''Module that store all the logic behind calculating profit and return'''


def refining_calculator_t4(data_frame):
    '''
    Calculates the formula 2 * T4_raw_resource + T3_refined_resource using a DataFrame.

    Args:
        data_frame |DataFrame| -- DataFrame with 'item_id' and 'sell_price_max' columns.

    Returns:
        final_result |float| -- Result of the formula.
    '''
    unique_item_id = data_frame["item_id"].unique()

    t3_refined_resource_data = data_frame[data_frame['item_id'] == unique_item_id[0]]
    t4_raw_resource_data = data_frame[data_frame['item_id'] == unique_item_id[1]]

    min_t3_refined_resource = t3_refined_resource_data['sell_price_max'].min()
    min_t4_raw_resource = t4_raw_resource_data['sell_price_max'].min()

    t4_raw_resource_price = 2 * min_t4_raw_resource

    t4_total_resource_price = t4_raw_resource_price + min_t3_refined_resource

    return t4_total_resource_price


def refining_calculator_t5(data_frame):
    '''
    Calculates the formula 2 * T5_raw_resource + T4_refined_resource using a DataFrame.

    Args:
        data_frame (DataFrame): DataFrame with 'item_id' and 'sell_price_max' columns.

    Returns:
        final_result (float): Result of the formula.
    '''
    unique_item_id = data_frame["item_id"].unique()

    t4_refined_resource_data = data_frame[data_frame['item_id'] == unique_item_id[0]]
    t5_raw_resource_data = data_frame[data_frame['item_id'] == unique_item_id[1]]

    min_t4_refined_resource = t4_refined_resource_data['sell_price_max'].min()
    min_t5_raw_resource = t5_raw_resource_data['sell_price_max'].min()

    t5_total_resource_price = 3 * min_t5_raw_resource + min_t4_refined_resource
    return t5_total_resource_price


def refining_calculator_t6(data_frame):
    '''
    Calculates the formula 2 * T6_raw_resource + T5_refined_resource using a DataFrame.

    Args:
        data_frame |DataFrame| -- DataFrame with 'item_id' and 'sell_price_max' columns.

    Returns:
        final_result |float| -- Result of the formula.
    '''
    unique_item_id = data_frame["item_id"].unique()

    t5_refined_resource_data = data_frame[data_frame['item_id'] == unique_item_id[0]]
    t6_raw_resource_data = data_frame[data_frame['item_id'] == unique_item_id[1]]

    min_t5_refined_resource = t5_refined_resource_data['sell_price_max'].min()
    min_t6_raw_resource = t6_raw_resource_data['sell_price_max'].min()

    t6_total_resource_price = 4 * min_t6_raw_resource + min_t5_refined_resource
    return t6_total_resource_price


def refining_calculator_t7(data_frame):
    '''
    Calculates the formula 2 * T7_raw_resource + T6_refined_resource using a DataFrame.

    Args:
        data_frame |DataFrame| -- DataFrame with 'item_id' and 'sell_price_max' columns.

    Returns:
        final_result |float| -- Result of the formula.
    '''
    unique_item_id = data_frame["item_id"].unique()

    t6_refined_resource_data = data_frame[data_frame['item_id'] == unique_item_id[0]]
    t7_raw_resource_data = data_frame[data_frame['item_id'] == unique_item_id[1]]

    min_t6_refined_resource = t6_refined_resource_data['sell_price_max'].min()
    min_t7_raw_resource = t7_raw_resource_data['sell_price_max'].min()

    t7_total_resource_price = 5 * min_t7_raw_resource + min_t6_refined_resource
    return t7_total_resource_price


def refining_calculator_t8(data_frame):
    '''
    Calculates the formula 2 * T8_raw_resource + T7_refined_resource using a DataFrame.

    Args:
        data_frame |DataFrame| -- DataFrame with 'item_id' and 'sell_price_max' columns.

    Returns:
        final_result |float| -- Result of the formula.
    '''

    unique_item_id = data_frame["item_id"].unique()

    t7_refined_resource_data = data_frame[data_frame['item_id'] == unique_item_id[0]]
    t8_raw_resource_data = data_frame[data_frame['item_id'] == unique_item_id[1]]

    min_t7_refined_resource = t7_refined_resource_data['sell_price_max'].min()
    min_t8_raw_resource = t8_raw_resource_data['sell_price_max'].min()

    t8_total_resource_price = 5 * min_t8_raw_resource + min_t7_refined_resource
    return t8_total_resource_price
