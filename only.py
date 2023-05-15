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
    elif user_choice == "for_info" and message.text.startswith("Poster -") and "Name:" in message.text and "Release info:" in message.text and "Language:" in message.text and "Quality:" in message.text and "Mb/gb size:" in message.text and "Genre:" in message.text and "Story -" in message.text and "Link 1 -" in message.textand and "480p Link -" in message.text and "720p Link -" in message.text and "1080p Link -" in message.text:
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

     text_msg = f'''<div> <div> <div style="text-align: center;">  <img alt="Movie Poster" class="posterimg" height="400" src="{Poster}" width="270" /> </div>   </div> <div> <br /> </div>   <!Information >   <div class="infobox"> <div class="infobox-item">  <label class="infobox-text">Name:</label>  <span>{Name}</span> </div> <div class="infobox-item">  <label class="infobox-text">Release info:</label>  <span>{Release_info}</span> </div> <div class="infobox-item">  <label class="infobox-text">Language:</label>  <span>{Language}</span> </div> <div class="infobox-item">  <label class="infobox-text">Subtitles:</label>  <span>Not/Conform</span> </div> <div class="infobox-item">  <label class="infobox-text">Quality:</label>  <span>{Quality}</span> </div> <div class="infobox-item">  <label class="infobox-text">Mb/gb size:</label>  <span>{total_size}</span> </div> <div class="infobox-item">  <label class="infobox-text">Genre:</label>  <span>{Genre}</span> </div>   </div>'''

     text_msg1 = f'''<div style="text-align: center;"> <script type="text/javascript">atOptions = {item_2i}'key' : '648bbfd31b057cd1d553addbbbbf3228','format' : 'iframe','height' : 250,'width' : 300,'params' : {item_2i}{item_1i}{item_1i};document.write('<scr' + 'ipt type="text/javascript" src="http' + (location.protocol === 'https:' ? 's' : '') + '://www.profitabledisplaynetwork.com/648bbfd31b057cd1d553addbbbbf3228/invoke.js"> </scr' + 'ipt>');</script> </div>'''

     text_msg2 = f'''<!Story Line > <div class="postbox">  <br />  <div class="hstorytxt" style="text-align: center;">Story Line</div>  <p class="storytxt" style="color: #000000;margin-left: 1%;margin-top: 2%;font-size: 15px;">{Story}  </p> </div> <!Download Links > <div class="postbox" style="text-align: center;">  <p class="size-text">[480p x {size_480p}] [720p x {size_720p}] [1080p x {size_1080p}]</p>  <a href="${link1}" target="_blank"> <button class="Download Download-btn">Download</button> </a> </div>'''

     text_msg3 = '''<div style="text-align: center;"> <script type="text/javascript">atOptions = {'key' : '648bbfd31b057cd1d553addbbbbf3228','format' : 'iframe','height' : 250,'width' : 300,'params' : {}}; document.write('<scr' + 'ipt type="text/javascript" src="http' + (location.protocol === 'https:' ? 's' : '') + '://www.profitabledisplaynetwork.com/648bbfd31b057cd1d553addbbbbf3228/invoke.js"> </scr' + 'ipt>'); </script> </div> <!Social Media Links > <div class="postbox" style="text-align: center;"> <div> <button class="followus followus-btn">Support Us<button> </div> <br /> <div> <label> <a href="https://www.facebook.com/hws.share" target="_blank"> <img class="socialimg" height="50" src="https://i.ibb.co/hRMKNW1/Document-1999010840.png" width="50" /> </a> </label> <label> <a href="https://twitter.com/HwShare?t=FVeFNU0gQOnbpHTJqGD2BQ&amp;s=35" target="_blank"> <img class="socialimg" height="50" src="https://i.ibb.co/72WKzpM/Document-1999010840.png" width="50" /> </a> </label> <label> <a href="https://youtube.com/@Hwshare" target="_blank"> <img class="socialimg" height="50" src="https://i.ibb.co/TKMQ4SX/Document-1999010840.png" width="50" /> </a> </label> <label> <a href="https://instagram.com/hws_share?igshid=ZDdkNTZiNTM=" target="_blank"> <img class="socialimg" height="50" src="https://i.ibb.co/NyxpbC9/Document-1999010840.png" width="50" /> </a> </label> <label> <a href="https://t.me/Hindi_world_series" target="_blank"> <img class="socialimg" height="50" src="https://i.ibb.co/7NmgY1L/Document-1999010840.png" width="50" /> </a> </label> </div> </div> <div>&amp;nbsp</div> </div>'''

     text_msg4 = '''.fullbody{background-color: #ffffff;} .posterimg{ width:270px; height:400px;margin: auto;margin-top: 5%;margin-bottom: 30px;border: 4px solid #ffdc00;box-shadow: 0 10px 20px 0 rgba(30,30,30,.07);background-color: #ffffff;border-radius: 5px;}.infobox{width: 90%;margin: auto;margin-bottom: 30px;border: 0.5px solid #ffdc00;box-shadow: 0 10px 20px 0 rgba(30,30,30,.07);background-color: #ffffff;border-radius: 5px;}.infobox-item{margin-bottom: 30px;margin-top: 30px;margin-left: 6%;color: #000000;font-size: 16px;}.infobox-text{font-weight: bold;margin-left: 2%;margin-top: 2%;} .storytxt{color: #000000;margin-left: 3%;margin-top: 2%;font-size: 15px;} .hstorytxt{width: 50%;font-weight: bold;color: #000000;border-bottom: 2px solid red;margin-left: 2%;margin-top: 3%;font-size: 30px;margin: auto;}.screenshot-button{background-image: linear-gradient(to right, #600000 , #D00000  , #E00000 ,  #900000 );box-shadow: 0 10px 20px 0 rgba(30,30,30,.07);border: none;color: white;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 20px;border-radius: 7px;cursor: pointer;}.screenshot-button-text{margin-left: 2%;margin-top: 2%;background-color: #400000  ;} .screenshot-item{width:320px;height:160px;margin-top: 4px;border: 3px solid #909090;box-shadow: 0 10px 20px 0 rgba(30,30,30,.07);border-radius: 5px;} .postbox{width: 98%;margin: auto;margin-bottom: 30px;border: 0.5px solid #ffdc00;box-shadow: 0 10px 20px 0 rgba(30,30,30,.07);background-color: #ffffff;border-radius: 5px;}.size-text{font-weight: bold;margin-left: 2%;margin-top: 2%;color: #000000;}.Download {padding: 10px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;transition-duration: 0.4s;cursor: pointer;}.Download-btn {background-color: white;color: black;border: 2px solid #4CAF50;}.Download-btn:hover {background-color: #4CAF50;color: white;border: 2px solid #ffdc00;}.followus{background-image: linear-gradient(to right, #00ffff, #3ea5ff);border: none;font-weight: bold;color: white;margin-top: 2%;padding: 10px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 20px;border-radius: 10px;cursor: pointer;}.screenshot-button-text{font-weight: bold;margin-left: 2%;margin-top: 2%;background-color: #400000  ;}.socialimg{height:50px;width:50px;}''' 

     message_text = f"`{Name} {yearinfo[2]} {Language} {Quality}`"
     message_text1 = f"`{text_msg}{text_msg1}{text_msg2}`"
     message_text4 = f"`{text_msg3}<style>{text_msg4}</style>`"

     app.set_parse_mode(enums.ParseMode.MARKDOWN)
     await message.reply_text(message_text, disable_web_page_preview=True)
     await message.reply_text(message_text1, disable_web_page_preview=True)
     await message.reply_text(message_text4, disable_web_page_preview=True)

    elif user_choice == "for_info2" and message.text.startswith("Poster -") and "Name:" in message.text and "Release info:" in message.text and "Language:" in message.text and "Quality:" in message.text and "Mb/gb size:" in message.text and "Genre:" in message.text and "Story -" in message.text and "Link 1 -" in message.text and "480p Link -" in message.text and "720p Link -" in message.text:
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

     itext_msg = f'''<div> <div> <div style="text-align: center;">  <img alt="Movie Poster" class="posterimg" height="400" src="{iPoster}" width="270" /> </div>   </div> <div> <br /> </div>   <!Information >   <div class="infobox"> <div class="infobox-item">  <label class="infobox-text">Name:</label>  <span>{iName}</span> </div> <div class="infobox-item">  <label class="infobox-text">Release info:</label>  <span>{iRelease_info}</span> </div> <div class="infobox-item">  <label class="infobox-text">Language:</label>  <span>{iLanguage}</span> </div> <div class="infobox-item">  <label class="infobox-text">Subtitles:</label>  <span>Not/Conform</span> </div> <div class="infobox-item">  <label class="infobox-text">Quality:</label>  <span>{iQuality}</span> </div> <div class="infobox-item">  <label class="infobox-text">Mb/gb size:</label>  <span>{itotal_size}</span> </div> <div class="infobox-item">  <label class="infobox-text">Genre:</label>  <span>{iGenre}</span> </div>   </div>'''

     itext_msg1 = f'''<div style="text-align: center;"> <script type="text/javascript">atOptions = {item_2i}'key' : '648bbfd31b057cd1d553addbbbbf3228','format' : 'iframe','height' : 250,'width' : 300,'params' : {item_2i}{item_1i}{item_1i};document.write('<scr' + 'ipt type="text/javascript" src="http' + (location.protocol === 'https:' ? 's' : '') + '://www.profitabledisplaynetwork.com/648bbfd31b057cd1d553addbbbbf3228/invoke.js"> </scr' + 'ipt>');</script> </div>'''

     itext_msg2 = f'''<!Story Line > <div class="postbox">  <br />  <div class="hstorytxt" style="text-align: center;">Story Line</div>  <p class="storytxt" style="color: #000000;margin-left: 1%;margin-top: 2%;font-size: 15px;">{iStory}  </p> </div> <!Download Links > <div class="postbox" style="text-align: center;">  <p class="size-text">[480p x {isize_480p}] [720p x {isize_720p}]</p>  <a href="${ilink1}" target="_blank"> <button class="Download Download-btn">Download</button> </a> </div>'''

     itext_msg3 = '''<div style="text-align: center;"> <script type="text/javascript">atOptions = {'key' : '648bbfd31b057cd1d553addbbbbf3228','format' : 'iframe','height' : 250,'width' : 300,'params' : {}}; document.write('<scr' + 'ipt type="text/javascript" src="http' + (location.protocol === 'https:' ? 's' : '') + '://www.profitabledisplaynetwork.com/648bbfd31b057cd1d553addbbbbf3228/invoke.js"> </scr' + 'ipt>'); </script> </div> <!Social Media Links > <div class="postbox" style="text-align: center;"> <div> <button class="followus followus-btn">Support Us</button> </div> <br /> <div> <label> <a href="https://www.facebook.com/hws.share" target="_blank"> <img class="socialimg" height="50" src="https://i.ibb.co/hRMKNW1/Document-1999010840.png" width="50" /> </a> </label> <label> < a href="https://twitter.com/HwShare?t=FVeFNU0gQOnbpHTJqGD2BQ&amp;s=35" target="_blank"> <img class="socialimg" height="50" src="https://i.ibb.co/72WKzpM/Document-1999010840.png" width="50" /> </a> </label> <label> <a href="https://youtube.com/@Hwshare" target="_blank"> <img class="socialimg" height="50" src="https://i.ibb.co/TKMQ4SX/Document-1999010840.png" width="50" /> </a> </label> <label> <a href="https://instagram.com/hws_share?igshid=ZDdkNTZiNTM=" target="_blank"> <img class="socialimg" height="50" src="https://i.ibb.co/NyxpbC9/Document-1999010840.png" width="50" /> </a> </label> <label> <a href="https://t.me/Hindi_world_series" target="_blank"> <img class="socialimg" height="50" src="https://i.ibb.co/7NmgY1L/Document-1999010840.png" width="50" /> </a> </label> </div> </div> <div>&amp;nbsp</div> </div>'''

     itext_msg4 = '''.fullbody{background-color: #ffffff;} .posterimg{ width:270px; height:400px;margin: auto;margin-top: 5%;margin-bottom: 30px;border: 4px solid #ffdc00;box-shadow: 0 10px 20px 0 rgba(30,30,30,.07);background-color: #ffffff;border-radius: 5px;}.infobox{width: 90%;margin: auto;margin-bottom: 30px;border: 0.5px solid #ffdc00;box-shadow: 0 10px 20px 0 rgba(30,30,30,.07);background-color: #ffffff;border-radius: 5px;}.infobox-item{margin-bottom: 30px;margin-top: 30px;margin-left: 6%;color: #000000;font-size: 16px;}.infobox-text{font-weight: bold;margin-left: 2%;margin-top: 2%;} .storytxt{color: #000000;margin-left: 3%;margin-top: 2%;font-size: 15px;} .hstorytxt{width: 50%;font-weight: bold;color: #000000;border-bottom: 2px solid red;margin-left: 2%;margin-top: 3%;font-size: 30px;margin: auto;}.screenshot-button{background-image: linear-gradient(to right, #600000 , #D00000  , #E00000 ,  #900000 );box-shadow: 0 10px 20px 0 rgba(30,30,30,.07);border: none;color: white;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 20px;border-radius: 7px;cursor: pointer;}.screenshot-button-text{margin-left: 2%;margin-top: 2%;background-color: #400000  ;} .screenshot-item{width:320px;height:160px;margin-top: 4px;border: 3px solid #909090;box-shadow: 0 10px 20px 0 rgba(30,30,30,.07);border-radius: 5px;} .postbox{width: 98%;margin: auto;margin-bottom: 30px;border: 0.5px solid #ffdc00;box-shadow: 0 10px 20px 0 rgba(30,30,30,.07);background-color: #ffffff;border-radius: 5px;}.size-text{font-weight: bold;margin-left: 2%;margin-top: 2%;color: #000000;}.Download {padding: 10px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;transition-duration: 0.4s;cursor: pointer;}.Download-btn {background-color: white;color: black;border: 2px solid #4CAF50;}.Download-btn:hover {background-color: #4CAF50;color: white;border: 2px solid #ffdc00;}.followus{background-image: linear-gradient(to right, #00ffff, #3ea5ff);border: none;font-weight: bold;color: white;margin-top: 2%;padding: 10px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 20px;border-radius: 10px;cursor: pointer;}.screenshot-button-text{font-weight: bold;margin-left: 2%;margin-top: 2%;background-color: #400000  ;}.socialimg{height:50px;width:50px;}'''       

    # Define the message for "Info 2"
     imessage_text = f"`{iName} {iyearinfo[2]} {iLanguage} {iQuality}`"
     imessage_text1 = f"`{itext_msg}{itext_msg1}{itext_msg2}`"
     imessage_text4 = f"`{itext_msg3}<style>{itext_msg4}</style>`"

     app.set_parse_mode(enums.ParseMode.MARKDOWN)
     await message.reply_text(imessage_text, disable_web_page_preview=True)
     await message.reply_text(imessage_text1, disable_web_page_preview=True)
     await message.reply_text(imessage_text4, disable_web_page_preview=True)

# Start the bot
p999 = "iam alive"
print(p999)
app.run()
