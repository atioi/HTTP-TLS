import enum
import struct

from Handshake import HandShake
from slice import slice


class ContentType(enum.Enum):
    """
    https://datatracker.ietf.org/doc/html/rfc8446#page-79

    enum {
          invalid(0),
          change_cipher_spec(20),
          alert(21),
          handshake(22),
          application_data(23),
          (255)
      } ContentType;
    """
    INVALID = 0
    CHANGE_CIPHER_SPEC = 20
    ALERT = 21
    HANDSHAKE = 22
    APPLICATION_DATA = 23


class TLSPlainText:
    """
    https://datatracker.ietf.org/doc/html/rfc8446#page-79

    struct {
        ContentType type; // 1 byte (max. number 255)
        ProtocolVersion legacy_record_version; //uint16
        uint16 length;  //  uint8 uint16[2];
        opaque fragment[TLSPlaintext.length];
    } TLSPlaintext;

    """

    def __init__(self, data):
        tls_text, data = slice(data, 5)
        self.content_type, self.major, self.minor, self.length = struct.unpack('>BBBH', tls_text)
        self.protocol_version = (self.major, self.minor)
        self.fragment, _ = slice(data, self.length)

        print('TLSPlaintext: ')
        print(f' Content Type: {self.content_type}')
        print(f' Protocol Version: {self.major}.{self.minor}')
        print(f' Length: {self.length}')
        print(f' Fragment: {self.fragment}')

        self.handle(self.fragment)

    def handle(self, data):
        if self.content_type == ContentType.HANDSHAKE.value:
            HandShake(data)
