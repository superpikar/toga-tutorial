import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack

def sayHello(fahrenheit, celcius):
    print(fahrenheit, "°F is equivalent to", celcius, "°C")

def build(app):
    def calculate(widget):
        try:
            celcius_input.value = (float(fahrenheit_input.value) - 32) * 5 / 9
            # call function outside the scope
            sayHello(fahrenheit_input.value, celcius_input.value)
        except ValueError:
            celcius_input.value = "???"

    celcius_box = toga.Box()
    fahrenheit_box = toga.Box()
    text_box = toga.Box()
    box = toga.Box()

    celcius_input = toga.TextInput(readonly=True)
    fahrenheit_input = toga.TextInput()

    celcius_label = toga.Label("Celcius")
    fahrenheit_label = toga.Label("Fahrenheit")
    text_label = toga.Label("is equivalent to", style=Pack(text_align=RIGHT))

    button = toga.Button("Calculate", on_press=calculate)

    celcius_box.add(celcius_label)
    celcius_box.add(celcius_input)

    fahrenheit_box.add(fahrenheit_label)
    fahrenheit_box.add(fahrenheit_input)

    text_box.add(text_label)

    box.add(fahrenheit_box)
    box.add(text_box)
    box.add(celcius_box)
    box.add(button)

    box.style.update(direction=COLUMN, padding=10)
    button.style.update(padding=15)

    return box


def main():
    return toga.App("Temperature converter", "org.beeware.toga.tutorial", startup=build)

if __name__ == "__main__":
    main().main_loop()