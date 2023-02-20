from PDFmodule import PDF
from MathExcerciseForFun import MathExcerciseRandomizer
from Exit import ExitEscape
import os

def main():
    instancePDF = PDF(['1.pdf', '2.pdf', '3.pdf'])
    instanceMathExcercise = MathExcerciseRandomizer()
    instanceExit = ExitEscape()

    main_menu = {
        "1": {"Description": "Join PDF", "Function": instancePDF.joinPDF},
        "2": {"Description": "Delete input PDF", "Function": instancePDF.deleteInputPDFFiles},
        "3": {"Description": "Draw two numbers", "Function": instanceMathExcercise.RandomNumbers},
        "4": {"Description": "Add two numbers", "Function": instanceMathExcercise.Adding},
        "5": {"Description": "Substract two numbers", "Function": instanceMathExcercise.Substraction},
        "6": {"Description": "Multiply two numbers", "Function": instanceMathExcercise.Multiplication},
        "7": {"Description": "Divide two numbers", "Function": instanceMathExcercise.Division},
        "8": {"Description": "Raise the numbers to a power", "Function": instanceMathExcercise.Powering},
        "0": {"Description": "Program exit", "Function": instanceExit}
    }

    while True:
        print("Main Menu: \n")
        for key, value in main_menu.items():
            print(f"{key}: {value['Description']}")

        choice = input("Select options: ")
        if choice in main_menu:
            function = main_menu[choice]["Function"]
            function()

        else:
            print("Incorrect choice")

if __name__ == '__main__':
    main()



