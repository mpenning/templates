import enum
import sys
import re

from ciscoconfparse import IPv4Obj
from traitlets import Instance, Undefined, CInt, Unicode, TCPAddress, CRegExp
from traitlets import HasTraits, UseEnum, TraitType
from loguru import logger

class BoatPower(enum.Enum):
    """
    Define discrete choices for BoatPower().  The choices will be limited to selections using this enum.Enum.
    """
    unknown = 0
    rowing = 1
    sail = 2
    unleaded = 3
    diesel = 4

class Boat(HasTraits):
    # Declare Boat() variable types below...
    power = UseEnum(BoatPower, default_value=BoatPower.rowing)
    tcp_socket = TCPAddress()
    addr = Instance(klass=IPv4Obj)
    name = Unicode()
    length = CInt(22)

    @logger.catch(default=True, onerror=lambda _: sys.exit(1))
    def __repr__(self):
        return "<Boat name={}>".format(self.name)


@logger.catch(default=True, onerror=lambda _: sys.exit(1))
def main(power=None,):
    my_boat = Boat()
    my_boat.name = "Billy-O-Tea"

    # .power is automatically cast into a BoatPower() attribute
    my_boat.power = "unknown"

    # .tcp_socket is automatically cast into a TCPAddress() attribute
    my_boat.tcp_socket = ("172.16.1.5/24", 443)

    my_boat.addr = IPv4Obj("172.16.5.80/23")

    my_boat.length = "22"
    my_boat.length += 5

    print(my_boat)
    print(my_boat.tcp_socket)
    print(my_boat.addr.network)

if __name__=="__main__":
    main()
