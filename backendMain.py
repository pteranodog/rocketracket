from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def return_homepage():
    return render_template('main.html')


@app.route('/rocket')
def return_rocket():
    return render_template('html/rocket.html')


@app.route('/missioncontrol')
def return_mission_control():
    return render_template('html/missioncontrol.html')


@app.route('/launchtower')
def return_launch_tower():
    return render_template('html/launchtower.html')


@app.route('/fueltanks')
def return_fuel_tanks():
    return render_template('html/fueltanks.html')


@app.route('/crawler')
def return_crawler():
    return render_template('html/crawler.html')


@app.route('/astronauts')
def return_astronaut_complex():
    return render_template('html/astronautcomplex.html')


@app.route('/player')
def return_player_client():
    return render_template('html/client.html')
