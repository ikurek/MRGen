import errno
import os
import sys


class PathService:
    ERROR_INVALID_NAME = 123
    path: str

    def __init__(self) -> None:
        if len(sys.argv) > 1 and sys.argv[1] is not None:
            self.path = sys.argv[1]
        else:
            self.path = os.getcwd()

    def is_pathname_valid(self, pathname: str) -> bool:
        try:
            if not isinstance(pathname, str) or not pathname:
                return False

            _, pathname = os.path.splitdrive(pathname)

            root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
                if sys.platform == 'win32' else os.path.sep

            root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

            for pathname_part in pathname.split(os.path.sep):
                try:
                    os.lstat(root_dirname + pathname_part)
                except OSError as exc:
                    if hasattr(exc, 'winerror'):
                        if exc.winerror == self.ERROR_INVALID_NAME:
                            return False
                    elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                        return False
        except TypeError as exc:
            return False
        else:
            return True
