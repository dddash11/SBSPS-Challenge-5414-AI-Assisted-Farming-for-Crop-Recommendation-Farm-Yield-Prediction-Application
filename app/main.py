########################################################################################
######################          Import packages      ###################################
########################################################################################
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app
from newsapi import NewsApiClient
import datetime


# from __init__ import db
#####################################################################################
# our main blueprint
main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)



@main.route('/news')
def news():
    d1=datetime.date.today() + datetime.timedelta(-31)
    d2= datetime.date.today()
    d1=d1.strftime("%Y,%m,%d")
    d2=d2.strftime("%Y,%m,%d")
    d1="-".join(d1.split(','))
    d2="-".join(d2.split(','))
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    all_articles = newsapi.get_everything(q='Agriculture+Farmer+India',
                                      from_param=d1,
                                      to=d2,
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
    articles = all_articles['articles']
    myarticles={}
    for i in range(len(articles)):
        myarticles[i]=articles[i]
    return render_template('news.html', context = myarticles)

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    # db.create_all(app=create_app()) # create the SQLite database
    app.run() # run the flask app on debug mode