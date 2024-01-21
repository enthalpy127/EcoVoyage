import Customer
import User
import shelve
from datetime import timedelta
from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from flask_mail import Mail, Message

from Forms import CreateUserForm, CreateCustomerForm, CustomerLoginForm

app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = 'xuanhongtay@gmail.com'
app.config['MAIL_PASSWORD'] = 'mrxs dofi hmgd murd'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
app.static_folder = 'static'


@app.route('/', methods=['GET','POST'])
def home():
    #login(session)
    error= None
    customer_login_form =  CustomerLoginForm(request.form)
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
    customer_login_form =  CustomerLoginForm(request.form)
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
    customer_login_form =  CustomerLoginForm(request.form)
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
    customer_login_form =  CustomerLoginForm(request.form)
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
    return render_template('Denmark.html')

@app.route('/singapore', methods=['GET','POST'])
def singapore():
    #login(session)
    error= None
    customer_login_form =  CustomerLoginForm(request.form)
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
    return render_template('Singapore.html')

@app.route('/switzerland', methods=['GET','POST'])
def switzerland():
    #login(session)
    error= None
    customer_login_form =  CustomerLoginForm(request.form)
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
    return render_template('Switzerland.html')

@app.route('/thailand', methods=['GET','POST'])
def thailand():
    #login(session)
    error= None
    customer_login_form =  CustomerLoginForm(request.form)
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
    return render_template('Thailand.html')

@app.route('/createUser', methods=['GET', 'POST'])
def create_user():

    #login(session)
    error= None
    customer_login_form =  CustomerLoginForm(request.form)
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

    #login(session)
    error= None
    customer_login_form =  CustomerLoginForm(request.form)
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

    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        print("EEE")
        customers_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")

        customer = Customer.Customer(create_customer_form.first_name.data,
                                     create_customer_form.last_name.data,
                                     create_customer_form.gender.data,
                                     create_customer_form.membership.data,
                                     create_customer_form.remarks.data,
                                     create_customer_form.email.data,
                                     create_customer_form.birthday.data,
                                     create_customer_form.address.data,
                                     create_customer_form.username.data,
                                     create_customer_form.password.data)
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        customers_dict = db['Customers']
        customer = customers_dict[customer.get_customer_id()]
        print(customer.get_first_name(), customer.get_last_name(), "was stored in user.db successfully with user_id ==",
              customer.get_customer_id())

        db.close()
        return redirect()
    return render_template('createCustomer.html', form=create_customer_form)


@app.route('/booknow' ,methods=['GET', 'POST'])
def booknow():

    #login(session)
    error= None
    customer_login_form =  CustomerLoginForm(request.form)
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
        msg = Message('Hello', sender = 'xuanhongtay@gmail.com', recipients = [f'{data["email"]}'])
        msg.body = f"Dear Mr/Mrs {data['lastname']}, \n You have succesfully booked our trip to {data['destination']}. \nThe departure date will be on {data['departure']} at {data['airport']}. \n Thank you for choosing to fly with EcoVoyage!"
        mail.send(msg)
        return render_template('index.html')

    return render_template('Booknow.html')

@app.route('/test')
def test():
    return render_template('staffpage.html')


if __name__ == '__main__':
    app.run(debug=True)
