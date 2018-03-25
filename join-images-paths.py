from tkinter import *
import collections
import os


def process_paths():
    filename = e1.get()

    print(filename + '.txt')
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__) + '\\' + ('%s' % filename) + '.txt') as images_paths:
        # with open('%s.txt' % filename, 'r') as images_paths:
        original_string = images_paths.read()  # original_string = """"""

    new_lines = collections.OrderedDict()
    i = 0
    for file_name in original_string.split('\n'):
        idx = file_name.split('-')[-2]
        # print(idx)
        if idx in new_lines:
            new_lines[idx] = new_lines[idx] + "," + file_name  # print(file_name)
        else:
            new_lines[idx] = file_name  # print(idx)
    new_string = "\n".join(list(new_lines.values()))

    f = open(filename + '-joined' + '.txt', "w+")
    f.write(new_string)
    import ctypes  # An included library with Python install.
    ctypes.windll.user32.MessageBoxW(0, "Look for new file named:\n" + filename + "-joined" + ".txt\n" + "in " + __location__, "Your joined paths", 1)
    print(new_string)


master = Tk()
Label(master, text="Data file Name (no extension)").grid(row=0)

e1 = Entry(master)

e1.grid(row=1, column=0)

Button(master, text='Quit', command=master.quit).grid(row=2, column=0, sticky=W, pady=4)
Button(master, text='OK', command=process_paths).grid(row=2, column=1, sticky=W, pady=4)

mainloop()
