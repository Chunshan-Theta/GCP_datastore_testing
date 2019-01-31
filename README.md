# GCP_datastore_testing

本篇使用 Google Cloud Platform (GCP) 中的 Datastore模組，並使用python3 ```google.cloud.datastore``` 模組進行CRUD四大功能。



# 什麼是 Google Cloud Platform (GCP) 中的 Datastore？ 他提供什麼服務？
GCP-Datastore 是具高度擴充性的 NoSQL 資料庫，適用於您的應用程式。Cloud Datastore 會自動處理資料分割及複製作業，也能隨著應用程式的負載而自動進行調整，因此穩定且可靠，方便您隨時存取。Cloud Datastore 的功能多樣齊全，包括 ACID 交易處理、類似 SQL 的查詢技術以及建立索引等功能。

# 定價與配額
Google Cloud Datastore 提供免費配額，讓您不需要一開始就支付費用。下表列出了各項資源的免費配額數量，歡迎多加利用。不過請注意，如果您需要更多配額，必須為專案啟用計費功能並設定支出上限。

### 每日都有一定額度的免費配額
您每天可使用的配額有一定的限制，系統會在太平洋時間凌晨 12 點左右重設配額。

```
            每日免費額度	           超過免費額度後的價格 (每單位)	    價格單位
儲存的資料	   1 GB 儲存空間	                   $0.207	                 GB/月
實體讀取數	   50,000 次	                       $0.069	                 每 100,000 個實體
實體寫入數	   20,000 次	                       $0.207	                 每 100,000 個實體
實體刪除數	   20,000 次	                       $0.029	                 每 100,000 個實體
小型作業	    50,000 次	                      Free
```

# 參考文獻：
## 快速入門 
本頁面說明如何在 Google Cloud Datastore 中利用 Google Cloud Platform 主控台儲存或查詢資料。
https://cloud.google.com/datastore/docs/quickstart?hl=zh-tw

## 設定金鑰
## Cloud Datastore Client Libraries 頁面顯示瞭如何開始使用Google Cloud Datastore API的Cloud Client Libraries。https://cloud.google.com/datastore/docs/reference/libraries?hl=zh-tw
