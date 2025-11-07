from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from MY_TOKEN import TOKEN
from handlers import (
    start,
    help,
    echo_text,
    echo_photo,
    echo_animation,
    echo_sticker,
    echo_audio,
    echo_contact,
    echo_copy,
    echo_dice,
    echo_voice,
    echo_video,
    echo_video_note,
    main_menu

)

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# Komandalar
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))

# Echo xabarlar uchun handlerlar
dispatcher.add_handler(MessageHandler(Filters.text("BOSH MENU"), main_menu))

dispatcher.add_handler(MessageHandler(Filters.text, echo_text))
dispatcher.add_handler(MessageHandler(Filters.photo, echo_photo))
dispatcher.add_handler(MessageHandler(Filters.animation, echo_animation))
dispatcher.add_handler(MessageHandler(Filters.sticker, echo_sticker))
dispatcher.add_handler(MessageHandler(Filters.audio, echo_audio))
dispatcher.add_handler(MessageHandler(Filters.voice, echo_voice))   # ovozli xabarlar
dispatcher.add_handler(MessageHandler(Filters.video, echo_video))   # video xabarlar
dispatcher.add_handler(MessageHandler(Filters.contact, echo_contact))
dispatcher.add_handler(MessageHandler(Filters.forwarded, echo_copy))
dispatcher.add_handler(MessageHandler(Filters.dice, echo_dice))
dispatcher.add_handler(MessageHandler(Filters.video_note, echo_video_note))  # yumaloq video

#message handerlar 
#dispatcher.add_handler(MessageHandler(Filters.text("BOSH MENU" ,main_menu )))
updater.start_polling()
updater.idle()
