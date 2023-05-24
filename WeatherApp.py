import tkinter as tk
import requests
import math
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Weather App")
root.geometry("600x500")


def get_weather(city):
    weather_key = '474353fb51318c27c69d17f42f2fb9de'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    weather = response.json()
    result['text'] = format_response(weather)


def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        ce = (temp-32)*5/9
        final_str = 'City : %s\nCloud Type : %s\nTemperature : %s °C' % (
            city, condition, math.ceil(ce))
    except:
        final_str = 'Something went wrong...!!'
    return final_str


bg_lbl = tk.Label(root, bg='#1e2026')
bg_lbl.place(x=0, y=0, width=600, height=500)

heading_tital = tk.Label(bg_lbl, text='Please Enter City Name',
                         fg='#ce3856', bg='#1e2026', font=('time new roman', 18, 'bold'))
heading_tital.place(x=80, y=18)

frame_one = tk.Frame(bg_lbl, bg="#1e2026", bd=5)
frame_one.place(x=80, y=60, width=450, height=50)

txt_box = tk.Entry(frame_one, font=('times new Roman', 25), width=17)
txt_box.grid(row=0, column=0, sticky='w')

btn = tk.Button(frame_one, text='Get Weather', fg='#cc9900', font=(
    'time new Roman', 16, 'bold'), command=lambda: get_weather(txt_box.get()))
btn.grid(row=0, column=1, padx=10)

frame_two = tk.Frame(bg_lbl, bg="#cc9900", bd=5)
frame_two.place(x=80, y=130, width=450, height=300)

result = tk.Label(frame_two, bg='#ce3856', fg='white', justify='left',
                  anchor='nw', font=('time new Roman', 20, 'bold'))
result.place(relwidth=1, relheight=1)

root.mainloop()
