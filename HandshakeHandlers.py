import ClientHello
from HandshakeType import HandshakeType

handler = {
    HandshakeType.client_hello: ClientHello.ClientHello
}
