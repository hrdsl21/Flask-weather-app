from flask import Flask
from flask import request, redirect ,url_for
from flask import render_template
import requests 


app = Flask(__name__)

Url = "https://api.openweathermap.org/data/2.5/forecast?q="
Api_key = #Paste your api here




@app.route("/", methods=["GET", "POST"])
def front():
    if request.method == "POST":
        city = request.form.get("search")
        return redirect(url_for("get_weather", city=city))
    return render_template("index.html")



@app.route("/get_weather/<city>")
def get_weather(city):
    
    url = f"{Url}{city}&appid={Api_key}"
    response = requests.get(url)

    
    if response.status_code == 200:
        weatherData = response.json()
        forcast = weatherData['list']

        if forcast:
            dt = forcast[0].get('dt_txt')
            weather = forcast[0].get('weather')[0]
            main = forcast[0].get('main')
            temp = main.get('temp', '-')
            feels_like_temp = main.get('feels_like')
            humidity = main.get('humidity')
            description = weather.get('description')
        
        temperature = round(float(temp) - 273.15, 2)
        feels_like_temperature = round(float(feels_like_temp) - 273.15, 2)
        weather_description = description
        humidity = humidity
        dt = dt

        

        return render_template("WeatherCity.html", city=city, temperature=temperature, Feels_temperature = feels_like_temperature,  
                               weather_description=weather_description, humidity=humidity, dt=dt)
    
    else:
        return render_template('errorPage.html')
    

@app.route("/error")
def error():
    return render_template("errorPage.html")




if __name__ == '__main__':
    app.run(debug=True)











