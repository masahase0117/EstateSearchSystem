import urllib.parse
from functools import partial
from typing import Generator

from estate_search_system import Pref
from estate_search_system import load_page


def main(pref=Pref.Osaka, page=1) -> Generator[dict, None, int]:
    """スーモのサイトにアクセスして中古一戸建ての情報を得る

    :param Pref pref: 取得する都道府県
    :param int page: ページ番号
    :return: 不動産情報を含んだ辞書のイテレータ。通常以下の内容を含む:
            - タイトル
            - 物件名
            - 販売価格
            - 所在地
            - 最寄り駅
            - 面積(土地/建物)
            - 間取り
            - 築年月
            - 取扱店情報
    """
    url = (
        "https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=060&bs=021&ta"
        "=%d&kb=1&kt=9999999&tb=0&tt=9999999&hb=0&ht=9999999&&tj=0&cnb=0"
        "&cn=9999999&pc=100" % pref.value
    )
    if page > 1:
        url += "&page=%d" % page
    try:
        soup = load_page(url)
    except Exception as e:
        print(e)
        return 1
    mother = soup.find("div", id="js-bukkenList")
    if not mother:
        return 1
    for child in mother.find_all("div", class_="property_unit-content"):
        title = child.find("h2", class_="property_unit-title")
        if title:
            sample = {
                "タイトル": title.a.text,
                "URL": urllib.parse.urljoin(url, title.a["href"]),
            }
            for line in child.find_all("div", class_="dottable-line"):
                for dl in line.find_all("dl"):
                    dt = dl.find("dt")
                    dd = dl.find("dd")
                    if dt and dd:
                        sample[dt.text.strip()] = dd.text.strip()
            if len(sample.keys()) > 1:
                tmp = child.find("div", class_="shopmore-title")
                if tmp:
                    sample["取扱店"] = tmp.text.strip()
                tmp = child.find("span", class_="makermore-tel-txt")
                if tmp:
                    sample["取扱店Tel"] = tmp.text.strip()
                tmp = child.find("div", class_="storecomment-txt")
                if tmp:
                    sample["取扱店からの情報"] = tmp.text.strip()
                yield sample
    return 0


def page_next(pref):
    func = partial(main, pref=pref)
    count = 1
    while True:
        tmp = yield from func(page=count)
        if tmp != 0:
            break
        count += 1


if __name__ == "__main__":
    print(page_next(Pref.Osaka).__next__())
    # tmp = list(page_next(tmp_func))
    # print(tmp[0])
    # print(len(tmp))
