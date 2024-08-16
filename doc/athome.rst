---------------
アットホーム
---------------

URL
-----

サンプル:

    大阪府の中古一戸建て一覧、
    https://www.athome.co.jp/kodate/chuko/osaka/list/

    兵庫
    https://www.athome.co.jp/kodate/chuko/hyogo/list/

    京都
    https://www.athome.co.jp/kodate/chuko/kyoto/list/

'<link rel="next">' で次のページが得られる。



内容
-----

一件ごとに '<div class="object-detail">' が存在し、その中に情報がある。

'<div class="thumb">' 内の '<a>' に物件ごとのURLが、ただしタイトル自体はさらにその中の '<img>' の 'alt' として記述されている。

'<div class="object-data_sg">' 内に価格等がテーブルの形であり、同一の '<tr>' 内の '<th>' と '<td>' が対応している。

'<div class="object-comment">' 内に取扱店の情報がある。

特記
-----

'wget' 等でページ内容を取得しようとするとまったく違う内容が取得されるため、単なる"GET"では取得できない模様。
Selenium等でブラウザ経由でデータを取得する必要がある。
