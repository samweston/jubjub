import requests
import xml.etree.ElementTree as ET
import datetime
import pytz
import time

# time module, uses google maps apis (geocode and timezone)
# to convert a string into a local time.

class JubJubModule():

    def __init__(self, bot):
        self.bot = bot

    def on_message(self, username, channel, msg):
        args = msg.split(' ')
        if len(args) > 0 and args[0] == '!timeat':
            location = msg[len(args[0])+1:]
            try:
                r1 = requests.get('http://maps.googleapis.com/maps/api/geocode/xml?address=' + location + '&sensor=false')
                xml = ET.fromstring(r1.text.encode('utf-8').strip())
                if xml.find('status').text == 'OK':
                    xml = xml.find('result')
                    actual_location = xml.find('formatted_address').text
                    coord = xml.find('geometry').find('location')
                    r2 = requests.get('https://maps.googleapis.com/maps/api/timezone/xml?location=' + coord[0].text + ',' + coord[1].text + '&timestamp=1331161200&sensor=false')
                    timezone = ET.fromstring(r2.text.encode('utf-8').strip()).find('time_zone_id').text
                    the_time = pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(timezone))
                    self.bot.say(channel, 'The time in ' + actual_location + ' is ' + the_time.strftime('%X %Z on %b %d, %Y'))
                else:
                    self.bot.say(channel, 'Sorry could not process that request')
            except Exception as e:
                #something bad happened
                print 'Exception in time: ', e



class TimeTest():

    def __init__(self):
        self.module = JubJubModule(self)
        self.cmd = '!timeat japan'
        self.module.on_message('user', 'channel', self.cmd)

    def say(self, channel, msg):
        print 'command: ' + self.cmd
        print 'bot says: ' + msg


def main():
    TimeTest()

if  __name__ =='__main__':main()
