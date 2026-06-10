import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(
    page_title="지역별 평균기온",
    page_icon="🌡️"
)

st.title("🌡️ 지역별 평균기온 조회")

# 데이터 읽기
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
            pass

    st.error("파일을 읽을 수 없습니다.")
    st.stop()

df = load_data()

# 컬럼 자동 찾기
region_col = None
temp_col = None

for col in df.columns:
    if "지점" in col:
        region_col = col
    if "평균기온" in col:
        temp_col = col

if region_col is None or temp_col is None:
    st.error("지점명 또는 평균기온 컬럼을 찾을 수 없습니다.")
    st.write(df.columns.tolist())
    st.stop()

# 지역별 평균기온 계산
region_avg = (
    df.groupby(region_col)[temp_col]
    .mean()
    .round(2)
    .reset_index()
)

# 지역 선택
selected_region = st.selectbox(
    "지역 선택",
    sorted(region_avg[region_col].unique())
)

avg_temp = float(
    region_avg.loc[
        region_avg[region_col] == selected_region,
        temp_col
    ].iloc[0]
)

# 색상 분류
if avg_temp >= 18.36:
    color = "#ff4d4d"
    label = "🔴 빨간색"

elif avg_temp == 18.35:
    color = "#ff9900"
    label = "🟠 주황색"

elif 18.24 <= avg_temp <= 18.25:
    color = "#ffd700"
    label = "🟡 노란색"

elif 18.12 <= avg_temp <= 18.15:
    color = "#4CAF50"
    label = "🟢 초록색"

elif 18.00 <= avg_temp <= 18.07:
    color = "#4da6ff"
    label = "🔵 파란색"

else:
    color = "#d9d9d9"
    label = "⚪ 구간 외"

# 결과 출력
st.markdown(
    f"""
    <div style="
        background-color:{color};
        padding:20px;
        border-radius:15px;
        text-align:center;
        font-size:30px;
        font-weight:bold;">
        {selected_region}<br>
        평균기온: {avg_temp:.2f}℃<br>
        {label}
    </div>
    """,
    unsafe_allow_html=True
)

# 전체 순위
st.subheader("전체 지역 평균기온")

st.dataframe(
    region_avg.sort_values(
        temp_col,
        ascending=False
    ),
    use_container_width=True
)
