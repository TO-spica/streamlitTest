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

src
st.write("簡単")
