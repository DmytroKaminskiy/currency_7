import databases
import sqlalchemy

from fastapi import FastAPI, Header, HTTPException, status

from schemas import ZoomEventSchema
from models import zoom_events_table, metadata
from settings import settings


app = FastAPI()

############
# SQLAlchemy specific code, as with any other app
# DATABASE_URL = "sqlite:///./test.db"


DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@" \
               f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)  # creates all tables
############


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/webhooks/zoom-events")
async def webhook_zoom_events(
        zoom_event: ZoomEventSchema,
        authorization: str = Header(default='')
):

    # TODO move to env
    if authorization != 'LuRhbD9RS1yqdt11v_RLaw':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access is not  allowed",
        )

    query = zoom_events_table.insert().values(
        event=zoom_event.event,
        event_ts=zoom_event.event_ts,
        payload=zoom_event.payload,
    )
    await database.execute(query)

    return {}

'''
crewejoubruwn34081@randomail.io
NAawdnaj#663626#%@&&*

ORM
SQLAlchemy
ORM - class (sync, !await!)
core - functional (async, await)

!!!alembic.ini envs + try to migrate!!
'''