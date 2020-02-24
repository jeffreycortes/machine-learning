import matplotlib.pyplot as plt
from src.shared.domain.utils.img.img_manager import ImageManager

class LineChart:
    plt = None

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.xdata = 0
        self.ydata = 0
        self.plt = plt

    def plot_default(self):
        self.plt.plot(self.x, self.ydata,  'bo')
        self.plt.plot(self.x, self.y, 'r')

    def set_labels(self, xlabel, ylabel):
        self.plt.xlabel(xlabel)
        self.plt.ylabel(ylabel)

    def print_to_imgb64(self):
        imgManager = ImageManager()
        plt.savefig(imgManager.get_img_buffer(), format='png')
        return imgManager.get_img_in_base64()

    def show(self):
        self.plt.show()
