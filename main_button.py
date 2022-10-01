# This is a sample Python script.
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
import mss
import mss.tools
import psutil
import datetime
import tkinter as tk


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

pyautogui.FAILSAFE = False

globvar_start = datetime.datetime.now()

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    global globvar_start    # Needed to modify global copy of globvar

    print("==========================")
    #globvar_start = datetime.datetime.now()
    end = datetime.datetime.now()
    elapsed_time = end - globvar_start
    globvar_start = end
    print(elapsed_time.microseconds / 1000)
    print(elapsed_time.seconds)


    # fahrenheit = ent_temperature.get()
    # celsius = (5 / 9) * (float(fahrenheit) - 32)
    # lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    x,y=pyautogui.position()
    print(x,y) # 输出的结果是：312,198  （结果是鼠标当前位置，可以想象成以屏幕左上角为原点的第一象限）
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    pyautogui.size()         # 输出的结果是：(1920,1080) （结果是当前屏幕分辨率）
    pyautogui.scroll(1,1)      #鼠标在(x,y)滚动

#    pyautogui.moveTo(2000,900, 1)  # 鼠标移动到(x,y)并保持s秒，同理还有拖动方法dragTo(x,y,s)

  #  pyautogui.rightClick(2000, 900)  # 鼠标点击(x,y)
    width, height = pyautogui.size()  # 获取屏幕的宽度和高度

    org_width = 2560
    org_height = 1440
    width, height = pyautogui.size()  # 获取屏幕的宽度和高度
    scaling_x = width / org_width  # any scaling factor you wish
    scaling_y = height / org_height  # any scaling factor you wish
    print(scaling_x, scaling_y)

    print(width, height)
  #  pyautogui.typewrite("hello")
   # pyautogui.rightClick(2000,900)
    # 不截全屏，截取区域图片。截取区域region参数为：左上角XY坐标值、宽度和高度
    img = pyautogui.screenshot('屏幕截图.png', region=(0, 0, 300, 400))


    #hello pyautogui.click()  # 鼠标当前位置点击一下
    pyautogui.PAUSE = 0.01
    pyautogui.click(2000 * scaling_x, 900 * scaling_y)  # 鼠标点击(x,y)

    #pyautogui.click(2000, 900)  # 鼠标点击(x,y)
   # pyautogui.typewrite("hello")

    window = tk.Tk()
    window.title("Temperature Converter")
   # window.resizable(width=False, height=False)

    frm_entry = tk.Frame(master=window)
    ent_temperature = tk.Entry(master=frm_entry, width=10)
    lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
    # greeting = tk.Label(text="Hello, Tkinter")
    # greeting.pack()
    # entry = tk.Entry(fg="yellow", bg="blue", width=50)
    # entry.pack()
    # text_box = tk.Text()
    # text_box.pack()
    # button = tk.Button(
    #     text="Click me!",
    #     width=25,
    #     height=5,
    #     bg="blue",
    #     fg="yellow",
    # )
    btn_decrease = tk.Button(master=window, text="-",
         width=50,
         height=20,
                             command=fahrenheit_to_celsius  # <--- Add this line
)
    btn_decrease.pack()

    window.mainloop()

def print_hiex_(name):

    try:
        for i in range(100):
            start = datetime.datetime.now()
            pyautogui.click(2000*scaling_x, 900*scaling_y)  # 鼠标点击(x,y)
            end = datetime.datetime.now()
            elapsed_time = end - start
            print(elapsed_time.microseconds / 1000)
            # pyautogui.typewrite("hello")  # 输入"hello"
            #pyautogui.press("A")  # 输入"hello"


            #pyautogui.scroll(200)
    except KeyboardInterrupt:
        print('\nDone.')


def print_hiex(name):
    with mss.mss() as sct:
        # The screen part to capture
        region = {'top': 0, 'left': 0, 'width': 100, 'height': 100}

        # Grab the data
        img = sct.grab(region)
        mss.tools.to_png(img.rgb, img.size, output='dummy.png')

    #, region = (0, 0, 400, 400)
  #  time.sleep(5)
    pyautogui.PAUSE = 1
    if (pyautogui.locateOnScreen('dummy.png',region = (0, 0, 400, 400), grayscale=True) is not None):
        pyautogui.hotkey('win', 'l')

    if "Client.exe" in (p.name() for p in psutil.process_iter()):
        print("发现旅")

    # for p in psutil.process_iter():
    #     print(p)
    # sleep(0)
    #
    # while 1:
    #     # if pyautogui.locateOnScreen('dummy.png' ,confidence=0.85) != None: #, region=(0, 0, 824, 616),
    #     #     print("I can see username")
    #     #     #time.sleep(.5)
    #
    #     x1_coordinates = pyautogui.locateOnScreen('dummy.png', confidence=0.9)
    #     print(x1_coordinates)  # This will print out where it is
    #
    #     if x1_coordinates:
    #         print(f"I can see it at {x1_coordinates}")
    #         pyautogui.confirm('Geek Shall I proceed?')
    #     else:
    #         print("I cannot see it.")


    pyautogui.click(2000, 900)  # 鼠标点击(x,y)

    pyautogui.PAUSE = 0.0001
    for x in range(0, 9):
        start = datetime.datetime.now()
        pyautogui.moveRel(1, 10)
        end = datetime.datetime.now()

        elapsed_time = end - start

        print(elapsed_time.microseconds/1000)