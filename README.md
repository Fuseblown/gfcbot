# GFC Bot

A useful Discord bot and group project for the GFC private server.

## Repository Branches

- `main` branch - Stable release running on the actual live GFC Discord server
- `beta` branch - Pre-release version running on live GFC Discord server as a Beta version of the bot. Only new features post-testing should be running on the Beta bot. Stable features should be disabled as to not affect the main bot. Databases and files will be shared between the stable and beta bots.
- `test` branch - New features out of the dev branch that need reviewed/tested and will be running on the shared test server (ask Dustin for the invite link).
- `dev` branch - New features currently in development, bug fixes, etc.

## Bot Installation & Usage

### Discord Bot Token

You will need a Discord Bot Token from the Developer Portal and assigned appropriate permissions in order to run this bot. **_Detailed instructions on how to obtain this token are coming soon._**

### Install Python Requirements

On your hosting server or development environment command line, from the `gfcbot` root directory:

`pip install -r requirements.txt`

### Invite the Bot to a Server

**IMPORTANT:** If you have admin access to the official GFC server, please do **NOT** invite a development copy of the bot to the main Discord server. Create a standalone Discord server to test on or use the shared test server and name the bot appropriately to maintain separation (i.e. 'GFC Bot - Dustin Test' or some such). Ask Dustin for the invite link to the shared test server.

Follow this URL for shared token access to invite the bot to a server (or use the URL generated in your developer portal (Select App -> Installation -> Install Link) if using your own token):

https://discord.com/oauth2/authorize?client_id=1303529371780255844

### Serve the Bot

In your terminal:

`python bot.py`

You should see some responses from discord.client and discord.gateway and a message that the bot is logged in and it's assigned name. There may be other messages in regards to certain configuration files loading and you may also see monitoring output coming through in the terminal as users send messages, etc.

If you see any bugs or errors, please report to the team for confirmation and/or create a new Github issue.

### Serving the User Interface

There is a Python Streamlit application for configuring features and monitoring the bot.

In your terminal:

`streamlit run app.py`

You will see confirmation that the server has started and that you can now view your Streamlit app in your browser.

The default URL to access the user interface once the app is running is: http://localhost:8501/

## Current Features in Development

### Auto-reactions

- Automatically reacts to a specific user's messages with a chosen emoji or emojis

## Ideas & Features Wishlist

### Artificial Intelligence

- Train the bot on past chat history
- Give the bot a personality
- Allow the bot to answer direct questions
- Could be used to generate trivia questions, make decisions, etc.
- Might be fun to have it randomly join in on conversations
- Start a new conversation or topic if the server or channel is quiet for a specified period of time

### Event Planning

- Calendar
- RSVP system
- Planning system (food, games, camping supplies, necessary items, etc.)

### Tournament Bracket Generation & Voting

- Allow users to nominate the inputs for generating the bracket
- Properly seed bracket based on nominations
- Voting system with start/end timer
- Close voting and generate new polls based on results
- Automatically fill the bracket based on results

### Trivia Game

- Have an on-going game or league
- Breakdown questions into categories like Trivial Pursuit, Jeopardy, etc.

### RPG Game

- Something like the BBS door game Legend of the Red Dragon (Legend of the Grey Dragon **_\*wink\*_**)
