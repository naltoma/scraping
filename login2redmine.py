# -*- coding: utf-8 -*-
'''
# 学科redmineサーバで認証通してから指定URLのHTMLを取得する例。
- 一般的にはusername, password等のパラメータ名はHTMLのformタグ内参照して見つけるべし。
- サイトによっては自動生成したセッションIDをURLに含めてたりすることも。
'''

import re
import requests

# ログイン時のアカウント＆パラメータを用意。
# ソース直書き怖いなら標準入力から読み込むようにするとか。
account = {
    'username': 'your account',
    'password': 'your password',
}

# redmine サーバへのログインURL
url = 'https://redmine.ie.u-ryukyu.ac.jp/login'

# アクティビティをチェックしたいユーザID指定してgetしよう。
# 一度認証通せば後はそのアカウントで見れる範囲のURLは一通りダウンロードできます。
s = requests.session()
r = s.post(url, params=account) #認証
r = s.get('https://redmine.ie.u-ryukyu.ac.jp/users/xxx')
print r.text

