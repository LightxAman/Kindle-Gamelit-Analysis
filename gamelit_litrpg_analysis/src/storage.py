# TODO: Implement storage.py
import pandas as pd
from sqlalchemy import create_engine
from .utils import load_config

config = load_config()
engine = create_engine(config['database_url'])


def save_books(books, table_name="books"):
    df = pd.DataFrame(books)
    df.to_sql(table_name, con=engine, if_exists='append', index=False)


def save_reviews(reviews, table_name="reviews"):
    df = pd.DataFrame(reviews)
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
