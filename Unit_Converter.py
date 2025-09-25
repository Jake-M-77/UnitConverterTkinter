from tkinter import *


def updateButton():
    button.config(text=f"Convert to {chosenConversionUnit.get()}")


def calculateConversion():
    userChosenUnit = chosenConversionUnit.get()

    try:
        userInput = float(Unit.get())

        if userChosenUnit == "Mph":
            result = userInput * 20
        elif userChosenUnit == "Kmh":
            result = userInput * 10
        elif userChosenUnit == "Celsius":
            result = userInput * 5
        elif userChosenUnit == "Fahrenheit":
            result = userInput * 2

        output.config(text=f"Result: {result}")

    except ValueError:
        output.config(text="Invalid Input!")
        


window = Tk()

chosenConversionUnit = StringVar()

chosenConversionUnit.set("Mph")

title = Label(window, text="Unit Converter", width=30, font="Verdana, 20")
title.pack()

Unit = Entry(window)
Unit.pack()

radio1 = Radiobutton(window, text="Kmh -> Mph", variable=chosenConversionUnit, value="Mph", command=updateButton)
radio2 = Radiobutton(window, text="Mph -> Kmh", variable=chosenConversionUnit, value="Kmh", command=updateButton)
radio3 = Radiobutton(window, text="Fahrenheit -> Celsius", variable=chosenConversionUnit, value="Celsius", command=updateButton)
radio4 = Radiobutton(window, text="Celsius -> Fahrenheit", variable=chosenConversionUnit, value="Fahrenheit", command=updateButton)



radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()

button = Button(window, text=f"Convert To {chosenConversionUnit.get()}", command=calculateConversion)
button.pack()

output = Label(window)
output.pack()



window.mainloop()