import sopel.module

@sopel.module.rule('retard!?')
def retard(bot, trigger):
    bot.say('Thats not something nice to say, eh? ' + trigger.nick)


@sopel.module.rule('[buggybot][,. ][Aa]re you buggy?')
def am_i_buggy(bot, trigger):
   bot.say('Umm, let me check my name.. ' + trigger.nick)
    


#@sopel.module.rule('
