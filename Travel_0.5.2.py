"""
-----------------
QLVZ
-----------------
"""

import os
import random
from tkinter import *
from tkinter import messagebox
import time


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def main():
    global root
    root = Tk()
    root.geometry("750x360+300+300")
    Window(root)
    root.mainloop()


class Car:
    def __init__(self, distance):
        self.fuel = 100
        self.distance = distance
        self.money = 35
        self.tire = 21
        self.p = 0
        self.w = 0

    def fullreset(self):
        self.p = 0
        self.w = 0
        self.fuel = 100
        self.money = 35
        self.tire = 21

    def change1(self):
        self.p = 0
        self.w = 1

    def change2(self):
        self.p = 1

    def fuel_left(self):
        return self.fuel

    def dist_left(self):
        return self.distance

    def move(self):
        self.distance -= 2
        self.fuel -= 3

    def prokol(self):
        Window.destroymove()
        text_var.set('!!!!!!!!!\nYou broke your tier!!')
        text.update()
        time.sleep(1)
        messagebox.showinfo('', 'You have 20 hp for your tire and it spends every move'
                                '\nYou can repair it on gas station for 5 coins\nIf air ends - you lose'
                                '\nNew HUD: "Air left:"')
        Window.movebttn()

    def dirty_road(self):
        messagebox.showinfo("Dirty road", "You stuck in a dirt, so you spend more fuel to get out of it")
        self.fuel -= 6

    def clean_road(self):
        messagebox.showinfo("Clean road", "The clean road was the way longer")
        self.distance += 5
        self.fuel -= 3

    def tire_hp(self):
        self.tire -= 1
        if self.tire <= 8:
            return '- Air left: ' + str(self.tire) + " (LOW AIR LEVEL)"
        else:
            return '- Air left: ' + str(self.tire)

    def zapravka(self):
        f = random.randint(2, 5)
        messagebox.showinfo('Fuel get', 'You gave money and got ' + str(f) + ' litres!')
        if self.fuel + f >= 100:
            g = 100 - self.fuel
            messagebox.showinfo("Can't refill", "Can't refill more than 100 (100 = full tank), so be refueled "
                                + str(g) + 'liters')
            self.fuel += g
        else:
            self.fuel += f

    def repairing(self):
        messagebox.showinfo('Done', 'Tire fixed!')

    def moneypocket(self):
        p = random.randint(1, 3)
        self.money += p
        messagebox.showinfo('Found money!', "You found " + str(p) + " coin(s) on the road\nTotal money: " + str(self.money) +
                            ' coin(s)')

    def rand_money(self):
        m = random.randint(1, 10)
        return m

    def spending(self):
        j = self.rand_money()
        if self.money < j:
            return TRUE
        else:
            return FALSE

    def gas_spend(self):
        j = self.rand_money()
        self.money -= j
        messagebox.showinfo('Money', 'You spent ' + str(j) + ' coin(s) \n Coins left: ' + str(self.money))

    def money_left(self):
        return self.money

    def hud(self):
        if self.fuel <= 30:
            return '- Fuel: ' + str(self.fuel) + ' \n - Dist: ' + str(self.distance) + '\n \n(LOW FUEL LEVEL!)'
        else:
            return '- Fuel: ' + str(self.fuel) + '\n - Dist: ' + str(self.distance)


