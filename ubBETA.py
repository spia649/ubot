# // importiamo quel che serve
from pyrogram import Client, Filters

# // sessioni
app = Client(
    "my_account",
    api_id=, # // api id (int) ed api hash (str) di my.telegram.org
    api_hash=""
)
voip = Client(
    "my_voip",
    api_id=, # // api id (int) ed api hash (str) di my.telegram.org
    api_hash=""
)

# // inserire il proprio id/i propri id in questo array...
myaccount = [653531932]

@app.on_message()
def onMsg(client, message):
#    global en
    global app
    if message.text is not None: # // il messaggio è vuoto?
        text = message.text
        splitted = text.split(" ") # // dividiamo in un array le parole separate da uno spazio (" ")

    # COMANDO -FLOOD
    if message.text is not None and splitted[0] == "-flood":
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
    username = "{}"
    if username != "":
        ginfotext = ginfotext+"   ➥ <b>Username.</b> 🌐 <i>"+"@{}"+"</i>\\n\\n"
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
    if message.text is not None and splitted[0] == "-online" and message.from_user.id in myaccount:
        app.edit_message_text(message.chat.id, message.message_id, "<b>userbot</b> online. ⛅️", "html")

    # ENABLE e DISABLE // non più in uso... il codice è tuttavia funzionante, se volete:
    # Togliete gli # da qui, mettendoli nello stesso modo nel blocco delimitato da "# ---- #" e "# // end";
    # nella funzione esegui, cambiate "and id in myaccount: #and en == True: // non più necessario" con:
    # "and id in myaccount and en == True:"
    # Dopodiché, sostituite "global en" con "en = False" all'inizio di questa funzione;
    # quindi togliete il cancelletto.
  # ------ #
#    if message.text is not None and splitted[0] == "-enable" and message.from_user.id in myaccount:
#        en = True // abilita l'ub
#        app.edit_message_text(message.chat.id, message.message_id, "🦋 <i>Userbot enabled.</i>", "html")
#    if message.text is not None and splitted[0] == "-noenable" and message.from_user.id in myaccount:
#        en = True // disabilita l'ub
#        app.edit_message_text(message.chat.id, message.message_id, "🦋 <b>Done</b>.", "html")
    # ---- #
    deprecated = ["-enable", "-noenable"]
    if message.text is not None and splitted[0] in deprecated and message.from_user.id in myaccount:
        app.edit_message_text(message.chat.id, message.message_id, "🦋 <b>Questo comando è deprecato.</b>", "html")
    # // end

    # STOP // comando disabilitato
#    if message.text is not None and splitted[0] == "-stop" and message.from_user.id in myaccount:
#        app.edit_message_text(message.chat.id, message.message_id, "<b>fermo</b> l'userbot come richiesto. ⛅️", "html")
#        app = ""

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
    if type (id) is int and id in myaccount: #and en == True: // non più necessario
        voip.start() # // avvia la sessione del voip
        ncode = compile(code, "string", "exec") # // non particolarmente utile, penso possiate disabilitarlo
        exec(ncode) # // esegue il codice | se disabilitate ncode, sostituite ncode con code qui
        voip.stop() # // ferma la sessione del voip per prevenire errori durante l'arresto

app.run()
