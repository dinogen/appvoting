from flask import Flask, render_template,request,redirect,url_for
from flask_login import LoginManager, login_required, current_user,login_user,logout_user
import user
import votation

app = Flask(__name__)
app.secret_key = "marcello ciao"
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_name):
    u = user.User(user_name)
    if u.is_valid():
        return u
    return None

@app.route("/")
@login_required
def index():
    return render_template('index_template.html', pagetitle="Votation")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':    
        user_name = request.form['user_name']
        pass_word = request.form['pass_word']
        u = user.User(user_name)
        if u.try_to_authenticate(pass_word):
            login_user(u)
    return render_template('login_template.html', pagetitle="Voting Login")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('logout_template.html', pagetitle="Voting Logout")

@app.route("/votation_propose", methods=['GET', 'POST'])
@login_required
def votation_propose():
    v = votation.get_blank_dto()
    message = "Please insert data"
    if request.method == 'POST':    
        v.votation_id = request.form['votation_id']
        v.votation_description = request.form['votation_description']
        v.begin_date = request.form['begin_date']
        v.end_date = request.form['end_date']
        v.votation_type = request.form['votation_type']
        v.promoter_user_id = current_user.u.user_id
        result, message = votation.validate_dto(v)
        if result:
            votation.insert_votation_dto(v)
            message = "Your votation is saved"
    return render_template('votation_propose_template.html', pagetitle="Votation Propose", votation_obj=v, message=message)

@app.route("/votation_list", methods=['GET', 'POST'])
@login_required
def votation_list():
    votations_array = votation.load_votations()
    return render_template('votation_list_template.html', pagetitle="Votation List", votations_array=votations_array)



@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True) 