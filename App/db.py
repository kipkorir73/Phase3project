from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.config import Config
from alembic import command
from models import Base  

engine = create_engine('sqlite:///gym.db')
Session = sessionmaker(bind=engine)

def create_database():
    Base.metadata.create_all(engine)

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

if __name__ == '__main__':
    create_database()
    run_migrations()
