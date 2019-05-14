from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route('/')
def index():
    encoded_error = request.args.get('error')
    return render_template('index.html', error = encoded_error)

@app.route('/welcome', methods= ['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    email_error = " "
    username_error = " "
    password_error = " "
    verify_error  = " "
    error = False 

    if not len(email) == 0 :
            if not is_email(email) or not is_valid(email): 
                    error = True
                    email_error = "BAD EMAIL"

    if not is_valid(username):
            error = True
            username_error = "BAD USERNAME"

    if not is_valid(password):
            error = True
            password_error = "BAD PASSWORD"

    if verify != password:
            error = True
            verify_error = "BAD VERIFY"
            
    if error:
            return render_template('index.html', email_error= email_error, username_error = username_error, password_error = password_error, verify_error =verify_error)
           # return redirect('/?error' + email_error + username_error + password_error + verify_error)
    else:
            return render_template('welcome.html', username = username)


def is_valid(string):
    space_index = string.find(' ')
    space_present = space_index >= 0
    if space_present:
            return False
    else:
        length = len(string)
        correct_length = length >=3 and length <= 20
        return correct_length
        
def is_email(string):
    # for our purposes, an email string has an '@' followed by a '.'
    # there is an embedded language called 'regular expression' that would crunch this implementation down
    # to a one-liner, but we'll keep it simple:
    atsign_index = string.find('@')
    atsign_present = atsign_index >= 0
    if not atsign_present:
        return False
    else:
        domain_dot_index = string.find('.', atsign_index)
        domain_dot_present = domain_dot_index >= 0
        return domain_dot_present


if __name__ == "__main__":
     app.run()
[]