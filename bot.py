import asyncio # это для запуска бота
from aiogram import Bot, Dispatcher, types # это библиотека для создания Tg-бота.
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)
#ReplyKeyboardMarkup - инициальзация обычной клавиатуры
# KeyboardButton - кнопка для обычной клавиатуры на телефоне 
# InlineKeyboardMarkup - инлайн клавиатуры
# InlineKeyboardButton - кнопка для инлайн клавиатуры

from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties # нужно для указания стандартных настроек бота
from api import Token #

# Создаем объект - бот и диспетчер
bot = Bot(token=Token, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

# Основная клавиатура
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет!"), KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True
)

# Инлайн клавиатуры
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Перейти на сайт", url="http://example.com")], # создаём кнопку перейти на сайт 
        [InlineKeyboardButton(text="Нажми", callback_data="button_click")]# создаём кнопку перейти на сайт 
    ]
)

@dp.message(Command("start")) # эта функция будет выполнятся, при вводе данной команды
async def start(message: types.Message):
    await message.answer("Привет! Я тестовый бот <b>test</b>", reply_markup=main_keyboard) # отправляет пользователю сообщение с текстом "Привет! Я тестовый бот"

@dp.message(lambda message: message.text == "Привет!") # эта функция будет выполнятся, когда пользователь напишет "Привет!"
async def hello(message: types.Message):
    await message.answer("Привет!!! Как дела?", reply_markup=inline_keyboard) # отправляет пользователю сообщение с текстом "Привет!!! Как дела?"

async def main(): # основная функция, которая запускает нашего бота
    await dp.start_polling(bot) # бот отслеживает новые команды от пользователя

if __name__ == "__main__": # данная команда проверяет, что бот запущен напрямую пользователем
    asyncio.run(main()) # Запускает функцию, которая включает бота