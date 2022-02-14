#!c:\users\arpishkinmi\desktop\utz\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'flask==1.1.2','console_scripts','flask'
__requires__ = 'flask==1.1.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('flask==1.1.2', 'console_scripts', 'flask')()
    )
