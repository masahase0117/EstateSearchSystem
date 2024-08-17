import urllib.parse
from enum import Enum
from typing import Generator

from estate_search_system import load_page


class Pref(Enum):
    """都道府県名"""

    Hyogo = 28
    Osaka = 27
    Kyoto = 26
    Shiga = 25


def main(pref: Pref, page: int = 1) -> Generator[dict, None, int]:
    url = (
            "https://realestate.yahoo.co.jp/used/house/search/06/%d/" %
            pref.value
    )
    if page > 1:
        url += "?page=%d" % page
    soup = load_page(url)
    mother = soup.find("div", class_="ListBukken2")
    if mother is None:
        return 1
    for child in mother.find_all(
            "li", class_="ListBukken2__list__item _listItem"
    ):
        sample = {
            "タイトル": child.find("h2").text.strip(),
            "URL": urllib.parse.urljoin(
                url,
                child.find("a", class_="_listCassetteDtlLink").attrs["href"],
            ),
        }
        if child.find("div", class_="ListCassette2__summary__cnt"):
            cnt = child.find(
                "div", class_="ListCassette2__summary__cnt"
            ).find_all("li")
            sample["最寄り"] = cnt[0].text.strip()
            sample["住所"] = cnt[1].text.strip()
            sample["築年月"] = cnt[2].text.strip()
            sample["間取り"] = cnt[3].text.strip()
            tmp = cnt[4].text.strip().split()
            sample["土地面積"] = tmp[1].strip()
            sample["建物面積"] = tmp[-1].strip()
            sample["価格"] = child.find(
                "li", class_="ListCassette2__info__price"
            ).text.strip()
            sample["取扱店"] = (
                child.find("li", class_="ListCassette2__info__cpName")
                .text.split()[1]
                .strip()
            )
            sample["取扱店Tel"] = child.find(
                "span", class_="ListCassette2__contact__phone__number"
            ).text.strip()
        else:
            cnt = child.find("dl", class_="ListCnt__info").find_all("dd")
            sample["最寄り"] = cnt[1].text.strip()
            sample["住所"] = cnt[2].text.strip()
            sample["築年月"] = cnt[3].text.strip()
            sample["間取り"] = cnt[4].text.strip() + "/" + cnt[5].text.strip()
            sample["土地面積"] = cnt[6].text.strip()
            sample["建物面積"] = cnt[7].text.strip()
            sample["価格"] = cnt[0].text.strip()
            sample["取扱店"] = child.find(
                "div", class_="ListCnt__comment__realtor"
            ).text.strip()
            sample["取扱店Tel"] = child.find(
                "span", class_="ListCnt__contact__phone__number"
            ).text.strip()
        yield sample

    return 0


if __name__ == "__main__":
    tmp = main(Pref.Osaka)
    print(tmp.__next__())
    print(tmp.__next__())
    print(tmp.__next__())
    print(tmp.__next__())
    tmp2 = list(tmp)
    print(len(tmp2))
