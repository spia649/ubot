from pyrogram import Client, Filters
import signal

app = Client(
    "my_account",
    api_id=667795,
    api_hash="f2e9b0fdd19eb992c4efbd465c0728c9"
)
pin = False
en = False
voip = Client(
    "my_voip",
    api_id=667795,
    api_hash="f2e9b0fdd19eb992c4efbd465c0728c9"
)
myaccount = [653531932]

@app.on_message()
def onMsg(client, message):
    global en
    if message.text is not None:
        text = message.text
        splitted = text.split(" ")

    # COMANDO -FLOOD
    if message.text is not None and splitted[0] == "-flood" and en == True:
        codice = """
try:
    n = int("{}") # converto il numero di volte in cui inviare il messaggio da str a int
except:
    app.edit_message_text({}, {}, "🦋 <b>Error.</b>\\n<i>Are you sure you typed a number after -flood?</i>", parse_mode="html")
finally:
    if n is not None: # trasformo il testo da mandare, da array a stringa pronta
        floodtext = ""
        for x in {}:
            floodtext = floodtext+" "+x
        repeat = 0
        while repeat != n: # e infine invio ...
            app.send_message({}, floodtext, parse_mode="html")
            repeat += 1
""".format(splitted[1], message.chat.id, message.message_id, splitted[2::], message.chat.id)
        ID = message.from_user.id
        esegui(id=ID, code=codice)

    #GINFO
    if message.text is not None and splitted[0] == "-ginfo":
        codice = """
if "{}" == "supergroup":
    ginfotext = "<b>Info of this Group:</b>\\n\\n"
    ginfotext = ginfotext+"   ➥ <b>ChatID.</b> 🐈 <code>"+str({})+"</code>\\n"
    ginfotext = ginfotext+"   ➥ <b>Type.</b> 🔭 <i>"+"{}"+"</i>\\n"
    if {} == True:
        ginfotext = ginfotext+"   ➥ <b>Is verified?</b> 🦚 <i>Yes</i>\\n"
    else:
        ginfotext = ginfotext+"   ➥ <b>Is verified?</b> 🦚 <i>No</i>\\n"
    ginfotext = ginfotext+"   ➥ <b>Name.</b> 🔮 <i>"+"{}"+"</i>\\n"
    ginfotext = ginfotext+"   ➥ <b>Members Count.</b> 📊 <i>"+str({})+"</i>\\n"
    if {} is not None:
        ginfotext = ginfotext+"   ➥ <b>Username.</b> 🌐 <i>"+"{}"+"</i>\\n\\n"
    else:
        ginfotext = ginfotext+"\\n"
    getch = app.get_chat({})
    if getch.description is not None:
        ginfotext = ginfotext+"-<b>Description.</b> 📚: <i>"+getch.description+"</i>"
    else:
        ginfotext = ginfotext+"-<b>Description.</b> 📚: <i>This group hasn't a description!</i>"
    app.edit_message_text({}, {}, ginfotext, "html")
""".format(message.chat.type, message.chat.id, message.chat.type, message.chat.is_verified, message.chat.title, message.chat.members_count, message.chat.username, message.chat.username, message.chat.id, message.chat.id, message.message_id)
        ID = message.from_user.id
        esegui(id=ID, code=codice)

    # PING
    if message.text is not None and splitted[0] == "-online" and message.from_user.id in myaccount and en == True:
        app.edit_message_text(message.chat.id, message.message_id, "<b>userbot</b> online. ⛅️", "html")

    # ENABLE
    if message.text is not None and splitted[0] == "-enable" and message.from_user.id in myaccount:
        en = True
        app.edit_message_text(message.chat.id, message.message_id, "🦋 <i>Userbot enabled.</i>", "html")
    # DISABLE
    if message.text is not None and splitted[0] == "-noenable" and message.from_user.id in myaccount:
        en = True
        app.edit_message_text(message.chat.id, message.message_id, "🦋 <b>Done</b>.", "html")

    # ENTRATA NEL GRUPPO DI CRISTIAN Z VOIP
    if message.text is not None and splitted[0] == "-forcejoin" and splitted[1] is not None:
        codice = """
if "t.me" in "{}":
    try:
        voip.join_chat("{}")
        app.edit_message_text({}, {}, "🦋 <b>Done</b>.", "html")
    except:
        app.edit_message_text({}, {}, "🦋 <b>Error</b>.", "html")
""".format(str(splitted[1]), str(splitted [1]), message.chat.id, message.message_id, message.chat.id, message.message_id)
        ID = message.from_user.id
        esegui(id=ID, code=codice)
    if message.text is not None and splitted[0] == "-forceleave" and splitted[1] is not None:
        codice = """
if "{}" == "this":
    try:
        voip.leave_chat({})
        app.edit_message_text({}, {}, "🦋 <b>Done</b>.", "html")
    except:
        app.edit_message_text({}, {}, "🦋 <b>Error</b>.", "html")
""".format(str(splitted[1]), message.chat.id, message.chat.id, message.message_id, message.chat.id, message.message_id)
        ID = message.from_user.id
        esegui(id=ID, code=codice)

def esegui(id, code):
    if type (id) is int and id in myaccount and en == True:
        voip.start()
        ncode = compile(code, "string", "exec")
        exec(ncode)
        voip.stop()

app.run()
