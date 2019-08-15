from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

#<li><a href="services"> SERVICES </a></li>
#@app.route('/services', methods=['GET', 'POST'])
#def service():
#    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

#<li><a href="hours"> HOURS </a></li>
#@app.route('/hours')
#def news():
#    return render_template('hours.html')

#<li><a href="FAQ"> FAQ </a></li>
#@app.route('/FAQ')
#def FAQ():
#    return render_template('FAQ.html')

if __name__ == "__main__":
    app.run(debug=True)
