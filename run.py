from layer import RelayLayer
from credentials import CREDENTIALS

from yowsup.stacks import YowStackBuilder
from yowsup.layers.auth import AuthError
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from yowsup.env import YowsupEnv


if __name__==  "__main__":
    stackBuilder = YowStackBuilder()

    stack = stackBuilder\
        .pushDefaultLayers(True)\
        .push(RelayLayer)\
        .build()

    stack.setCredentials(CREDENTIALS) 

    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal

    
    stack.loop() #this is the program mainloop
    
