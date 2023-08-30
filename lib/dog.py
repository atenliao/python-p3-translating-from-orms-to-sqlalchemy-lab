from models import Dog


def create_table(Base,engine):
    Base.metadata.create_all(engine)
    
def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name.like(name)).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()
    

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name.like(name), Dog.breed.like(breed)).first()

def update_breed(session, dog, breed):
    return session.query(Dog).filter(Dog.name==dog.name).update({Dog.breed: breed})