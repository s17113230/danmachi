# 台版地城邂逅(戰鬥編年史)刷首抽腳本,設定為5個UR停止

詳細的 log 會記錄在同一資料夾的 log.txt 內

---

## 測試環境

#### 建議為 960*540 解析度,理論上來說支援所有 16x9 解析度

#### 但是解析度過高會導致執行效率過慢&其他問題

只要"模擬器"設定為 960*540 即可,模擬器的大小可以隨意縮放無所謂

#### python 3.7.9

---

## 使用方法

1.下載源碼後解壓縮

|--------重要部分--------|

### 2.然後到"重來"的畫面

![](https://github.com/s17113230/danmachi/blob/master/example_image/example.jpg)

是以"![](https://github.com/s17113230/danmachi/blob/master/example_image/again.jpg)"為判斷基準

|-----------------------------|

3.點擊 start.bat,確認目標設備是否有在選單,沒有的話可以自行添加(可以填入設備名稱,或是全數字的 port 號)

- BS 多開的 port 號,可以去設定->偏好設定->往下拉到 ADB 勾選的那欄->下面黃字有寫說你可以在 127.0.0.1:多少連接,新增 port 號只需輸入":"後面的數字即可

4.如果需要多開則可以再點擊一次 start.bat 並新增腳本工作
