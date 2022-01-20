# Import the modules required
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

# Create the engine
engine = create_engine(
    "postgresql+psycopg2://postgresql:postgresql@localhost:5432/data-prod"
)

# Initialize the session
session = Session(engine)

# Initialize the declarative base
Base = declarative_base()
