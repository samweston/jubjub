from twisted.internet import reactor

class JubJubModule():

    # giveops

    check_time = 5 #seconds

    def __init__(self, bot):
        self.bot = bot

        self.ops = self.bot.database['ops']
        if self.ops == None:
            self.ops = []
            self.bot.database['ops'] = self.ops

        #TODO giveops config, (store ops, start ops)

    def cmd_op(self, username, channel):
        self.bot.mode(channel, '+', 'o', user=username)

    def check_user(self, user, channel):
        if user.username in self.ops and not user.is_op:
            self.cmd_op(user.username, channel)

    def check_users(self, channel):
        for user in self.bot.get_users(channel):
            self.check_user(user, channel)
        reactor.callLater(self.check_time, self.check_users, channel)

    def on_chan_join(self, channel):
        reactor.callLater(self.check_time, self.check_users, channel)

    def on_message(self, username, channel, msg):
        if msg.startswith('!adduser ') and len(msg.split(' ')) > 1:
            self.cmd_op(msg.split(' ')[1], channel)
            self.bot.database.save()

    def on_user_join(self, username, channel):
        if username in self.ops and username[0] != '@':
            self.cmd_op(username, channel)
