import subprocess
import os


def read_devices(path, NOX=False):
    if NOX:
        adb_path = "{}/adb/nox/nox_adb.exe".format(path)
    else:
        adb_path = "{}/adb/adb.exe".format(path)
    devices = subprocess.Popen("{0} devices".format(
        adb_path), shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8")
    lists = devices.split("\n")
    devicesNames = []
    for item in lists:
        if(item.strip() == ""):
            continue
        elif (item.startswith("List of")):
            continue
        else:
            devicesNames.append(item.split("\t")[0])
    return devicesNames


def select_devices(path, devicesIds, NOX=False):
    if NOX:
        adb_path = "{}/adb/nox/nox_adb.exe".format(path)
    else:
        adb_path = "{}/adb/adb.exe".format(path)
    os.system('cls')
    print("\033[31mScrpit made by\033[0m \033[41;37mLeeChing\033[0m,github:\033[37;34mhttps://github.com/s17113230\033[0m")
    print(
        "\033[31m此腳本作者為\033[0m \033[41;37mLeeChing\033[0m,github頁面:\033[37;34mhttps://github.com/s17113230\033[0m")
    print("請選擇你要控制的設備:")
    i = 1
    for deviceId in devicesIds:
        print("\033[1;34m {0}:{1}\033[0m".format(i, deviceId))
        i += 1
    print("\033[1;36m a: 新增\033[0m")
    print("\033[1;31m e: 離開\033[0m")
    try:
        inputIndex = input(
            "請輸入編號 [1 ~ {0}]:".format(i-1))
        value = int(inputIndex)
        if value < 1 or value >= i:
            raise Exception("編號過大")
        return devicesIds[value - 1]
    except (KeyboardInterrupt, SystemExit):
        raise Exception("KeyboardInterrupt")
    except Exception as e:
        if "e" == inputIndex.lower():
            return -1
        elif "a" == inputIndex.lower():
            port = input("請輸入設備名稱或連接在127.0.0.1的port: ")
            if port.isdigit():
                os.system("{0} connect 127.0.0.1:{1}".format(adb_path, port))
            else:
                os.system("{0} connect {1}".format(adb_path, port))
            input("輸入enter繼續")
            return select_devices(path, read_devices(path), NOX)
        else:
            print(
                "\033[1;31m編號輸入錯誤,請在試一次\033[0m")
            input("請輸入enter繼續")
            return select_devices(path, devicesIds)


def get_devices(path, NOX=False):
    devices = read_devices(path, NOX)
    client = select_devices(path, devices, NOX)
    if client == -1:
        raise Exception("使用者終止")
    return client
