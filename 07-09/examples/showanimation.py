# Демо-програма з кнопкою анімації

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation

class AnimatedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        start_color = self.background_color
        start_size_h = self.size_hint
        start_pos_hint = self.pos_hint
        start_font_size = self.font_size

        animate = Animation(background_color=(0, 0, 1, 1), duration=1.5)
        animate = animate + Animation(size_hint=(1, 1))
        animate = animate + Animation(font_size=35)
        animate = animate + Animation(size_hint=(.5, .5), font_size=14, background_color=(1, 1, 0, 1), duration=1.5)
        animate = animate + Animation(pos_hint={'center_x': 1.1}, background_color=(0, 1, 1, 1))
        animate = animate + Animation(pos_hint={'center_x': 0.1}, background_color=(0, 0, 1, 1), duration=0.5)
        back = Animation(background_color=start_color, size_hint=start_size_h, pos_hint=start_pos_hint, font_size=start_font_size )

        self.animate = animate + back

    def start_animation(self):
        self.animate.start(self)

class MyApp(App):
    def build(self):
        txt = Label(text='Це напис')
        btn = AnimatedButton(text='Натисни мене.', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5}, font_size = 22)
        btn.on_press = btn.start_animation 
                                     
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout

MyApp().run() 