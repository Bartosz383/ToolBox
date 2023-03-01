import time

class StartTextGame():
    def __init__(self):
        pass

    def intro(self):
        print("Witaj na bezludnej wyspie!")
        time.sleep(1)
        print("Nie masz nic poza kilkoma przedmiotami.")
        time.sleep(1)
        print("Musisz przetrwać.")
        time.sleep(1)
        print("Jaki będzie twój pierwszy krok.")
        self.first_step()
    def first_step(self):
        choice = input("W którą stronę idziesz? (lewo/prawo): ")
        if choice == "lewo":
            print("Odnajdujesz źródło wody.")
            time.sleep(1)
            print("Możesz pić bez obaw!")
        elif choice == "prawo":
            print("Natknąłeś się na jadowitego węża i zginąłeś!")
            time.sleep(1)
            print("Gra się skończyła!")
            time.sleep(1)
            print("Dziękujemy za grę!")
            exit()
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
            self.first_step()
        self.second_step()

    def second_step(self):
        choice = input("Co robisz? (budujesz schronienie / szukasz jedzenia): ")
        if choice == "budujesz schronienie" or "buduje schronienie":
        #if choice in ["lewo", "w lewo", "po lewej", "lewooo"]:
            print("Udało Ci się zbudować schronienie i przetrwać na wyspie!")
            time.sleep(1)
            print("Gratulacje, wygrałeś!")
        elif choice == "szukasz jedzenia" or "szukam jedzenia":
            print("Znalazłeś jagody, ale były one trujące. Zginąłeś!")
            time.sleep(1)
            print("Gra się skończyła!")
            time.sleep(1)
            print("Dziękujemy za grę!")
            exit()
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
            self.second_step()

