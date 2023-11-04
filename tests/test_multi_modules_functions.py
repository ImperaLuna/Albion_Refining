"""
Test suite for multi_modules_functions module.

This test suite contains test cases for the functions in the user_input module.
"""
import pytest
from multi_modules_functions import (generate_variable_name,
                                     strip_variable_name,
                                     calculate_daily_crafts, 
                                     calculate_returned_resources_value)

# Test Cases for generate_variable_name

def test_generate_variable_name_t4_0():
    """
    Test for generating variable names for Tier 4.0 with ore.
    """
    result = generate_variable_name('T4.0', 'ore')
    assert result == ['T4_ORE', 'T3_METALBAR']

def test_generate_variable_name_t4_4():
    """
    Test for generating variable names for Tier 4.4 with fiber.
    """
    result = generate_variable_name('T4.4', 'fiber')
    assert result == ['T4_FIBER_LEVEL4@4', 'T3_CLOTH']

def test_generate_variable_name_t5_0():
    """
    Test for generating variable names for Tier 5.0 with wood.
    """
    result = generate_variable_name('T5.0', 'wood')
    assert result == ['T5_WOOD', 'T4_PLANKS']

def test_generate_variable_name_t5_3():
    """
    Test for generating variable names for Tier 5.3 with hide.
    """
    result = generate_variable_name('T5.3', 'hide')
    assert result == ['T5_HIDE_LEVEL3@3', 'T4_LEATHER_LEVEL3@3']

# Test Case for strip_variable_name

def test_strip_variable_name_valid_names():
    """
    Test for stripping variable names to obtain resource types.
    """
    variable_names = ['T4_WOOD', 'T4_ORE_LEVEL3@3', 'T5_CLOTH', 'T8_HIDE_LEVEL2@2']
    result = strip_variable_name(variable_names)
    assert result == ['wood', 'ore', 'cloth', 'hide']

# Test Cases for calculate_daily_crafts

def test_calculate_daily_crafts_tier_5_0():
    """
    Test for calculating daily crafts for Tier 5.0 Fiber.
    """
    variable_name = ['T5_FIBER']
    result = calculate_daily_crafts(variable_name)
    assert result == pytest.approx(1666.66, abs=0.01)

def test_calculate_daily_crafts_tier_4_0_cloth():
    """
    Test for calculating daily crafts for Tier 4.0 Cloth.
    """
    variable_name = ['T4_CLOTH']
    result = calculate_daily_crafts(variable_name)
    assert result == pytest.approx(3333.33, abs=0.01)  

def test_calculate_daily_crafts_tier_8_4_wood():
    """
    Test for calculating daily crafts for Tier 8.4 Wood with high enchantment.
    """
    variable_name = ['T8_WOOD_LEVEL4@4']
    result = calculate_daily_crafts(variable_name)
    assert result == pytest.approx(2.12, abs=0.01)

# Test Case for calculate_returned_resources_value

def test_calculate_returned_resources_value_positive_values():
    """
    Test for calculating the value of returned resources with positive values.
    """
    daily_crafts = 100
    resource_value = 1.5
    result = calculate_returned_resources_value(daily_crafts, resource_value)
    assert result == pytest.approx(80.85, abs=0.1)
