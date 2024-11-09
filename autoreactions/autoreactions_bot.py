import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Load environment variables from .env file
load_dotenv()

# Get the token from environment variable
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
AUTOREACTIONS_FILE = 'autoreactions.json'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Load reactions configuration
if os.path.exists(AUTOREACTIONS_FILE):
    with open(AUTOREACTIONS_FILE, 'r') as file:
        reactions = json.load(file)
else:
    reactions = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print(f'Auto-Reactions configuration: {reactions}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_id = str(message.author.id)
    print(f'Message received from user: {user_id}')

    if user_id in reactions:
        emoji = reactions[user_id]
        print(f'Reacting to message from {user_id} with emoji {emoji}')
        try:
            await message.add_reaction(emoji)
        except discord.errors.HTTPException as e:
            print(f'Failed to add reaction: {e}')
    else:
        print(f'No auto-reaction configured for user {user_id}')

    await bot.process_commands(message)

def update_reactions():
    global reactions
    if os.path.exists(AUTOREACTIONS_FILE):
        with open(AUTOREACTIONS_FILE, 'r') as file:
            reactions = json.load(file)
        print(f'Updated auto-reactions configuration: {reactions}')

class ReactionsFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(AUTOREACTIONS_FILE):
            update_reactions()

# Set up file watcher
event_handler = ReactionsFileHandler()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=False)
observer.start()

# Run the bot
try:
    bot.run(DISCORD_BOT_TOKEN)
except KeyboardInterrupt:
    observer.stop()
observer.join()
