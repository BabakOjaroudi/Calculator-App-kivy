import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
    def calculation(self, event):
        if event:
            try:
                self.display.text = str(eval(event))
            except:
                self.display.text = 'Error'

class CalculatorApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    CalculatorApp().run()
