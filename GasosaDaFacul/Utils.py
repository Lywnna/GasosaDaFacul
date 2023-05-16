import matplotlib.pyplot as plt

class Util():
    @staticmethod
    def Separator(char = "=-=", step = 20):
        print("\n" + char * step + "\n")


    @staticmethod
    def Graph(xinfo, yinfo, xtext, ytext, title):
        plt.plot(xinfo, yinfo)

        plt.xlabel(xtext)
        plt.ylabel(ytext)
        plt.title(title)
        plt.show()


