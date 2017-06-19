import sopel.module

@sopel.module.commands('whoru')
def helloworld(bot, trigger):
    bot.say("ya,ya, I am a buggy bot :/ ")

