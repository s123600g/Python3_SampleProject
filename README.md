# Python3 練習範例專案

目錄結構說明：
----------------------------------------------------------------------------------------------------------------------------------
1.sample_program：基本型態練習範例。<br/>
2.sample_filerw：基本讀檔寫檔練習範例。<br/>
3.sample_SQLite：基本SQLite操作練習範例。<br/>
4.sample_SQLAlchemy：使用ORM操作資料庫練習範例-以MySQL為操作資料庫。<br/>
5.sample_SQLAlchemy_SQLite：使用ORM操作資料庫練習範例-以SQLite為操作資料庫。<br/>

sample_SQLAlchemy、sample_SQLAlchemy_SQLite：使用ORM操作資料庫練習範例。
----------------------------------------------------------------------------------------------------------------------------------
#### 內容架構如下：
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

#### 更新資料表操作：
1.以DB_initialize.bat腳本運行，需要先確認腳本是否存在專案目錄所在的位置，並且確認腳本內容變數**DirPath**參數值，是否跟專案目錄所在的位置一樣
> Set DirPath=專案所在的位置<br/>

Ex： 
> Set DirPath=E:\Project\Python3_SampleProject\sample_SQLAlchemy\

sample_program：基本型態練習範例
----------------------------------------------------------------------------------------------------------------------------------
#### 內容架構如下：
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

