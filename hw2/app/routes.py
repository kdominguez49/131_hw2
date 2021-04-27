from flask import render_template, redirect
from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route("/", methods=['GET', 'POST'])
def home():
        form=MessageForm()
        if form.validate_on_submit():
           #check if if user exists in database
           #if not create user and add to database
           user = User.query.filter_by(author=form.author.data).first()
           if user is None :
                user = User(author=form.author.data)
                db.session.add(user)
                db.session.commit()
           #create row in Message table with user (created/found) add to ta database
           message= Messages( message=form.message.data, author=user)
           db.session.add(message)
           db.session.commit()
        
        posts=[]
        #get all messsages
        allmess = Messages.query.all()
        #for all messages
        for m in allmess:
            #append to posts {list of dictionaries}
            posts.append([ {'author': m.author.author, 'messages': m.message} ])
     
        #Is this output all messages?
        return render_template('home.html', posts=posts, form=form)