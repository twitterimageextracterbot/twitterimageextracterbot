import twint
import nest_asyncio
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
  
    update.message.reply_text("Hello there!!\n\nSend me the Twitter Username wihtout '@', for more details press /help.\n\n Let's see what I Get...🙃")


def help(update, context):
    
    update.message.reply_text('Reply me with any Twitter Username to get the Recent Pictures of that account.\n\nExample: To get the recent pictures of Justin Bieber,\n just send me the username as "justinbieber" (without quotes).')

def echo(update, context):   
    update.message.reply_text("Searching... ")

    c = twint.Config()
    c.Images=True
    c.Username = str(update.message.text)
    c.Since = '2021-01-01'
    c.Store_object = True
    c.Pandas =True
    twint.run.Search(c)
    nest_asyncio.apply()
    try:
      for x in twint.storage.panda.Tweets_df["id"].index:
          print (twint.storage.panda.Tweets_df["thumbnail"][x])
          update.message.reply_text(twint.storage.panda.Tweets_df["thumbnail"][x])
      update.message.reply_text("Sent all images with that username")
    except:
      update.message.reply_text("No Images found for that username, try different usernames")




def main():
    """Start the bot."""
    updater = Updater("1543057258:AAFwMKDP8akrRp9x0P8emNO9D25RZo1kO9Y", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    
    dp.add_handler(CommandHandler("help", help))
    
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()
    
    updater.idle()


if __name__ == '__main__':
    main()