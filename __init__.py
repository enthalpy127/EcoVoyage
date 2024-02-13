
import sys

from Login.Forms import CreateFeedbackForm

sys.path.append('../Login')
from Login import User
from Login import Customer
from Login import Forms
from Login import Feedback
import shelve
from datetime import timedelta, datetime
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_session import Session
from flask_mail import Mail, Message
from Order import Orders
from Order.order_forms import CreateOrderForm
import csv
import flask
from Order.models import df
from dash import Dash, html, dash_table, dcc
import stripe



#from Forms import CreateUserForm, CreateCustomerForm, CustomerLoginForm
import traceback

app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = 'myatkophone981@gmail.com'
app.config['MAIL_PASSWORD'] = 'nith ifhf rfpk jkbr'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)



dash_app1 = Dash(__name__, server=app, url_base_pathname='/plotly/')
dash_app1.layout = html.Div([
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure={}, id="controls-and-graph"),
    dcc.RadioItems(options=['sum', 'avg'], value='sum', id='controls-and-radio-item-x'),
    dcc.RadioItems(options=['Number of Adults', 'Number of Children', 'total_amount', 'Refunded'], value='Number of Adults', id='controls-and-radio-item-y'),

])

app.static_folder = 'static'


@app.route('/', methods=['GET','POST'])
def home():
    #login(session)
    error= None
    customer_login_form =  Forms.CustomerLoginForm(request.form)
    print(customer_login_form.changelogin.data)
    print(customer_login_form.data)
    if customer_login_form.logout.data != None:
            print("III")
            session['Username'] = None
    if request.method == 'POST' and (customer_login_form.changelogin.data == 'customer'):
        print("login form ok")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        password = customer_login_form.password.data
        customers_dict = db['Customers']
        print(customers_dict)
        for i in customers_dict:
            print(customers_dict[i])
            if customers_dict[i].get_password() == password:
                print(f"Customer {customers_dict[i].get_username} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print(customers_dict[i].get_password())
                print(password)
                print(customers_dict[i])
                error = "Username or password incorrect!"
        db.close()
    elif request.method == 'POST' and (customer_login_form.changelogin.data == 'staff'):
        staff_dict = {}
        db = shelve.open('staff.db', 'c')
        password = customer_login_form.password.data
        staff_dict = db['Staff']
        if 'logout' in customer_login_form:
            print("III")
            session['Username'] = None
        for i in staff_dict:
            print(staff_dict[i])
            if staff_dict[i][1] == password:
                print(f"Staff {staff_dict[i][0]} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print("Staff not found")
                print(password)
                print(staff_dict[i][1])
                error = "Username or password incorrect!"
        db.close()
        #login(session)end

    return render_template('index.html',error=error)

@app.route('/countries', methods=['GET','POST'])
def countriespage():
    error= None
    customer_login_form =  Forms.CustomerLoginForm(request.form)
    print(customer_login_form.changelogin.data)
    print(customer_login_form.data)
    if customer_login_form.logout.data != None:
            print("III")
            session['Username'] = None
    if request.method == 'POST' and (customer_login_form.changelogin.data == 'customer'):
        print("login form ok")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        password = customer_login_form.password.data
        customers_dict = db['Customers']
        print(customers_dict)
        for i in customers_dict:
            print(customers_dict[i])
            if customers_dict[i].get_password() == password:
                print(f"Customer {customers_dict[i].get_username} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print(customers_dict[i].get_password())
                print(password)
                print(customers_dict[i])
                error = "Username or password incorrect!"
        db.close()
    elif request.method == 'POST' and (customer_login_form.changelogin.data == 'staff'):
        staff_dict = {}
        db = shelve.open('staff.db', 'c')
        password = customer_login_form.password.data
        staff_dict = db['Staff']
        if 'logout' in customer_login_form:
            print("III")
            session['Username'] = None
        for i in staff_dict:
            print(staff_dict[i])
            if staff_dict[i][1] == password:
                print(f"Staff {staff_dict[i][0]} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print("Staff not found")
                print(password)
                print(staff_dict[i][1])
                error = "Username or password incorrect!"
        db.close()
        #login(session)end
    return render_template("Countries.html")

@app.route('/Login_page', methods=['GET','POST'])
def login_page():
    #login(session)
    error= None
    customer_login_form =  Forms.CustomerLoginForm(request.form)
    print(customer_login_form.changelogin.data)
    print(customer_login_form.data)
    if customer_login_form.logout.data != None:
            print("III")
            session['Username'] = None
    if request.method == 'POST' and (customer_login_form.changelogin.data == 'customer'):
        print("login form ok")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        password = customer_login_form.password.data
        customers_dict = db['Customers']
        print(customers_dict)
        for i in customers_dict:
            print(customers_dict[i])
            if customers_dict[i].get_password() == password:
                print(f"Customer {customers_dict[i].get_username} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print(customers_dict[i].get_password())
                print(password)
                print(customers_dict[i])
                error = "Username or password incorrect!"
        db.close()
    elif request.method == 'POST' and (customer_login_form.changelogin.data == 'staff'):
        staff_dict = {}
        db = shelve.open('staff.db', 'c')
        password = customer_login_form.password.data
        staff_dict = db['Staff']
        if 'logout' in customer_login_form:
            print("III")
            session['Username'] = None
        for i in staff_dict:
            print(staff_dict[i])
            if staff_dict[i][1] == password:
                print(f"Staff {staff_dict[i][0]} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print("Staff not found")
                print(password)
                print(staff_dict[i][1])
                error = "Username or password incorrect!"
        db.close()
        #login(session)end
    return render_template('Login_page.html')

@app.route('/denmark', methods=['GET','POST'])
def denmark():
    #login(session)
    error= None
    customer_login_form =  Forms.CustomerLoginForm(request.form)
    print(customer_login_form.changelogin.data)
    print(customer_login_form.data)
    if customer_login_form.logout.data != None:
            print("III")
            session['Username'] = None
    if request.method == 'POST' and (customer_login_form.changelogin.data == 'customer'):
        print("login form ok")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        password = customer_login_form.password.data
        customers_dict = db['Customers']
        print(customers_dict)
        for i in customers_dict:
            print(customers_dict[i])
            if customers_dict[i].get_password() == password:
                print(f"Customer {customers_dict[i].get_username} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print(customers_dict[i].get_password())
                print(password)
                print(customers_dict[i])
                error = "Username or password incorrect!"
        db.close()
    elif request.method == 'POST' and (customer_login_form.changelogin.data == 'staff'):
        staff_dict = {}
        db = shelve.open('staff.db', 'c')
        password = customer_login_form.password.data
        staff_dict = db['Staff']
        if 'logout' in customer_login_form:
            print("III")
            session['Username'] = None
        for i in staff_dict:
            print(staff_dict[i])
            if staff_dict[i][1] == password:
                print(f"Staff {staff_dict[i][0]} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print("Staff not found")
                print(password)
                print(staff_dict[i][1])
                error = "Username or password incorrect!"
        db.close()
        #login(session)end
    return render_template('/Destinations/Denmark.html')

@app.route('/singapore', methods=['GET','POST'])
def singapore():
    #login(session)
    error= None
    customer_login_form =  Forms.CustomerLoginForm(request.form)
    print(customer_login_form.changelogin.data)
    print(customer_login_form.data)
    if customer_login_form.logout.data != None:
            print("III")
            session['Username'] = None
    if request.method == 'POST' and (customer_login_form.changelogin.data == 'customer'):
        print("login form ok")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        password = customer_login_form.password.data
        customers_dict = db['Customers']
        print(customers_dict)
        for i in customers_dict:
            print(customers_dict[i])
            if customers_dict[i].get_password() == password:
                print(f"Customer {customers_dict[i].get_username} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print(customers_dict[i].get_password())
                print(password)
                print(customers_dict[i])
                error = "Username or password incorrect!"
        db.close()
    elif request.method == 'POST' and (customer_login_form.changelogin.data == 'staff'):
        staff_dict = {}
        db = shelve.open('staff.db', 'c')
        password = customer_login_form.password.data
        staff_dict = db['Staff']
        if 'logout' in customer_login_form:
            print("III")
            session['Username'] = None
        for i in staff_dict:
            print(staff_dict[i])
            if staff_dict[i][1] == password:
                print(f"Staff {staff_dict[i][0]} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print("Staff not found")
                print(password)
                print(staff_dict[i][1])
                error = "Username or password incorrect!"
        db.close()
        #login(session)end
    return render_template('/Destinations/Singapore.html')

@app.route('/switzerland', methods=['GET','POST'])
def switzerland():
    #login(session)
    error= None
    customer_login_form =  Forms.CustomerLoginForm(request.form)
    print(customer_login_form.changelogin.data)
    print(customer_login_form.data)
    if customer_login_form.logout.data != None:
            print("III")
            session['Username'] = None
    if request.method == 'POST' and (customer_login_form.changelogin.data == 'customer'):
        print("login form ok")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        password = customer_login_form.password.data
        customers_dict = db['Customers']
        print(customers_dict)
        for i in customers_dict:
            print(customers_dict[i])
            if customers_dict[i].get_password() == password:
                print(f"Customer {customers_dict[i].get_username} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print(customers_dict[i].get_password())
                print(password)
                print(customers_dict[i])
                error = "Username or password incorrect!"
        db.close()
    elif request.method == 'POST' and (customer_login_form.changelogin.data == 'staff'):
        staff_dict = {}
        db = shelve.open('staff.db', 'c')
        password = customer_login_form.password.data
        staff_dict = db['Staff']
        if 'logout' in customer_login_form:
            print("III")
            session['Username'] = None
        for i in staff_dict:
            print(staff_dict[i])
            if staff_dict[i][1] == password:
                print(f"Staff {staff_dict[i][0]} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print("Staff not found")
                print(password)
                print(staff_dict[i][1])
                error = "Username or password incorrect!"
        db.close()
        #login(session)end
    return render_template('/Destinations/Switzerland.html')

@app.route('/thailand', methods=['GET','POST'])
def thailand():
    #login(session)
    error= None
    customer_login_form =  Forms.CustomerLoginForm(request.form)
    print(customer_login_form.changelogin.data)
    print(customer_login_form.data)
    if customer_login_form.logout.data != None:
            print("III")
            session['Username'] = None
    if request.method == 'POST' and (customer_login_form.changelogin.data == 'customer'):
        print("login form ok")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        password = customer_login_form.password.data
        customers_dict = db['Customers']
        print(customers_dict)
        for i in customers_dict:
            print(customers_dict[i])
            if customers_dict[i].get_password() == password:
                print(f"Customer {customers_dict[i].get_username} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print(customers_dict[i].get_password())
                print(password)
                print(customers_dict[i])
                error = "Username or password incorrect!"
        db.close()
    elif request.method == 'POST' and (customer_login_form.changelogin.data == 'staff'):
        staff_dict = {}
        db = shelve.open('staff.db', 'c')
        password = customer_login_form.password.data
        staff_dict = db['Staff']
        if 'logout' in customer_login_form:
            print("III")
            session['Username'] = None
        for i in staff_dict:
            print(staff_dict[i])
            if staff_dict[i][1] == password:
                print(f"Staff {staff_dict[i][0]} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print("Staff not found")
                print(password)
                print(staff_dict[i][1])
                error = "Username or password incorrect!"
        db.close()
        #login(session)end
    return render_template('/Destinations/Thailand.html')

@app.route('/createUser', methods=['GET', 'POST'])
def create_user():

    #login(session)
    error= None
    customer_login_form =  Forms.CustomerLoginForm(request.form)
    print(customer_login_form.changelogin.data)
    print(customer_login_form.data)
    if customer_login_form.logout.data != None:
            print("III")
            session['Username'] = None
    if request.method == 'POST' and (customer_login_form.changelogin.data == 'customer'):
        print("login form ok")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        password = customer_login_form.password.data
        customers_dict = db['Customers']
        print(customers_dict)
        for i in customers_dict:
            print(customers_dict[i])
            if customers_dict[i].get_password() == password:
                print(f"Customer {customers_dict[i].get_username} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print(customers_dict[i].get_password())
                print(password)
                print(customers_dict[i])
                error = "Username or password incorrect!"
        db.close()
    elif request.method == 'POST' and (customer_login_form.changelogin.data == 'staff'):
        staff_dict = {}
        db = shelve.open('staff.db', 'c')
        password = customer_login_form.password.data
        staff_dict = db['Staff']
        if 'logout' in customer_login_form:
            print("III")
            session['Username'] = None
        for i in staff_dict:
            print(staff_dict[i])
            if staff_dict[i][1] == password:
                print(f"Staff {staff_dict[i][0]} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print("Staff not found")
                print(password)
                print(staff_dict[i][1])
                error = "Username or password incorrect!"
        db.close()
        #login(session)end

    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.User(create_user_form.first_name.data,
                         create_user_form.last_name.data,
                         create_user_form.gender.data,
                         create_user_form.membership.data,
                         create_user_form.remarks.data,
                         create_user_form.password.data)
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

    #login(session)
    error= None
    customer_login_form =  Forms.CustomerLoginForm(request.form)
    print(customer_login_form.changelogin.data)
    print(customer_login_form.data)
    if customer_login_form.logout.data != None:
            print("III")
            session['Username'] = None
    if request.method == 'POST' and (customer_login_form.changelogin.data == 'customer'):
        print("login form ok")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        password = customer_login_form.password.data
        customers_dict = db['Customers']
        print(customers_dict)
        for i in customers_dict:
            print(customers_dict[i])
            if customers_dict[i].get_password() == password:
                print(f"Customer {customers_dict[i].get_username} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print(customers_dict[i].get_password())
                print(password)
                print(customers_dict[i])
                error = "Username or password incorrect!"
        db.close()
    elif request.method == 'POST' and (customer_login_form.changelogin.data == 'staff'):
        staff_dict = {}
        db = shelve.open('staff.db', 'c')
        password = customer_login_form.password.data
        staff_dict = db['Staff']
        if 'logout' in customer_login_form:
            print("III")
            session['Username'] = None
        for i in staff_dict:
            print(staff_dict[i])
            if staff_dict[i][1] == password:
                print(f"Staff {staff_dict[i][0]} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print("Staff not found")
                print(password)
                print(staff_dict[i][1])
                error = "Username or password incorrect!"
        db.close()
        #login(session)end

    create_customer_form = Forms.CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        print("EEE")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")

        customer = Customer.Customer(create_customer_form.username.data,
            create_customer_form.first_name.data,
                                     create_customer_form.last_name.data,
                                     create_customer_form.gender.data,
                                     create_customer_form.membership.data,
                                     create_customer_form.remarks.data,
                                     create_customer_form.email.data,
                                     create_customer_form.birthday.data,
                                     create_customer_form.address.data,
                                     create_customer_form.password.data)
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        customers_dict = db['Customers']
        customer = customers_dict[customer.get_customer_id()]
        print(customer.get_first_name(), customer.get_last_name(), "was stored in user.db successfully with user_id ==",
              customer.get_customer_id())

        db.close()
        return redirect('/')
    return render_template('createCustomer.html', form=create_customer_form)


@app.route('/booknow' ,methods=['GET', 'POST'])
def booknow():

    #login(session)
    error= None
    customer_login_form =  Forms.CustomerLoginForm(request.form)
    print(customer_login_form.changelogin.data)
    print(customer_login_form.data)
    if customer_login_form.logout.data != None:
            print("III")
            session['Username'] = None
    if request.method == 'POST' and (customer_login_form.changelogin.data == 'customer'):
        print("login form ok")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        password = customer_login_form.password.data
        customers_dict = db['Customers']
        print(customers_dict)
        for i in customers_dict:
            print(customers_dict[i])
            if customers_dict[i].get_password() == password:
                print(f"Customer {customers_dict[i].get_username} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print(customers_dict[i].get_password())
                print(password)
                print(customers_dict[i])
                error = "Username or password incorrect!"
        db.close()
    elif request.method == 'POST' and (customer_login_form.changelogin.data == 'staff'):
        staff_dict = {}
        db = shelve.open('staff.db', 'c')
        password = customer_login_form.password.data
        staff_dict = db['Staff']
        if 'logout' in customer_login_form:
            print("III")
            session['Username'] = None
        for i in staff_dict:
            print(staff_dict[i])
            if staff_dict[i][1] == password:
                print(f"Staff {staff_dict[i][0]} logged in")
                session['Username'] = customer_login_form.username.data
                session.permanent = True
            else:
                print("Staff not found")
                print(password)
                print(staff_dict[i][1])
                error = "Username or password incorrect!"
        db.close()
        #login(session)end

    if request.method == 'POST':
        data = request.form
        print(data.values)
        print(list(data))
        with shelve.open('order_data', 'c') as db:
            orderid_list = []
            dictte = {}
            for i in db:
                orderid_list.append(i)
            orderid_list.sort()
            orderid = int(orderid_list[-1]) + 1
            dictte['order_id'] = orderid
            for i in list(data):
                dictte[i] = data[i]
            total_amount = Orders.calculate_price(dictte['destination'], int(dictte['adults']), int(dictte['children']))

            key_names = ["adult_price", "children_price", "total_amount"]
            num = 0
            for i in total_amount:
                dictte[key_names[num]] = str(i)
                num += 1
            dictte["Refunded"] = "F"
            print(dictte)
            db[str(dictte['order_id'])] = dictte

            for i in db:
                for a in db[i].values():
                    print(type(a))
                print(f"{i}, {db[i]}")


        msg = Message('Hello', sender = 'xuanhongtay@gmail.com', recipients = [f'{data["email"]}'])
        msg.body = f"Dear Mr/Mrs {data['lastname']}, \n You have succesfully booked our trip to {data['destination']}. \nThe departure date will be on {data['departure']} at {data['airport']}. \n Thank you for choosing to fly with EcoVoyage!"
        mail.send(msg)


        return redirect('/show_payment_method')

    return render_template('Booknow.html')




@app.route('/test')
def test():
    return render_template('staffpage.html')


@app.route('/staff_booking_page', methods=['GET'])
def show_orders():
    with shelve.open('order_data') as db:  # Replace 'order_db' with your database name
        orders = list(db.values())
        orders.reverse()
    # Get the 'start' index from query parameters, defaulting to 0 if not present
    start = int(request.args.get('start', 0))

    # Prevent negative start index
    start = max(start, 0)  # This line handles the negative start index

    # Calculate the 'end' index for pagination (exclusive)
    end = start + 10

    # Slice the orders list to retrieve the appropriate subset
    orders_to_display = orders[start:end]

    # Render the template, passing the orders, start, and end values
    return render_template('staff_bookings_page.html', orders=orders_to_display, start=start, end=end)


@app.route('/update_order/<int:id>', methods=['GET', 'POST'])
def update_order(id):
    id = str(id)
    update_order_form = CreateOrderForm(request.form)
    if request.method == 'POST':
        db = shelve.open('order_data', 'c')
        order = db[id]
        print('Before update')
        print(order)
        order['firstname'] = update_order_form.first_name.data
        order['lastname'] = update_order_form.last_name.data
        order['email'] = update_order_form.email.data
        order['phone'] = update_order_form.phone.data
        order['destination'] = update_order_form.destination.data
        order['adults'] = update_order_form.number_of_adult_ticket.data
        order['children'] = update_order_form.number_of_child_ticket.data
        # total_amount = int(order['destination price']) * int(order['number of ticket'])
        # order['Total amount'] = str(total_amount)
        key_names = ["adult_price", "children_price", "total_amount"]
        num = 0
        for i in Orders.calculate_price(order['destination'], int(order['adults']), int(order['children'])):
            print(i)
            order[key_names[num]] = i
            num += 1

        print('Updated')
        print(order.values())
        db[id] = order
        db.close()

        return redirect('/staff_booking_page')
    else:
        db = shelve.open('order_data', 'r')
        order_dict = []
        id = str(id)
        print(db)
        for value in db[id].values():
            order_dict.append(str(value))

        order = order_dict
        print(order)
        update_order_form.first_name.data = order[1]
        update_order_form.last_name.data = order[2]
        update_order_form.email.data = order[3]
        update_order_form.phone.data = order[4]
        update_order_form.destination.data = order[6]
        update_order_form.number_of_adult_ticket.data = order[8]
        update_order_form.number_of_child_ticket.data = order[9]
        return render_template('update_order.html', form=update_order_form)



@app.route('/refund/<int:id>')
def refund(id):

    print('Refunded')
    id = str(id)
    # if request.method == 'POST':
    db = shelve.open('order_data', 'c')
    order = db[id]
    print('Before update')
    print(order)

    if order['Refunded'] == 'F':
        order['Refunded'] = 'T'

        print('Updated')
        print(order.values())
    db[id] = order
    db.close()

    return redirect('/staff_booking_page')


@app.route('/delete_order/<int:id>')
def delete(id):
    try:
        with shelve.open('order_data', 'c') as db:
            id = str(id)
            db.pop(id)
            if db[id] in db:
                for i in db:
                    print(f'{type(i)}, {db[i]}')
        return redirect('/staff_booking_page')
    except:
        return redirect('/staff_booking_page')



@app.route('/Export_to_csv')
def export():
    with open('order_data_export.csv', 'w', newline='') as file:
        with shelve.open('order_data', 'c') as db:
            writer = csv.writer(file)
            writer.writerow(["order_id", "firstname", "lastname", "email", "phone", "airport", "destination", "departure",
                             "Number of Adults", "Number of Children", "Card number", "Cardholder", "Card expiry",
                             "Card sec", "Adult price",
                             "Children price", "total_amount", "Refunded"])
            for i in db:
                x = db[i].values()
                # print(list(x))
                writer.writerow(x)
        return redirect('/staff_booking_page')


@app.route('/showall')
def show():
    return flask.redirect('/plotly/')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback_pg():
    create_feedback_form = CreateFeedbackForm(request.form)
    print('This code works')
    # If method is POST, it adds data
    if request.method == 'POST':
        feedbacks_list = []

        db = shelve.open('feedback.db', 'c')

        try:
            feedbacks_list = db['Feedbacks']
            print('Debugging')
            for feedback in feedbacks_list:
                print(feedback)
            print(f'Feedback dict type => {type(feedbacks_list)}')
        except:
            print('Error in retrieving feedback data from feedback.db')

        feedback = Feedback.Feedback(
            create_feedback_form.name.data,
            create_feedback_form.star_rating.data,
            create_feedback_form.title.data,
            create_feedback_form.message.data,
            datetime.now().strftime('%Y-%m-%d')
        )
        print(feedback.name)
        print(feedback.star_rating)
        print(feedback.title)
        print(feedback.message)
        print(feedback.date_submitted)

        feedbacks_list.append(feedback)
        db['Feedbacks'] = feedbacks_list

        if len(feedbacks_list) > 8:
            early_feedbacks = feedbacks_list[:8]
        else:
            early_feedbacks = feedbacks_list[:]

        #return render_template('feedback_page.html', early_feedbacks=early_feedbacks)
        return redirect(url_for('feedback_pg', early_feedbacks=early_feedbacks))

    # If method is GET, it reads data
    db = shelve.open('feedback.db', 'c')

    try:
        feedbacks_list = db['Feedbacks']
        early_feedbacks = []

        if len(feedbacks_list) > 8:
            early_feedbacks = feedbacks_list[:8]
        else:
            early_feedbacks = feedbacks_list[:]

        return render_template('feedback_page.html', early_feedbacks=early_feedbacks)

    except Exception as e:
        print(f'ERROR: {e}')
        print(traceback.print_exc())

    return render_template('error_found.html')


@app.route('/test_feedback', methods=['GET', 'POST'])
def test_feedback_pg():
    create_feedback_form = CreateFeedbackForm(request.form)

    feedbacks_list = []

    db = shelve.open('feedback.db', 'c')

    # try:
    #     feedbacks_list = db['Feedbacks']
    #     print(f'Feedback dict type => {type(feedbacks_list)}')
    # except:
    #     print('Error in retrieving feedback data from feedback.db')

    feedback = Feedback.Feedback(
        'John Doe',
        4,
        'Testing',
        'Wtf bro now it is working!',
        datetime.now().strftime('%Y-%m-%d')
    )

    feedbacks_list.append(feedback)
    db['Feedbacks'] = feedbacks_list

    if len(feedbacks_list) > 8:
        early_feedbacks = feedbacks_list[:8]
    else:
        early_feedbacks = feedbacks_list[:]

    print('Test data is added successfully')
    print(feedbacks_list)
    print(early_feedbacks)

    return render_template('feedback_page.html', early_feedbacks=early_feedbacks)



@app.route('/show_payment_method')
def show_payment_method():
    return redirect('http://localhost:4242/checkout.html')


if __name__ == '__main__':
    app.run(debug=True)
