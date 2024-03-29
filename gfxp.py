import pygame
import tkinter as tk

def init(pygame=True):
    global pygame_enabled
    pygame_enabled = pygame
    if pygame_enabled:
        pygame.init()
    else:
        root = tk.Tk()
        root.withdraw()
        
def window(title, size=(640, 480)):
    if pygame_enabled:
        return pygame.display.set_mode(size)
    else:
        win = tk.Tk()
        win.geometry(str(size[0]) + "x" + str(size[1]))
        win.title(title)
        return win

def quit(root=None):
    if pygame_enabled:
        pygame.quit()
        exit()
    else:
        root.destroy()
        exit()

def mainloop(root=None):
    if not pygame_enabled:
        root.mainloop()
    else:
        pygame.display.flip()
        
def update(root=None):
    if not pygame_enabled:
        root.update()
    else:
        pygame.display.update()

def label(text, root=None, fsize = 20, font="Arial"):
    if pygame_enabled:
        return pygame.font.SysFont(font, fsize).render(text, True, (255, 255, 255))
    else:
        return tk.Label(root, text=text, font=(font, fsize))
    
def button(text, root=None, command=None):
    if pygame_enabled:
        print("WARNING: You cannot use buttons in pygame, as this functionality is easily implemented using a label().")
        return label(text, root)
    else:
        return tk.Button(root, text=text, command=lambda: command())
        
def entry(root=None):
    if pygame_enabled:
        print("ERROR: You cannot use entries in pygame.")
    else:
        return tk.Entry(root)

def entry_get(textbox):
    if pygame_enabled:
        print("ERROR: You cannot use textboxes in pygame.")
    else:
        return textbox.get()

def entry_set(textbox, text):
    if pygame_enabled:
        print("ERROR: You cannot use textboxes in pygame.")
    else:
        textbox.insert(0, text)
        
def drawshape(shape, color, surface):
    if pygame_enabled:
        pygame.draw.polygon(surface, color, shape)
    else:
        print("ERROR: You cannot draw shapes in tkinter.")
        
def drawline(start, end, color, surface):
    if pygame_enabled:
        pygame.draw.line(surface, color, start, end)
    else:
        print("ERROR: You cannot draw lines in tkinter.")

def help():
    print("GFXP HELP")
    print("Initializing: gfxp.init(pygame=True/False)")
    print("pygame=True means that pygame will be used, otherwise tkinter will be used.")
    print("Creating a window: gfxp.window(title, size=(w, h))")
    print("Creating a label: gfxp.label(text)")
    print("Creating a button: gfxp.button(text, command=lambda: command())")
    print("Creating a textbox: gfxp.textbox() (TK only)")
    print("Getting text from a textbox: gfxp.textbox_get(textbox) (TK only)")
    print("Setting text in a textbox: gfxp.textbox_set(textbox, text) (TK only)")
    print("Drawing a shape: gfxp.drawshape(shape, color, surface) (Pygame only)")
    print("Drawing a line: gfxp.drawline(start, end, color, surface) (Pygame only)")
    print("Quitting: gfxp.quit()")
    print("Mainloop: gfxp.mainloop()")
    print("Update screen: gfxp.update()")
    ep = input("Would you like to see an example program? (y/n)")
    if ep == "y":
        sample()

def sample():
    init(pygame=False)
    win = window("Example Program")
    win.tk_setPalette(["#ff8800"])
    lb = label("This is an example of GFXP!", win, fsize=40)
    lb.place(x=10, y=10)
    bt = button("Click me!", win, lambda: print("You clicked me!"))
    bt.place(x=10, y=90)
    en = entry(win)
    en.place(x=10, y=140)
    en.bind("<Return>", lambda event: print("You typed: " + entry_get(en)))
    qu = button("Quit", win, lambda: quit(win))
    qu.place(x=10, y=170)
    lb2 = label("It is easy to use tkinter/pygame in conjunction with GFXP, too!", win, fsize=20)
    lb2.place(x=10, y=200)
    lb2.bind("<Button-1>", lambda event: lb2.config(text="For example, you can detect clicks on labels!"))
    lb2.place(x=10, y=230)
    en2 = entry(win)
    en2.place(x=10, y=260)
    entry_set(en2, "Type a hex color!")
    en2.bind("<Return>", lambda event: win.tk_setPalette([str(entry_get(en2))]))
    def newwin():
        winnew = window("Another Window")
        lb3 = label("This is a new window!", winnew)
        lb3.place(relx=0.5, rely=0.5, anchor="center")
        lb4 = label("You can click the button multiple times to make more windows like this!", winnew)
        lb4.place(relx=0.5, rely=0.6, anchor="center")
    bt2 = button("Nice dual window setup!", win, lambda: newwin())
    bt2.place(x=100, y=90)
    mainloop(win)
    quit(win)

if __name__ == "__main__":
    sample()
