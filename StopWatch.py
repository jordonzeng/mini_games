
import simplegui


time = 0
num = 0
time_check = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D


def start_button():
    global time, num, time_check

    timer.start()
    time_check = True

def stop_button():
    global time, num
    
    num += 1
    timer.stop()


def reset_button():
    global time, num
    
    time = 0
    num = 0
    timer.stop()



def timer_handler():
    global time
    time += 1
    

def format(t):
    minutes = t//600
    temp = (t//10)%60
    seconds = temp//10
    tens_of_second = temp % 10
    tenths_of_second = t % 10
    return str(minutes)+":"+str(seconds)+str(tens_of_second)+"."+str(tenths_of_second)

    


def draw_handler(c):
    c.draw_text(str(format(time)), (60, 100), 30, "Red")
    c.draw_text("This is "+str(num)+" round", (100, 30), 15, "white")
    



frame = simplegui.create_frame("StopWatch", 200 ,200)
timer = simplegui.create_timer(100, timer_handler)
button_start = frame.add_button("Start", start_button, 100)
button_stop = frame.add_button("Stop", stop_button, 100)
button_reset = frame.add_button("Reset", reset_button, 100)


frame.set_draw_handler(draw_handler)


# start frame
frame.start()

