## Запуск бота

```
git clone https://github.com/Dancoder777/test_tg_bot
cd tgbot-itstep
```

```
pip install - r requirements.txt
python bot.py
```

### Инлайн клавиатуры - наши кнопки в боте
```
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Перейти на сайт", url="http://example.com")], # создаём кнопку перейти на сайт 
        [InlineKeyboardButton(text="Нажми", callback_data="button_click")]# создаём кнопку перейти на сайт 
    ]
)
```
