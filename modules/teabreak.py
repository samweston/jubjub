
class JubJubModule():

    def __init__(self, bot):
        self.bot = bot

    def __human_time_diff(self, seconds):
        """ Convert seconds into human readable time periods """
        if seconds < 0:
            seconds = 0
        timediffstr = ""
        if seconds > 3600:
            timediffstr += str(seconds/3600)+" hour(s) "
            seconds -= (seconds/3600)*3600
        if seconds > 60:
            timediffstr += str(seconds/60)+" minute(s) "
            seconds -= (seconds/60)*60
        if seconds > 0 or timediffstr == "":
            timediffstr += str(seconds)+" second(s)"
        return timediffstr.strip()

    def on_message(self, user, channel, msg):
        """This will get called when the bot receives a message."""
        print user,"PRIVMSG",channel,msg

        user = user.split('!', 1)[0]

        # is the message at us?
        splitmsg = self.message.match(msg.lower())
        if splitmsg:
            splitmsg = splitmsg.group(1).strip()
            if "when" in splitmsg.lower() and "last" in splitmsg.lower():
                if self.lastbreaktime > 0:
                    currenttime = int(time.time())
                    timediffstr = self.__human_time_diff(currenttime - self.lastbreaktime)
                    self.bot.say(channel, "The last break was a "+self.lastbreaktype+", it happened "+timediffstr+" ago at "+datetime.datetime.fromtimestamp(self.lastbreaktime).strftime('%H:%M'))
            elif "break" in splitmsg.lower():
                if "lunch" in splitmsg.lower():
                    breaktype = "lunchbreak"
                elif "beer" in splitmsg.lower():
                    breaktype = "beerbreak"
                else:
                    breaktype = "teabreak"
                if not self.bot.get_users()[channel][user].is_op:
                    print "** "+breaktype.upper()+" DETECTED **",user,"has called a "+breaktype
                    nowbreak = int(time.time())
                    if (nowbreak - self.lastbreaktime) >= self.teabreaklength:
                        self.lastbreaktime = nowbreak
                        self.lastbreaktype = breaktype
                        teabreakcount = 0
                    else:
                        print "** "+breaktype.upper()+" DENIED ** Please wait another "+self.__human_time_diff(self.teabreaklength - (nowbreak - self.lastbreaktime))+" before calling a break"
                        self.say(channel, breaktype+" denied! Please wait another "+self.__human_time_diff(self.teabreaklength - (nowbreak - self.lastbreaktime))+" before calling a break")
                else:
                    print "** UNAUTHORISED USER",user,"ATTEMPTED TO CALL A "+breaktype.upper()+" **"
                    self.bot.say(channel, breaktype+" denied! You need ops to call a break")
