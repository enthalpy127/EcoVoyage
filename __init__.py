from flask import Flask, render_template, request, redirect, url_for
from Login.Forms import CreateUserForm, CreateCustomerForm
import shelve
from Login import User, Customer

import traceback

app = Flask(__name__)

app.static_folder = 'static'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Staff_Login_page')
def staff_login_page():
    return render_template('Staff_Login_page.html')


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
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
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
                                     create_customer_form.date_joined.data,
                                     create_customer_form.address.data,
                                     create_customer_form.password.data)
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        customers_dict = db['Customers']
        customer = customers_dict[customer.get_customer_id()]
        print(customer.get_first_name(), customer.get_last_name(), "was stored in user.db successfully with user_id ==",
              customer.get_customer_id())

        db.close()
        return redirect(url_for('home'))
    return render_template('createCustomer.html', form=create_customer_form)


@app.route('/login')
def login():
    return render_template('Login_page.html')


@app.route('/retrieveData', methods=['GET', 'POST'])
def retrieveData():
    db1 = shelve.open('user.db', 'c')
    db2 = shelve.open('customer.db', 'c')

    try:
        users_dict = db1['Users']
        keys = users_dict.keys()
        for key in keys:
            print(users_dict[key].get_first_name(), users_dict[key].get_last_name())

        users_list = []
        for key in users_dict:
            user = users_dict.get(key)
            users_list.append(user)

        print('\n')


        customers_dict = db2['Customers']
        keys = customers_dict.keys()
        for key in keys:
            print(customers_dict[key].get_first_name(), customers_dict[key].get_last_name())

        customers_list = []
        for key in customers_dict:
            customer = customers_dict.get(key)
            customers_list.append(customer)

        return render_template('retrieveData.html',
                               count1=len(users_list),
                               users_list=users_list,
                               count2=len(customers_list),
                               customers_list=customers_list)

    except Exception as e:
        print(f'ERROR: {e}')
        print(traceback.print_exc())

    return render_template('error_found.html')


@app.route('/updateUser/<string:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)

    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')
        users_dict = db['Users']
        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_password(update_user_form.password.data)
        user.set_gender(update_user_form.gender.data)
        user.set_membership(update_user_form.membership.data)
        user.set_remarks(update_user_form.remarks.data)
        db['Users'] = users_dict
        db.close()
        print('Updated!')
        return redirect(url_for('retrieveData'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()
        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.password.data = user.get_password()
        update_user_form.gender.data = user.get_gender()
        update_user_form.membership.data = user.get_membership()
        update_user_form.remarks.data = user.get_remarks()
        print('Show info')
        print(f'FORM ERROR: {update_user_form.errors}')
        return render_template('updateUser.html', form=update_user_form)


@app.route('/updateCustomer/<string:id>/', methods=['GET', 'POST'])
def update_customer(id):
    update_customer_form = CreateCustomerForm(request.form)

    if request.method == 'POST' and update_customer_form.validate():

        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_first_name(update_customer_form.first_name.data)
        customer.set_last_name(update_customer_form.last_name.data)
        customer.set_password(update_customer_form.password.data)
        customer.set_gender(update_customer_form.gender.data)
        customer.set_email(update_customer_form.email.data)
        customer.set_date_joined(update_customer_form.date_joined.data)
        customer.set_address(update_customer_form.address.data)
        customer.set_membership(update_customer_form.membership.data)
        customer.set_remarks(update_customer_form.remarks.data)

        db['Customers'] = customers_dict
        db.close()

        print('Updated successfully')

        return redirect(url_for('retrieveData'))

    else:

        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.first_name.data = customer.get_first_name()
        update_customer_form.last_name.data = customer.get_last_name()
        update_customer_form.password.data = customer.get_password()
        update_customer_form.gender.data = customer.get_gender()
        update_customer_form.email.data = customer.get_email()
        update_customer_form.date_joined.data = customer.get_date_joined()
        update_customer_form.address.data = customer.get_address()
        update_customer_form.membership.data = customer.get_membership()
        update_customer_form.remarks.data = customer.get_remarks()

        print('Show Info')

        return render_template('updateCustomer.html', form=update_customer_form)


@app.route('/deleteUser/<string:id>', methods=['POST'])
def delete_user(id):

    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    return redirect(url_for('retrieveData'))


@app.route('/deleteCustomer/<string:id>', methods=['POST'])
def delete_customer(id):

    customers_dict = {}
    db = shelve.open('customer.db', 'w')
    customers_dict = db['Customers']

    customers_dict.pop(id)

    db['Customers'] = customers_dict
    db.close()

    return redirect(url_for('retrieveData'))


if __name__ == '__main__':
    app.run(debug=True)