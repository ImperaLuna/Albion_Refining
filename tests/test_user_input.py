"""
Test suite for user_input module.

This test suite contains test cases for the functions in the user_input module.
"""
from user_input import (get_tier_input,
                        get_enchantment_input,
                        get_resource_input,
                        convert_user_input)

# Test Cases for get_tier_input
def test_get_tier_input(monkeypatch):
    """
    Test for the get_tier_input function with valid input.
    """
    # Test valid input
    monkeypatch.setattr('builtins.input', lambda x: "5")
    assert get_tier_input() == "5"

# Test Cases for get_enchantment_input
def test_get_enchantment_input(monkeypatch):
    """
    Test for the get_enchantment_input function with valid input.
    """
    # Test valid input
    monkeypatch.setattr('builtins.input', lambda x: "3")
    assert get_enchantment_input() == "3"

# Test Cases for get_resource_input
def test_get_resource_input(monkeypatch):
    """
    Test for the get_resource_input function with valid input.
    """
    # Test valid input
    monkeypatch.setattr('builtins.input', lambda x: "2")
    assert get_resource_input() == "ore"

# Test Cases for convert_user_input
def test_convert_user_input():
    """
    Test for the convert_user_input function with different inputs.
    """
    assert convert_user_input("6", "2", "cloth") == ["t6.2", "cloth"]
    assert convert_user_input("5", "0", "wood") == ["t5.0", "wood"]
    assert convert_user_input("4", "4", "hide") == ["t4.4", "hide"]
