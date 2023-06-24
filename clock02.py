import time

# 等待时间（以秒为单位）
wait_time = 35

# 定义函数以进行倒计时
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('时间到！')

# 开始倒计时
countdown(wait_time)
