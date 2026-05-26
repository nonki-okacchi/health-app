import streamlit as st
import pandas as pd
from datetime import date
import os

st.title("頭痛・健康ログ")

today = st.date_input("日付", date.today())
headache = st.slider("頭痛レベル", 1, 5)
sleep = st.slider("睡眠時間（時間）", 0, 12)
meal_time = st.selectbox("食事時間", ["早い", "普通", "遅い"])
weather = st.selectbox("天気", ["晴れ", "雨", "寒い"])
medicine = st.selectbox("薬", ["飲んだ", "飲んでない"])

file_path = "health_log.csv"

if st.button("保存"):
    new_data = pd.DataFrame([{
        "日付": today,
        "頭痛": headache,
        "睡眠": sleep,
        "食事時間": meal_time,
        "天気": weather,
        "薬": medicine
    }])

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, new_data], ignore_index=True)
    else:
        df = new_data

    df.to_csv(file_path, index=False)

    st.success("保存しました！")
