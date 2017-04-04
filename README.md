## Taiwan Geographic Open Data (tgod)
## 臺灣地理開放資料介接工具 (for python)

### 背景
這專案的目的在於提供將臺灣地理相關的開放資料抓下來，並轉成 pandas.dataframe 的一個小工具。
主要是因爲各公家單位準備的開放資料的格式都不太一樣，即使是同一個單位，不同的資料也會有不同的格式設定，包括有些會壓縮... 之類。
所以我想說將資料直接整理成表單的 dataframe 格式，對於後續分析、應用、甚至再轉成特定格式(JSON/XML)，應該都會相對直觀與容易。

目前我已整理的資料表主要有臺北市、新北市、高雄市的一些交通相關資料表。項目及資料來源記錄在 data_info.ods 中。
未來有時間的時候會試着將其他資料的介接也整理起來。

### 簡單說明
這專案分成兩大部分 (預計):
- 第一部分，主要是 (近)即時更新的資料，包括公車、Youbike 等資訊，這部分仰賴開放資料的 API (JSON, XML)，透過人工的針對資料欄位作處理之後生成 dataframe 格式；同時也自動增加 unix timestamp 欄位作爲後續應用。  
    這部分目前整理了臺北市、新北市、高雄市部分的交通開放資料。
- 第二部分，主要是將一些常用的空間資料，包括行政區 (從縣市到最小統計區)、國道省道、鐵路路線、火車站、捷運站等，可以獲取的官方開放的空間資料，整理成壓縮的pbf 格式 放到專案中，以供後續只要透過一些function 及 key 就可以直接叫出這些資料(GeoDataFrame 格式)。


### 使用 (Usage)
使用方法可參考 testing.py、 testing_static.py 
或者簡單來說：

- 即時資料的臺北市公車位置資料:

    ```python
    from tgod import taipei_transport as tt
    busdf = tt.bus()
    print busdf.head(10)
    ```

- 靜態的空間資料 (取屏東最小統計區資料):
    
    ```python
    from tgod import get_map
    gdf = get_map.get_boundary('bsu0_pingtung')
    print gdf.head()

    ```


### 依賴工具 (dependencies)
- pandas (目標格式是 pandas DataFrame)
- geopandas (所以包括其依賴的 fiona、shapely、 pyproj ... windows 使用者請自行安裝好~~)
- geobuf (爲了這專案才發現的一個新玩意，換句話說我也不熟...)

---

2017-03-30 - v 0.0.1 : 初步建立整個架構
