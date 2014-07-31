# -*- coding: utf-8 -*-
'''
# 学科redmineサーバで認証通してから「ユーザのアクティビティ」をチェックする例。
- ユーザ指定は sys.argv[1] でファイルを用意。
-- 上記ファイルは [loginAccount redmienID] という書式で、1行1ユーザ。
-- loginAccount自体は出力用に利用しているだけ。
'''

import sys
if (len(sys.argv) == 2):
    target = sys.argv[1]
else:
    print "argv[1] = target(account redmine-ID) file"
    sys.exit()


import re
import requests

# ログイン時のアカウント＆パラメータを用意。
# ソース直書き怖いなら標準入力から読み込むようにするとか。(getpassの例)
import getpass
print "=== to login redmine server. ==="
print "Your account: ",
account = raw_input()
password = getpass.getpass()
account = {
    'username': account,
    'password': password,
}

# redmine サーバへのログインURL
url = 'https://redmine.ie.u-ryukyu.ac.jp/login'

# アクティビティをチェックしたいユーザID指定してgetしよう。
# 一度認証通せば後はそのアカウントで見れる範囲のURLは一通りダウンロードできます。
# チェックしたいアクティビティは <span class="project">G*</span>という形式で掲載されてるので、その数をカウント。
s = requests.session()
r = s.post(url, params=account) #認証
userURL = 'https://redmine.ie.u-ryukyu.ac.jp/users/'

import csv
reader = csv.reader(open(target,'r'), delimiter=' ')
for row in reader:
    userAccount = row[0]
    redmineID = row[1]
    activityURL = userURL + redmineID
    #print "userAccount = %s, redmineID = %s, activityURL = %s" % (userAccount, redmineID, activityURL)
    r = s.get(activityURL)
    count = r.text.count('<span class="project">G')
    print "%s %d" % (userAccount, count)

