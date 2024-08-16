-------------
Suumo
-------------

URL
----
サンプル:

    中古一戸建て、兵庫県すべて、並び替えなし、通常表示、表示件数30件、1ページ目
    https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=060&bs=021&ta=28&jspIdFlg=patternShikugun&kb=1&kt=9999999&tb=0&tt=9999999&hb=0&ht=9999999&ekTjCd=&ekTjNm=&tj=0&cnb=0&cn=9999999

    中古一戸建て、兵庫県すべて、並び替えなし、通常表示、表示件数30件、2ページ目
    https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=060&bs=021&ta=28&jspIdFlg=patternShikugun&kb=1&kt=9999999&tb=0&tt=9999999&hb=0&ht=9999999&ekTjCd=&ekTjNm=&tj=0&cnb=0&cn=9999999&page=2

    中古一戸建て、兵庫県すべて、並び替えなし、通常表示、表示件数100件
    https://suumo.jp/jj/bukken/ichiran/JJ012FC001/?ar=060&bs=021&cn=9999999&cnb=0&ekTjCd=&ekTjNm=&hb=0&ht=9999999&kb=1&kt=9999999&ta=28&tb=0&tj=0&tt=9999999&po=0&pj=1&pc=100

    中古一戸建て、兵庫県すべて、並び替え:新着更新順、通常表示、表示件数50件
    https://suumo.jp/jj/bukken/ichiran/JJ012FC001/?ar=060&bs=021&cn=9999999&cnb=0&ekTjCd=&ekTjNm=&hb=0&ht=9999999&kb=1&kt=9999999&ta=28&tb=0&tj=0&tt=9999999&pc=50&po=1&pj=2

    中古一戸建て、大阪府すべて、並び替えなし、通常表示、表示件数30件
    https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=060&bs=021&ta=27&jspIdFlg=patternShikugun&kb=1&kt=9999999&tb=0&tt=9999999&hb=0&ht=9999999&ekTjCd=&ekTjNm=&tj=0&cnb=0&cn=9999999

引数
====

ar
    ? 060
bs
    ? 021
cn
    ? 9999999
cnb
    ? 0
ekTjCd
    ? 空
ekTjNm
    ? 空
hb
    建物面積下限(0)
ht
    建物面積上限(9999999)
jspIdFlg
    ?ない場合もあり (patternShikugun)
kb
    価格下限(1)
kt
    価格上限(9999999)
ta
    県

    滋賀
        25
    京都
        26
    大阪
        27
    兵庫
        28
tj
    ?ない場合もあり(0)
tb
    土地面積下限(0)
tt
    土地面積上限(9999999)
pc
    表示件数(10, 20, 30, 50, 100)
po&pj
    並び替え

    なし
        po=0&pj=1
    新着・更新順
        po=1&pj=2
    所在地順（昇順）
        po=3&pj=1
    所在地順（降順）
        po=3&pj=2
    価格が安い順
        po=5&pj=1
    価格が高い順
        po=5&pj=2
    土地面積が広い順
        po=9&pj=2
    土地面積が狭い順
        po=9&pj=1
    建物面積が広い順
        po=10&pj=2
    建物面積が狭い順
        po=10&pj=1
    築年月が新しい順
        po=16&pj=2
    築年月が古い順
        po=16&pj=1
md
    間取り

    1K/DK/LDK
        1
    2K/DK/LDK
        2
    3K/DK/LDK
        3
    4K/DK/LDK
        4
    5K/DK/LDK以上
        5
et
    駅徒歩(1, 3, 5, 7, 10, 15, 20, 9999999)
page
    ページ番号、1は省略

内容
----

物件リストは '<div id="js-bukkenList" class="property_unit_group">' にある。

個々の物件は '<div class="property_unit ">' にあるが、重要な情報はその中の '<div class="property_unit-content">' にある。

'<div class="dottable-line">' で情報の書かれた表の1行を取り出せるが、間取り写真等も含まれる。
文字情報は '<table>' さらに '<dl>' で囲まれているのでそれで区別する。
築年や間取りなどは建物面積や建築面積の2行目に書かれているので注意が必要。

取り扱い店名は '<div class="shopmore-title">' で取得できる。
取扱店の電話番号は '<span class="makermore-tel-txt">' で取得できる。
'<div class="storecomment-txt">' で店からのコメントが取得できる。
