# app.py（ファイル名は任意）
import streamlit as st
import requests
import plotly.graph_objects as go
import json
import datetime
import re

# 取得対象のURLと測定者をリストにする
src = []
src.append(["Toshi@横浜 さん (神奈川県横浜市青葉区)", "https://weathernews.jp/pollen/pollen.html?pid=POLLEN_2025-0101"])
src.append(["はるわんだ さん (横浜市青葉区)", "https://weathernews.jp/pollen/pollen.html?pid=POLLEN_2025-0102"])
src.append(["ノブ さん (神奈川県大和市中央林間西)", "https://weathernews.jp/pollen/pollen.html?pid=POLLEN_2025-0110"]) 
src.append(["Masahiro さん (横浜市都筑区)", "https://weathernews.jp/pollen/pollen.html?pid=POLLEN_2025-0100"]) 
src.append(["abe さん (東京都町田市森野)", "https://weathernews.jp/pollen/pollen.html?pid=POLLEN_2025-0088"]) 
src.append(["パライラル さん (東京都町田市成瀬台)", "https://weathernews.jp/pollen/pollen.html?pid=POLLEN_2025-0089"]) 
src.append(["ぽんぽん さん (町田市金井)", "https://weathernews.jp/pollen/pollen.html?pid=POLLEN_2025-0091"]) 

# 表記ゆれをなくすため、都県を削除
for i in range(len(src)):
  src[i][0] = src[i][0].replace("東京都","").replace("神奈川県","")
  
# 今日から1週間前までのyyyy/mm/ddを取得し、URLからAPI用URIに変換。
# https://weathernews.jp/pollen/pollen.html?pid=POLLEN_2025-0101
# を
# https://site.weathernews.jp/site/pollen/json/obs/2025/02/28/POLLEN_2025-0101.json
# という形にする。

dtnow = datetime.datetime.now()
st.write(dtnow)

for j in range(7):
  dt = dtnow + datetime.timedelta(days = -j) + datetime.timedelta(hours = +9)
  # API用URIを合成し、リストuriに追加。POLLEN_2025-0101　という部分を抽出してくっつける。
  uri = []
  for i in range(len(src)):
    match = re.search(r"POLLEN_\d{4}-\d{4}", src[i][1])
    if match:
      url = "https://site.weathernews.jp/site/pollen/json/obs/" + dt.strftime("%Y/%m/%d") + "/" + match.group() + ".json"
      #print(match.group())
      #print(url)
      uri.append(url)

  # 各URIを使って花粉(個)のデータを取得する。
  kafun = []
  for i in range(len(src)):
    # ウェブページの内容を取得
    response = requests.get(uri[i])
    response.encoding = response.apparent_encoding  # 文字エンコーディングを適切に設定
    # ① JSONデータを直接取得
    json_data = response.json()  # decode() は不要
    # ② 必要なデータ（pollenの配列）を取得
    recv = json_data["obs"]["pollen"]
    kafun.append([list(range(1,len(recv)+1)),recv])

  # グラフ作成
  fig = go.Figure()
  for i in range(len(src)):
    fig.add_trace(go.Scatter(x=kafun[i][0], y=kafun[i][1], name=src[i][0])
  st.plotly_chart(fig)

  #plt.figure(figsize=(10, 6))

  # 折れ線グラフをプロット
  #for i in range(len(src)):
  #  plt.plot(kafun[i][0], kafun[i][1], label=src[i][0], marker='o', linestyle='-')
  #plt.legend()

  # グラフのタイトルとラベルを設定
  #plt.title(dt.strftime("%Y/%m/%d"))
  #plt.xlabel('日時')
  #plt.ylabel('花粉(個)')

  # グリッドを表示
  #plt.grid(True)

  # グラフを表示
  #plt.show()
