import streamlit as st
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

AUTOREACTIONS_FILE = 'autoreactions.json'

# Load reactions configuration
if os.path.exists(AUTOREACTIONS_FILE):
    with open(AUTOREACTIONS_FILE, 'r') as file:
        reactions = json.load(file)
else:
    reactions = {}

st.title("Discord Bot Auto-Reaction Manager")

# Add new or update existing reaction
st.subheader("Add/Update Auto-Reaction")
user_id = st.text_input("Discord User ID")
emoji = st.text_input("Reaction Emoji")

if st.button("Add/Update Auto-Reaction"):
    if user_id and emoji:
        reactions[user_id] = emoji
        with open(AUTOREACTIONS_FILE, 'w') as file:
            json.dump(reactions, file)
        st.success(f"Updated auto-reaction for user {user_id} to {emoji}")
        st.rerun()  # Refresh the app to show updated list

# Display and manage current reactions
st.subheader("Current Auto-Reactions")
for user_id, emoji in reactions.items():
    st.write(f"User ID: {user_id} | Emoji Reaction: {emoji}")
    
    # Edit existing reaction
    new_emoji = st.text_input(f"Update Auto-Reaction for {user_id}", value=emoji, key=f"update_{user_id}")
    if st.button(f"Update {user_id}", key=f"update_btn_{user_id}"):
        reactions[user_id] = new_emoji
        with open(AUTOREACTIONS_FILE, 'w') as file:
            json.dump(reactions, file)
        st.success(f"Updated auto-reaction for user {user_id} to {new_emoji}")
        st.rerun()  # Refresh the app to show updated list

    # Delete reaction
    if st.button(f"Delete {user_id}", key=f"delete_{user_id}"):
        del reactions[user_id]
        with open(AUTOREACTIONS_FILE, 'w') as file:
            json.dump(reactions, file)
        st.success(f"Deleted auto-reaction for user {user_id}")
        st.rerun()  # Refresh the app to show updated list

if st.button("Refresh"):
    st.rerun()  # Updated to use st.rerun()
