import psycopg2  # type: ignore # noqa # pylint: disable=unused-import

from models import Base

from dotenv import load_dotenv
from os import getenv
from sqlalchemy import create_engine


try:
    load_dotenv()
except Exception as e:
    print("Error loading .env file:", str(e))
    raise

# DATABASE_URI = "database+driver://username:password@host:port/database_name"
DATABASE_URI = f"postgresql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@localhost:{getenv('DB_PORT')}/{getenv('DB_NAME')}"


engine = create_engine(DATABASE_URI, echo=True)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection successful!")
        connection.close()
except Exception as e:
    print("Connection failed:", str(e))


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine, checkfirst=True)
    print("#" * 80)
    print("Tables created successfully!")
    print("#" * 80)
