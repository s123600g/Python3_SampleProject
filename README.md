# Python3 練習範例專案

目錄結構說明：
----------------------------------------------------------------------------------------------------------------------------------
1. sample_program：基本型態練習範例。<br/>
2. sample_filerw：基本讀檔寫檔練習範例。<br/>
3. sample_SQLite：基本SQLite操作練習範例。<br/>
4. sample_SQLAlchemy：使用ORM操作資料庫練習範例-以MySQL為操作資料庫。<br/>
5. sample_SQLAlchemy_SQLite：使用ORM操作資料庫練習範例-以SQLite為操作資料庫。<br/>

sample_SQLAlchemy、sample_SQLAlchemy_SQLite：使用ORM操作資料庫練習範例。
----------------------------------------------------------------------------------------------------------------------------------
### 內容架構如下：
[1].sample_SQLAlchemy/DB_Data/sample_user.sql：user資料表Data。 <br/>
[2].sample_SQLAlchemy/DB_Data/sample_score：score資料表Data。 <br/>
[2].sample_SQLAlchemy_SQLite/sample.db：sample資料庫內有user資料表、score資料表，兩個資料表都有Data。 <br/>
[3].migrations/：此為flask針對資料庫操作所產生目錄。<br/>
[4].Config2.py：一般參數配置。 <br/>
[5].DB_initialize.bat：更新資料庫內資料表操作管理腳本-Windows 10。 <br/>
[6].MainControl.py：主要執行運作程式。 <br/>
[7].Manage.py：操作資料庫針對資料表更動管理，使用flask、flask_migrate、flask_script。 <br/>
[8].Model.py：放置資訊資料表模型。 <br/>
[9].Score2.py：成績登錄查詢系統主體。 <br/>
[10].SQLConfig.py：放置資料庫連接設定參數 <br/>

*關於SQLAlchemy ORM操作可參考以下連結：* <br/>
[Python3+SQLAlchemy+Sqlite3实现ORM教程](https://www.cnblogs.com/lsdb/p/9835894.html)<br/>
[SQLAlchemy 1.3 Documentation](https://docs.sqlalchemy.org/en/13/orm/session_basics.html#what-does-the-session-do)<br/>

*關於SQLAlchemy 資料庫連接語法：* <br/>
[1].SQLite之連接語法：<br/>
> "sqlite:///filename.db" <br/>

[2].MySQL之連接語法： <br/>

> "mysql://db_User:db_Password@db_Host/db_Schema" <br/>
<p></p>

### 執行程式前設置：
#### 1. 確認是否有存在建立好資料庫。<br/>
在本專案使用的資料庫名為**sample**，如果想更改使用的資料庫命名，需要更改**SQLConfig.py**內指定參數，可參考以下針對兩種模式資料庫更改方式。<br/>
**針對sample_SQLAlchemy-使用MySQL**<br/>
<pre><code>
db_config = {
        'db_user': "帳戶名稱",
        'db_psw': "帳戶密碼", 
        'db_host': "資料庫位址", 
        'db_schema': "資料庫名稱",  <-- 更改此處即可更動使用資料庫。
        }
</code></pre>

<p></p>

**針對sample_SQLAlchemy_SQLite-使用SQLite** <br/>
<pre><code>
# SQLite 檔案名稱
SQLite_File = '檔案名稱.db' <-- 在SQLite檔案名稱等於資料庫名稱。
</code></pre>

<p></p>

#### 2. 確認SQLConfig.py內配置。 <br/>

**針對sample_SQLAlchemy-使用MySQL SQLConfig.py內配置。**<br/>
需設置**db_config**內參數：<br/>
<pre><code>
    db_config = {
        'db_user': "帳戶名稱",
        'db_psw': "帳戶密碼", 
        'db_host': "資料庫位址", 
        'db_schema': "資料庫名稱",
    }
</code></pre>
    
資料庫連接語法會抓取**SQLALCHEMY_DATABASE_URI**參數，此參數會去抓取**db_config**內參數自動產生配置完整DB API 語法。<br/>
<pre><code>
SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}/{}".format(
    db_config['db_user'], 
    db_config['db_psw'], 
    db_config['db_host'], 
    db_config['db_schema']
   )
</code></pre>

<p></p>

