from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


GUI = Builder.load_file("main0.kv")

class Myapp(App):
    def build(self):
        self.root = Builder.load_file("main0.kv")
        self.root.transition = FadeTransition()
        self.ba1 = self.root.get_screen("first").ids["ba1"]
        self.bb1 = self.root.get_screen("second").ids["bb1"]
        self.ba1.bind(on_release = self.ba1_on_release)
        self.bb1.bind(on_release = self.bb1_on_release)
        return self.root

    def ba1_on_release(self, instance):
        if instance.text == "Send MSG":
            self.root.current = "second"
            self.root.transition.direction = "left"
    

    def bb1_on_release (self, instance):
        if instance.text == "Back":
            self.root.current = "first"
            self.root.transition.direction = "right"


    def on_start(self):
        pass

def runapp():
    Myapp().run()

runapp()