import os
import time
from datetime import datetime
from core.tool import tool


class auto():
    def __init__(self, device, NOX=False):
        try:
            port = device.split(":")[1]
        except:
            port = device
        self.log = open('log-{0}.txt'.format(port), 'a+', encoding="utf-8")
        self.line = "//================================================\n"
        self.ship_flag = False
        self.space_flag = False
        self.sand_flag = False
        self.times = 0
        self.path = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))) + "\images"
        self.adbtool = tool(device, NOX)
        self.start = None
        self.end = None

    def log_info(self, str):
        self.log.write(str)
        print(str, end='')

    def bot_start(self):
        os.system('cls')
        print("\033[31mScrpit made by\033[0m \033[41;37mLeeChing\033[0m,github:\033[37;34mhttps://github.com/s17113230\033[0m")
        print(
            "\033[31m此腳本作者為\033[0m \033[41;37mLeeChing\033[0m,github頁面:\033[37;34mhttps://github.com/s17113230\033[0m")
        self.log_info(self.line)
        self.start = datetime.now()
        self.log_info("開始運行,開始時間: {}\n".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        print("已鎖定:", end='')
        i = 0
        for ark in self.adbtool.ark:
            print("\033[1;{0}m{1}\033[0m\t".format(
                33+i, ark.split('.')[0]), end='')
            i += 1
        self.log_info("\n{}".format(self.line))
        POG = []
        again = False
        # Note: 如果換遊戲的話，要記得換Again的圖片
        again = self.adbtool.compare(
            ["{0}\\again.jpg".format(self.path)])
        try:
            self.adbtool.tap(again, raw=True)
        except:
            raise Exception("沒有偵測到\"再抽一次\",或是解析度不是16x9的解析度\n退出程式")
        
        # Note: 這裡是因為按下重來後，還有一個確認的按鈕，所以要再按一次
        time.sleep(1)
        againCheck = self.adbtool.compare(
            ["{0}\\againCheck.jpg".format(self.path)])
        self.adbtool.tap(againCheck, raw=True)

        # Note: 這裡是加速Skip動畫的按鈕
        time.sleep(2)
        againSkip = self.adbtool.compare(
            ["{0}\\skip.jpg".format(self.path)])
        self.adbtool.tap(againSkip, raw=True)

        time.sleep(0.5)
        while len(POG) != len(self.adbtool.ark):
            t_start = time.time()
            POG = []
            again = False
            #Note: 當沒有再抽一次的時候，就會每1.5秒持續點擊畫面的(30, 30)座標
            while not again:
                again = self.adbtool.compare(
                    ["{0}\\again.jpg".format(self.path)], gach=True)
                if not again:
                    self.adbtool.tap((30, 30))
                time.sleep(1.5)
                    
            POG = again[1]
            t_end = time.time()
            cost_time = round(t_end-t_start, 2)
            if self.times == 0:
                self.times += 1
            if self.times != 0 and cost_time > 5:
                self.log_info("第{0}次結果:\n".format(self.times))
                if len(POG) > 0:
                    self.log_info('命中數量: {0}\n'.format(len(POG)))
                    for i in range(len(POG)):
                        self.log_info("{0}.{1}\t".format(
                            i+1, POG[i].split('.')[0]))
                    self.log_info('\n')
                else:
                    self.log_info('命中數量: 0\n')
                self.log_info("耗時 {0} 秒\n".format(cost_time))
                self.log_info(self.line)

                #Note: 當{偵測的UR數量}與所設定的條件相同時，則會停止動作
                if len(POG) >= 5:
                    self.end = datetime.now()
                    print(
                        "執行結束,總共執行 {0} 次, 結束時間 {1} ,共花費 {2} ".format(self.times, self.end, str(self.end-self.start)))
                    input("請輸入enter繼續")
                    break

                #Note: 當{偵測的UR}與{所選的UR}不同時，會重新點擊再抽一次
                if len(POG) != len(self.adbtool.ark):
                    self.adbtool.tap(again[0], raw=True)
                    time.sleep(1)
                    againCheck = self.adbtool.compare(
                        ["{0}\\againCheck.jpg".format(self.path)])
                    self.adbtool.tap(againCheck, raw=True)
                    
                    time.sleep(2)
                    againSkip = self.adbtool.compare(
                        ["{0}\\skip.jpg".format(self.path)])
                    self.adbtool.tap(againSkip, raw=True)

                    self.times += 1
