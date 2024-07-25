import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, PACK

def build(app):
    celcius_box = toga.Box()
    fahrenheit_box = toga.Box()
    box = toga.Box()

    celcius_input = toga.TextInput(readonly=True)
    fahrenheit_input = toga.TextInput()

    celcius_label = toga.Label("Celcius")
    fahrenheit_label = toga.Label("Fahrenheit")

    celcius_box.add(celcius_label)
    celcius_box.add(celcius_input)

    fahrenheit_box.add(fahrenheit_label)
    fahrenheit_box.add(fahrenheit_input)

    box.add(celcius_box)
    box.add(fahrenheit_box)

    box.style.update(direction=COLUMN, padding=10)

    return box

def main():
    return toga.App("Temperature converter", "org.beeware.toga.tutorial", startup=build)

if __name__ == "__main__":
    main().main_loop()