########################################################################################
######################          Import packages      ###################################
########################################################################################
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User,users
from flask_login import login_user, logout_user, login_required, current_user
import ibm_db
from utils.ibm_tools import ibm_ob
import requests
import json
import numpy
from utils.helper import yield_pred
auth = Blueprint('auth', __name__) # create a Blueprint object that we name 'auth'


@auth.route('/login', methods=['GET', 'POST']) # define login page path
def login(): # define login page fucntion
    if request.method=='GET': # if the request is a GET we return the login page
        return render_template('login.html')
    else: # if the request is POST the we check if the user exist and with te right password
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = ibm_ob.get_data(email)
        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user:
            flash('Please sign up before!')
            return redirect(url_for('auth.signupasfarmer'))
        elif not check_password_hash(user['PASSWORD'], password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
        # if the above check passes, then we know the user has the right credentials
        users[user['ID']]=User(id=user['ID'],name=user['NAME'],email=user['EMAIL'],password=user['PASSWORD'],typeofuser=user['TYPEOFUSER'])
        user1=User.get(user['ID'])
        login_user(user1, remember=remember)

        return redirect(url_for('main.index'))

@auth.route('/signupasfarmer', methods=['GET', 'POST'])# we define the sign up path
def signupasfarmer(): # define the sign up function
    if request.method=='GET': # If the request is GET we return the sign up page and forms
        return render_template('signupasfarmer.html')
    else: # if the request is POST, then we check if the email doesn't already exist and then we save data
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        user = ibm_ob.get_data(email)
        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('auth.signupasfarmer'))
        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        password=generate_password_hash(password, method='sha256')
        ibm_ob.insert_row(email,name,password,typeofuser='farmer')        
        return redirect(url_for('auth.login'))


@auth.route('/signupbuyer', methods=['GET', 'POST'])# we define the sign up path
def signupbuyer(): # define the sign up function
    if request.method=='GET': # If the request is GET we return the sign up page and forms
        return render_template('signupbuyer.html')
    else: # if the request is POST, then we check if the email doesn't already exist and then we save data
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        user = ibm_ob.get_data(email)
        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('auth.signupbuyer'))
        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        password=generate_password_hash(password, method='sha256')
        ibm_ob.insert_row(email,name,password,typeofuser='buyer')        
        return redirect(url_for('auth.login'))

@auth.route('/farmboard') # define logout path
@login_required
def farmboard(): #define the logout function
    return render_template('farmboard.html')

@auth.route('/logout') # define logout path
@login_required
def logout(): #define the logout function
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/prediction', methods=['GET', 'POST']) 
@login_required
def prediction():
    if request.method=='GET': # If the request is GET we return the sign up page and forms
        return render_template('prediction.html')
    


@auth.route('/farmerupload', methods=['GET', 'POST']) 
@login_required
def farmerupload():
    if request.method=='GET': # If the request is GET we return the sign up page and forms
        return render_template('farmerupload.html')

@auth.route('/buyer', methods=['GET', 'POST']) 
@login_required
def buyer():
    if request.method=='GET': # If the request is GET we return the sign up page and forms
        return render_template('buyer.html')

@auth.route('/getnpkvalues', methods=['GET','POST'])
def getnpkvalues():
    r=requests.get('http://169.57.96.248:32450/data')
    return r.json()


@auth.route('/croprecomm',methods=['POST'])
def get_javascript_data():
    if request.method=='POST':
        data=request.get_json()
        for i in range(len(data)):
            data[i]=float(data[i])
        
        # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
        API_KEY = "3vJ4WahpXCOtxmOvW4emBWPYpqNPaHDHu0mCnYv0aX3v"
        token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
        mltoken = token_response.json()["access_token"]

        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = payload_scoring = {"input_data": [{"field": [["N","P","K","temperature","humidity","ph","rainfall"]], "values":  [[data[0],data[1],data[2],data[3],data[4],data[5],data[6]]]}]}

        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5fb4c671-0103-476c-9567-331ce552497d/predictions?version=2021-09-02', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
        # print("Scoring response")
        # print(response_scoring.json()['predictions'][0]['values'][0][0])
        return {"values":response_scoring.json()['predictions'][0]['values'][0][0]}

@auth.route('/cropprod',methods=['POST'])
def get_javascript():
    if request.method=='POST':
        data=request.get_json()
        data[1]=data[1].upper()
        data[4]=float(data[4])
        x=yield_pred(data)
        return {"production":x}


@auth.route('/farmeruploadform', methods=['GET', 'POST']) 
@login_required
def farmeruploadform():
    if request.method=='GET': # If the request is GET we return the sign up page and forms
        return render_template('farmerupload.html')
    if request.method=='POST':        
        state=request.form.get('state')
        district=request.form.get('district')
        crop=request.form.get('inputcrop')
        price=request.form.get('price')
        crop_qty=request.form.get('crop_qty')
        ibm_ob.insert_farmer_data(state,district,crop,price,crop_qty)

        return redirect(url_for('auth.farmeruploadform'))

@auth.route('/farmerupdatedata', methods=['GET','POST'])
def farmerupdatedata():
    return json.dumps(ibm_ob.update_farmer_data())


@auth.route('/buyergetdata', methods=['GET','POST'])
def buyergetdata():
    return json.dumps(ibm_ob.buyergetdata())

@auth.route('/buyergetdatabystate', methods=['GET','POST'])
def buyergetdatabystate():
    print("hello")
    if request.method=='POST':
        state=request.get_json()
        return json.dumps(ibm_ob.buyergetdatabystate(state))

@auth.route('/buyerform', methods=['GET', 'POST']) 
@login_required
def buyerform():
    if request.method=='GET': # If the request is GET we return the sign up page and forms
        return render_template('buyer.html')
    if request.method=='POST': 
        ref_id=request.form.get('reference_id')
        farm_id=request.form.get('farmid')
        crop=request.form.get('inputcropbuyer')
        price=request.form.get('pricebuyer')
        crop_qty=request.form.get('qtybuyer')
        ph_no=  request.form.get('ph_no')     
        ibm_ob.buyerformupdate(ref_id,farm_id,crop,price,crop_qty,ph_no)
        return redirect(url_for('auth.buyerform'))

@auth.route('/responsedatafrombuyer', methods=['GET','POST'])
def responsedatafrombuyer():
    return json.dumps(ibm_ob.responsedatafrombuyer())

@auth.route('/responsefromfarmer', methods=['GET', 'POST']) 
@login_required
def responsefromfarmer():
    if request.method=='GET': # If the request is GET we return the sign up page and forms
        return render_template('farmerupload.html')
    if request.method=='POST': 
        buyer_id=request.form.get('buyer_id')
        farm_id=request.form.get('farm_unique_id')
        crop_qty=request.form.get('crop_qnty')
        print(buyer_id,farm_id,crop_qty)
        ibm_ob.updatebothtable(buyer_id,farm_id,crop_qty)

        return redirect(url_for('auth.farmerupload'))

@auth.route('/getsoldcrop', methods=['GET', 'POST']) 
@login_required
def getsoldcrop():
    return json.dumps(ibm_ob.getsoldcrop())

@auth.route('/approvedcrop', methods=['GET', 'POST']) 
@login_required
def approvedcrop():
    return json.dumps(ibm_ob.approvedcrop())

@auth.route('/for_approval', methods=['GET', 'POST']) 
@login_required
def for_approval():
    return json.dumps(ibm_ob.for_approval())