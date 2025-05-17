from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
   message = "Hello, Flask!"
   return message
@app.route('/thanks')
def thanks():
   person = "Bob"
   action = "dancing"
   object= "shoes"
   thing= "dancer"
   closer= "thanks"
   writer= "Richard"
   return render_template("tynote.html", name = person, gift=object, verb=action, noun=thing, closing_word=closer, author=writer)
@app.route('/results', methods=["POST"])
def results():
   color = request.form['color']
   luck_num = request.form['luck_num']
   fav_class = request.form['fav_class']
   best_pix = request.form['best_pix']
   return render_template('form_results.html', color = color, luck_num = luck_num, fav_class=fav_class, best_pix=best_pix)
@app.route('/form')
def form():
   return render_template("favorite_form.html")
if __name__ == '__main__':
   app.run()