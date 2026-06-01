import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(
    page_title="서울 기온 예측",
    layout="wide"
)

plt.rcParams["axes.unicode_minus"] = False

st.title("🌡️ 서울 특정 날짜 미래 기온 예측")

@st.cache_data
def load_data():

    encodings = ["cp949", "utf-8", "utf-8-sig"]

    for enc in encodings:
        try:
            df = pd.read_csv("seoul.csv", encoding=enc)
            break
        except:
            continue

    df["날짜"] = df["날짜"].astype(str)

    date_parts = df["날짜"].str.extract(
        r"(\d{4})[-./](\d{1,2})[-./](\d{1,2})"
    )

    df["연도"] = pd.to_numeric(date_parts[0], errors="coerce")
    df["월"] = pd.to_numeric(date_parts[1], errors="coerce")
    df["일"] = pd.to_numeric(date_parts[2], errors="coerce")

    df = df.dropna(subset=["연도", "월", "일"])

    df["연도"] = df["연도"].astype(int)
    df["월"] = df["월"].astype(int)
    df["일"] = df["일"].astype(int)

    return df


df = load_data()

month = st.selectbox(
    "월 선택",
    range(1, 13)
)

available_days = sorted(
    df[df["월"] == month]["일"].unique()
)

day = st.selectbox(
    "일 선택",
    available_days
)

latest_year = int(df["연도"].max())

future_year = st.number_input(
    "예측할 미래 연도",
    min_value=latest_year + 1,
    max_value=2200,
    value=2050
)

filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

filtered = filtered.dropna(
    subset=["최고기온(℃)", "최저기온(℃)"]
)

filtered = filtered.sort_values("연도")

X = filtered[["연도"]]

# 최고기온 모델
max_model = LinearRegression()
max_model.fit(X, filtered["최고기온(℃)"])

# 최저기온 모델
min_model = LinearRegression()
min_model.fit(X, filtered["최저기온(℃)"])

future_X = np.array([[future_year]])

pred_max = max_model.predict(future_X)[0]
pred_min = min_model.predict(future_X)[0]

result_df = pd.DataFrame({
    "구분": ["최고기온", "최저기온"],
    "예측기온(℃)": [pred_max, pred_min]
})

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(
    ["최고기온"],
    [pred_max],
    marker="o",
    markersize=10,
    linewidth=2,
    color="red",
    label="최고기온"
)

ax.plot(
    ["최저기온"],
    [pred_min],
    marker="o",
    markersize=10,
    linewidth=2,
    color="blue",
    label="최저기온"
)

ax.set_title(
    f"{future_year}년 {month}월 {day}일 예측 기온"
)

ax.set_ylabel("기온(℃)")
ax.legend()
ax.grid(alpha=0.3)

st.pyplot(fig)

st.subheader("예측 결과")

st.dataframe(
    result_df,
    use_container_width=True
)
