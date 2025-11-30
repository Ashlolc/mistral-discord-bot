# Mistral Discord Bot

This is a Discord bot that uses the Mistral API to answer questions.

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with the following variables:
   ```env
   MISTRAL_API_KEY=your_mistral_api_key
   MISTRAL_API_ENDPOINT=your_mistral_api_endpoint
   DISCORD_BOT_TOKEN=your_discord_bot_token
   ```

3. Start the bot:
   ```bash
   python bot.py
   ```