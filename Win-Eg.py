# beloved/DHS 
import tkinter as tk
import random
import time
import threading
import winsound
#第一阶段，折磨
def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('haha')
    window.geometry("300x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window, text='def_marshmello', bg='blue',
             font=('宋体', 17), width=50, height=4).pack()
    window.mainloop()
 
 
time.sleep(1)
 
threads = []
for i in range(40):
    t = threading.Thread(target=boom)
    threads.append(t)
    time.sleep(0)
    threads[i].start()
time.sleep(1.0)
 
 
def lu():
    TK = tk.Tk()
    width = TK.winfo_screenwidth()
    height = TK.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    TK.title("嘿嘿!")
    TK.geometry("400x100" + "+" + str(a) + "+" + str(b))
    tk.Label(TK, text='hahaha', bg='red',
             font=('宋体', 17), width=40, height=4).pack()
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    TK.mainloop()
 
 
if __name__ == '__main__':
    threads = []
    for i in range(50):
        t = threading.Thread(target=boom)
        p = threading.Thread(target=lu)
        threads.append(t)
        threads.append(p)
        time.sleep(0.6)
        threads[i].start()
#第二阶段，铺满全屏
def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('hello')
    window.geometry("30000x50000" + "+" + str(a) + "+" + str(b))
    tk.Label(window, text='yhtyrerg', bg='blue',
             font=('宋体', 17), width=10000, height=10000).pack()
    window.mainloop()
 
 
time.sleep(1)
 
threads = []
for i in range(10):
    t = threading.Thread(target=boom)
    threads.append(t)
    time.sleep(0)
    threads[i].start()
time.sleep(1.0)
#第三阶段，演奏音乐
def lu():
    TK = tk.Tk()
    width = TK.winfo_screenwidth()
    height = TK.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    TK.title("嘿嘿!")
    TK.geometry("400x100" + "+" + str(a) + "+" + str(b))
    tk.Label(TK, text='hahaha', bg='red',
             font=('宋体', 17), width=40, height=4).pack()
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    TK.mainloop()
 
 
if __name__ == '__main__':
    threads = []
    for i in range(18):
        p = threading.Thread(target=lu)
        threads.append(p)
        threads[i].start()
        time.sleep(0.2)
def lu():
    TK = tk.Tk()
    width = TK.winfo_screenwidth()
    height = TK.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    TK.title("嘿嘿!")
    TK.geometry("400x100" + "+" + str(a) + "+" + str(b))
    tk.Label(TK, text='hahaha', bg='red',
             font=('宋体', 17), width=40, height=4).pack()
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    TK.mainloop()
 
 
if __name__ == '__main__':
    threads = []
    for i in range(30):
        p = threading.Thread(target=lu)
        threads.append(p)
        threads[i].start()
        time.sleep(0.3)
def lu():
    TK = tk.Tk()
    width = TK.winfo_screenwidth()
    height = TK.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    TK.title("嘿嘿!")
    TK.geometry("400x100" + "+" + str(a) + "+" + str(b))
    tk.Label(TK, text='hahaha', bg='red',
             font=('宋体', 17), width=40, height=4).pack()
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    TK.mainloop()
 
 
if __name__ == '__main__':
    threads = []
    for i in range(30):
        p = threading.Thread(target=lu)
        threads.append(p)
        threads[i].start()
        time.sleep(0.8)
def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('haha')
    window.geometry("300x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window, text='关注def_marshmello', bg='blue',
             font=('宋体', 17), width=50, height=4).pack()
    window.mainloop()
 
 
time.sleep(1)
 
threads = []
for i in range(40):
    t = threading.Thread(target=boom)
    threads.append(t)
    time.sleep(0.01)
    threads[i].start()
 
def lu():
    TK = tk.Tk()
    width = TK.winfo_screenwidth()
    height = TK.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    TK.title("嘿嘿!")
    TK.geometry("400x100" + "+" + str(a) + "+" + str(b))
    tk.Label(TK, text='hahaha', bg='red',
             font=('宋体', 17), width=40, height=4).pack()
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    TK.mainloop()
 
 
if __name__ == '__main__':
    threads = []
    for i in range(30):
        p = threading.Thread(target=lu)
        threads.append(p)
        threads[i].start()
        time.sleep(0.2)
def lu():
    TK = tk.Tk()
    width = TK.winfo_screenwidth()
    height = TK.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    TK.title("嘿嘿!")
    TK.geometry("400x100" + "+" + str(a) + "+" + str(b))
    tk.Label(TK, text='好听', bg='red',
             font=('宋体', 17), width=40, height=4).pack()
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    TK.mainloop()
 
 
if __name__ == '__main__':
    threads = []
    for i in range(30):
        p = threading.Thread(target=lu)
        threads.append(p)
        threads[i].start()
        time.sleep(0.54)
while 1:
    def boom():
        window = tk.Tk()
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        a = random.randrange(0, width)
        b = random.randrange(0, height)
        window.title('haha')
        window.geometry("300x50" + "+" + str(a) + "+" + str(b))
        tk.Label(window, text='def_marshmello', bg='blue',
                 font=('宋体', 17), width=50, height=4).pack()
        window.mainloop()
 
 
    time.sleep(1)
 
    threads = []
    for i in range(40):
        t = threading.Thread(target=boom)
        threads.append(t)
        time.sleep(0)
        threads[i].start()
 
    time.sleep(1.0)
 
 
    def lu():
        TK = tk.Tk()
        width = TK.winfo_screenwidth()
        height = TK.winfo_screenheight()
        a = random.randrange(0, width)
        b = random.randrange(0, height)
        TK.title("嘿嘿!")
        TK.geometry("400x100" + "+" + str(a) + "+" + str(b))
        tk.Label(TK, text='好听', bg='red',
                 font=('宋体', 17), width=40, height=4).pack()
        winsound.MessageBeep(winsound.MB_ICONASTERISK)
        TK.mainloop()
 
 
    if __name__ == '__main__':
        threads = []
        for i in range(30):
            p = threading.Thread(target=lu)
            threads.append(p)
            threads[i].start()
    time.sleep(0.5)