# Albion Automated Refining Profit Calculator


For those unaware, Albion is an online sandbox MMORPG with a player-driven economy. To fully understand the scope of this project, let's begin with some background about the game. Albion features multiple cities, each with its own isolated marketplace, making refining and crafting central to its economy.

This project utilizes an API provided by Albiondata-Client (https://github.com/ao-data/albiondata-client). In order to run the program, the following steps are required:

Run the following command to fetch and save the necessary data locally in a CSV file:

```bash
python project.py --update
```
This command connects to the API and utilizes Beautiful Soup to gather the required data.

Once the CSV file is created, you can run the program with the following command:

```bash
python project.py
```

The program will prompt you to provide the following information via the terminal menu:
- Resource tier
- Enchantment level for the selected tier
- Type of resources

After inputting these details, the program will execute the necessary calculations and utilize Pandas to display a list of resource prices required for the refining process, ordered by the cheapest option.

With this Albion Automated Refining Profit Calculator, you can efficiently make informed decisions when it comes to resource refining in the game.



