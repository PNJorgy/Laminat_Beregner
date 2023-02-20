from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyW(Widget):
    velg_enhet = ObjectProperty(None)
    lengde_rom = ObjectProperty(None)
    lengde_laminat = ObjectProperty(None)
    bredde_rom = ObjectProperty(None)
    bredde_laminat = ObjectProperty(None)


    def spinner_clicked(self, value):
        self.ids.VE.text = value

    def btn(self):
        print("Beregner....")


class Laminat_BeregnerApp(App):
     def build(self):
        return MyW()

if __name__ == "__main__":
    Laminat_BeregnerApp().run()