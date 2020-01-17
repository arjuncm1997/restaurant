from restaurant import db, app



class Login(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(20))
    image = db.Column(db.String(50))
    usertype = db.Column(db.String(20))


class AddCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.VARCHAR(200), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

class AddFood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemtype = db.Column(db.VARCHAR(200), nullable=False)
    timeinterval = db.Column(db.VARCHAR(200), nullable=False)
    category = db.Column(db.VARCHAR(200), nullable=False)
    foodname = db.Column(db.VARCHAR(200), nullable=False)
    amount = db.Column(db.VARCHAR(200), nullable=False)

class AddContact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.VARCHAR(200), nullable=False)
    lastname = db.Column(db.VARCHAR(200), nullable=False)
    email = db.Column(db.VARCHAR(200), nullable=False)
    subject = db.Column(db.VARCHAR(200), nullable=False)
    message = db.Column(db.VARCHAR(200), nullable=False)