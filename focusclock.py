import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Time remaining: {seconds // 60:02d}:{seconds % 60:02d}")
        time.sleep(1)
        seconds -= 1
    print("Time is up! Good job focusing.")

focus_timer(25) # 25分钟
