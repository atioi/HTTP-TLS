class Extension:
    """
    https://datatracker.ietf.org/doc/html/rfc8446#page-35
    struct {
        ExtensionType extension_type;
        opaque extension_data<0..2^16-1>;
    } Extension;
    """

    def __init__(self, extension_type, extension_data):
        self.extension_type = extension_type
        self.extension_data = extension_data
