''' Transactions logging application server '''
# Import libraries
from flask import Flask, request, url_for, redirect,render_template

# Instantiate Flask functionality
app = Flask('Transactions logging app')

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100.0},
    {'id': 2, 'date': '2023-06-02', 'amount': -200.0},
    {'id': 3, 'date': '2023-06-03', 'amount': 300.0}
]

# Read operation
@app.route('/')
def get_transactions():
    ''' Get list of transactions '''
    print ('Transactions list request')
    return render_template("transactions.html", transactions=transactions)

# Create operation
@app.route('/add', methods = ['POST', 'GET'])
def add_transaction():
    print ('Add transaction')
    ''' Add new transaction '''
    if request.method == 'POST':
        print ('Add page POST')
        id = len(transactions) + 1
        date = request.form['date']
        amount = float(request.form['amount'])
        print(f'id: {id}, date: {date}, amount: {amount}')
        transactions.append({'id': id, 'date': str(date), 'amount': amount})

        # Redirect to the transactions list page
        return redirect(url_for('get_transactions'))
    
    # Render the form template to display the add transaction form
    return render_template("form.html")
        
    
# Update operation
@app.route('/edit/<int:transaction_id>', methods = ['POST', 'GET'])
def edit_transaction(transaction_id):
    ''' Edit existed transaction '''
    print ('Edit transaction')
    if request.method == 'POST':
    # for POST method update requested transaction
        # id = request.form['id']
        date = request.form['date']
        amount = request.form['amount']
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break

        # Redirect to the transactions list page
        return redirect(url_for('get_transactions'))
    
    # for GET method render form to edit transaction
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template('edit.html', transaction=transaction)
    
    return {'message':'Record not find'}, 422

# Delete operation
# Update operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    ''' Delete existed transaction '''
    print ('Delete transaction')
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    
    # Redirect to the transactions list page
    return redirect(url_for('get_transactions'))

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    