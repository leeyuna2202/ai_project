import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="지역별 미세먼지 최고·최저 분석",
    page_icon="🌫️",
    layout="wide"
)

st.title("🌫️ 지역별 미세먼지 최고·최저 분석")

@st.cache_data
def load_data():
    encodings = ["cp949", "euc-kr", "utf-8"]

    for enc in encodings:
        try:
            return pd.read_csv("leeyuna.csv", encoding=enc)
        except:
            pass

    st.error("CSV 파일을 읽을 수 없습니다.")
    st.stop()

df = load_data()

# 컬럼명 정리
df["일시"] = pd.to_datetime(df["일시"])

# '평균' 제외
df = df[df["구분"] != "평균"]

# 지역 선택
region_list = sorted(df["구분"].unique())

selected_region = st.selectbox(
    "지역 선택",
    region_list
)

region_df = df[df["구분"] == selected_region].copy()

# 날짜별 최고/최저 PM10
daily_pm10 = (
    region_df.groupby(region_df["일시"].dt.date)["미세먼지(PM10)"]
    .agg(["max", "min"])
    .reset_index()
)

st.subheader(f"{selected_region} 미세먼지 최고·최저")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    daily_pm10["일시"],
    daily_pm10["max"],
    color="red",
    label="최고 PM10",
    linewidth=2
)

ax.plot(
    daily_pm10["일시"],
    daily_pm10["min"],
    color="blue",
    label="최저 PM10",
    linewidth=2
)

ax.set_xlabel("날짜")
ax.set_ylabel("PM10")
ax.set_title(f"{selected_region} 미세먼지 최고·최저 추이")
ax.legend()
ax.grid(True)

st.pyplot(fig)

st.dataframe(
    daily_pm10,
    use_container_width=True
)
