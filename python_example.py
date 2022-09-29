import enum
import sys
import re

from ciscoconfparse import IPv4Obj
from traitlets import Undefined, CInt, Unicode, TCPAddress, CRegExp
from traitlets import HasTraits, UseEnum
from loguru import logger

class BoatPower(enum.Enum):
    """
    Define discrete choices for BoatPower().  The choices will be stored in
    this enum.Enum
    """
    unknown = 0
    rowing = 1
    sail = 2
    unleaded = 3
    diesel = 4

class Boat(HasTraits):
    """
    TODO - find a way to use ciscoconfparse.ccp_util.IPv4Obj() with the IP addr
    """
    power = UseEnum(BoatPower, default_value=BoatPower.rowing)
    tcp_socket = TCPAddress()
    # FIXME find a way to cast a Boat() attribute as IPv4Obj()
    #addr = IPv4Obj()

    @logger.catch(default=True, onerror=lambda _: sys.exit(1))
    def __repr__(self):
        return "<Boat power={}, tcp={}>".format(self.power, self.tcp_socket,)


@logger.catch(default=True, onerror=lambda _: sys.exit(1))
def main(power=None,):
    my_boat = Boat()
    # .power is automatically cast into a BoatPower() attribute
    my_boat.power = "unknown"
    # .tcp_socket is automatically cast into a TCPAddress() attribute
    my_boat.tcp_socket = ("172.16.1.5/24", 443)
    my_boat.addr = "172.16.1.5/24"
    my_boat.addr = "FIXME"

    print(my_boat)
    print(my_boat.tcp_socket)
    # my_boat.addr does NOT correctly enforce IPv4Obj() as the .addr type...
    print(my_boat.addr)

if __name__=="__main__":
    main()
