#librerias
from flask import Flask, send_file
from flask import request, render_template

# Configuracion
sensor = Flask(__name__)

@sensor.route('/welcome', methods=["GET"])
def welcome():
    return ("Welcome")

@sensor.route('/payload', methods=["GET"])
def payload():
    data = open("tallerpycon/scripts/payload","r+")
    return data.read()

@sensor.route('/image', methods=["GET"])
def image():
    return send_file("tallerpycon/images/wallpaper.jpg",mimetype="image/jpg")

@sensor.route('/upload', methods=["POST"])
def upload_file():
    data = None
    file = request.get_data()
    with open('tallerpycon/results/result', 'a') as the_file:
        the_file.write(str(file).replace("\\x00","").replace("\\r","").replace("\\t","").replace("\\n",""))
    return "success"


if __name__ == "__main__":
    sensor.run(host="0.0.0.0", port="18080", debug=True)