from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)

def generate_teams(player_names, num_teams):
    random.shuffle(player_names)
    
    teams = []
    for i in range(num_teams):
        team = player_names[i::num_teams]
        teams.append(team)

    return teams


@app.template_filter('enumerate')
def jinja2_enumerate(iterable, start=0):
    return enumerate(iterable, start)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_teams', methods=['POST'])
def generate_teams_route():

    names = request.form.get('names')
    num_teams = int(request.form.get('num_teams'))

    # Split the names and shuffle them
    name_list = names.split(',')
    random.shuffle(name_list)

    # Calculate the number of names per team
    names_per_team = (len(name_list) + num_teams - 1) // num_teams

    # Divide the names into teams and enumerate them
    teams = [(i + 1, name_list[i:i+names_per_team]) for i in range(0, len(name_list), names_per_team)]

    return render_template('teams.html', teams=teams, names=names, num_teams=num_teams)

if __name__ == "__main__":
    app.run(debug=True)

