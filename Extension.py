from ExtensionType import ExtensionType


class Extension:
    """
    https://datatracker.ietf.org/doc/html/rfc8446#page-35
    struct {
        ExtensionType extension_type;
        opaque extension_data<0..2^16-1>;
    } Extension;
    """

    def __init__(self, ext_type):
        self.extension_type = ext_type


def check_extension_type(ext_type):
    try:
        ExtensionType(ext_type)
    except ValueError as exception:
        return -1
    return type


def add_extension(ext_type):
    if check_extension_type(ext_type):
        print('Ignore')
