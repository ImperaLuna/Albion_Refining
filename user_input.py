'''
This module provides a simple command-line interface for collecting user inputs,
including tier selection, enchantment level, and resource type.
'''

from typing import List

def get_tier_input() -> str:
    """
    Prompt the user to enter a tier (4/5/6/7/8) and validate the input.
    
    Returns:
        - tier |str| -- The selected tier (4, 5, 6, 7, or 8).
    """
    while True:
        tier = input("Enter tier (4/5/6/7/8): ")
        if tier in ["4", "5", "6", "7", "8"]:
            return tier
        else:
            print("Invalid input. Please enter a valid tier.")


def get_enchantment_input() -> str:
    """
    Prompt the user to enter an enchantment level (0/1/2/3/4) and validate the input.
    
    Returns:
        - enchantment |str| -- The selected enchantment level (0, 1, 2, 3, or 4).
    """
    while True:
        enchantment = input("Enter enchantment (0/1/2/3/4): ")
        if enchantment in ["0", "1", "2", "3", "4"]:
            return enchantment
        else:
            print("Invalid input. Please enter a valid enchantment.")


def get_resource_input() -> str:
    """
    Display a menu for the user to select the type of resource (wood, ore, cloth, hide)
    using numbers (1-4) and validate the input.
    
    Returns:
        - resource_menu[choice] |str| -- The selected resource type (wood, ore, cloth, or hide).
    """
    resource_menu = {
        "1": "wood",
        "2": "ore",
        "3": "fiber",
        "4": "hide"
    }

    while True:
        print("Select the type of resource:")
        for key, value in resource_menu.items():
            print(f"{key}: {value}")

        choice = input("Enter the number for the resource (1-4): ")

        if choice in resource_menu:
            return resource_menu[choice]
        else:
            print("Invalid input. Please enter a valid number (1-4).")

def convert_user_input(tier: str, enchantment: str, resource_type: str) -> List[str]:
    """
    Converts user input into a list of strings.

    Args:
        - tier (str) -- The tier of the resource.
        - enchantment (str) -- The enchantment of the resource.
        - resource_type (str) -- The type of resource.

    Returns:
        - List[str]: A list containing two strings:
            - The resource tier and enchantment in the format 't{tier}.{enchantment}'.
            - The resource type.
    """
    resource_tier = f"t{tier}.{enchantment}"
    generate_variable_name_input = [resource_tier, resource_type]
    return generate_variable_name_input
