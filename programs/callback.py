import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery, Message)
from programs.commands import cmd, help, home, dev, id, mention, telegraph, name, username, botinfo, about
#dont remove this this is must





@Client.on_callback_query()
async def button(Tgraph, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await help(Tgraph, update.message)
      elif "close" in cb_data:
        await update.message.edit(
            text="want to realy close the current position",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("yes", callback_data='chosecl'),
                InlineKeyboardButton("no", callback_data='home')
                ]]
            )
     
        )
        await update.answer("JOIN @SEPTEMBERFILMS") 
      elif "home" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await home(Tgraph, update.message)
      elif "help" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await help(Tgraph, update.message)
      elif "cmd" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await cmd(Tgraph, update.message)
      elif "dev" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await dev(Tgraph, update.message)
      elif "id" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await id(Tgraph, update.message)
      elif "mention" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await mention(Tgraph, update.message)
      elif "tgraph" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await telegraph(Tgraph, update.message)
      elif "name" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await name(Tgraph, update.message)
      elif "username" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await username(Tgraph, update.message)
      elif "botinfo" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await botinfo(Tgraph, update.message)
        
      elif "about" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        await about(Tgraph, update.message)
      elif update.data == "alert":
        await update.answer("IAM A BOT USED MAIN PUPOSE IS UPLOAD TO TELEGRAPH AND MANY OTHER FEWTURES CREATED BY @DEVOURDEVILS", show_alert=True)
      elif "chosecl" in cb_data:
        await update.message.edit(
            text="███25%"
        )
        await update.message.edit(
            text="█████50%"
        )
        await update.message.edit(
            text="████████75%"
        )
        await update.message.edit(
            text="████████████100%"
        )
        await update.answer("JOIN @SEPTEMBERFILMS")
        await update.message.delete()
        
        
        
      
