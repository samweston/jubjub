
class JubJubModule():

    def __init__(self, bot):
        print 'Template init()'
        self.bot = bot

    def pre_load_config(self, bot):
        print 'Template pre_load_config()'

    def post_load_config(self, bot):
        print 'Template post_load_config()'

    def on_connect(self):
        print 'Template on_connect()'

    def on_message(self, user, channel, msg):
        print 'Template on_message()'

    def on_directed_message(self, user, channel, msg):
        print 'Template on_directed_message()'

    def on_user_join(self, user, channel):
        print 'Template on_user_join()'

    def on_user_leave(self, user, channel):
        print 'Template on_user_leave()'
