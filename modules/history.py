from datetime import datetime, timedelta

class JubJubModule():

    def __init__(self, bot):
        self.bot = bot
        # handle configuration
        self.history = self.bot.database['history']
        if self.history == None:
            self.history = dict()
            self.bot.database['history'] = self.history

    def on_chan_join(self, channel):
        # check if a history log exists for this channel
        if channel not in self.history:
            self.history[channel] = []

    def on_message(self, username, channel, msg):
        # Store message in history
        new = HistoryEntry(datetime.now(), username, msg)
        tosort = False
        if len(self.history[channel]) > 0 and self.history[channel][-1] > new:
            tosort = True

        self.history[channel].append(new)
        if tosort:
            self.history[channel].sort()
        self.bot.database.save()

        if msg.startswith('!historyget'):
            # get history for this channel
            # send private messages to user with history contents
            pass

class HistoryEntry():

    def __init__(self, time, username, msg):
        self.time = time
        self.username = username
        self.msg = msg

    def __cmp__(self, other):
        if self.time < other.time:
            return -1
        elif self.time > other.time:
            return 1
        return 0
