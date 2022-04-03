import os
import sys
import time
import turtle
import keyboard
import mouse
import ctypes
from colorama import Fore

"""
|||||||||||||||||||||||||||
THE IMPORTANT NOTES HERE
|||||||||||||||||||||||||||
THE COMMANDLINE OPTIONS:
/C      Carries out the command specified by string and then terminates
/K      Carries out the command specified by string but remains
/S      Modifies the treatment of string after /C or /K (see below)
/Q      Turns echo off
/D      Disable execution of AutoRun commands from registry (see below)
/A      Causes the output of internal commands to a pipe or file to be ANSI
/U      Causes the output of internal commands to a pipe or file to be
        Unicode
|||||||||||||||||||||||||||
"""


def clear():
    # Clear Windows command prompt.
    if os.name in ('ce', 'nt', 'dos'):
        os.system('cls')

    # Clear the Linux terminal.
    elif 'posix' in os.name:
        os.system('clear')


def developermain():
    clear()
    print(Fore.GREEN + "You just unlocked the developer mode!")
    print("What do you want to choose?")
    print("1.Python Package Manager")
    print("2.Python Compiler")
    devchoice = input()
    if devchoice == "1":
        print("What do you want to do?")
        print("1.Install Package")
        print("2.Uninstall Package")
        print("3.Check what packages i have installed")
        print("4.run package")
        print("5.reinstall package")
        choice = input()
        if choice == "1":
            print("type what package do you want to install:")
            package = input()
            os.system("cmd /k pip install " + package)
            print("package is installed!")
            print("press enter to go back")
            keyboard.wait("enter")
            main()
        if choice == "2":
            print("type what package do you want to uninstall:")
            package = input()
            os.system("cmd /k pip uninstall " + package)
            print("package is uninstalled!")
            print("press enter to go back")
            keyboard.wait("enter")
            main()
        if choice == "3":
            installed_packages = os.system("cmd /c pip list")
            print(installed_packages)
            print("=====================================================")
            print("press enter to go back")
            keyboard.wait("enter")
            main()
        if choice == "4":
            print("type name of the package you want to run:")
            package = input()
            os.system("cmd /k " + package)
        if choice == "5":
            print("type what package do you want to uninstall:")
            package = input()
            print("Uninstalling the package..")
            os.system("cmd /k pip uninstall " + package)
            print("Installing the package..")
            os.system("cmd /k pip install " + package)
            print("press enter to go back")
            keyboard.wait("enter")
            main()
    elif devchoice == "2":
        compiler = "auto-py-to-exe"
        os.system("cmd /k pip list")
        installed_packages = os.system("cmd /k pip freeze")
        if compiler not in installed_packages:
            print("you don't have compiler installed!")
            print("do you want to install it?")
            devchoice = input()
            if devchoice == "yes":
                os.system("cmd /k pip install auto-py-to-exe")
                os.system("auto-py-to-exe")
            else:
                pass
        os.system("auto-py-to-exe")


