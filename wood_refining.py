'''Wood Refining module - To be updated'''

table_base_url = "https://west.albion-online-data.com/api/v2/stats/view/"
wood_items = []
plank_items = ['T3_PLANKS']
locations = "Martlock,Fort%20Sterling,Thetford,Lymhurst,Bridgewatch"

tier = ('T4', 'T5', 'T6', 'T7', 'T8')
enchantment = (0, 1, 2, 3, 4)

for t in tier:
    base_wood_added = False  # Flag to track if base wood item has been added for the tier
    base_plank_added = False
    for e in enchantment:
        if not base_wood_added:
            wood_items.append(f'{t}_WOOD')
            plank_items.append(f'{t}_PLANKS')
            base_wood_added = True  # Set the flag to True after adding the base item
            base_plank_added = True
        if e > 0:
            wood_items.append(f'{t}_WOOD_LEVEL{e}@{e}')
            plank_items.append(f'{t}_PLANKS_LEVEL{e}@{e}')

# Combine wood_items and plank_items into a single list
all_items = wood_items + plank_items

# Create a URL using join method
url = f"{table_base_url}{','.join(all_items)}?locations={locations}"

print("Combined URL:")
print(url)
