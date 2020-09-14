from flask import Flask, render_template
from flask_sqlalchemy import SQLalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLalchemy(app)

class Todo(db.Model):
  	id = db.Column(db.Interger, )

@app.route('/')
def index():
  	return render_template('index.html')

if __name__ == '__main__':
			app.run(debug=True)
				