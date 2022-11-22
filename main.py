from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from fileshare import FileSharer
import time

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        """Starts camera and change Button text"""
        self.ids.camera.play = True
        self.ids.start.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera.texture

    def stop(self):
        """Stops camera and change Button text"""
        self.ids.camera.play = False
        self.ids.start.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        """Create a file name with the current time
        stamp and save an image under that filename"""
        time_stamp = time.strftime("%Y%m%d-%H%M%S")
        filepath = f'files/{time_stamp}.png'
        self.ids.camera.export_to_png(filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = filepath


class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()


