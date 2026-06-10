import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="지역별 평균기온",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ 지역별 평균기온 조회")

# 파일 읽기
@st.cache_data
def load_data():
    encodings = ["cp949", "euc-kr", "utf-8"]

    for enc in encodings:
        try:
            return pd.read_csv(
                "ISSUE_HW_DAY_2025-05_2025-05_2025.xls",
                sep="\t",
                encoding=enc
            )
        except:
            continue

    st.error("데이터 파일을 읽을 수 없습니다.")
    st.stop()

df = load_data()

# 컬럼 자동 탐색
region_col = None
temp_col = None

for col in df.columns:
    if "지점" in col:
        region_col = col

    if "평균기온" in col:
        temp_col = col

if region_col is None:
    st.error("지점명 컬럼을 찾을 수 없습니다.")
    st.write(df.columns.tolist())
    st.stop()

if temp_col is None:
    st.error("평균기온 컬럼을 찾을 수 없습니다.")
    st.write(df.columns.tolist())
    st.stop()

# 지역별 평균기온 계산
avg_df = (
    df.groupby(region_col)[temp_col]
    .mean()
    .round(2)
    .reset_index()
)

# 지역 선택
region = st.selectbox(
    "지역을 선택하세요",
    sorted(avg_df[region_col].unique())
)

temp = float(
    avg_df.loc[
        avg_df[region_col] == region,
        temp_col
    ].iloc[0]
)

# 색상 결정
if temp >= 18.36:
    bg_color = "#ff4d4d"
    level = "🔴 빨간색"

elif temp == 18.35:
    bg_color = "#ff9900"
    level = "🟠 주황색"

elif 18.24 <= temp <= 18.25:
    bg_color = "#ffd700"
    level = "🟡 노란색"

elif 18.12 <= temp <= 18.15:
    bg_color = "#4CAF50"
    level = "🟢 초록색"

elif 18.00 <= temp <= 18.07:
    bg_color = "#4da6ff"
    level = "🔵 파란색"

else:
    bg_color = "#d9d9d9"
    level = "⚪ 구간 외"

# 결과 출력
st.markdown(
    f"""
    <div style="
        background:{bg_color};
        padding:25px;
        border-radius:15px;
        text-align:center;
        font-size:30px;
        font-weight:bold;
        color:black;
    ">
        {region}<br>
        평균기온 {temp:.2f}℃<br>
        {level}
    </div>
    """,
    unsafe_allow_html=True
)

# 전체 순위
with st.expander("전체 지역 평균기온 순위"):
    st.dataframe(
        avg_df.sort_values(
            temp_col,
            ascending=False
        ),
        use_container_width=True
    )