def main():
    print("================================")
    print("Multitasker")
    print("By: MarioVercetti")
    print("================================")
    time.sleep(0.7)
    while True:
        clear()
        print("================================")
        print("Multitasker")
        print("By: MarioVercetti")
        print("================================")
        print("================================")
        print("1.Calculator")
        print("================================")
        print("2.Notatnik")
        print("================================")
        print("3.Drawer")
        print("================================")
        print("4.FNF Input")
        print("================================")
        print("5.Mining Bot")
        print("================================")
        print("6.Windows Activator")
        print("================================")
        print("7.FNF Keybinds Rebinder")
        print("================================")
        print("8.Half Life 2 Speedrun Tricks")
        print("================================")
        print("9.Windows Activation Check")
        print("================================")
        print("10.Keyboard Rebinder")
        print("================================")
        print("(Jeżeli chcesz wyjść wpisz: wyjdz)")
        choice = input()
        if choice == "1" or choice == "Calculator" or choice == "calculator" or choice == "kalkulator":
            print("1.full numbers or "
                  "2.more complex numbers like: 10.3 or 52.2543")
            choice = input()
            if choice == "1":
                pass
            elif choice == "2":
                num1 = float(input("Wpisz pierwszą liczbę: "))
                print("(1. dodawanie, 2. odejmowanie, 3. mnożenie, 4. dzielenie)")
                op = input("Wpisz operatora: ")
                num2 = float(input("Wpisz drugą liczbę: "))
                if op == "1" or op == "dodawanie" or op == "+":
                    print("Wynik: ", num1 + num2)
                    input("Wciśnij enter aby powrócić")
                elif op == "2" or op == "odejmowanie" or op == "-":
                    print("Wynik: ", num1 - num2)
                    input("Wciśnij enter aby powrócić")
                elif op == "3" or op == "mnożenie" or op == "mnozenie" or op == "*":
                    print("Wynik: ", num1 * num2)
                    input("Wciśnij enter aby powrócić")
                elif op == "4" or op == "dzielenie" or op == "/":
                    print("Wynik: ", num1 / num2)
                    input("Wciśnij enter aby powrócić")
                else:
                    print("wpisuj operatora z małej litery oraz bez polskich znaków"
                          "np: mnozenie\n"
                          "np: dzielenie")
                    input("wciśnij enter aby powrócić")
            num1 = int(input("Wpisz pierwszą liczbę: "))
            print("(1. dodawanie, 2. odejmowanie, 3. mnożenie, 4. dzielenie)")
            op = input("Wpisz operatora: ")
            num2 = int(input("Wpisz drugą liczbę: "))
            if op == "1" or op == "dodawanie" or op == "+":
                print("Wynik: ", num1 + num2)
                input("Wciśnij enter aby powrócić")
            elif op == "2" or op == "odejmowanie" or op == "-":
                print("Wynik: ", num1 - num2)
                input("Wciśnij enter aby powrócić")
            elif op == "3" or op == "mnożenie" or op == "mnozenie" or op == "*":
                print("Wynik: ", num1 * num2)
                input("Wciśnij enter aby powrócić")
            elif op == "4" or op == "dzielenie" or op == "/":
                print("Wynik: ", num1 / num2)
                input("Wciśnij enter aby powrócić")
            else:
                print("wpisuj operatora z małej litery oraz bez polskich znaków"
                      "np: mnozenie\n"
                      "np: dzielenie")
            input("wciśnij enter aby powrócić")
        elif choice == "2" or choice == "notatnik" or choice == "Notatnik":
            f = open("notatki.txt", "w+")
            notes = input("wpisz to co chcesz: ")
            f.write(notes)
            time.sleep(0.2)
            print("Czy chcesz zobaczyć zawartość pliku txt?: ")
            noteschoice = input()
            if noteschoice == "tak":
                print("================================")
                print(notes)
                print("================================")
                time.sleep(0.3)
                input("Wciśnij enter aby powrócić")
            elif noteschoice == "nie":
                continue
        elif choice == "wyjdz" or choice == "Wyjdz":
            sys.exit()
        elif choice == "3" or choice == "t" or choice == "T":
            # Its buggy right now, I have to fix that
            print("Starting up..")
            time.sleep(1)
            sc = turtle.Screen()
            sc.title("Drawer")
            turtle.forward(0)
            turtle.bgcolor("gray")
            print("Controls:")
            print("Press R to clear")
            print("Press Shift to speed up turning")
            print("Press T if you want to draw and Y if you want to not draw")
            print("Press Q to quit")
            while True:
                if keyboard.is_pressed("w") or keyboard.is_pressed("up"):
                    turtle.forward(3)
                elif keyboard.is_pressed("s") or keyboard.is_pressed("down"):
                    turtle.back(3)
                elif keyboard.is_pressed("d") or keyboard.is_pressed("right"):
                    turtle.right(3)
                elif keyboard.is_pressed("a") or keyboard.is_pressed("left"):
                    turtle.left(3)
                if keyboard.is_pressed("q"):
                    sys.exit()
                if keyboard.is_pressed("r"):
                    turtle.clear()
                if keyboard.is_pressed("shift"):
                    turtle.speed(12)
                if keyboard.is_pressed("T"):
                    turtle.pendown()
                if keyboard.is_pressed("Y"):
                    turtle.penup()
        elif choice == "4":
            while True:
                # may be improved
                print("1.instant click (may not work properly)")
                print("2.delayed but still fast input(work properly)")
                print("3.human like")
                inputchoice = input()
                leftarrow = input("left Arrow: ")
                downarrow = input("Down Arrow: ")
                uparrow = input("Up Arrow: ")
                rightarrow = input("Right Arrow: ")
                print("You can type for example: DFJK or HJKL")
                if inputchoice == "1":
                    while True:
                        if keyboard.on_press(leftarrow):
                            time.sleep(0.02)
                            keyboard.release(leftarrow)
                        if keyboard.on_press(downarrow):
                            time.sleep(0.02)
                            keyboard.release(downarrow)
                        if keyboard.on_press(uparrow):
                            time.sleep(0.02)
                            keyboard.release(uparrow)
                        if keyboard.on_press(rightarrow):
                            time.sleep(0.02)
                            keyboard.release(rightarrow)
                            continue
                elif inputchoice == "2":
                    while True:
                        if keyboard.on_press(leftarrow):
                            time.sleep(0.1)
                            keyboard.release(leftarrow)
                        if keyboard.on_press(downarrow):
                            time.sleep(0.1)
                            keyboard.release(downarrow)
                        if keyboard.on_press(uparrow):
                            time.sleep(0.1)
                            keyboard.release(uparrow)
                        if keyboard.on_press(rightarrow):
                            time.sleep(0.1)
                            keyboard.release(rightarrow)
                            continue
                elif inputchoice == "3":
                    while True:
                        if keyboard.on_press(leftarrow):
                            time.sleep(0.15)
                            keyboard.release(leftarrow)
                        if keyboard.on_press(downarrow):
                            time.sleep(0.15)
                            keyboard.release(downarrow)
                        if keyboard.on_press(uparrow):
                            time.sleep(0.15)
                            keyboard.release(uparrow)
                        if keyboard.on_press(rightarrow):
                            time.sleep(0.15)
                            keyboard.release(rightarrow)

        elif choice == "5":
            print("1.mouse hold only"
                  "2.mouse and keyboard")
            choice = input()
            if choice == "1":
                print("press N to start")
                if keyboard.is_pressed("n"):
                    mouse.press(button="left")
                    while True:
                        if keyboard.is_pressed("n"):
                            mouse.release(button="left")
                            break
            elif choice == "2":
                pass
            while True:
                mining = False
                holding = False
                if keyboard.is_pressed("n"):
                    while mining:
                        mining = True
                        mouse.press(button="left")
                        while holding:
                            holding = True
                            for i in range(1, 3):
                                keyboard.press("a")
                                time.sleep(0.10)
                                keyboard.release("a")
                                keyboard.press("d")
                                time.sleep(0.10)
                                keyboard.release("d")
                            if keyboard.is_pressed("m"):
                                mouse.release(button="left")
                                sys.exit()
                            keyboard.press("s")
                            time.sleep(1)
                            keyboard.release("s")
                            keyboard.press("space")
                            time.sleep(2)
                            keyboard.release("space")
                            time.sleep(0.25)
        elif choice == "6":
            # asking about what system does user use
            print("1.window 11 or\n"
                  "2.windows 10 or\n"
                  "3.windows 8.1?")
            choice = input()
            if choice == "3":
                print("1.Pro or "
                      "2.core?")
                choice = input()
                if choice == "1":
                    # Re-run the program with admin rights
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                    # Starting all this shit
                    os.system("cmd /c slmgr /ipk GCRJD-8NW9H-F2CDX-CCM8D-9D6T9")
                    print("setting up ")
                    os.system("cmd /c slmgr /skms kms8.msguides.com")
                    os.system("cmd /c slmgr /ato")
                    # finally ending this crap + adding messagebox
                    ctypes.windll.user32.MessageBoxW(0, "Windows has been activated!", "Done", 0)
                elif choice == "2":
                    # Re-run the program with admin rights
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                    # Starting all this shit
                    os.system("cmd /c slmgr /ipk M9Q9P-WNJJT-6PXPY-DWX8H-6XWKK")
                    os.system("cmd /c slmgr /skms kms8.msguides.com")
                    os.system("cmd /c slmgr /ato")
                    # finally ending this crap + adding messagebox
                    ctypes.windll.user32.MessageBoxW(0, "Windows has been activated!", "Done", 0)
            elif choice == "1" or "2":
                pass
            # asking about version of Windows
            print("1.Pro or "
                  "2.Home?")
            choice = input()
            if choice == "1":
                # Re-run the program with admin rights
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                # Starting all this shit
                os.system("cmd /c slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
                os.system("cmd /c slmgr /skms kms8.msguides.com")
                os.system("cmd /c slmgr /ato")
            elif choice == "2":
                # Re-run the program with admin rights
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                # Starting all this shit but other version
                os.system("cmd /c slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
                os.system("cmd /c slmgr /skms kms8.msguides.com")
                os.system("cmd /c slmgr /ato")
            # finally ending this crap + adding messagebox
            ctypes.windll.user32.MessageBoxW(0, "Windows has been activated!", "Done", 0)
        elif choice == "7":
            print("Type keys you want to be binded to arrow keys")
            print("You can type for example: DFJK or HJKL")
            leftarrow = input("left Arrow: ")
            downarrow = input("Down Arrow: ")
            uparrow = input("Up Arrow: ")
            rightarrow = input("Right Arrow: ")
            print("Have Fun!")
            keyboard.remap_key(leftarrow, "left")
            keyboard.remap_key(downarrow, "down")
            keyboard.remap_key(uparrow, "up")
            keyboard.remap_key(rightarrow, "right")
            keyboard.wait()
        elif choice == "8":
            clear()
            print("1.bunnyhop")
            print("2.wallclimbing")
            hlchoice = input()
            if hlchoice == "1":
                while True:
                    if keyboard.on_press("space"):
                        keyboard.press("space")
                        time.sleep(0.001)
                        keyboard.release("space")
                        continue
            elif hlchoice == "2":
                while True:
                    if keyboard.on_press("c"):
                        keyboard.press_and_release("e")
                        time.sleep(0.01)
                        keyboard.press_and_release("space")
        elif choice == "9":
            os.system("cmd /c slmgr /xpr")
            print("If Windows is succesfully activated, the dialog will indicate is is either 'Permanently"
                  "Activated' as shown below, or if using a time-limited volume license activation the time"
                  "the activation is due to expire will be shown.")
            print("press Q to restart program")
            keyboard.wait("q")
            main()
        elif choice == "10":
            print("type key you want to be binded")
            keytobind = input()
            print("type key you want to bind")
            bindedkey = input()
            print("Have Fun!")
            keyboard.remap_key(keytobind, bindedkey)
            keyboard.wait()
        elif choice == "developermode":
            developermain()
        else:
            print("Wskazówka: Wpisuj numery bądź napisy z małej litery i bez polskich znaków")
            input()


if __name__ == '__main__':
    main()
