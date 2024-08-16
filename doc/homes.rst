------------
ホームズ
------------

URL
-----

サンプル:

    大阪中古戸建一覧
    https://www.homes.co.jp/kodate/chuko/osaka/list/

    大阪中古戸建一覧、2ページ目
    https://www.homes.co.jp/kodate/chuko/osaka/list/?page=2

'<link rel="next">' で次のページが得られる。

内容
-----

1件ごとに '<div class="mod-mergeBuilding--sale cKodate ui-frame ui-frame-cacao-bar">' の中に情報がある。

'<span class="bukkenName">' がタイトル。

'<a class="prg-bukkenNameAnchor">' が物件ごとのURL。

'<div class="bukkenSpec">' に概況がテーブルとしてあり '<tr>' で一つの情報。

'<table class="unitSummary">' に情報がテーブルとしてあるが、1行目にヘッダ、2行目に内容となっている上に、
一つのセル内に複数の情報が含まれているため、決め打ちで読むしかなさそう。

特記
-----

'wget' 等でページ内容を取得しようとするとまったく違う内容が取得されるため、単なる"GET"では取得できない模様。
Selenium等でブラウザ経由でデータを取得する必要がある。

