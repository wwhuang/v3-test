from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
import random
import json

app = Flask(__name__)


@app.route('/generate_random_chords')
def generate_random_chords():
    data = {}
    data['ids'] = []
    data['data'] = []
    data['title'] = 'Dynamic Chord Test'

    for i in range(7):
        data['ids'].append(str(i))
        data['data'].append([])
        for n in range(7):
            data['data'][i].append(random.randint(1, 100))

    return json.dumps(data)

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['SERVER_NAME'] = 'localhost:5005'
    app.run()
