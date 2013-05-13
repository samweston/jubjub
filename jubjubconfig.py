import ConfigParser
import os

def read_config():
    filenames = ['/etc/jubjub.cfg',
            os.path.expanduser('~/.jubjub.cfg'),
            'jubjub.cfg']

    config = ConfigParser.SafeConfigParser()

    config.add_section("irc")
    config.set("irc","nickname","jubjub")
    config.set("irc","username","jubjub")
    config.set("irc","host","localhost")
    config.set("irc","port","6667")
    config.set("irc","chan","#teabreakbot")

    config.add_section("log")
    config.set("log", "enabled","false")
    config.set("log", "path", "~/.jubjub.log")

    config.add_section("database")
    config.set("database", "path", "db/.db")

    config.add_section("misc")
    config.set("misc","teabreaklength","600")

    config.read(filenames)

    return config

# vim: set smartindent shiftwidth=4 tabstop=4 softtabstop=4 expandtab :
