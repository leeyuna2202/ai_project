import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="Countries MBTI Analysis",
    layout="centered"
)

st.title("🌍 국가별 MBTI 비율 분석")

# CSV 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 국가 컬럼 제외한 MBTI 컬럼
mbti_cols = [col for col in df.columns if col != "Country"]

# 국가 선택
country = st.selectbox(
    "국가를 선택하세요",
    df["Country"].sort_values().unique()
)

# 선택된 국가 데이터
country_data = df[df["Country"] == country].iloc[0]

# MBTI 비율 추출
mbti_values = country_data[mbti_cols].astype(float)

# 내림차순 정렬
mbti_values = mbti_values.sort_values(ascending=False)

# 1등 MBTI
top_mbti = mbti_values.idxmax()

# 색상 생성
colors = []

# 하늘색 → 흐려지는 그라데이션
base_blue = np.array([135, 206, 250]) / 255  # skyblue

for i in range(len(mbti_values)):
    fade = 1 - (i / len(mbti_values)) * 0.7
    color = base_blue * fade + np.array([1, 1, 1]) * (1 - fade)
    colors.append(color)

# 1등은 노란색
colors[0] = "#FFD700"

# 그래프
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    mbti_values.index,
    mbti_values.values,
    color=colors
)

# 값 표시
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha='center',
        va='bottom',
        fontsize=9
    )

# 그래프 스타일
ax.set_title(f"{country} MBTI Distribution", fontsize=18)
ax.set_xlabel("MBTI Type")
ax.set_ylabel("Ratio")
ax.set_ylim(0, mbti_values.max() * 1.15)

plt.xticks(rotation=45)

st.pyplot(fig)

# 1위 MBTI 표시
st.success(f"🏆 {country}의 가장 높은 MBTI는 **{top_mbti}** 입니다.")
