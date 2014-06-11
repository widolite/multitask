__author__ = 'Hector Guerrero'

from urllib2 import *
from telnetlib import Telnet


class CustomURLError(URLError):
    pass


class RelayNumberError(Exception):
    pass


class BoardConnectionError(Exception):
    pass


class RelayLib(object):
    relays = frozenset((1, 2, 3, 4, 5, 6, 7))

    def __init__(self, ip='192.168.1.199', username='admin', password='admin', port=80):

        try:
            self._ip = ip
            self._port = port
            self.board_alive()
            self._url = 'http://%s/' % ip
            self._username = username
            self._password = password
            # Support for Basic HTTP Authentication...
            auth_handler = HTTPBasicAuthHandler()
            auth_handler.add_password(realm='Protected',
                                      uri=self._url,
                                      user=username,
                                      passwd=password)
            opener = build_opener(auth_handler)
            install_opener(opener)
            urlopen(self._url)
        except URLError as u:
            raise CustomURLError("Authentication failed. Server responded with --> %s" % u)
        except BoardConnectionError:
            raise BoardConnectionError("The connection with the board is lost")

    def board_alive(self):
        """
        This method verify the connection network with the relay board through
        Telnet to the port that the board is listen.
        """
        try:
            telnet = Telnet(self._ip, self._port, 1)
            telnet.close()
        except:
            raise BoardConnectionError("The connection with the board is lost")

    @property
    def status(self):
        """This method return the current status of the relays in a list."""
        self.board_alive()
        resource = urlopen(self._url + "relays.cgi")
        line = ''
        while True:
            line = resource.readline()
            if line.startswith("Status"):
                break
        status = line.split()
        status.pop(0)
        status = [int(x) for x in status]
        return status

    def toggle(self, rel_num):
        """
        This method toggle the relay the user is responsible of know the status of
        the relays with the 'status' method
        """
        try:
            rel_num = int(rel_num)
            if rel_num not in RelayLib.relays:
                raise RelayNumberError("The relay number had to be between 1 and 8. You enter: %s" % rel_num)
            urlopen(self._url + "relays.cgi?relay=%s" % rel_num)
        except URLError as u:
            raise CustomURLError("Authentication failed. Server responded with --> %s" % u)
        except ValueError:
            raise ValueError("The value had to be a integer")


def main():
    relay = RelayLib()
    print relay.status
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(8)
    relay.toggle(4)
    relay.toggle(5)
    relay.toggle(6)
    relay.toggle(8)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(8)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(8)
    relay.toggle(4)
    relay.toggle(5)
    relay.toggle(6)
    relay.toggle(8)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(8)
    relay.toggle(4)
    relay.toggle(5)
    relay.toggle(6)
    relay.toggle(8)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(8)
    relay.toggle(4)
    relay.toggle(5)
    relay.toggle(6)
    relay.toggle(8)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
    relay.toggle(1)
    relay.toggle(2)
    relay.toggle(3)
    relay.toggle(4)
if __name__ == '__main__':
    main()