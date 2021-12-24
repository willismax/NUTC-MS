# NUTC-MS

- 範例程式碼下載(需先安裝git)

    ```
    git clone https://github.com/willismax/NUTC-MS.git
    cd NUTC-MS
    ```

- 啟動虛擬環境pipenv(需先`pip install pipenv`，並在本機安裝對應的python版本)
    ```
    pipenv --python 3.9.9
    ```

- 安裝相依套件

    ```
    pipenv install -r requirements.txt
    ```
    如已經有Pipfile.lock檔，可執行:
    ```
    pipenv sync
    ```

- 執行服務
    ```
    # 開啟虛擬環境並進入環境執行
    pipenv shell
    python app.py
    
    # 或未進入虛擬環境由本機執行
    pipenv run app.py
    ```
    
- 移除虛擬環境
    ```
    pipenv --rm
    ```

## LINE-BOT-DEMO

- 提醒:
    - 請配合LINE MESSAGE API填入資訊於`config.py`
        ```
        CHANNEL_ACCESS_TOKEN = ''
        CHANNEL_SERET = ''
        ```

## flask-api-DEMO

> 以開放資料台灣電影院票房統計示範

- 依前述方式執行
    ```
    #進入目錄
    cd flask-api

    #開虛擬環境
    pipenv --python 3.9.9  

    #同步安裝Pipfile.lock對應檔案
    pipenv sync 

    #進入虛擬環境
    pipenv shell 
    
    #執行程式
    python app.py 
    ```
- 執行後可以觀察的網址
    - v1
        - http://localhost:5000
        - http://localhost:5000/api/all
        - http://localhost:5000/api/美國
        - http://localhost:5000/api/尚氣與十環傳奇
    - v2
        - http://localhost:5000/api/v2/GET/all
        - http://localhost:5000/api/v2/GET/country/美國
        - http://localhost:5000/api/v2/GET/movie/期末考


