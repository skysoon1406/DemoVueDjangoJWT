⚙️ 安裝與啟動
後端 Django   (mysite)
1️⃣ 建立虛擬環境
python -m venv venv
source venv/bin/activate  （Windows 用 venv\Scripts\activate）

2️⃣ 安裝依賴
pip install -r requirements.txt

3️⃣ 遷移資料庫
python manage.py migrate

4️⃣ 啟動 Django Server
python manage.py runserver


前端 Vue(myvue)
1️⃣ 安裝依賴
npm install

2️⃣ 啟動開發伺服器
npm run dev
