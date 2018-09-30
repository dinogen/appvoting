#!/usr/bin/env python3
import os
from flask import Flask, render_template,request,redirect,url_for
from flask_login import LoginManager, login_required, current_user,login_user,logout_user
import user
import votation
import candidate
import guarantor
import backend

app = Flask(__name__)
app.secret_key = os.urandom(24) 
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
        #v.votation_id = request.form['votation_id']
        v.votation_description = request.form['votation_description']
        v.begin_date = request.form['begin_date']
        v.end_date = request.form['end_date']
        v.votation_type = request.form['votation_type']
        v.promoter_user = current_user.u
        v.votation_status = votation.STATUS_WAIT_FOR_CAND_AND_GUAR
        result, message = votation.validate_dto(v)
        if result:
            if votation.insert_votation_dto(v):
                message = "Your votation is saved"
            else:
                message = "Error, your votation is not saved"                    
    return render_template('votation_propose_template.html', pagetitle="Start a Votation", \
    votation_obj=v, message=message)

@app.route("/votation_list", methods=['GET', 'POST'])
@login_required
def votation_list():
    votations_array = votation.load_votations()
    return render_template('votation_list_template.html', pagetitle="Votation List", \
    votations_array=votations_array,states=votation.states)

@app.route("/be_a_candidate/<int:votation_id>")
@login_required
def be_a_candidate(votation_id):
    v = votation.load_votation_by_id(votation_id)
    return render_template('be_a_candidate_template.html', pagetitle="Candidate confirm", v=v)

@app.route("/be_a_guarantor/<int:votation_id>")
@login_required
def be_a_guarantor(votation_id):
    v = votation.load_votation_by_id(votation_id)
    return render_template('be_a_guarantor_template.html', pagetitle="Guarantor confirm", v=v)

@app.route("/be_a_candidate_confirm")
@login_required
def be_a_candidate_confirm():
    votation_id = int(request.args.get('votation_id'))
    v = votation.load_votation_by_id(votation_id)
    message = "Now, you are a candidate"
    o = candidate.candidate_dto()
    app.logger.info(o)
    o.votation_id = votation_id
    o.u.user_id = current_user.u.user_id
    o.passphrase_ok = 0
    error = candidate.validate_dto(o)
    if error == 0:
        candidate.insert_dto(o)
    else:
        message = candidate.error_messages[error] + ": " + v.votation_description 
    return render_template('be_a_candidate_confirm_template.html', pagetitle="Candidate confirm", v=v,message=message)

@app.route("/be_a_guarantor_confirm")
@login_required
def be_a_guarantor_confirm():
    votation_id = int(request.args.get('votation_id'))
    v = votation.load_votation_by_id(votation_id)
    message = "Now, you are a guarantor"
    o = guarantor.guarantor_dto()
    #app.logger.info(o)
    o.votation_id = votation_id
    o.u = current_user.u
    o.hash_ok = 0
    o.passphrase_ok = 0
    error = guarantor.validate_dto(o)
    if error == 0:
        guarantor.insert_dto(o)
    else:
        message = guarantor.error_messages[error] + ": " + v.votation_description 
    return render_template('be_a_guarantor_confirm_template.html', pagetitle="Guarantor confirm", v=v,message=message)

@app.route("/votation_detail/<int:votation_id>")
@login_required
def votation_detail(votation_id):
    v = votation.load_votation_by_id(votation_id)
    candidates_array = candidate.load_candidate_by_votation(votation_id)
    guarantors_array = guarantor.load_guarantor_by_votation(votation_id)
    return render_template('votation_detail_template.html', pagetitle="Votation detail", \
    v=v, candidates_array=candidates_array, guarantors_array=guarantors_array,states=votation.states)

@app.route("/start_election/<int:votation_id>")
@login_required
def start_election(votation_id):
    v = votation.load_votation_by_id(votation_id)
    candidates_array = None
    guarantors_array = None
    if current_user.u.user_id == v.promoter_user.user_id:
        candidates_array = candidate.load_candidate_by_votation(votation_id)
        guarantors_array = guarantor.load_guarantor_by_votation(votation_id)
        # TODO error handling
        backend.create_election(v.votation_id, len(candidates_array), len(guarantors_array) )
        votation.update_status(votation_id, votation.STATUS_WAIT_FOR_GUAR_HASHES)
    return render_template('start_election_template.html', pagetitle="Start Election", \
      v=v, candidates_array=candidates_array, guarantors_array=guarantors_array)

@app.route("/send_passphrase", methods=['POST',])
@login_required
def send_passphrase():
    message = None
    votation_id = int(request.form['votation_id'])
    passphrase = request.form['passphrase']
    v = votation.load_votation_by_id(votation_id)
    u = current_user.u
    if v.votation_status == votation.STATUS_WAIT_FOR_GUAR_HASHES:
        # TODO scramble the key in the javascript
        # TODO handle this with ajax
        hash_key = "bla bla bla" # TODO in the javascript
        # TODO error handling
        backend.guarantor_send_hash(votation_id, u.user_id, hash_key)
        message = "Guarantor, your passphrase was registered."
        guarantor.set_hash_ok(u.user_id,votation_id)
        # check if every guarantors has sent the hash
        if guarantor.guarantors_hash_complete(votation_id):
            votation.update_status(votation_id,votation.STATUS_WAIT_FOR_CAND_KEYS)
    if v.votation_status == votation.STATUS_WAIT_FOR_CAND_KEYS:
        backend.candidate_send_passphrase(votation_id,u.user_id,passphrase)
        message = "Candidate, your passphrase was registered."
        candidate.set_passphrase_ok(u.user_id,votation_id)
        if candidate.candidates_passphrases_complete(votation_id):
            votation.update_status(votation_id,votation.STATUS_WAIT_FOR_GUAR_KEYS)
    if v.votation_status == votation.STATUS_WAIT_FOR_GUAR_KEYS:
        backend.guarantor_confirm_passphrase(votation_id, u.user_id, passphrase)
        message = "Guarantor, your passphrase was confirmed."
        guarantor.set_passphrase_ok(u.user_id,votation_id)
        if guarantor.guarantors_passphrase_complete(votation_id):
            votation.update_status(votation_id,votation.STATUS_CALCULATION)
    return render_template('thank_you_template.html', pagetitle="Thank you", message=message)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


@app.route("/version")
def print_version():
    return render_template('version_template.html', pagetitle="Thank you", version=os.environ['version'])
  
   

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
