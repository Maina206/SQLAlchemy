from sqlalchemy.orm import sessionmaker
from models import User, engine

session = sessionmaker(bind=engine)

