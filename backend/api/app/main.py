from dotenv import load_dotenv
from fastapi import FastAPI, Depends, Query
from os import getenv
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing import Annotated, AsyncGenerator, Optional
from uuid import UUID

from app.models import Tenant, Farm


app = FastAPI()

try:
    load_dotenv()
except Exception as e:
    print("Error loading .env file:", str(e))
    raise


# DATABASE_URI = "postgresql+asyncpg://<db_user>:<db_password>@<db_host>:<db_port>/<db_name>"
DATABASE_URI = f"postgresql+asyncpg://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}"

engine = create_async_engine(url=DATABASE_URI, echo=False, future=True)

async_session = async_sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession, autoflush=True, autocommit=False
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    print(DATABASE_URI)
    async with async_session() as db_session:
        try:
            db_session.begin()
            yield db_session
        except Exception as e:
            await db_session.rollback()
            print("Async session failed:", str(e))
            raise
        finally:
            await db_session.close()


@app.get("/")
async def root():
    return {"message": "Hello Hydrostat User!"}


@app.get("/tenants")
async def get_tenants(db_session: AsyncSession = Depends(get_session)):
    result = await db_session.execute(select(Tenant).order_by(Tenant.name))

    # # commit database session
    await db_session.commit()

    return result.scalars().all()


@app.get("/farms/")
async def get_farms(
    tenant_id: Annotated[
        Optional[UUID], Query(example="8a480af3-7c2e-415e-bb3e-e1c18fe7aace")
    ] = None,
    db_session: AsyncSession = Depends(get_session),
):
    if tenant_id is None:
        result = await db_session.execute(select(Farm).order_by(Farm.name))
    else:
        result = await db_session.execute(select(Farm).filter(Farm.tenant_id == tenant_id))

    # # commit database session
    await db_session.commit()

    return result.scalars().all()
