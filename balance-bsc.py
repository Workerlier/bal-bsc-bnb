import requests
from telegram.ext import Updater, CommandHandler

# Замените YOUR_BINANCE_API_KEY и YOUR_BINANCE_API_SECRET на ваши данные API ключа Binance
BINANCE_API_KEY = "YOUR_BINANCE_API_KEY"
BINANCE_API_SECRET = "YOUR_BINANCE_API_SECRET"

def get_bnb_balance(address):
    url = f"https://api.bscscan.com/api?module=account&action=balance&address={address}&apikey={BINANCE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        balance_bnb = int(response.json()['result']) / 10**18  # Переводим баланс из wei в BNB
        return balance_bnb
    else:
        return "Ошибка при получении баланса"

# Функция-обработчик команды /balance
def balance(update, context):
    bnb_address = "YOUR_BNB_ADDRESS"
    balance = get_bnb_balance(bnb_address)
    if isinstance(balance, float):
        update.message.reply_text(f"Баланс кошелька {bnb_address}: {balance} BNB")
    else:
        update.message.reply_text(balance)

def main():
    # Создаем объект Updater и передаем в него токен вашего бота
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /balance
    dp.add_handler(CommandHandler("balance", balance))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
