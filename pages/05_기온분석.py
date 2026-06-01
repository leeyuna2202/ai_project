import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정 (Streamlit Cloud에서도 오류 없이 동작)
plt.rcParams["axes.unicode_minus"] = False

st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

st.title("🌡️ 서울 특정 날짜의 연도별 기온 변화")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("seoul.csv", encoding="cp949")
    except:
        df = pd.read_csv("seoul.csv", encoding="utf-8")

    df["날짜"] = pd.to_datetime(df["날짜"])

    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df

df = load_data()

# -----------------------
# 날짜 선택
# -----------------------
col1, col2 = st.columns(2)

with col1:
    month = st.selectbox(
        "월 선택",
        range(1, 13)
    )

available_days = sorted(
    df[df["월"] == month]["일"].unique()
)

with col2:
    day = st.selectbox(
        "일 선택",
        available_days
    )

# -----------------------
# 필터링
# -----------------------
filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

filtered = filtered.sort_values("연도")

filtered = filtered.dropna(
    subset=["최고기온(℃)", "최저기온(℃)"]
)

# -----------------------
# 그래프
# -----------------------
fig, ax = plt.subplots(figsize=(14, 6))

# 최고기온 (연한 핑크)
ax.plot(
    filtered["연도"],
    filtered["최고기온(℃)"],
    color="#ffb6c1",
    linewidth=2.5,
    label="최고기온"
)

# 최저기온 (연한 하늘색)
ax.plot(
    filtered["연도"],
    filtered["최저기온(℃)"],
    color="#87cefa",
    linewidth=2.5,
    label="최저기온"
)

ax.set_title(
    f"{month}월 {day}일의 연도별 최고·최저기온 변화",
    fontsize=16
)

ax.set_xlabel("연도")
ax.set_ylabel("기온(℃)")

ax.grid(True, alpha=0.3)

# 범례 표시
ax.legend()

st.pyplot(fig)

# -----------------------
# 데이터 보기
# -----------------------
st.subheader("선택한 날짜의 데이터")

st.dataframe(
    filtered[
        ["연도", "최고기온(℃)", "최저기온(℃)"]
    ],
    use_container_width=True
)
