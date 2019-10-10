from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_NUMBER = 1.60934


class MilesToKilometres(App):
    output_kilometres = StringProperty()


    def build(self):
        self.title = "Convert miles to kilometers"
        self.root = Builder.load_file('miles_to_kilometers.kv')
        return self.root

    def handle_conversion(self, miles_input):
        try:
            miles = int(miles_input)
        except ValueError:
            miles = 0
        self.output_kilometres = str(miles * CONVERSION_NUMBER)

    def handle_increment(self, miles_input, increment):
        print("handling")
        miles = int(miles_input) + increment
        self.root.ids.input_miles.text = str(miles)


MilesToKilometres().run()
