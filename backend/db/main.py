import psycopg2  # type: ignore # noqa # pylint: disable=unused-import

from sqlalchemy import create_engine
from db.models import Base

# DATABASE_URI = "postgresql://your_username:your_password@your_host/your_database"
DATABASE_URI = "postgresql://postgres:postgres@localhost:5433/hydrostat_db"

engine = create_engine(DATABASE_URI, echo=True)

# Test the connection
try:
    connection = engine.connect()
    print("Connection successful!")
    connection.close()
except Exception as e:
    print("Connection failed:", str(e))


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine, checkfirst=True)
    print("#" * 80)
    print("Tables created successfully!")
    print("#" * 80)
