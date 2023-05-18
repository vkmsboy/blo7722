import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from pyrogram import enums
from config import API_ID,API_HASH,TOKEN

API_ID = API_ID
API_HASH = API_HASH
TOKEN = TOKEN
# Initialize the bot with your API ID and API hash
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

item_2 = "<"
item_1 = ">"
item_2i = "{"
item_1i = "}"

MAX_MESSAGE_LENGTH = 4096

# Function to send messages in batches
async def send_messages_in_batches(chat_id, messages):
    for i in range(0, len(messages), MAX_MESSAGE_LENGTH):
        batch = messages[i:i + MAX_MESSAGE_LENGTH]
        message_text = "\n".join(batch)
        try:
            await app.send_message(chat_id=chat_id, text=message_text)
        except MessageTooLong:
            # If the message is too long, split it into smaller batches recursively
            await send_messages_in_batches(chat_id, batch)

# Define the inline keyboard for the "Settings" command
settings_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("For Link", callback_data="for_link"), InlineKeyboardButton("For Info", callback_data="for_info")],
    [InlineKeyboardButton("For Info 2", callback_data="for_info2")]
])

# Add this line at the beginning of your code to create a dictionary to store user choices
user_choices = {}

# Define an event handler for new messages
@app.on_message(filters.command("start"))
async def settings_command_handler(client, message):
    # Reply to the user with a welcome message
    await message.reply_text("I Am Alive")

# Define the callback function for the "Settings" command
@app.on_message(filters.command("settings"))
async def settings_command_handler(client, message):
    await message.reply_text("Please select an option:", reply_markup=settings_keyboard)

# Define the callback function for the inline keyboard buttons
@app.on_callback_query()
async def callback_query_handler(client, query):
    user_id = query.from_user.id
    if query.data == "for_link":
        user_choices[user_id] = "for_link"
        message = "."
    elif query.data == "for_info":
        user_choices[user_id] = "for_info"
        message = "."
    elif query.data == "for_info2":
        user_choices[user_id] = "for_info2"
        message = "."
    await query.message.reply_text(message)

