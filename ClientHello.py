from slice import slice


class ClientHello:
    """
    https://datatracker.ietf.org/doc/html/rfc8446#page-27

    struct {
        ProtocolVersion legacy_version = 0x0303;    /* TLS v1.2 */
        Random random;
        opaque legacy_session_id<0..32>;
        CipherSuite cipher_suites<2..2^16-2>;
        opaque legacy_compression_methods<1..2^8-1>;
        Extension extensions<8..2^16-1>;
    } ClientHello;
    """

    def __init__(self, data):
        self.protocol_version, data = slice(data, 2)

        random, data = slice(data, 32)
        self.random = random.hex()

        length, data = slice(data, 1)
        length = int(length.hex(), 16)

        legacy_session_id, data = slice(data, length)
        self.legacy_session_id = legacy_session_id.hex()

        length, data = slice(data, 2)
        length = int(length.hex(), 16)

        cipher_suites, data = slice(data, length)
        self.cipher_suites = [cipher_suites[start:start + 2].hex() for start in range(0, len(cipher_suites), 2)]

        length, data = slice(data, 1)
        length = int(length.hex(), 16)

        legacy_compression_methods, data = slice(data, length)
        self.legacy_compression_methods = [legacy_compression_methods[start:start + 1].hex() for start in
                                           range(0, len(legacy_compression_methods), 1)]

        length, data = slice(data, 2)
        length = int(length.hex(), 16)

        self.extensions, data = slice(data, length)

        print('\nClientHello: ')
        print(f' Protocol Version = {self.protocol_version[0]}.{self.protocol_version[1]}')
        print(f' Random = {self.random}')
        print(f' Legacy Session ID: {self.legacy_session_id}')
        print(f' Cipher Suites: {self.cipher_suites}')
        print(f' Legacy Compression Methods: {self.legacy_compression_methods}')
        print(f' Extensions: {self.extensions}')

        # ***************
        print(self.extensions)
        type, data = slice(self.extensions, 1)
        print(int(type.hex(), 16))
        # length = length.hex()
        # print(length)
        # ***************
