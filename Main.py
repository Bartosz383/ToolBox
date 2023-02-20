from PyPDF2 import PdfMerger
import os
import sys
from PDFmodule import PDF
from MathExcerciseForFun import MathExcerciseRandomizer
from Exit import ExitEscape

def main():
    instancePDF = PDF(['merged_file.pdf', 'merger.pdf', 'merger2.pdf'])
    instanceMathExcercise = MathExcerciseRandomizer()
    instanceExit = ExitEscape()

    main_menu = {
        "1": {"Opis": "Wywołaj funkcję 1", "Funkcja": instancePDF.joinPDF},
        "2": {"Opis": "Wywołaj funkcję 1", "Funkcja": instancePDF.deleteInputPDFFiles},
        "3": {"Opis": "Wywołaj funkcję 1", "Funkcja": instanceMathExcercise.RandomNumbers},
        "4": {"Opis": "Wywołaj funkcję 1", "Funkcja": instanceMathExcercise.Adding},
        "5": {"Opis": "Wywołaj funkcję 1", "Funkcja": instanceMathExcercise.Substraction},
        "6": {"Opis": "Wywołaj funkcję 1", "Funkcja": instanceMathExcercise.Multiplication},
        "7": {"Opis": "Wywołaj funkcję 1", "Funkcja": instanceMathExcercise.Division},
        "8": {"Opis": "Wywołaj funkcję 1", "Funkcja": instanceMathExcercise.Powering},
        "0": {"Opis": "Wyjście z programu", "Funkcja": instanceExit}
    }

    while True:
        print("Menu główne: \n")
        for key, value in main_menu.items():
            print(f"{key}: {value['Opis']}")

        choice = input("Wybierz opcję: ")
        if choice in main_menu:
            function = main_menu[choice]["Funkcja"]
            function()

        else:
            print("Nieprawidłowy wybór")

if __name__ == '__main__':
    main()



