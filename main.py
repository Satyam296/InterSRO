from flask import Flask, render_template, request
import requests
from datetime import datetime
import smtplib
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        my_email = "interesro@gmail.com"
        password = "wnidsblgtqxdezuy"
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        email = str(request.form["email"])
        age = int(request.form["age"])
        if age < 12 :
            connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg="Subject:Hello Junior\n\n Welcome in our junior section of our website. Here you will get some exciting games for increasing your interest in space")
            return render_template("junior.html")
        else :
            connection.sendmail(from_addr=my_email, to_addrs=email,
                                msg="Subject:Hello Senior\n\n Welcome in our senior section of our website. Here you will get some exciting articles for getting some excited news related space.")
            return render_template("senior.html")
        connection.close()
    return render_template("login.html")

@app.route('/iss')
def iss():
    def is_iss_overhead():
        if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
            return True



    my_email = "dummysingh372@gmail.com"
    password = "fguffxmwltkufvqc"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.login(user=my_email, password=password)

    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    MY_LAT = 30.306030
    MY_LONG = 78.098587

    def is_night():
        if time_now >= sunset and time_now <= sunrise:
            return True

    parameters = {

            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0  # By offing this we can get time in 24 hrs fashion .
        }
    response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
        # giving inputs to an api :
        # https://api.sunrise-sunset.org/json?lat=45.2433&lng=23.34523
    response.raise_for_status()
    data = response.json()["results"]
    sunrise = data["sunrise"]
    sunset = data["sunset"]
    sunrise_hour = sunrise.split("T")[1].split(":")[0]  # Yahan se T ko breakage point bna do hai iska matlab.
    sunset_hour = sunset.split("T")[1].split(":")[0]

    time_now = datetime.now().hour

    while True:
        if is_iss_overhead() and is_night():
            time.sleep(60)
            connection.sendmail(from_addr=my_email, to_addrs="sunitachhetri629@gmail.com",
                                    msg="Subject : ISS ! \n\n Look up!")

if __name__ == "__main__":
    app.run(debug=True)
