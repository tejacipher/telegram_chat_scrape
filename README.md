# Telegram Direct Chats Exporter

This Python script exports all your Telegram direct chat messages to a JSON file. It uses the Telethon library to interact with Telegram's API and extracts text messages from your direct conversations while skipping media content.

## Prerequisites

1. Python 3.7 or higher
2. Visual Studio Code
3. Telegram account
4. Telegram API credentials (api_id and api_hash)

## Setup Instructions

### 1. Install Python
1. Download Python from python.org
2. During installation, make sure to check "Add Python to PATH"
3. Verify installation by opening Command Prompt and typing:
   python --version

### 2. Get Telegram API Credentials
1. Go to https://my.telegram.org/
2. Log in with your phone number
3. Click on "API development tools"
4. Create a new application if you haven't already
5. Note down your api_id and api_hash

### 3. Project Setup
1. Create a new folder for your project
2. Open VS Code and select File > Open Folder > Select your project folder
3. Create a new file called telegram_export.py
4. Copy the provided script into this file
5. Open VS Code terminal (View > Terminal) and create a virtual environment:
   python -m venv venv

6. Activate the virtual environment:
   .\venv\Scripts\activate

7. Install required packages:
   pip install telethon

### 4. Configure the Script
Replace the following values in the script with your own:
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone = 'YOUR_PHONE_NUMBER'  # Format: +1234567890

## Running the Script

1. Make sure your virtual environment is activated in VS Code terminal
2. Run the script:
   python telegram_export.py
3. On first run, you'll be prompted to enter the verification code sent to your Telegram account
4. The script will create a session file to remember your authentication

## Output

The script will generate a JSON file with the following naming format:
telegram_direct_chats_export_YYYYMMDD_HHMMSS.json

The JSON file contains:
- Export date
- Total number of direct chats
- Total number of messages
- For each chat:
  - User information (ID, name, username, phone)
  - Message count
  - Messages (ID, text, date, sender, reply information)

## Features

- Exports only text messages (skips media)
- Includes message metadata (date, sender, reply information)
- Progress tracking during export
- Error handling for individual chats
- Clean JSON output format

## Troubleshooting

1. Authentication Error
   - Delete the session_name.session file
   - Run the script again
   - Enter the new verification code

2. ModuleNotFoundError
   - Ensure virtual environment is activated
   - Run pip install telethon again

3. Connection Error
   - Check your internet connection
   - Verify API credentials
   - Ensure your Telegram account isn't restricted

## Security Notes

- Keep your api_id and api_hash confidential
- Don't share your session file
- Be cautious when sharing exported JSON files as they contain private conversations

## Limitations

- Only exports text messages
- Media files are skipped
- Group chats are not included
- Rate limiting may apply for large exports

## Support

For issues with:
- Telethon library: https://docs.telethon.dev/
- Telegram API: https://core.telegram.org/api
