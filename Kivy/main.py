from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout


class Clase_Base(App):
  def build(self):
    bl = BoxLayout(orientation= "horizontal")
    def texto(instancia, valor):
      print("Mi primer boton en Kivy")

    l = Label(text = "Presiona \n el botón.", font_size=70)
    bt = Button(text = "¡Mensaje!", pos=(300,350), size_hint=(0.30,0.20))
    bt.bind(state = texto)
    slide = Slider(orientation="vertical",min = -10, max =5, value_track="True", value_track_color = (0.5,0.5,1))
    bl.add_widget(slide)
    bl.add_widget(bt)
    bl.add_widget(l)
    return bl

if __name__ == "__main__":
  Clase_Base().run()

