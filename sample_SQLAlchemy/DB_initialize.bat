@Echo On

:: 執行更新資料庫Schema結構腳本檔，使用flask-script、flask-migrate
:: 透過Manage.py程式執行flask-script和flask-migrate
:: 要做資料庫Schema更動之前，要先刪除migrations目錄與資料庫中alembic_version資料表
:: 使用flask-script管理資料庫更動，命令如下：
:: 1. python manage.py db init
:: 2. python manage.py db migrate
:: 3. python mange.py db upgrade

Setlocal

:: 設置migrations目錄名稱
Set DirectoryName=migrations\

:: 設置所在位置目錄
Set DirPath=E:\Project\Python3_SampleProject\sample_SQLAlchemy\

echo Remove 'migrations' Directory.

echo %DirPath%%DirectoryName%

rmdir /s /q %DirPath%%DirectoryName%

:: 初始化建立migrations目錄
echo Create Initialize 'migrations' Directory , by Run SQLAlchemy init.

python Manage.py db init

:: 產生資料表結構
echo Run SQLAlchemy migrate.

python Manage.py db migrate

:: 更新資料表結構
echo Run SQLAlchemy upgrade.

python Manage.py db upgrade

Endlocal