class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.interface()

    def interface(self):
        self.parent.title("Travel_Game")

        global DistButton, inputBox, text, text_var, Inputhere, RU_Lang_Button, ENG_Lang_Button, Set_Button

        text_var = StringVar()
        text = Label(root, font='Arial 16', bg="green yellow", width=100, height=13, textvariable=text_var)
        text.pack()

        self.pack(fill=BOTH, expand=True)

        self.logo()

    def settings(self):
        global RulesButton, DistButton, inputBox, text, text_var, Inputhere, BackButton
        text.pack_forget()
        Set_Button.destroy()
        DistButton.destroy()
        inputBox.destroy()
        Inputhere.destroy()
        RulesButton.destroy()
        self.pack(fill=NONE, expand=True)
        RU_Lang_Button = Button(self, text="RUS", command=self.lang_ru)
        RU_Lang_Button.pack(side=TOP, padx=5)
        BackButton = Button(self, text="Back", bg="sandy brown", command=self.back)
        BackButton.pack(side=RIGHT, padx=5, pady=5)

    def back(self):
        text.pack()
        self.pack(fill=BOTH, expand=True)
        BackButton.destroy()
        RU_Lang_Button.destroy()
        Set_Button.destroy()
        self.logo()

    def lang_ru(self):
        global lang, RU_Lang_Button, ENG_Lang_Button
        lang = 'RU'
        RU_Lang_Button.destroy()
        ENG_Lang_Button = Button(self, text="ENG", command=self.lang_eng)
        ENG_Lang_Button.pack(side=TOP, padx=5)
        return lang

    def lang_eng(self):
        global lang, RU_Lang_Button, ENG_Lang_Button
        lang = 'ENG'
        ENG_Lang_Button.destroy()
        RU_Lang_Button = Button(self, text="RUS", command=self.lang_ru)
        RU_Lang_Button.pack(side=TOP, padx=5)
        return lang

    def logo(self):
        global RulesButton, DistButton, inputBox, text, text_var, Inputhere, BackButton, Set_Button
        Set_Button = Button(self, text="Settings", command=self.settings)
        Set_Button.pack(side=RIGHT, padx=5, pady=5)
        Inputhere = Label(self, text='Input distance :')
        Inputhere.pack(side=LEFT, padx=5, pady=5)
        inputBox = Entry(self, width=20, bg='lightgrey')
        inputBox.pack(side=LEFT, padx=5, pady=5)
        DistButton = Button(self, text="Start", command=self.start)
        DistButton.pack(side=LEFT, padx=5, pady=5)
        RulesButton = Button(self, text="Rules", command=self.rules)
        RulesButton.pack(side=RIGHT, padx=5, pady=5)
        text_var.set('TRAVEL\n\nThe python game\n\n\nv 0.5.1')

    def rules(self):
        global BackButton
        DistButton.destroy()
        inputBox.destroy()
        Inputhere.destroy()
        RulesButton.destroy()
        Set_Button.destroy()
        BackButton = Button(self, text="Back",bg="sandy brown", command=self.back)
        BackButton.pack(side=RIGHT, padx=5, pady=5)
        return text_var.set('In this game you will drive a car from point A to B'
                            '\nYou can choose the distance between this points by yourself'
                            '\nWhile driving you will get into various events'
                            '\nThat events can cause different effects\nYou win if you reached the destination point')

    def start(self):
        global My_Car
        temp = int(inputBox.get())
        My_Car = Car(temp)
        RulesButton.destroy()
        DistButton.destroy()
        inputBox.destroy()
        Inputhere.destroy()
        text_var.set(My_Car.hud() + '\n Press "Move"')
        self.game()

    def game(self):
        self.movebttn()

    def movebttn(self):
        global MoveButton
        MoveButton = Button(self, text="Move", width=20, bg="sienna2", command=lambda: self.dvij())
        MoveButton.pack(side=RIGHT, padx=260, pady=5)

    def destroymove(self):
        MoveButton.destroy()

    def dvij(self):
        text_var.set(My_Car.hud() + '\n Press "Move"')
        self.game_code()

    def game_code(self):
        My_Car.move()
        if My_Car.tire == 0:
            text_var.set('OUT OF AIR - GAME OVER')
            text.update()
            time.sleep(1)
            z = messagebox.askyesno("Restart?", "Restart?")
            if z == TRUE:
                restart_program()
            else:
                quit(0)
        elif My_Car.fuel_left() <= 0:
            text_var.set('OUT OF FUEL = GAME OVER')
            text.update()
            time.sleep(1)
            z = messagebox.askyesno("Restart?", "Restart?")
            if z == TRUE:
                restart_program()
            else:
                quit(0)
        elif My_Car.dist_left() <= 0:
            text_var.set('End of the road = You won!')
            text.update()
            time.sleep(1)
            z = messagebox.askyesno("Restart?", "Restart?")
            if z == TRUE:
                restart_program()
            else:
                quit(0)
        gas = random.randint(0, 100)
        mon = random.randint(0, 100)
        ways = random.randint(0, 100)
        broke = random.randint(0, 100)
        if gas <= 20:
            self.destroymove()
            text_var.set('!GAS STATION! \n\nYou have:\n- Coins: ' + str(My_Car.money_left()) + '\n' + My_Car.hud())
            text.update()
            time.sleep(1)
            j = messagebox.askyesno('Gas', 'Do you want to spend randomly 1-10 coins for 2-5 liters?')
            self.movebttn()
            if j == TRUE:
                if My_Car.spending() == TRUE:
                    messagebox.showinfo('No money', 'Not enough money! \nMoving without refueling!')
                elif My_Car.spending() == FALSE:
                    My_Car.gas_spend()
                    My_Car.zapravka()
            if My_Car.p == 1:
                z = messagebox.askyesno('Tire', 'You have a broken tire\nDo you want to repair it for 5 coins?')
                if z == TRUE:
                    if My_Car.spending() == 1:
                        messagebox.showinfo('Not enough money!', 'No repairing!')
                    elif My_Car.spending() == 0:
                        My_Car.repairing()
                        My_Car.change1()
                else:
                    messagebox.showinfo('', 'No repairing!')
            if j == FALSE:
                messagebox.showinfo('', 'No refueling!')
        elif mon <= 7:
            self.destroymove()
            text_var.set('Found money!')
            text.update()
            time.sleep(1)
            My_Car.moneypocket()
            self.movebttn()
        elif ways <= 4:
            self.destroymove()
            text_var.set('The road branches in 2 ways\nThe dirty one is faster, but full of dirt (-3 ext fuel)\n'
                         'There is also clean one but a way longer (+5 distance)')
            text.update()
            time.sleep(1)
            q = messagebox.askyesno('Road', 'Will you use the dirty road?')
            self.movebttn()
            if q == TRUE:
                My_Car.dirty_road()
            else:
                My_Car.clean_road()
        elif broke <= 4:
            if My_Car.p == 0 and My_Car.w == 0:
                My_Car.prokol()
                My_Car.change2()
        if My_Car.p == 1:
            text_var.set('Moving...\n\n' + My_Car.hud() + '\n' + My_Car.tire_hp())
            text.update()
        else:
            text_var.set('Moving...\n\n' + My_Car.hud())
            text.update()
        self.destroymove()
        self.game()


main()
