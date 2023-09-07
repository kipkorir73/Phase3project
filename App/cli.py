import click
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from datetime import datetime

# Define the database connection URL
DATABASE_URL = 'sqlite:///gym.db'  # Update this with your actual database URL

# Create a SQLAlchemy engine and session factory
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()
metadata = Base.metadata

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    date = Column(DateTime(timezone=True), server_default=func.now())
    name = Column(String(255), nullable=False)

class Billing(Base):
    __tablename__ = 'billing'
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    payment_date = Column(DateTime(timezone=True), server_default=func.now())

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Enter member name', help='Member name')
def add_member(name):
    session = Session()
    member = Member(name=name)
    session.add(member)
    session.commit()
    click.echo(f'Member "{name}" added successfully.')

@cli.command()
def init_db():
    """Initialize the database."""
    Base.metadata.create_all(bind=engine)
    click.echo('Initialized the database.')

@cli.command()
@click.argument('member_id', type=int)
def delete_member(member_id):
    session = Session()
    member = session.query(Member).filter_by(id=member_id).first()
    if member:
        session.delete(member)
        session.commit()
        click.echo(f'Member with ID {member_id} deleted successfully.')
    else:
        click.echo(f'Member with ID {member_id} not found.')

@cli.command()
@click.argument('member_id', type=int)
@click.option('--name', prompt='Enter new member name', help='New member name')
def update_member(member_id, name):
    session = Session()
    member = session.query(Member).filter_by(id=member_id).first()
    if member:
        member.name = name
        session.commit()
        click.echo(f'Member with ID {member_id} updated successfully.')
    else:
        click.echo(f'Member with ID {member_id} not found.')

@cli.command()
def list_members():
    session = Session()
    members = session.query(Member).all()
    click.echo('List of Members:')
    for member in members:
        click.echo(f'ID: {member.id}, Name: {member.name}, Active: {member.active}')

@cli.command()
@click.argument('member_id', type=int)
def list_billing(member_id):
    session = Session()
    member = session.query(Member).filter_by(id=member_id).first()
    if member:
        billings = session.query(Billing).filter_by(member_id=member.id).all()
        click.echo(f'List of Billings for Member {member.name}:')
        for billing in billings:
            click.echo(f'ID: {billing.id}, Amount: {billing.amount}, Date: {billing.payment_date}')
    else:
        click.echo(f'Member with ID {member_id} not found.')

@cli.command()
@click.argument('billing_id', type=int)
@click.option('--amount', type=int, prompt='Enter new billing amount', help='New billing amount')
def update_billing(billing_id, amount):
    session = Session()
    billing = session.query(Billing).filter_by(id=billing_id).first()
    if billing:
        billing.amount = amount
        session.commit()
        click.echo(f'Billing with ID {billing_id} updated successfully.')
    else:
        click.echo(f'Billing with ID {billing_id} not found.')

@cli.command()
@click.argument('member_id', type=int)
def record_attendance(member_id):
    session = Session()
    member = session.query(Member).filter_by(id=member_id).first()
    if member:
        attendance = Attendance(member_id=member.id, date=datetime.now(), name=member.name)
        session.add(attendance)
        session.commit()
        click.echo(f'Attendance recorded for Member ID {member.id}.')
    else:
        click.echo(f'Member with ID {member_id} not found.')

@cli.command()
@click.argument('member_id', type=int)
@click.option('--amount', type=int, prompt='Enter billing amount', help='Billing amount')
def add_billing(member_id, amount):
    session = Session()
    member = session.query(Member).filter_by(id=member_id).first()
    if member:
        billing = Billing(member_id=member.id, amount=amount)
        session.add(billing)
        session.commit()
        click.echo(f'Billing recorded for Member ID {member.id}.')
    else:
        click.echo(f'Member with ID {member_id} not found.')

if __name__ == '__main__':
    cli()
