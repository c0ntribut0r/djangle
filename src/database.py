# https://fastapi.tiangolo.com/tutorial/sql-databases/
import databases
import sqlalchemy


# -------- database -----------
DATABASE_URL = "postgresql://user:password@postgresserver/db"
database = databases.Database(DATABASE_URL, min_size=5, max_size=20)

# metadata = sqlalchemy.MetaData()
# notes = sqlalchemy.Table(
#     "notes",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("text", sqlalchemy.String),
#     sqlalchemy.Column("completed", sqlalchemy.Boolean),
# )
# engine = sqlalchemy.create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
# metadata.create_all(engine)


async def db_connect():
    pass
    # await database.connect()


async def db_disconnect():
    pass
    # await database.disconnect()
