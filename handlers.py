
from telegram.ext import Updater ,CallbackContext 
from telegram import Update , ReplyKeyboardMarkup

from db import add_user



def start(update: Update ,context: CallbackContext):
    if add_user(
        tg_id=update.message.from_user.id ,
        full_name=update.message.from_user.full_name,
        username=update.message.from_user.username
     ):
        update.message.reply_text(
            text=f"assolomu  alaykum {update.message.from_user.full_name}, botga xush kelibsiz" ,
            reply_markup = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        "BOSH MENU ",
                    "SOZLAMALAR" , "OPERATOR"
                    ]
                ]

            )
            
        )
    else:
        update.message.reply_text(
            text=f" qaytganingiz bilan  {update.message.from_user.full_name}",
             reply_markup = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        "BOSH MENU ",
                    "SOZLAMALAR" , "OPERATOR"
                    ]
                ]

            )
        )
   
def help(update: Update , context: CallbackContext):
    update.message.reply_text(
        text=f"{update.message.from_user.full_name} sizga qanday yordam bera olaman  ",
                    reply_markup = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        " yordam  ",
                    "contact" , "tizim bilan muammo"
                    ]
                ]

            )
            
        )


    
def echo_photo(update: Update , context: CallbackContext):
    update.message.reply_photo(update.message.photo[1])

def echo_text(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def echo_animation(update: Update, context: CallbackContext):
    update.message.reply_animation(update.message.animation)

def echo_sticker(update: Update, context: CallbackContext):
    update.message.reply_sticker(update.message.sticker)

def echo_audio(update: Update, context: CallbackContext):
    update.message.reply_audio(update.message.audio)

def echo_contact(update: Update, context: CallbackContext):
    update.message.reply_contact(update.message.contact)

def echo_copy(update: Update, context: CallbackContext):
    update.message.reply_copy(update.message.copy)

def echo_dice(update: Update, context: CallbackContext):
    update.message.reply_dice(update.message.dice)

def echo_voice(update: Update, context: CallbackContext):
    update.message.reply_voice(update.message.voice)

def echo_video(update: Update, context: CallbackContext):
    update.message.reply_video(update.message.video)
def echo_video_note(update: Update, context: CallbackContext):
    update.message.reply_video_note(update.message.video_note)

def main_menu(update:Update , context:CallbackContext):
    update.message.reply_text("asosiy saxifaga  keldez !!")
