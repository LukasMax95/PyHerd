from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("main.kv")


def runapp():
    Myapp().run()

class Myapp(App):
    def build(self):
        return GUI

runapp()