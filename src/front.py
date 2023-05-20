import streamlit as st
import requests
import json
from task import Task
from backend import get_log

# アプリタイトル表示
st.title("タスク管理アプリ")

# テキストボックス表示
title = st.text_input(label="タスク内容")
# プルダウンリスト表示
time = st.selectbox(label="処理時間を選択", options=[10, 30, 60])

# タスク定義
task = Task(
    id=0,
    title=title,
    time=time,
    start_time="",
    end_time=""
)

# ボタン表示
exe_btn = st.button("実行")
log_btn = st.button("実行状況")

# 実行ボタンが押下された場合
if exe_btn:
    if title !="":
        r = requests.post("http://127.0.0.1:8000/tasks", data=json.dumps(dict(task)))
        st.success(r.json())
    else:
        st.error("タスク内容が入力されていません")

# 実行状況ボタンが押下された場合
if log_btn:
    log_df = get_log()
    st.dataframe(log_df)

