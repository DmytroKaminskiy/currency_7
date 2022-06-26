from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

import httpx
import databases
import sqlalchemy
from sqlalchemy.sql import select



# https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples


# TODO move to env or use pydantic settings
TOKEN = '5445418074:AAF-1no0OkYORZ4d0o4cOLeWIdtoMTXehXg'
CURRENCY_URL = 'http://localhost:8000'
DATABASE_URL = f"postgresql://example_user:superSecretPassword@localhost:5432/currency"
# TODO move to env


class CurrencyAPIv1:
    RATES_GET = '/api/v1/rates/'
    SOURCES_GET = '/api/v1/sources/'

    def __init__(self, base_url: str):
        self.base_url = base_url

    async def rates_list(self):
        async with httpx.AsyncClient() as client:
            url = f'{CURRENCY_URL}{self.RATES_GET}'
            response = await client.get(url)
            return response.json()['results']


class CurrencyDB:
    def __init__(self, database_url):
        self.database_url = database_url

    async def rates_list(self):
        from models import rate_table

        database = databases.Database(self.database_url)
        # engine = sqlalchemy.create_engine(self.database_url)

        await database.connect()
        query = rate_table.select()
        rates = await database.fetch_all(query)
        await database.disconnect()

        result_rates = []
        for rate in rates:
            result_rates.append({
                'id': rate.id,
                'buy': rate.buy,
                'sale': rate.sale,
            })

        return str(result_rates)


# currency_api = CurrencyAPIv1(base_url=CURRENCY_URL)
currency_api = CurrencyDB(DATABASE_URL)


async def start(update: Update, context) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="/rates"),
            InlineKeyboardButton("Option 2", callback_data="/hello"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)

# TODO DEFAULT_TYPE is not defined
# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
async def hello(update: Update, context) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def rates_list(update: Update, context):
    response_json = await currency_api.rates_list()
    await update.message.reply_text(response_json)


async def button(update: Update, context) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("rates", rates_list))

app.run_polling()
