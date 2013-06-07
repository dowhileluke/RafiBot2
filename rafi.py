from IRCBot import *
from Modules.Test import *

rafi = IRCBot()
rafi.attach(Test())
rafi.run()
