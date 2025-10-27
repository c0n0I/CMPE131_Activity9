from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret'  


listings = [
    {'id': 1, 'title': 'Apartment near San Jose State University', 'price': 70, 'desc': 'Cheap 2 Bedroom Apartment'},
    {'id': 2, 'title': 'House in San Francisco', 'price': 200, 'desc': '2 Story house near the ocean.'},
    {'id': 3, 'title': 'House in Los Angeles', 'price': 250, 'desc': '2 Story house near Disne '}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/listings')
def show_listings():
    return render_template('listings.html', listings=listings)

@app.route('/listing/<int:id>')
def detail(id):
    listing = next((l for l in listings if l['id'] == id), None)
    if not listing:
        return "Listing not found", 404
    return render_template('detail.html', listing=listing)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    username = session.get('username', None)
    if not username:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=username, bookings=listings[:2])

if __name__ == '__main__':
    app.run(debug=True)
