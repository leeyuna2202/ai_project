import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="지역별 평균기온 조회",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ 지역별 평균기온 조회")

# 데이터 불러오기
@st.cache_data
def load_data():
    # 탭으로 구분된 기상청 파일
    df = pd.read_csv(
        "ISSUE_HW_DAY_2025-05_2025-05_2025.xls",
        sep="\t",
        encoding="cp949"
    )
    return df

df = load_data()

# 컬럼명 확인
region_col = "지점명"
temp_col = "평균기온(℃)"

# 지역별 평균기온 계산
region_temp = (
    df.groupby(region_col)[temp_col]
    .mean()
    .round(2)
    .reset_index()
)

# 지역 선택
selected_region = st.selectbox(
    "지역을 선택하세요",
    sorted(region_temp[region_col].unique())
)

# 선택 지역 평균기온
avg_temp = float(
    region_temp.loc[
        region_temp[region_col] == selected_region,
        temp_col
    ].iloc[0]
)

# 색상 구분
if avg_temp >= 18.36:
    bg_color = "#ff4d4d"  # 빨강
    text = "🔴 매우 높음"

elif avg_temp == 18.35:
    bg_color = "#ff9900"  # 주황
    text = "🟠 높음"

elif 18.24 <= avg_temp <= 18.25:
    bg_color = "#ffd700"  # 노랑
    text = "🟡 보통"

elif 18.12 <= avg_temp <= 18.15:
    bg_color = "#4CAF50"  # 초록
    text = "🟢 낮음"

elif 18.00 <= avg_temp <= 18.07:
    bg_color = "#4da6ff"  # 파랑
    text = "🔵 매우 낮음"

else:
    bg_color = "#d9d9d9"  # 회색
    text = "⚪ 구간 외"

# 결과 표시
st.markdown(
    f"""
    <div style="
        background-color:{bg_color};
        padding:25px;
        border-radius:15px;
        text-align:center;
        color:black;
        font-size:30px;
        font-weight:bold;">
        {selected_region}<br>
        평균기온 : {avg_temp:.2f} ℃<br>
        {text}
    </div>
    """,
    unsafe_allow_html=True
)

# 전체 지역 순위 보기
with st.expander("전체 지역 평균기온 순위"):
    st.dataframe(
        region_temp.sort_values(
            temp_col,
            ascending=False
        ),
        use_container_width=True
    )
