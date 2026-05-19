import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 외국인 인기 관광지 TOP10",
    layout="wide"
)

st.title("🌏 외국인이 좋아하는 서울 주요 관광지 TOP10")
st.markdown("Folium 지도로 서울의 인기 관광지를 확인하세요.")

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선 왕조의 대표 궁궐"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "desc": "쇼핑과 길거리 음식의 중심지"
    },
    {
        "name": "N서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울 야경 명소"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "desc": "전통 한옥 거리"
    },
    {
        "name": "홍대거리",
        "lat": 37.556355,
        "lon": 126.922852,
        "desc": "젊음과 문화의 거리"
    },
    {
        "name": "강남",
        "lat": 37.497942,
        "lon": 127.027621,
        "desc": "트렌디한 쇼핑과 K-문화"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009223,
        "desc": "미래형 건축 랜드마크"
    },
    {
        "name": "인사동",
        "lat": 37.574187,
        "lon": 126.984952,
        "desc": "전통 문화와 기념품 거리"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.513068,
        "lon": 127.102749,
        "desc": "서울 스카이라인 대표 건물"
    },
    {
        "name": "한강공원",
        "lat": 37.528316,
        "lon": 126.932455,
        "desc": "서울 시민 휴식 공간"
    }
]

# 서울 중심 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="OpenStreetMap"
)

# 마커 추가
for place in places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=f"""
        <b>{place['name']}</b><br>
        {place['desc']}
        """,
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
st_folium(m, width=1200, height=700)

# 관광지 리스트
st.subheader("📍 관광지 목록")

for idx, place in enumerate(places, start=1):
    st.write(f"{idx}. {place['name']} - {place['desc']}")
