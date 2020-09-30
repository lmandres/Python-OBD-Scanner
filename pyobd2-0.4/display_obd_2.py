#!/usr/bin/python

import PyOBD2

if __name__ == "__main__":

    pyobd2 = PyOBD2.PyOBD2("/dev/ttyUSB_OBD0")
    pyobd2.startInterface()

    try:
        while True:
            data = pyobd2.runMonitor()
            print(data)
    except KeyboardInterrupt:
        pass

    pyodb2.shutdown()

