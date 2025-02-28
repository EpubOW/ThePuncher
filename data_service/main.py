from src.depends import *
import time
from loguru import logger
# from data_processing.MainProcessing import MainProcessing

if __name__ == '__main__':
    app.start_app()
    # try:
    #     while True:
    #         print(puncher_client.read_data())
    #         time.sleep(0.5)
    # except KeyboardInterrupt:
    #     logger.warning('Interrupting...')
    #     logger.info('Interrupted')