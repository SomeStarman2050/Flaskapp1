from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/hello')
def hello():
   message = "Hello, Flask!"
   return message

@app.route('/goodbye')
def goodbye():
   message = "<h2>This is the second page!</h2>"
   return message

if __name__ == '__main__':
   app.run()