# Very Cool Bot

Very cool bot is a Discord bot written in Python using the Lightbulb library. It provides various functionalities for server moderation and entertainment.
*it is an open source version of *

## Features:

- **Ping Command:** Responds with "Pong!" to check bot latency.
- **Echo Command:** Repeats the provided text.
- **Help Command:** Shows a list of all available commands.
- **Clear Command:** Clears a specified number of messages in the current channel (requires Manage Messages permission).
- **Rank Command:** Assigns a staff role (mod, head mod, or admin) to a member (requires appropriate permissions).
- **Unrank Command:** Removes a staff role from a member (requires appropriate permissions).
- **Slowmode Command:** Sets slowmode for a channel (requires Manage Channel permission).
- **Tags Command:** Displays a list of tags and their descriptions from a text file.
- **Tag Command:** Shows the description of a specific tag from the text file. (Command options update automatically)

## Getting Started:
0. **Open Discord's development portal**
### Press "Create a new application"
![[press]](images/ss1.png)
1. **Install Dependencies:** Make sure you have Python and the required libraries (`hikari`, `lightbulb`, and any others) installed. You can use `pip install` for this.
2. **Configuration:** Replace the placeholder values in the code for `mod_id`, `hmod_id`, `admin_id`, `BOT_TOKEN`, and potentially file paths if needed.
3. **Run the Bot:** Execute the script using `python bot.py`.

## Additional Notes:

- This is a basic example showcasing some functionalities. You can extend it further by adding new commands and features.
- The code includes comments for better readability.

**Feel free to customize and improve the bot according to your needs!**
