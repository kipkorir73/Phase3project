from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Member  


engine = create_engine('sqlite:///gym.db')
Session = sessionmaker(bind=engine)
print("seeding.....")

fake = Faker()


session = Session()

for _ in range(5):  
    member = Member(
        name=fake.name(),
        active=fake.boolean(),
        
    )
    session.add(member)


session.commit()
