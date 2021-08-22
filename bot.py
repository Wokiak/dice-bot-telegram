from aiogram import Bot, Dispatcher, types, executor
from asyncio import sleep

bot = Bot('enter your own token')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def on_message(message : types.Message):
	await bot.send_message(message.from_user.id,"Hi, send me dice to start a game")

@dp.message_handler(commands=['stop'])
async def on_message(message : types.Message):
	await bot.send_message(message.from_user.id,"Good bye")


@dp.message_handler ( content_types = ['dice'])
async def on_message (message:types.Message):
	user_data = message['dice']['value']
	print(user_data)
	await sleep (2)
	bot_data = await bot.send_dice(message.from_user.id)
	bot_data = bot_data['dice']['value']
	print(bot_data)

	await sleep(5)
	if bot_data > user_data :
		await bot.send_message(message.from_user.id , "Try again~")
	elif bot_data < user_data :
		await bot.send_message(message.from_user.id , "Good game ! You win")
	else :
		await bot.send_message(message.from_user.id , "Tie( Let's try again")

@dp.message_handler()
async def on_message(message : types.Message):
	await bot.send_message(message.from_user.id," I can only recognize dice :3")



if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True )


# i will update this code later with new lines( i will add buttons )
