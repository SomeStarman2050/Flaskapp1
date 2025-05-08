from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
   message = "Hello, Flask!"
   return message
@app.route('/form')
def form():
   return render_template("favorite_form.html")
if __name__ == '__main__':
   app.run()
