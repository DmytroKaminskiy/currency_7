from pydantic import BaseModel


class ZoomEventSchema(BaseModel):
    event: str
    event_ts: int
    payload: dict
