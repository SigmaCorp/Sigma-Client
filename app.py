import sys
import asyncio

from PyQt5 import QtWidgets
from application.client import SigmaClient


async def process_events(
    application: QtWidgets.QApplication, main_window: QtWidgets.QMainWindow
):
    while True:
        await asyncio.sleep(0.001)
        application.processEvents()
        if not main_window.isVisible():
            sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SigmaClient(MainWindow)
    MainWindow.show()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(process_events(app, MainWindow))