# Define the function to handle messages
@app.on_message(filters.text)
async def message_handler(client, message):
    user_id = message.from_user.id
    user_choice = user_choices.get(user_id, None)
    # Check if the user has selected "Info 1"
    if user_choice == "for_link" and message.text.startswith("480p Link -") and "720p Link -" in message.text and "1080p Link -" in message.text:
        # Split the message into lines
        lines = message.text.split(" ")
        # Initialize the variables
        link_480p = ""
        link_720p = ""
        link_1080p = ""
        # Loop through the lines and extract the links
        for line in lines:
            if line.startswith("480p Link -"):
                link_480p = line.replace("480p Link - ", "")
            elif line.startswith("720p Link -"):
                link_720p = line.replace("720p Link - ", "")
            elif line.startswith("1080p Link -"):
                link_1080p = line.replace("1080p Link - ", "")
        # Define the message for "Info 1"
        message_text = f"Your link is ready:\n\n| 480p | {link_480p}\n| 720p | {link_720p}\n| 1080p | {link_1080p}"
        # Send the message to the user
        await message.reply_text(message_text)
    # Check if the user has sent the required information for "Info 2"
    elif user_choice == "for_info" and message.text.startswith("Poster -") and "Name:" in message.text and "Release info:" in message.text and "Language:" in message.text and "Quality:" in message.text and "Mb/gb size:" in message.text and "Genre:" in message.text and "Story -" in message.text and "480p Link -" in message.text and "720p Link -" in message.text and "1080p Link -" in message.text:
     # Split the message into lines
     lines = message.text.split("\n")
    # Initialize the variables
     Poster = ""
     Name = ""
     Release_info = ""
     Language = ""
     Quality = ""
     total_size = ""
     Genre = ""
     Story = ""
     l480p = ""
     l720p = ""
     l480p = ""
     link1 = ""
    # Loop through the lines and extract the links
     for line in lines:
        if line.startswith("Poster -"):
            Poster = line.replace("Poster - ", "").strip()
        elif line.startswith("Name:"):
            Name = line.replace("Name: ", "").strip()
        elif line.startswith("Release info:"):
            Release_info = line.replace("Release info: ", "").strip()
            yearinfo = [s.strip() for s in Release_info.split()]
        elif line.startswith("Language:"):
            Language = line.replace("Language: ", "").strip()
        elif line.startswith("Quality:"):
            Quality = line.replace("Quality: ", "").strip()
        elif line.startswith("Mb/gb size:"):
            total_size = line.replace("Mb/gb size: ", "").strip()
        elif line.startswith("Genre:"):
            Genre = line.replace("Genre: ", "").strip()
        elif line.startswith("Story -"):
            Story = line.replace("Story - ", "").strip()
        elif line.startswith("Mb/gb size:"):
            l480p = line.replace("480p Link - ", "").strip()
        elif line.startswith("Genre:"):
            l720p = line.replace("720p Link - ", "").strip()
        elif line.startswith("Story -"):
            l1080p = line.replace("1080p Link - ", "").strip()
        elif line.startswith("Link 1 -"):
            link1 = line.replace("Link 1 - ", "").strip()
    # Split the total_size string into individual sizes
     sizes = total_size.split(" ")
     size_480p = sizes[0]
     size_720p = sizes[1]
     size_1080p = sizes[2]

     message_text = f"`{Name} {yearinfo[2]} {Language} {Quality}`\n1:1 Size `{size_480p}` `{size_720p}` `{size_1080p}`\n\n`{Poster}`\nName `{Name}`\nYear Info `{Release_info}`\nLanguage `{Language}`\nQuality `{Quality}`\nSize `{total_size}`\nGenres `{Genre}`\n\nStory `{Story}`"

     app.set_parse_mode(enums.ParseMode.MARKDOWN)
     await message.reply_text(message_text, disable_web_page_preview=True)

    elif user_choice == "for_info2" and message.text.startswith("Poster -") and "Name:" in message.text and "Release info:" in message.text and "Language:" in message.text and "Quality:" in message.text and "Mb/gb size:" in message.text and "Genre:" in message.text and "Story -" in message.text and "480p Link -" in message.text and "720p Link -" in message.text:
     # Split the message into lines
     ilines = message.text.split("\n")
    # Initialize the variables
     iPoster = ""
     iName = ""
     iRelease_info = ""
     iLanguage = ""
     iQuality = ""
     itotal_size = ""
     iGenre = ""
     iStory = ""
     i480p = ""
     i720p = ""
     ilink1 = ""

    # Loop through the lines and extract the links
     for iline in ilines:
        if iline.startswith("Poster -"):
            iPoster = iline.replace("Poster - ", "").strip()
        elif iline.startswith("Name:"):
            iName = iline.replace("Name: ", "").strip()
        elif iline.startswith("Release info:"):
            iRelease_info = iline.replace("Release info: ", "").strip()
            iyearinfo = [s.strip() for s in iRelease_info.split()]
        elif iline.startswith("Language:"):
            iLanguage = iline.replace("Language: ", "").strip()
        elif iline.startswith("Quality:"):
            iQuality = iline.replace("Quality: ", "").strip()
        elif iline.startswith("Mb/gb size:"):
            itotal_size = iline.replace("Mb/gb size: ", "").strip()
        elif iline.startswith("Genre:"):
            iGenre = iline.replace("Genre: ", "").strip()
        elif iline.startswith("Story -"):
            iStory = iline.replace("Story - ", "").strip()
        elif iline.startswith("Genre:"):
            i480p = iline.replace("480p Link - ", "").strip()
        elif iline.startswith("Story -"):
            i720p = iline.replace("720p Link - ", "").strip() 
        elif iline.startswith("Link 1 -"):
            ilink1 = iline.replace("Link 1 - ", "").strip()
    # Split the total_size string into individual sizes
     isizes = itotal_size.split(" ")
     isize_480p = isizes[0]
     isize_720p = isizes[1]

    # Define the message for "Info 2"
     imessage_text = f"`{iName} {iyearinfo[2]} {iLanguage} {iQuality}`\n1:1 Quality `{isize_480p}` `{isize_720p}`\n\n`{iPoster}`\nName `{iName}`\nYear Info `{iRelease_info}`\nLanguage `{iLanguage}`\nQuality `{iQuality}`\nSize `{itotal_size}`\nGenres `{iGenre}`\n\nStory `{iStory}`"

     app.set_parse_mode(enums.ParseMode.MARKDOWN)
     await message.reply_text(imessage_text, disable_web_page_preview=True)

# Start the bot
p999 = "iam alive"
print(p999)
app.run()
