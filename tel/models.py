import sqlalchemy


metadata = sqlalchemy.MetaData()


rate_table = sqlalchemy.Table(
    "currency_rate",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("buy", sqlalchemy.DECIMAL),
    sqlalchemy.Column("sale", sqlalchemy.DECIMAL),
)
