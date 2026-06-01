import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="기온 분석",
    layout="wide"
)

plt.rcParams["axes.unicode_minus"] = False

st.title("🌡️ 특정 날짜의 연도별 최고·최저기온")

@st.cache_data
def load_data():

    # 인코딩 자동 처리
    encodings = ["cp949", "utf-8", "utf-8-sig"]

    for enc in encodings:
        try:
            df = pd.read_csv("seoul.csv", encoding=enc)
            break
        except:
            continue

    # 날짜를 문자열로 변환
    df["날짜"] = df["날짜"].astype(str)

    # 연도/월/일 추출
    split_date = df["날짜"].str.extract(
        r"(\d{4})[-./](\d{1,2})[-./](\d{1,2})"
    )

    df["연도"] = pd.to_numeric(split_date[0], errors="coerce")
    df["월"] = pd.to_numeric(split_date[1], errors="coerce")
    df["일"] = pd.to_numeric(split_date[2], errors="coerce")

    df = df.dropna(subset=["연도", "월", "일"])

    df["연도"] = df["연도"].astype(int)
    df["월"] = df["월"].astype(int)
    df["일"] = df["일"].astype(int)

    return df


df = load_data()

# 월 선택
month = st.selectbox(
    "월 선택",
    range(1, 13)
)

# 해당 월에 존재하는 일만 표시
available_days = sorted(
    df[df["월"] == month]["일"].unique()
)

day = st.selectbox(
    "일 선택",
    available_days
)

# 데이터 필터링
filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

filtered = filtered.sort_values("연도")

# 그래프
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(
    filtered["연도"],
    filtered["최고기온(℃)"],
    color="#FFB6C1",
    linewidth=2.5,
    label="최고기온"
)

ax.plot(
    filtered["연도"],
    filtered["최저기온(℃)"],
    color="#87CEFA",
    linewidth=2.5,
    label="최저기온"
)

ax.set_title(
    f"{month}월 {day}일 연도별 최고·최저기온"
)

ax.set_xlabel("연도")
ax.set_ylabel("기온(℃)")
ax.grid(alpha=0.3)
ax.legend()

st.pyplot(fig)

# 데이터 표
st.subheader("데이터")

st.dataframe(
    filtered[
        ["연도", "최고기온(℃)", "최저기온(℃)"]
    ],
    use_container_width=True
)
