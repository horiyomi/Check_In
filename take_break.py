import time
import webbrowser

total_breaks = 3
break_count = 0

while break_count < total_breaks:
    print("The time now "+time.ctime())
    time.sleep(3)
    webbrowser.open('https://www.youtube.com/watch?v=447yaU_4DF8')
    break_count +=1

