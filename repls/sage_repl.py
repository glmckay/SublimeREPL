import re
from . import subprocess_repl

class SageRepl(subprocess_repl.SubprocessRepl):
    TYPE = "sage"

    def __init__(self, encoding, **kwds):
        self.prompt_re = re.compile(b'^In \[\d+\]: $')
        super(SageRepl, self).__init__(encoding, **kwds)

    def read_bytes(self):
        bytes = super(SageRepl, self).read_bytes()
        # Output from subprocess is read one byte at a time,
        # this won't work on windows
        if self.prompt_re.match(bytes) is not None:
            bytes = b"sage: "
        return bytes
