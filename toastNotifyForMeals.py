import schedule
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()

def meal():
    toaster.show_toast("Oiii Matee!!!", "Eat Yo Meal, Fool!!", icon_path="luffy.ico", duration=10)

schedule.every().day.at("10:50").do(meal)
schedule.every().day.at("12:50").do(meal)
schedule.every().day.at("14:50").do(meal)
schedule.every().day.at("16:50").do(meal)

while True:
    schedule.run_pending()
    time.sleep(1)