from flask import Flask, render_template, request, redirect, url_for, session, flash
import pandas as pd
import csv
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load products
def load_products(file_name='data/products.csv'):
    try:
        df = pd.read_csv(file_name)
        return df
    except FileNotFoundError:
        print("Error: File not found!")
        return pd.DataFrame()

products = load_products()

@app.route('/')
def index():
    if 'username' in session:
        return render_template('dashboard.html', products=products.to_dict(orient='records'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simple authentication (for demonstration purposes)
        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials. Please try again.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        new_product = {
            'ProductID': int(request.form['product_id']),
            'ProductName': request.form['product_name'],
            'Category': request.form['category'],
            'Price': float(request.form['price']),
            'Stock': int(request.form['stock']),
            'ManufactureDate': request.form['manufacture_date'],
            'CompanyDetails': request.form['company_details'],
            'Image': request.form['image']
        }
        global products
        products = products.append(new_product, ignore_index=True)
        products.to_csv('data/products.csv', index=False)
        flash('Product added successfully!')
        return redirect(url_for('index'))
    return render_template('add_item.html')

@app.route('/delete_item/<int:product_id>')
def delete_item(product_id):
    global products
    products = products[products['ProductID'] != product_id]
    products.to_csv('data/products.csv', index=False)
    flash('Product deleted successfully!')
    return redirect(url_for('index'))

@app.route('/print_invoice')
def print_invoice():
    # Logic to print customer invoice
    return "Invoice printed!"

if __name__ == '__main__':
    app.run(debug=True)