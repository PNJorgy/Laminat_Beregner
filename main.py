#from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class MenuScreen(Screen):
    pass

class LaminatBeregner(Screen):
    pass
    # Denne skal i kv filen
    #velg_enhet: VE
    #lengde_rom: LR
    #lengde_laminat: LL
    #bredde_rom: BR
    #bredde_laminat: BL
    #
    #Disse skal ligge her
    #velg_enhet = ObjectProperty(None)
    #lengde_rom = ObjectProperty(None)
    #lengde_laminat = ObjectProperty(None)
    #bredde_rom = ObjectProperty(None)
    #bredde_laminat = ObjectProperty(None)

class WindowManager(ScreenManager):
    pass



class Laminat_BeregnerApp(MDApp):
     def build(self):
        self.title = "EmberFiles - Laminat Beregner"
        self.icon = 'icon/EmberFiles_Icon.png'
        self.theme_cls.theme_style = 'Dark'
        Builder.load_file('laminat_Beregner.kv')
        return WindowManager()

if __name__ == "__main__":
    Laminat_BeregnerApp().run()