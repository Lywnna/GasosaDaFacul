from base64 import b16decode
import matplotlib.pyplot as plt
import os

class Util():
    @staticmethod
    def Separator(b, char = "=-=", step = 20):
        s = "\n" + char * step + "\n"
        if not b:
            print(s)
        return s


    @staticmethod
    def Graph(xinfo, yinfo, xtext, ytext, title):
        plt.plot(xinfo, yinfo)

        plt.xlabel(xtext)
        plt.ylabel(ytext)
        plt.title(title)
        plt.show()

    @staticmethod
    def Clear():
        os.system("cls")
