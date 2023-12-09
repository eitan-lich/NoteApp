from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR, nullable=False)
    content = db.Column(db.TEXT, nullable=False)
    # user_id = db.Column(db.Integer, foreign_key=True)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/add-note', methods=['POST'])
def add_note():
    all_notes = []
    new_note = {}

    new_note['title'] = request.form.get('note-title')
    new_note['content'] = request.form.get('note-content')

    all_notes.append(new_note)

    return render_template("notes.html", notes=all_notes)
    


if __name__ == "__main__":
    app.run(debug=True)

