# bot.py

import os
import discord
import re
from dotenv import load_dotenv
from datetime import datetime
import random
import encryptdecrypt


#Default replies
sorry_reply = ["That\'s OK.", "It happens.", "No problem.", "Don\'t worry about it.", "I forgive you."]
condition = ["I\'m good.", "I\'m fine.", "Pretty good.", "I\'m well.", "I\'m OK.", "Not too bad.", "Just the same old same old.", "Yeah, all right."]
#


#help msg
help_msg = '''
General Commands:                   
-hi/-hello/-bye/-ciao                       Greeting
-how are you                                Ask bot's mood
+<any_number> <text(optional)>              Ask bot to print (the given number/ text) from 1 to the given number
-time                                       Ask bot the current time

Encryption/Decrytion
-encrypt <your_text>                        Encrypts your text
-decrypt <your_text>                        Decrypts your text
$hutdown
'''
#


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')




client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is connected to the following server:\n')
    for guild in client.guilds:
        print(f'{guild.name}(id: {guild.id})')

    #await client.get_channel(your_channel_id).send(msge + '@here')



@client.event
async def on_message(message):

    if message.author == client.user:       #if the author of the message is the bot itself, then it doesnot take commands
        return    
    
    now = datetime.now()
    time = now.strftime('%H:%M:%S')
    hour = int(now.strftime('%H'))
    if hour < 12:
        msge = "Ohayo! "
    elif hour >= 12:
        msge = "Konnichiwa! "

    msg = message.content.lower().startswith
    author = (str(message.author)).split('#')[0]    #the name of author without ID

    #help
    if msg('-help'):
        await message.channel.send(help_msg)
    #help end

    if message.content == '-scissor' or message.content == '-paper' or message.content == '-rock':
        await message.channel.send(scissorpaperrock.style())

    #Greetings and messages
    if msg('-hello') or msg('-hi'):
        await message.channel.send('Hello, {0}'.format(author))
    
    if msg('-ciao'):
        await message.channel.send(msge + author +  "-san , Eliya-desu~!")
    
    if msg('-bye'):
        await message.channel.send('Bye, {0}'.format(author))
    
    if message.content.startswith('+'):         #repetition of number
        try:
            st = str(message.content)
            st = st.replace('+','')
            n_split = st.split()
            if len(n_split) > 1:
                if n_split[0].isdigit():
                    for i in range(1,int(n_split[0]) + 1):
                        mes = " ".join(n_split[1:])
                        await message.channel.send(mes)
            elif len(n_split) == 1:
                for i in range(1,int(n_split[0]) + 1):
                    await message.channel.send(i)
        except ValueError:
            print('Alphabets used with +')

    if 'fuck' in message.content.lower():
        await message.channel.send("Fuck you too. Don\'t use such words here.")
    
    if 'sorry' in message.content.lower():
        await message.channel.send(random.choice(sorry_reply))

    if 'how are you' in message.content.lower():
        await message.channel.send(random.choice(condition))

    if message.content.startswith('$hutdown'):
        print('\n\nShutdown time: ' + str(time) + '\n\n')
        await message.channel.send("Sayounara, @here")
        await client.close()
    #End of Greetings and Messages


    #Encrypt Decrypt
    if msg('-encrypt'):
        encrypt_st = str(message.content.lower())
        encrypt_str = encrypt_st.replace("-encrypt ", '')
        encrypted_msg = author + ": " + encryptdecrypt.encryptor(encrypt_str)
        await message.delete()
        await message.channel.send(encrypted_msg)

    if msg('-decrypt'):
        decrypt_st = str(message.content.lower())
        decrypt_str = decrypt_st.replace("-decrypt ",'')
        decrypted_msg = author + ": " + encryptdecrypt.decryptor(decrypt_str)
        await message.delete()
        await message.channel.send(decrypted_msg)
    #ED

    if msg('-time'):
        await message.channel.send(time)





client.run(TOKEN)
