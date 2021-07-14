from HandshakeHandlers import handler
from HandshakeType import HandshakeType
from slice import slice


class HandShake:
    """
    https://datatracker.ietf.org/doc/html/rfc8446#page-124

    struct {
          HandshakeType msg_type;    /* handshake type */
          uint24 length;             /* bytes in message */
          select (Handshake.msg_type) {
              case client_hello:          ClientHello;
              case server_hello:          ServerHello;
              case end_of_early_data:     EndOfEarlyData;
              case encrypted_extensions:  EncryptedExtensions;
              case certificate_request:   CertificateRequest;
              case certificate:           Certificate;
              case certificate_verify:    CertificateVerify;
              case finished:              Finished;
              case new_session_ticket:    NewSessionTicket;
              case key_update:            KeyUpdate;
          };
      } Handshake;

    """

    def __init__(self, data):
        msg_type, data = slice(data, 1)
        self.msg_type = int(msg_type.hex(), 16)

        length, data = slice(data, 3)
        self.length = int(length.hex(), 16)

        print('\nHandshake: ')
        print(f' Handshake Type: {self.msg_type}')
        print(f' Length: {self.length}')

        handshake_type = HandshakeType(self.msg_type)
        handler.get(handshake_type)(data)
