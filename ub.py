from pyrogram import Client, Filters
import signal

app = Client(
    "my_account",
    api_id=667795,
    api_hash="f2e9b0fdd19eb992c4efbd465c0728c9"
)
pin = False
id = 653531932
en = False
voip = Client(
    "my_voip",
    api_id=667795,
    api_hash="f2e9b0fdd19eb992c4efbd465c0728c9"
)

@app.on_message()
def onMsg(client, message):
    global en
    if message.text is not None:
        text = message.text
        splitted = text.split(" ")

    # COMANDO -FLOOD
    if message.text is not None and splitted[0] == "-flood" and message.from_user.id == id and en == True:
        try:
            n = int(splitted[1]) # converto il numero di volte in cui inviare il messaggio da str a int
        except:
            message.reply("🦋 <b>Error.</b>\n<i>Are you sure you typed a number after -flood?</i>", parse_mode="html")
        finally:
            if n is not None: # trasformo il testo da mandare, da array a stringa pronta
                floodtext = ""
                for x in splitted[2::]:
                    floodtext = floodtext+" "+x
                repeat = 0
                while repeat != n: # e infine invio ...
                    app.send_message(message.chat.id, floodtext, parse_mode="html")
                    repeat += 1
    #GINFO
    if message.text is not None and splitted[0] == "-ginfo" and message.from_user.id == id and en == True:
        if message.chat.type == "supergroup":
            ginfotext = "<b>Info of this Group:</b>\n\n"
            ginfotext = ginfotext+"   ➥ <b>ChatID.</b> 🐈 <code>"+str(message.chat.id)+"</code>\n"
            ginfotext = ginfotext+"   ➥ <b>Type.</b> 🔭 <i>"+message.chat.type+"</i>\n"
            if message.chat.is_verified == True:
                ginfotext = ginfotext+"   ➥ <b>Is verified?</b> 🦚 <i>Yes</i>\n"
            else:
                ginfotext = ginfotext+"   ➥ <b>Is verified?</b> 🦚 <i>No</i>\n"
            ginfotext = ginfotext+"   ➥ <b>Name.</b> 🔮 <i>"+message.chat.title+"</i>\n"
            ginfotext = ginfotext+"   ➥ <b>Members Count.</b> 📊 <i>"+str(message.chat.members_count)+"</i>\n"
            if message.chat.username is not None:
                ginfotext = ginfotext+"   ➥ <b>Username.</b> 🌐 <i>"+message.chat.username+"</i>\n\n"
            else:
                ginfotext = ginfotext+"\n"
            getch = app.get_chat(message.chat.id)
            if getch.description is not None:
                ginfotext = ginfotext+"-<b>Description.</b> 📚: <i>"+getch.description+"</i>"
            else:
                ginfotext = ginfotext+"-<b>Description.</b> 📚: <i>This group hasn't a description!</i>"
            app.edit_message_text(message.chat.id, message.message_id, ginfotext, "html")

    # PING
    if message.text is not None and splitted[0] == "-online" and message.from_user.id == id and en == True:
        app.edit_message_text(message.chat.id, message.message_id, "<b>userbot</b> online. ⛅️", "html")

    # ENABLE
    if message.text is not None and splitted[0] == "-enable" and message.from_user.id == id:
        en = True
        app.edit_message_text(message.chat.id, message.message_id, "🦋 <i>Userbot enabled.</i>", "html")
    # DISABLE
    if message.text is not None and splitted[0] == "-noenable" and message.from_user.id == id:
        en = True
        app.edit_message_text(message.chat.id, message.message_id, "🦋 <b>Done</b>.", "html")

    # ENTRATA NEL GRUPPO DI CRISTIAN Z VOIP
    if message.text is not None and splitted[0] == "-forcejoin" and message.from_user.id == id:
        if splitted[1] is not None:
            voip.start()
            try:
                voip.join_chat(splitted[1])
                app.edit_message_text(message.chat.id, message.message_id, "🦋 <b>Done</b>.", "html")
                voip.stop()
            except:
                app.edit_message_text(message.chat.id, message.message_id, "🦋 <b>Error</b>.", "html")
    if message.text is not None and splitted[0] == "-forceleave" and message.from_user.id == id:
        if splitted[1] == "this":
            voip.start()
            try:
                voip.leave_chat(message.chat.id)
                app.edit_message_text(message.chat.id, message.message_id, "🦋 <b>Done</b>.", "html")
                voip.stop()
            except:
                app.edit_message_text(message.chat.id, message.message_id, "🦋 <b>Error</b>.", "html")

app.run()
