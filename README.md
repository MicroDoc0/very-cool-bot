# Very Cool Bot (Rewritten)

Very cool bot REWRITTEN is a Discord bot written in Python using both the hikari and Lightbulb libraries. It provides various functionalities for server moderation and entertainment.
### have fun!

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
- **Open Discord's development portal**
### Press "Create a new application"
![[press]](images/ss1.PNG)
### Choose your app name and agree to the guidelines
![[press]](images/ss2.PNG)
### Press the "Bot" tab
![[press]](images/ss3.PNG)
### Click on "reset token"
![[press]](images/ss4.PNG)
![[press]](images/ss5.PNG)
### Modify the code to incllude the correct values. 
### (config.py)
![[press]](images/ss6.PNG)
### (bot.py)
![[press]](images/ss7.PNG)
### Modify tags.txt if neccesary.

### Next Step: Coding
1. **Install Dependencies:** Make sure you have Python and the required libraries (`hikari`, `lightbulb`, and any others) installed. You can use `pip install` for this.
2. **Configuration:** Replace the placeholder values in the code for `mod_id`, `hmod_id`, `admin_id`, `BOT_TOKEN`, and potentially file paths if needed.
### ^^ if you somehow forgot to do it before.
3. **Run the Bot:** Execute the script using `python bot.py`.

## Additional Notes:

- This is a basic example showcasing some functionalities. You can extend it further by adding new commands and features.
- The code includes comments for better readability.

**Feel free to customize and improve the bot according to your needs!**
