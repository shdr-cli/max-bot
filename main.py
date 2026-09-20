import asyncio
import logging
import os

from dotenv import load_dotenv
from maxapi import Bot, Dispatcher, F
from maxapi.filters.command import CommandStart, Command
from maxapi.types import BotStarted, MessageCreated

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.bot_started()
async def bot_started(event: BotStarted) -> None:
    await bot.send_message(
        chat_id=event.chat_id,
        text=f"Привет {event.user.first_name}, отправь мне /start"
    )

@dp.message_created(CommandStart())
async def welcome(event: MessageCreated) -> None:
    await event.message.answer(
        "MAX 💙"
    )

@dp.message_created(F.message.body.text)
async def echo(event: MessageCreated):
    await event.message.answer(event.message.body.text)

async def main():
    await dp.start_polling(
        bot=bot,
        skip_updates=True
    )

if __name__ == "__main__":
    asyncio.run(main())