**針對sample_SQLAlchemy_SQLite-使用SQLite SQLConfig.py內配置** <br/>
需設置**SQLite_File、SQLite_Path**內參數：<br/>
<pre><code>
# SQLite 檔案名稱
SQLite_File = 'sample.db'
# SQLite 檔案位置(自動產生)
SQLite_Path = os.path.join(os.getcwd(), 'sample_SQLAlchemy_SQLite' , SQLite_File)
</code></pre>

資料庫連接語法會抓取**SQLALCHEMY_DATABASE_URI**參數，此參數會去抓取**SQLite_Path**內參數自動產生配置完整DB API 語法。<br/>
<pre><code>
SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(SQLite_Path)
</code></pre>

<p></p>

### 更新資料表操作：
使用flask-script和flask-migrate <br/>
可參考以下連結資源：<br/>
[在flask中使用flask-migrate管理数据库](https://blog.csdn.net/qq_33279781/article/details/79803376)<br/>
[flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)<br/>

使用flask-script管理資料庫更動，命令如下：
> python manage.py db init <br/>

> python manage.py db migrate  <br/>

> python mange.py db upgrade <br/>
<p></p>

**以DB_initialize.bat腳本運行：**<br/>
  1.需要先確認腳本是否存在專案目錄所在的位置，並且確認腳本內容變數**DirPath**參數值，是否跟專案目錄所在的位置一樣。
  > Set DirPath=專案所在的位置<br/>

  例如： 
  > Set DirPath=E:\Project\Python3_SampleProject\sample_SQLAlchemy\
  
  <br/>
  2.開啟終端機(命令提示視窗)，終端機所在的位置必須要跟專案目錄一樣。<br/>
  以 **E:\Project\Python3_SampleProject\sample_SQLAlchemy** 位置為例子：<br/>  
  
  切換到E槽<br/>
  > E:  <br/>
  
  切換到 Project\Python3_SampleProject\sample_SQLAlchemy 底下<br/>
  > cd Project\Project\Python3_SampleProject\sample_SQLAlchemy <br/>
   
  執行DB_initialize.bat<br/>
  > DB_initialize.bat <br/>
  
**以手動更新資料庫操作：**<br/>
  1.先手動刪除**migrations**目錄與資料庫中**alembic_version**資料表。 <br/>
  
  2.開啟終端機(命令提示視窗)，終端機所在的位置必須要跟專案目錄一樣。<br/>
    以 **E:\Project\Python3_SampleProject\sample_SQLAlchemy** 位置為例子：<br/>  

   切換到E槽<br/>
   > E:  <br/>

   切換到 Project\Python3_SampleProject\sample_SQLAlchemy 底下<br/>
   > cd Project\Project\Python3_SampleProject\sample_SQLAlchemy <br/>
    
   執行db init <br/>
   > python3 manage.py db init <br/>
  
   執行db migrate <br/>
   > python3 manage.py db migrate <br/>
    
   執行db upgrade <br/>
   > python3 mange.py db upgrade  <br/>

sample_program：基本型態練習範例
----------------------------------------------------------------------------------------------------------------------------------
### 內容架構如下：
##### Demo： 
[1].demo_01.py <br/>
[2].demo_02.py <br/>
[3].demo_03.py <br/>
[4].demo_04.py <br/>
[5].demo_05.py <br/>
[6].demo_06.py <br/>
[7].demo_07.py <br/>
[8].demo_08.py <br/>
<p><p/>

##### sample： 
[1].sample_01.py <br/>
[2].sample_02.py <br/>
[3].sample_03.py <br/>
[4].sample_04.py <br/>
[5].sample_05.py <br/>
[6].sample_06.py <br/>
[7].sample_07.py <br/>
[8].sample_08.py <br/>
[9].sample_09.py <br/>
[10].sample_10.py <br/>
<p><p/>

##### 成績登錄查詢系統簡單應用： 
[1].Score1.py <br/>
[2].Config1.py <br/>
<p><p/>

##### 其他檔案：
[1].data.db <br/>
[2].data.txt <br/>
[3].output.txt <br/>

sample_filerw：基本讀檔寫檔練習範例。
----------------------------------------------------------------------------------------------------------------------------------
#### 內容架構如下：
[1].sample_filerw.py <br/>
[2].data.txt <br/>
[3].output.txt <br/>

sample_SQLite：基本SQLite操作練習範例。
----------------------------------------------------------------------------------------------------------------------------------
#### 內容架構如下：
[1].sample_SQLite.py <br/>
[2].data.db <br/>

