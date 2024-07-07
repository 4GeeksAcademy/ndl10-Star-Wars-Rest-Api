from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(55), nullable = False)
    films = db.Column(db.Integer, nullable = False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "films": self.films,
        }


class Vehicles(db.Model):
    __tablename__ = "Vehicles"
    id= db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(55), nullable = False)
    passengers = db.Column(db.Integer, db.ForeignKey('people.id'), nullable = False)
    films = db.Column(db.Integer, nullable = False)
                      
    passenger = db.relationship(People)
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "passengers": self.passengers,
            "films": self.films,
            
        }
    


class Planets(db.Model):
    __tablename__ = 'planets'

    Id = db.Column(db.Integer, primary_key = True)
    Name= db.Column(db.String(60), nullable = False, unique = True)
   

    def serialize(self):
        return {
            "Id": self.Id,
            "Name": self.Name,
            
        }
    
class Favorites(db.Model):
    __tablename__ = 'favorites'

    Id = db.Column(db.Integer, primary_key=True)
    user_Id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_Id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    planets_Id = db.Column(db.Integer, db.ForeignKey('planets.Id'), nullable=False)
    vehicles_Id = db.Column(db.Integer, db.ForeignKey('Vehicles.id'), nullable=False)

    user = db.relationship(User)
    people = db.relationship(People)
    planets = db.relationship(Planets)
    vehicles = db.relationship(Vehicles)

    def serialize(self):
        return { 
            "ID": self.Id,
            "user_Id": self.user_Id,
            "people_Id": self.people_Id,
            "planets_Id": self.planets_Id,
            "vehicles_Id": self.vehicles_Id
        }
