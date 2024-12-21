from telethon import TelegramClient, sync
from telethon.tl.types import User, MessageMediaPhoto, MessageMediaDocument, Dialog
import asyncio
import json
from datetime import datetime
import os

# Replace these with your own values
api_id = 'your_api_id_here'
api_hash = 'your_api_hash_here'
phone = 'your_phone_number_here'

async def get_user_info(user):
    """Extract relevant user information."""
    return {
        'user_id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'phone': user.phone,
        'is_bot': user.bot
    }

async def get_message_data(message):
    """Extract relevant message information."""
    return {
        'message_id': message.id,
        'text': message.text,
        'date': message.date.isoformat(),
        'out': message.out,  # True if message was sent by you
        'from_id': message.from_id.user_id if message.from_id else None,
        'reply_to_msg_id': message.reply_to.reply_to_msg_id if message.reply_to else None
    }

async def export_direct_chats():
    """Export all direct chat messages to a JSON file."""
    
    # Initialize the client
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()
    
    try:
        # Get all dialogs
        print("Fetching dialogs...")
        dialogs = await client.get_dialogs()
        
        # Initialize the export data structure
        export_data = {
            'export_date': datetime.now().isoformat(),
            'total_direct_chats': 0,
            'total_messages': 0,
            'chats': []
        }
        
        # Process only direct chats
        direct_chats = [dialog for dialog in dialogs if isinstance(dialog.entity, User)]
        export_data['total_direct_chats'] = len(direct_chats)
        
        print(f"\nFound {len(direct_chats)} direct chats")
        
        # Process each direct chat
        for chat_index, dialog in enumerate(direct_chats, 1):
            try:
                user = dialog.entity
                print(f"\nProcessing chat {chat_index}/{len(direct_chats)}: {user.first_name or 'Unknown'}")
                
                # Initialize chat data structure
                chat_data = {
                    'user': await get_user_info(user),
                    'message_count': 0,
                    'messages': []
                }
                
                # Fetch all messages from this chat
                message_count = 0
                async for message in client.iter_messages(dialog):
                    # Skip messages with media
                    if isinstance(message.media, (MessageMediaPhoto, MessageMediaDocument)):
                        continue
                        
                    if message.text:  # Only process text messages
                        chat_data['messages'].append(await get_message_data(message))
                        message_count += 1
                        
                        # Print progress every 100 messages
                        if message_count % 100 == 0:
                            print(f"Processed {message_count} messages...")
                
                chat_data['message_count'] = message_count
                export_data['total_messages'] += message_count
                export_data['chats'].append(chat_data)
                
                print(f"Completed chat with {message_count} messages")
                
            except Exception as e:
                print(f"Error processing chat {chat_index}: {str(e)}")
                continue
        
        # Save to file
        output_filename = f"telegram_direct_chats_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)
        
        print(f"\nExport complete!")
        print(f"Total direct chats: {export_data['total_direct_chats']}")
        print(f"Total messages: {export_data['total_messages']}")
        print(f"Saved to: {output_filename}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    finally:
        await client.disconnect()

def main():
    asyncio.run(export_direct_chats())

if __name__ == "__main__":
    main()
