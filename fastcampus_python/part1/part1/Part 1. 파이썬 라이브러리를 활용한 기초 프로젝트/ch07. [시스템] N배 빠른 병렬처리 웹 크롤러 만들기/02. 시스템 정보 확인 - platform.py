import platform, psutil
import os

def printOsInfo():
    print('OS                   :\t', platform.system())
    print('OS Version           :\t', platform.version())

def printSystemInfor():
    print('Process information  :\t', platform.processor())
    print('Process Architecture :\t', platform.machine())
    print('CPU Cores          :\t', os.cpu_count())
    print('RAM Size             :\t', str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + "(GB)")


if __name__ == "__main__":
    # 운영체제 정보
    printOsInfo()

    # CPU / RAM 정보
    printSystemInfor()