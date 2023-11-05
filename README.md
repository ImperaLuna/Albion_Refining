# Albion Automated Resource Price Comparison Tool

For those who may be unfamiliar, Albion Online is an online sandbox MMORPG with a dynamic player-driven economy. This project serves as a valuable tool for players, allowing them to efficiently locate the best prices for various in-game items, eliminating the need for manual price checks.

This project harnesses the capabilities of the Albiondata-Client API (https://github.com/ao-data/albiondata-client) to streamline this process. To utilize the tool effectively, follow these steps:

1. Begin by running the following command to fetch and store the necessary data locally in a CSV file:

```bash
python project.py --update
```

This command establishes a connection with the API and uses Beautiful Soup to gather the essential data.

2. Once the CSV file is created, execute the program with the following command:

```bash
python project.py
```

The program will provide a user-friendly terminal menu, prompting you to enter the following information:

- Resource tier
- Enchantment level for the selected tier
- Type of resources or items you wish to compare

Upon providing these details, the program will perform the necessary calculations, leveraging the data obtained from the API. It will then present a list of resource prices or item prices, ordered by the most cost-effective options. This automation eliminates the need for players to manually check prices in the game.
