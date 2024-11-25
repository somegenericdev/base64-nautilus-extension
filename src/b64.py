from gi.repository import Nautilus, GObject
import os
import base64
import logging
import xerox


class BaseCopyExtension(GObject.GObject, Nautilus.MenuProvider):

    def __init__(self):
        # uncomment to log stuff to a file
        #logging.basicConfig(filename="/home/debian/pylog",
        #                    filemode='a',
        #                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        #                    datefmt='%H:%M:%S',
        #                    level=logging.DEBUG)
        pass

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='b64Open',
            label='b64',
            tip='Opens '
        )
        logging.info("in get file items before connect")
        item.connect('activate', self._doStuff, files[0])

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='b64OpenBackground',
            label='b64',
            tip='Opens '
        )
        item.connect('activate', self._doStuff, file_)

        return [item]

    def _doStuff(self, menu, filepath):
        try:
            filepath = filepath.get_location().get_path()
            if not os.path.isdir(filepath) and os.path.exists(filepath):
                with open(filepath, 'rb') as f:
                    b64 = base64.b64encode(f.read()).decode('ascii')
                    xerox.copy(b64)
        except Exception as e:
            logging.info(e)
