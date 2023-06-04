import time

def focus_timer(minutes):
    """将分钟转换为秒，并启动倒计时"""
    seconds = minutes * 60
    for i in range(seconds,0,-1):
        time.sleep(1)
        countdown = time.strftime("%M:%S", time.gmtime(i))
        print(f"倒计时: {countdown}", end="\r")
    print("专注时间结束！")

if __name__ == "__main__":
    minutes = int(input("请输入专注时间（以分钟为单位）："))
    print(f"开始专注 {minutes} 分钟...")
    focus_timer(minutes)
