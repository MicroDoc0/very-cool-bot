# import stuff [NEEDED]

import hikari
import lightbulb
import logging
import random
from config import mod_id, hmod_id, admin_id, INTENTS, BOT_TOKEN
from lightbulb.ext import tasks
from lightbulb import OptionModifier

# ------/bot config\------

intents = INTENTS

bot = lightbulb.BotApp(
    token=BOT_TOKEN, intents=intents,
    default_enabled_guilds = GUILD_ID,
)

logging.basicConfig(level=logging.INFO)

@bot.listen(hikari.StartedEvent)
async def event_started(event):
    print("bot has started!")

# --- status
@bot.listen()
async def on_started(event: hikari.StartedEvent) -> None:
    await bot.update_presence(
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(name="status", type=hikari.ActivityType.PLAYING),
    )

# ------/ping------

@bot.command
@lightbulb.command("ping", "Says pong!")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("Pong!")

# ------/echo------

@bot.command
@lightbulb.option("text", "text to repeat", modifier=OptionModifier.CONSUME_REST)
@lightbulb.command(
    name="echo",  # Command name (required)
    description="Repeats the given text",  # Command description (optional)
)
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.options.text)

# ------/help------

@bot.command
@lightbulb.command("help", "Shows all commands")
@lightbulb.implements(lightbulb.SlashCommand)
async def help_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(
        title="Commands",
        description=(
            "/clear <amount> - Clear messages from a channel\n"
            "/help - Shows all commands\n"
            "/rank <member> <rank> - Rank a member\n"
            "/slowmode <time> - Sets slowmode for the channel\n"
            "/ping - Reply with pong\n"
            "/steal <image url> <emoji name> - Steal an emoji and add it on the server\n"
            "/unrank <member> - Unrank a staff member\n"
        ),
        color=hikari.Color.from_rgb(52, 152, 219),
    )

    await ctx.respond(embed=embed)

# ------/clear------

@bot.command
@lightbulb.option("amount", "Number of messages to clear", type=int, min_value=1, max_value=100, default=1)
@lightbulb.command(
    name="clear",
    description="Clears the specified number of messages in the current channel",
)
@lightbulb.implements(lightbulb.SlashCommand)
async def clear(ctx: lightbulb.Context) -> None:
    amount = ctx.options.amount
    channel = ctx.channel_id

    # Check if the user has the required permissions to manage messages
    if not ctx.member.permissions & hikari.Permissions.MANAGE_MESSAGES:
        await ctx.respond("You don't have the necessary permissions to clear messages.")
        return

    # Fetch the specified number of messages in the channel
    messages = await bot.rest.fetch_messages(channel).limit(amount)

    # Delete the fetched messages
    await bot.rest.delete_messages(channel, messages)

    # Send a confirmation message
    await ctx.respond(f"Cleared {len(messages)} message(s) in this channel.")

# ------/rank------

@bot.command
@lightbulb.option("member", "The member to rank", type=hikari.Member)
@lightbulb.option("rank", "The rank to assign (mod/admin)", type=str)
@lightbulb.command("rank", "Rank a member")
@lightbulb.implements(lightbulb.SlashCommand)
async def rank_command(ctx: lightbulb.SlashContext) -> None:
    member = ctx.options.member
    rank = ctx.options.rank.lower()

    if rank == "mod":
        role_id = mod_id
    elif rank == "head mod":
        role_id = hmod_id
    elif rank == "admin":
        role_id = admin_id
    else:
        await ctx.respond("Invalid rank. Please choose either 'mod', 'head mod', or 'admin'.")
        return

    role = ctx.get_guild().get_role(role_id)
    await member.add_role(role)
    await ctx.respond(f"{member.mention} has been ranked as {role.name}.")

# ------/unrank------

@bot.command
@lightbulb.option("member", "The member to unrank", type=hikari.Member)
@lightbulb.command("unrank", "Unrank a staff member")
@lightbulb.implements(lightbulb.SlashCommand)
async def unrank_command(ctx: lightbulb.SlashContext) -> None:
    member = ctx.options.member

    mod_role = ctx.get_guild().get_role(mod_id)
    admin_role = ctx.get_guild().get_role(admin_id)

    if mod_role in member.get_roles():
        await member.remove_role(mod_role)
    elif admin_role in member.get_roles():
        await member.remove_role(admin_role)
    else:
        await ctx.respond(f"{member.mention} does not have any staff roles.")
        return

    await ctx.respond(f"{member.mention} has been unranked.")

# ------/slowmode------

@bot.command
@lightbulb.option("time", "The slowmode duration in seconds", type=int)
@lightbulb.command("slowmode", "Sets slowmode for the channel")
@lightbulb.implements(lightbulb.SlashCommand)
async def slowmode_command(ctx: lightbulb.SlashContext) -> None:
    time = ctx.options.time

    await ctx.get_channel().edit(rate_limit_per_user=time)
    await ctx.respond(f"Slowmode has been set to {time} seconds.")

# ------/tag------

@bot.command
@lightbulb.option("tag", "Select a tag", type=str)
@lightbulb.command("tag", "Display a tag")
@lightbulb.implements(lightbulb.SlashCommand)
async def tag_command(ctx: lightbulb.SlashContext) -> None:
    tag_name = ctx.options.tag
    tag_info = get_tag_info(tag_name)
    
    if tag_info:
        name, desc = tag_info
        embed = hikari.Embed(title=f"{name.capitalize()} (#):", description=f"**{desc}**")
        await ctx.respond(embed=embed)
    else:
        await ctx.respond("Tag not found.")

def get_tag_info(tag_name):
    with open("C:/Users/Genius/Desktop/very cool bot/tags.txt", "r") as file:
        lines = file.readlines()
        
        for i in range(0, len(lines), 2):
            if lines[i].startswith(f'name="{tag_name}"'):
                name = lines[i].split('"')[1]
                desc = lines[i+1].split('"')[1]
                return name, desc
    
    return None

@tasks.task(s=60)  # Run every 60 seconds
async def update_tag_options():
    tag_options = []
    
    with open("C:/Users/Genius/Desktop/very cool bot/tags.txt", "r") as file:
        lines = file.readlines()
        
        for i in range(0, len(lines), 2):
            if lines[i].startswith('name="'):
                tag_name = lines[i].split('"')[1]
                tag_options.append(tag_name)
    
    tag_command.options["tag"].choices = tag_options

update_tag_options.start()

# ------/tags------

@bot.command
@lightbulb.command("tags", "Display tags from a text file")
@lightbulb.implements(lightbulb.SlashCommand)
async def tags_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="Tags")
    
    with open("C:/Users/Genius/Desktop/very cool bot/tags.txt", "r") as file:
        for line in file:
            if line.startswith("name="):
                name = line.split("=")[1].strip().replace('"', '')
                embed.add_field(name=name, value="")
            elif line.startswith("desc="):
                desc = line.split("=")[1].strip().replace('"', '')
                embed.edit_field(-1, embed.fields[-1].name, f"**{desc}**")
    
    await ctx.respond(embed=embed)

@tasks.task(s=10)  # Run the task every 10 seconds
async def update_tags():
    # Perform any necessary updates to the tags file here
    pass

# ------/more-commands-coming-soon------

# ------- end of code --------

# Run the bot
bot.run()
