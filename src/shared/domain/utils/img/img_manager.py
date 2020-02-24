import io
import urllib
import base64

class ImageManager():
    # constructor
    def __init__(self):
        self.__img_buffer = self.__create_buffer()

    # public methods
    def get_img_buffer(self):
        return self.__img_buffer

    def reset_img(self):
        self.__img_buffer = self.__create_buffer()

    def get_img_in_base64(self, url_escape = True):
        self.__rewind_buffer()

        if (url_escape):
            return urllib.parse.quote(self.__encode_img_to_base64())
        else:
            return self.__encode_img_to_base64()

    # private methods
    def __create_buffer(self):
        return io.BytesIO()

    def __rewind_buffer(self):
        self.__img_buffer.seek(0)

    def __encode_img_to_base64(self):
        return base64.b64encode(self.__img_buffer.read()).decode()
