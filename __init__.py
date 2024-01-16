import Customer
import User
import shelve
from datetime import timedelta
from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

from Forms import CreateUserForm, CreateCustomerForm, CustomerLoginForm

app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.static_folder = 'static'
'''
customers_dict = {}
db = shelve.open('customer.db', 'c')

try:
    customers_dict = db['Customers']
except:
    print("Error in retrieving Customers from customer.db.")
customers_dict[]'''
@app.route('/', methods=['GET','POST'])
def home():
    error= None
    customer_login_form =  CustomerLoginForm(request.form)
    if request.method == 'POST':
        print("login form ok")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        password = customer_login_form.password.data
        customers_dict = db['Customers']
        if 'logout' in customer_login_form:
            print("III")
            session['Username'] = None
        for i in customers_dict:
            print(customers_dict[i])
            if customers_dict[i][1] == password:
                print(f"Customer {customers_dict[i][0]} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print("Customer not found")
                print(password)
                print(customers_dict[i][1])
                error = "Username or password incorrect!"
        db.close()

    return render_template('index.html',error=error)


@app.route('/Login_page')
def login_page():
    return render_template('Login_page.html')


@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data,
                         create_user_form.gender.data, create_user_form.membership.data, create_user_form.remarks.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        # Test codes
        users_dict = db['Users']
        user = users_dict[user.get_user_id()]
        print(user.get_first_name(), user.get_last_name(), "was stored in user.db successfully with user_id ==",
              user.get_user_id())

        db.close()

        return redirect(url_for('home'))
    return render_template('createUser.html', form=create_user_form)


@app.route('/createCustomer', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")

        customer = Customer.Customer(create_customer_form.first_name.data, create_customer_form.last_name.data,
                                     create_customer_form.gender.data,
                                     create_customer_form.email.data, create_customer_form.birthdate.data,
                                     create_customer_form.address.data)
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        customers_dict = db['Customers']
        customer = customers_dict[customer.get_customer_id()]
        print(customer.get_first_name(), customer.get_last_name(), "was stored in user.db successfully with user_id ==",
              customer.get_customer_id())

        db.close()
        return redirect(url_for('home'))
    return render_template('createCustomer.html', form=create_customer_form)

@app.route('/test')
def test():
    return render_template('staffpage.html')


if __name__ == '__main__':
    app.run(debug=True)
session['Username'] = None