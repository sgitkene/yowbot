from yowsup.layers.interface                          import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.protocol_acks.protocolentities     import *
from yowsup.layers.protocol_presence                  import YowPresenceProtocolLayer
from yowsup.layers.protocol_media                     import YowMediaProtocolLayer
from yowsup.layers.protocol_receipts                  import YowReceiptProtocolLayer
from yowsup.layers.protocol_groups                    import YowGroupsProtocolLayer
from yowsup.layers.protocol_ib                        import YowIbProtocolLayer
from yowsup.layers.protocol_notifications             import YowNotificationsProtocolLayer
from yowsup.layers.protocol_iq                        import YowIqProtocolLayer
from yowsup.layers.protocol_contacts                  import YowContactsIqProtocolLayer
from yowsup.layers.protocol_chatstate                 import YowChatstateProtocolLayer
from yowsup.layers.protocol_privacy                   import YowPrivacyProtocolLayer
from yowsup.layers.protocol_profiles                  import YowProfilesProtocolLayer

from pytg.receiver import Receiver
from pytg.utils import coroutine

import threading

class RelayLayer(YowInterfaceLayer):
    def __init__(self):
        super(RelayLayer, self).__init__()
        self.receiver = Receiver (host="localhost", port=4458)
        self.QUIT = False
        self.receiver.start()
        self.rcv = threading.Thread(target = self.startReceiver)
        self.rcv.daemon = True

    def startReceiver(self):
        self.receiver.message(self.main_loop())

    @ProtocolEntityCallback("success")  # we get this at the start of yowsup, only once.
    def onSuccess(self, ProtocolEntity):
        self.rcv.start()

    @coroutine
    def main_loop(self):
        while True:
            msg = (yield)
            if msg.event != "message":     #not a message
                continue         
            if msg.own:                    #message from us
                continue
            if msg.text == None:           #message not text
                continue
            outgoingMessageProtocolEntity = TextMessageProtocolEntity(    #currently broken, will crash on emoji and other symbols.
                msg.text, to = msg.peer.name + "@s.whatsapp.net")
            self.toLower(outgoingMessageProtocolEntity)
        
