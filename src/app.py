from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy

import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True)
    done = db.Column(db.Boolean)

    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def __repr__(self):
        return '{}'.format(self.description)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {'description':self.description, 'done':self.done, 'id':self.id}


db.create_all()

@app.route("/")
def index():
    return make_response(open('templates/index.html').read())


@app.route('/tasks', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        t = request.data.decode()
        task = Task(t)
        task.save()
        return 'ok', 200
    elif request.method == 'GET':
        return json.dumps([t.to_dict() for t in Task.query.all()])


if __name__ == '__main__':
    app.run()
