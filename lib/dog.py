from models import Dog
from sqlalchemy import create_engine

engine = create_engine('sqlite:///dogs.db')

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session,dog):
    session.add(dog)
    session.commit()
    
def get_all(session):
    fetch_all_dogs = session.query(Dog)
    all_dogs = [dog for dog in fetch_all_dogs]
    return all_dogs

def find_by_name(session, name):
    name_query = session.query(Dog).filter(Dog.name == name)
    return name_query.first()

def find_by_id(session, id):
    id_query = session.query(Dog).filter(Dog.id == id)
    return id_query.first()

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter(Dog.name.like(name), Dog.breed == breed)
    for name in dog:
        return name

def update_breed(session, dog, breed):
    name = dog.name
    the_dog = find_by_name(session,name)
    the_dog.breed = breed
    session.add(the_dog)
    session.commit()


# joey = Dog(name="joey", breed="cocker spaniel")
# save(session, joey)
# print(joey.name)