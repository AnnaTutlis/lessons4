from aiogram.utils import executor
from config import dp
from hendlers import admin, client, callback, extra, fsm_anketa
import logging

client.register_handler_client(dp)
admin.register_handlers_admin(dp)
fsm_anketa.register_hendler_fsmanketa(dp)
callback.register_handler_callback(dp)
extra.register_hendler_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
