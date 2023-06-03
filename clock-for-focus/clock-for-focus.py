import time

def start_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"\r{seconds} seconds left", end="")
        time.sleep(1)
        seconds -= 1
    print("\rTime's up!")

if __name__ == "__main__":
    minutes = int(input("Enter the number of minutes to focus: "))
    start_timer(minutes)
