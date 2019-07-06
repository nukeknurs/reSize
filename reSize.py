import pyglet
import win32gui
import win32con
import keyboard
import ctypes
import pygetwindow as gw
from infi.systray import SysTrayIcon

def say_hello(systray):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, 'Operational.\nPress "CTRL+F1" to reSize window.', 'reSize - status', 0)

#def printuj_staty_kurwo():
#    print(win32gui.GetWindowRect(win32gui.GetForegroundWindow()))

def wysokosc():
    rect=win32gui.GetWindowRect(win32gui.GetForegroundWindow())
    y = rect[1]
    h1 = (rect[3] - y)
    #print(h1)
    return h1

def zakresy(monitory):
    x=[]
    for monitor in monitory:
       x.append([monitor.x,monitor.width])
    x.sort()
    #print('dddupa',x)
    return x


def callback(*argv):    #lista wartości współczynnika x od których rozpoczyna się kolejny monitor zaczynając od pierwszego oraz szerokości monitora
    rect = win32gui.GetWindowRect(win32gui.GetForegroundWindow())
    y = rect[1]
    x = rect[0]
    h1 = (rect[3] - y)
    

    if len(argv[1])==1 or x+rect[2]/2<argv[1][0]:
        actualWindow = gw.getWindowsWithTitle(win32gui.GetWindowText(win32gui.GetForegroundWindow()))[0]
        win32gui.SetWindowPos(win32gui.GetForegroundWindow(), win32con.HWND_TOP, argv[0][0]-14, int(y), argv[0][1]+14, int(h1), 0) #zmienia szerokość okna

        a=wysokosc()
        actualWindow.moveRel(5, 0)      #zmiana pierwszej wartości w nawiasie pozwala na przesunięcie okna
        b=wysokosc()
        actualWindow.resizeRel(0,int((a-b)*1.60))

        #print('2188?\t',c)
        #printuj_staty_kurwo()
        #print(c-a)

    else:
        actualWindow = gw.getWindowsWithTitle(win32gui.GetWindowText(win32gui.GetForegroundWindow()))[0]
        win32gui.SetWindowPos(win32gui.GetForegroundWindow(), win32con.HWND_TOP, argv[1][0], int(y), argv[1][1], int(h1), 0)
        actualWindow.moveRel(-10, 0)

    

monitory=[]
menu_options = (("Status", None, say_hello),)
systray = SysTrayIcon('reSize.ico', 'Ready to reSize!', menu_options)  #Icon made by Freepik from www.flaticon.com
systray.shutdown()                                                     #https://www.flaticon.com/free-icon/maximize_1141984#term=resize&page=1&position=64
systray.start()


platform = pyglet.window.get_platform()
display = platform.get_default_display()
for screen in display.get_screens():
    monitory.append(screen)
zakresy_var=zakresy(monitory)


keyboard.add_hotkey('ctrl+f1', callback,(zakresy_var))