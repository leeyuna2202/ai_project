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
    encodings = ["cp949", "euc-kr", "utf-8"]

    for enc in encodings:
        try:
            return pd.read_csv("lee.csv", encoding=enc)
        except:
            continue

    st.error("파일을 읽을 수 없습니다.")
    st.stop()

df = load_data()

# 컬럼 자동 찾기
region_col = None
temp_col = None

for col in df.columns:
    if "지점명" in col or "지점" in col:
        region_col = col

    if "평균기온" in col:
        temp_col = col

if region_col is None or temp_col is None:
    st.error("지역 또는 평균기온 컬럼을 찾을 수 없습니다.")
    st.write(df.columns.tolist())
    st.stop()

# 지역별 평균기온 계산
avg_temp_df = (
    df.groupby(region_col)[temp_col]
    .mean()
    .round(2)
    .reset_index()
)

# 지역 선택
selected_region = st.selectbox(
    "지역을 선택하세요",
    sorted(avg_temp_df[region_col].unique())
)

# 선택 지역 평균기온
avg_temp = float(
    avg_temp_df.loc[
        avg_temp_df[region_col] == selected_region,
        temp_col
    ].iloc[0]
)

# 색상 지정
if avg_temp >= 20:
    color = "#ff4d4d"   # 빨강
    level = "🔴 20도 이상"

elif avg_temp >= 15:
    color = "#ff9900"   # 주황
    level = "🟠 15도 이상"

else:
    color = "#ffd700"   # 노랑
    level = "🟡 15도 미만"

# 결과 출력
st.markdown(
    f"""
    <div style="
        background-color:{color};
        padding:30px;
        border-radius:15px;
        text-align:center;
        color:black;
        font-size:30px;
        font-weight:bold;">
        {selected_region}<br>
        평균기온: {avg_temp:.2f}℃<br>
        {level}
    </div>
    """,
    unsafe_allow_html=True
)

# 전체 지역 평균기온 보기
with st.expander("전체 지역 평균기온"):
    st.dataframe(
        avg_temp_df.sort_values(
            temp_col,
            ascending=False
        ),
        use_container_width=True
    )
