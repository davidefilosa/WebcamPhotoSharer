from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from fileshare import FileSharer
from kivy.core.clipboard import Clipboard
import time
import webbrowser

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
        self.filepath = f'files/{time_stamp}.png'
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):

    link_message = 'Please create a link first'
    def create_link(self):
        """Creates a sharable link"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(file_path)
        self.link = filesharer.share()
        self.ids.link.text = self.link

    def copy_link(self):
        """Copies link in the clipboard"""
        try:
            Clipboard.copy(self.link)
        except AttributeError:
            self.ids.link.text = self.link_message

    def open_link(self):
        """Opens link in the browser"""
        try:
            webbrowser.open(self.link)
        except AttributeError:
            self.ids.link.text = self.link_message






class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()


