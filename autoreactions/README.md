# Auto-Reactions Feature

    Author(s): Dustin Cohenour
    Current Stable Version: N/A
    Current Dev Version: v0.01a

---

**This feature is currently in development. While it does currently function, it has not been strenuously tested and it really needs some TLC on the user interface to make it more user-friendly.**

1. Follow this URL for shared token access to invite the bot to a server (or use the URL generated in your developer portal (Select App -> Installation -> Install Link) if using your own token):

https://discord.com/oauth2/authorize?client_id=1303529371780255844

1. In a termina, run `pip install requirements.txt`

2. Then run `python autoreactions_bot.py` to bring the bot online.

3. Double-check that the bot is online on the intended server.

4. In another terminal, run `streamlit run autoreactions_app.py` to bring the Streamlit user interface online at http://localhost:8501/.

5. The input requires a raw user ID # to specify the correct user. With the proper permissions this can be obtained from the user's modview or, another way, is when a user sends a message to the server it will currently show up in the terminal window of the running bot script.

6. Requires the emoji name and raw ID # to specify the correct emoji for the auto-reaction. Usage is `<:emoji_name:emoji_id_number>` The emoji_name is the text shortcut for that emoji on the active server. You obtain the emoji_id_number by right-clicking on an emoji -> Copy Link, then paste the URL into a text file and extract the ID number from there.

7. If you have any questions at all, just ask.

8. I originally made this to react a :pocket_hoagie: emoji to every message that Tony sends on the main GFC server. I just never activated it.
