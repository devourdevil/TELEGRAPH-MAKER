import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery, Message)
import logging
import random



ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "https://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]

    
@Client.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[

        InlineKeyboardButton('ADD ME TO GROUP', url='t.me/ddtelegraphbot?startgroup=true'),
    ],
    [

        InlineKeyboardButton('🤔Help', callback_data='help'),
        InlineKeyboardButton('Close🔐', callback_data='close')
    ],
    [

    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""<b>👋Hello {message.from_user.mention} ,
        
`Am a telegraph Uploader That Can Upload Photo, Video And Gif
        
Simply send me photo, video or gif under 5MB I will upload it to Telegra.ph
want know more about this bot click help button
        
Made With Love By` </b> <a href="t.me/devourdevils">DEVOURDEVIL </a>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )


ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "https://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]


@Client.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('🏡Home', callback_data='home'),
        InlineKeyboardButton('Close🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('⚕️Our group⚕️', url='t.me/septemberfilms'),
        InlineKeyboardButton('cmd', callback_data='cmd')
    ],
    [   
        InlineKeyboardButton('bot info', callback_data='botinfo')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""hello  {message.from_user.mention},
this bot par may be add somany cool and hot fewtures in feuture want know the
present commands of this bot click or press cmd button
and Just Send Me A Video/gif/photo under 5mb.
i'll upload it to telegra.ph and give you the direct link**""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )


ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "https://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]

@Client.on_message(filters.command(["cmd"]))
async def cmd(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close'),
        InlineKeyboardButton('id', callback_data='id'),
        InlineKeyboardButton('dev', callback_data='dev'),
    ],
    [
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('mention', callback_data='mention'),
        InlineKeyboardButton('telegraph', callback_data='tgraph'),
        InlineKeyboardButton('username', callback_data='username'),
    ],
    [
        InlineKeyboardButton('tap alert', callback_data='alert'),
        InlineKeyboardButton('botinfo', callback_data='botinfo'),
        InlineKeyboardButton('about', callback_data='about'),
        InlineKeyboardButton('name', callback_data='name')    
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""Hello  {message.from_user.mention}
  my commands are""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      ) 

ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "https://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]


@Client.on_message(filters.command(["id"]))
async def id(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('🤔Help', callback_data='help'),
        InlineKeyboardButton('⚕️Our Channel⚕️', url='t.me/septemberfilms')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""THIS IS YOUR ID ` -{message.from_user.id} `""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )

ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "https://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]


@Client.on_message(filters.command(["dev"]))
async def dev(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('🤔Help', callback_data='help'),
        InlineKeyboardButton('⚕️Our Channel⚕️', url='t.me/septemberfilms')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""this is my developer information
FIRST NAME:`DEVOUR`
LAST NAME :`DEVIL`
USERNAME  :@DEVOURDEVILS
GITHUB PRO:</b> <a href="github.com/kamarjahan">GITHUB </a>
WHO ASKED DEV INFO :{message.from_user.mention}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )

ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "https://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]


@Client.on_message(filters.command(["telegraph"]))
async def telegraph(client, message):
  buttons = [[
        InlineKeyboardButton('🏡Home', callback_data='home'),
        InlineKeyboardButton('Close🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('⚕️Our group⚕️', url='t.me/septemberfilms'),
        InlineKeyboardButton('back⏪', callback_data='cmd')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""SENT ME A PHOTO,VIDEO,GIF,OR ANY ANIMATION I WILL UPLOADNIT TO TELEGRAPH AND GIVE THE PERMENENT LINK""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )

ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "https://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]

@Client.on_message(filters.command(["mention"]))
async def mention(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('back⏪', callback_data='cmd'),
        InlineKeyboardButton('⚕️Our Channel⚕️', url='t.me/septemberfilms')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""THIS IS YOUR PERMENENT LINK {message.from_user.mention}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )

ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "https://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]

@Client.on_message(filters.command(["username"]))
async def username(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('back⏪', callback_data='cmd'),
        InlineKeyboardButton('⚕️Our Channel⚕️', url='t.me/septemberfilms')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""THIS IS YOUR CURRENT USERNAME @{message.from_user.username}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )

ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "https://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]


@Client.on_message(filters.command(["name"]))
async def name(client, message):
  buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('back⏪', callback_data='cmd'),
        InlineKeyboardButton('⚕️Our Channel⚕️', url='t.me/septemberfilms')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""THIS IS YOUR FIRST AND LAST NAME {message.from_user.first_name} {message.from_user.last_name}""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )   
  

ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "https://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]

@Client.on_message(filters.command(["botinfo"]))
async def botinfo(client, message):
  buttons = [[
        InlineKeyboardButton('back⏪', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('about', callback_data='about')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""hello bro/sis this is the bot information""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )   

ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "https://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]

@Client.on_message(filters.command(["about"]))
async def about(client, message):
  buttons = [[
        InlineKeyboardButton('back⏪', callback_data='botinfo'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('devoleper', url='http://telegram.me/devourdevils'),
        InlineKeyboardButton('deploy own', url='https://heroku.com/deploy?template=https://github.com/kamarjahan/TELEGRAPH-MAKER')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""
MY NAME:TELEGRAPH BOT
CREATOR:@DEVOURDEVILS
LIBRARY:PYROGRAM
LANGUAGE:PYTHON 3
DATABASE:MONGO DB
        :redislabs
BOT SERVER:HEROKU
BUILD STATUS:V2.0.0 [edit]""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id,
      )   



ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/3b150ca1e1fa3998f4479.jpg",
 "https://telegra.ph/file/5418df1528c0c466c8cda.jpg",
 "https://telegra.ph/file/9682513b3a019f58e4f4d.jpg",
 "https://telegra.ph/file/eebd8bf520218f0fe53e8.jpg",
 "https://telegra.ph/file/1721beb890958fea346ba.jpg",
 "https://telegra.ph/file/a36eb74ffd8357b1e4cd8.jpg",
 "https://telegra.ph/file/7fd76e2190cfde57e4739.jpg",
 "https://telegra.ph/file/9f0334896310bb22bdcb1.jpg",
 "https://telegra.ph/file/3b274bc5398df81dcd820.jpg",
 "https://telegra.ph/file/66af3aff75335ebdfe049.jpg",
 "https://telegra.ph/file/02763d802fcaa64aa2d27.jpg",
 "https://telegra.ph/file/e15f827c3e06982023ac7.jpg"
]

@Client.on_message(filters.command(["status"]))
async def status(client, message):
  buttons = [[
        InlineKeyboardButton('home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('back', callback_data='cmd'),
        InlineKeyboardButton('botinfo', callback_data='botinfo')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""
TOTAL TIME:500H
TIME SPENT:96H
TIME LEFT.:404H(THEN IDLING)
BOT STATUS:ACTIVE SINCE 96H
TOTAL USER:4529
TOTAL CHAT:567
BANNEDUSER:56
GLOBAL BAN:8
BOT BANNED:12
BOT ADMINS:452
   (IDLING)""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
      )   
