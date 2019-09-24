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

    payload = {'keyid': API_KEY, 'freeword': 'ワイン'}
    response = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3", params=payload)

    # response = requests.get(url)

    reply_name = response.json()['rest'][0]['name']
    reply_url = response.json()['rest'][0]['url']
    reply_linename = response.json()['rest'][0]['access']['line']
    reply_station = response.json()['rest'][0]['access']['station']

    print(f'{reply_name}\n{reply_url}\n{reply_linename}\n{reply_station}')


if __name__ == '__main__':
    main()
