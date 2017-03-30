Taiwan Geographic Open Data (tgod)
臺灣地理開放資料介接工具 (python)

這專案的目的在於提供將臺灣地理相關的開放資料抓下來，並轉成 pandas.dataframe 的一個小工具。
主要是因爲各公家單位準備的開放資料的格式都不太一樣，即使是同一個單位，不同的資料也會有不同的格式設定，包括有些會壓縮... 之類。
所以我想說將資料直接整理成表單的 dataframe 格式，對於後續分析、應用、甚至再轉成特定格式(JSON/XML)，應該都會相對直觀與容易。

目前我已整理的資料表主要有臺北市、新北市、高雄市的一些交通相關資料表。項目及資料來源記錄在 data_info.ods 中。
未來有時間的時候會試着將其他資料的介接也整理起來。

v 0.0.1 : 初步建立整個架構
