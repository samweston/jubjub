import time

class JubJubModule():

    # status module !statusset, !statusget, !statusrm

    def __init__(self, bot):
        self.bot = bot
        self.status = self.bot.database['status']
        if self.status == None:
            self.status = dict()
            self.bot.database['status'] = self.status

    def on_message(self, username, channel, msg):
        username = username.split('!')[0]
        spl = msg.split(' ')
        if msg.startswith('!statusset'):
            #set status of 'username'
            status = msg[len(spl[0])+1:]
            self.status[username] = status
            self.bot.database.save()
            self.bot.say(channel, username + ' set status to ' + status)
        elif msg.startswith('!statusget'):
            #if no argument, then get all status
            if len(spl) == 1:
                for key, value in self.status.items():
                    self.bot.say(channel, key + ' - ' + value)
            else:
                user = spl[1]
                if user in self.status:
                    status = self.status[user]
                    if status == None:
                        self.bot.say(channel, 'No status set for ' + user)
                    else:
                        self.bot.say(channel, user + ' - ' + status)
        elif msg.startswith('!statusrm'):
            # if no argument, then remove from 'username'
            if len(spl) > 1:
                del(self.status[spl[1]])
            else:
                del(self.status[username])
            self.bot.database.save()

    def on_user_join(self, username, channel):
        username = username.split('!')[0]
        time.sleep(0.5)
        self.bot.say(channel, 'Greetings ' + username + ' the current user statuses are:')
        for key, value in self.status.items():
            self.bot.say(channel, key + ' - ' + value)
