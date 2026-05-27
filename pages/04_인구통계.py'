import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

# ---------------------------
# 한글 폰트 설정
# ---------------------------
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
else:
    plt.rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False

# ---------------------------
# 데이터 불러오기
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("population.csv", encoding="euc-kr")
    return df

df = load_data()

st.title("행정구별 연령 인구 분석")

# ---------------------------
# 행정구 선택
# ---------------------------
regions = df["행정구역"].unique()

selected_region = st.selectbox(
    "행정구를 선택하세요",
    regions
)

# ---------------------------
# 선택된 지역 데이터
# ---------------------------
row = df[df["행정구역"] == selected_region].iloc[0]

# ---------------------------
# 연령별 데이터 추출
# ---------------------------
ages = []
population = []

for col in df.columns:
    if "2026년04월_거주자_" in col:
        age_text = col.replace("2026년04월_거주자_", "")

        # 숫자 나이만 추출
        if age_text.endswith("세"):
            try:
                age = int(age_text.replace("세", ""))

                value = str(row[col]).replace(",", "")
                value = int(value)

                ages.append(age)
                population.append(value)

            except:
                pass

# ---------------------------
# 그래프 생성
# ---------------------------
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(
    ages,
    population,
    color="hotpink",
    linewidth=2
)

# x축 10살 단위 구분선
ax.set_xticks(range(0, 101, 10))
ax.grid(axis='x', linestyle='--', alpha=0.5)

# 제목 및 축 이름
ax.set_title(f"{selected_region} 연령별 인구수", fontsize=16)
ax.set_xlabel("나이", fontsize=12)
ax.set_ylabel("인구수", fontsize=12)

st.pyplot(fig)
