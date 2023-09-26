'''Wood Refining module - To be updated'''

TABLE_BASE_URL = 'https://west.albion-online-data.com/api/v2/stats/view/'
LOCATIONS = 'Martlock,Fort%20Sterling,Thetford,Lymhurst,Bridgewatch'
wood_items = []
plank_items = ['T3_PLANKS']

# Define the tiers and enchantments
tier = ('T4', 'T5', 'T6', 'T7', 'T8')
enchantment = (0, 1, 2, 3, 4)

for t in tier:
    BASE_WOOD_ADDED = False # Flag to track if base wood item has been added for the tier
    BASE_PLANK_ADDED = False
    for e in enchantment:
        if not BASE_WOOD_ADDED:
            wood_items.append(f'{t}_WOOD')
            BASE_WOOD_ADDED = True # Set the constant to True after adding the base item
        if not BASE_PLANK_ADDED:
            plank_items.append(f'{t}_PLANKS')
            BASE_PLANK_ADDED = True
        if e > 0:
            wood_items.append(f'{t}_WOOD_LEVEL{e}@{e}')
            plank_items.append(f'{t}_PLANKS_LEVEL{e}@{e}')

# Combine wood_items and plank_items into a single list
wood_refining_items = wood_items + plank_items

# Create the URL and print it
url = f'{TABLE_BASE_URL}{",".join(wood_refining_items)}?locations={LOCATIONS}'

print('URL TableView Format):')
print(url)
