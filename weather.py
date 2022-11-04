from tkinter import *
import requests

drive = Tk()


def find_weather():
    place = cityName.get()
    key = "1550bf27013ad36bb6d6ebfe8c840f9f"
    url = "http://api.openweathermap.org/data/2.5/weather"
    parameters = {
        "q": place,
        "appid": key,
        "units": "metric"
    }

    final_info = requests.get(url, params=parameters)
    weather = final_info.json()
    info["text"] = (f'{str(weather["name"])}: {weather["main"]["temp"]}')



drive["bg"] = "#fafafa"
drive.title("Приложения для погоды")
drive.geometry("300x300")
drive.resizable(width=False, height=False)

frame_setting_top = Frame(drive, bg='#ffb700', bd=5)
frame_setting_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
frame_setting_bottom = Frame(drive, bg='#ffb700', bd=5)
frame_setting_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityName = Entry(frame_setting_top, bg="red", font=30)
cityName.pack()

press_button = Button(frame_setting_top, text="Узнать погоду", font=("TimesNewRoman 10"), command=find_weather)
press_button.pack()

info = Label(frame_setting_bottom, text="Инфа о погоде", bg='#ffb700', font=("TimesNewRoman 15"))
info.pack()

drive.mainloop()
