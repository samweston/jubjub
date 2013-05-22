
class JubJubModule():

    def __init__(self, bot):
        print 'Template init()'
        self.bot = bot
        # handle configuration

    def on_connect(self):
        print 'Template on_connect()'

    def on_chan_join(self, channel):
        print 'Template on_chan_join()'

    def on_message(self, username, channel, msg):
        print 'Template on_message()'

    def on_directed_message(self, username, target, channel, msg):
        print 'Template on_directed_message()'

    def on_user_join(self, username, channel):
        print 'Template on_user_join()'

    def on_user_leave(self, username, channel):
        print 'Template on_user_leave()'
