"""
ぐるなびapi

目標：フリーワード検索の結果上位5件における必要情報を出力する

フォーマット
店名,URL,路線名駅名

ex:「ワイン」なら
"""
import requests


def main():
    API_KEY = '7d6b0063f9927658f4c7a95c6b4b5ee5'

    # url = f'https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid={API_KEY}&freeword=ワイン'

    payload = {'keyid': API_KEY, 'freeword': 'ワイン', 'hit_per_page': 5}
    response = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3", params=payload)

    # response = requests.get(url)

    restaurant_list = response.json()['rest']

    for restaurant in restaurant_list:
        reply_name = restaurant['name']
        reply_url = restaurant['url']
        reply_access_line = restaurant['access']['line']
        reply_access_station = restaurant['access']['station']

        print("===================================")
        print(f'{reply_name}\n{reply_url}\n{reply_access_line}\n{reply_access_station}')


if __name__ == '__main__':
    main()
