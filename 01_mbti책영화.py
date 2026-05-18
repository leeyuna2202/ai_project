import streamlit as st

st.set_page_config(
    page_title="MBTI 책 & 영화 추천",
    page_icon="📚",
    layout="centered"
)

# MBTI별 추천 데이터
mbti_data = {
    "ENFP": {
        "books": [
            "📘 어린 왕자 - 생텍쥐페리",
            "📗 미드나잇 라이브러리 - 매트 헤이그"
        ],
        "movies": [
            "🎬 월터의 상상은 현실이 된다",
            "🎬 라라랜드"
        ]
    },
    "INTJ": {
        "books": [
            "📘 사피엔스 - 유발 하라리",
            "📗 데미안 - 헤르만 헤세"
        ],
        "movies": [
            "🎬 인터스텔라",
            "🎬 인셉션"
        ]
    },
    "INFP": {
        "books": [
            "📘 연금술사 - 파울로 코엘료",
            "📗 아몬드 - 손원평"
        ],
        "movies": [
            "🎬 코코",
            "🎬 이터널 선샤인"
        ]
    },
    "ENTP": {
        "books": [
            "📘 생각에 관한 생각 - 대니얼 카너먼",
            "📗 멋진 신세계 - 올더스 헉슬리"
        ],
        "movies": [
            "🎬 아이언맨",
            "🎬 나이브스 아웃"
        ]
    },
    "INFJ": {
        "books": [
            "📘 모모 - 미하엘 엔데",
            "📗 죽고 싶지만 떡볶이는 먹고 싶어 - 백세희"
        ],
        "movies": [
            "🎬 굿 윌 헌팅",
            "🎬 소울"
        ]
    },
    "ENTJ": {
        "books": [
            "📘 원씽 - 게리 켈러",
            "📗 넛지 - 리처드 탈러"
        ],
        "movies": [
            "🎬 소셜 네트워크",
            "🎬 울프 오브 월스트리트"
        ]
    },
    "ISTJ": {
        "books": [
            "📘 총, 균, 쇠 - 재레드 다이아몬드",
            "📗 공부의 본질 - 이윤규"
        ],
        "movies": [
            "🎬 이미테이션 게임",
            "🎬 머니볼"
        ]
    },
    "ISFJ": {
        "books": [
            "📘 나미야 잡화점의 기적 - 히가시노 게이고",
            "📗 아주 작은 습관의 힘 - 제임스 클리어"
        ],
        "movies": [
            "🎬 원더",
            "🎬 리틀 포레스트"
        ]
    },
    "ESTJ": {
        "books": [
            "📘 성공하는 사람들의 7가지 습관",
            "📗 부자 아빠 가난한 아빠"
        ],
        "movies": [
            "🎬 탑건 매버릭",
            "🎬 포드 V 페라리"
        ]
    },
    "ESFJ": {
        "books": [
            "📘 미움받을 용기",
            "📗 완벽하지 않은 것들에 대한 사랑"
        ],
        "movies": [
            "🎬 어바웃 타임",
            "🎬 인사이드 아웃"
        ]
    },
    "ISTP": {
        "books": [
            "📘 해커스",
            "📗 팩트풀니스"
        ],
        "movies": [
            "🎬 존 윅",
            "🎬 매드맥스"
        ]
    },
    "ISFP": {
        "books": [
            "📘 달러구트 꿈 백화점",
            "📗 방구석 미술관"
        ],
        "movies": [
            "🎬 비긴 어게인",
            "🎬 업"
        ]
    },
    "ESTP": {
        "books": [
            "📘 트렌드 코리아",
            "📗 돈의 속성"
        ],
        "movies": [
            "🎬 분노의 질주",
            "🎬 스파이더맨: 노웨이홈"
        ]
    },
    "ESFP": {
        "books": [
            "📘 오늘 밤, 세계에서 이 사랑이 사라진다 해도",
            "📗 나는 나로 살기로 했다"
        ],
        "movies": [
            "🎬 위대한 쇼맨",
            "🎬 알라딘"
        ]
    },
    "INTP": {
        "books": [
            "📘 코스모스 - 칼 세이건",
            "📗 이기적 유전자 - 리처드 도킨스"
        ],
        "movies": [
            "🎬 마션",
            "🎬 테넷"
        ]
    },
    "ENFJ": {
        "books": [
            "📘 인간관계론 - 데일 카네기",
            "📗 페인트 - 이희영"
        ],
        "movies": [
            "🎬 죽은 시인의 사회",
            "🎬 빅 히어로"
        ]
    }
}

# 제목
st.title("✨ MBTI 책 & 영화 추천 📚🎬")
st.write("너의 MBTI에 딱 어울리는 작품들을 추천해줄게 😎")

# MBTI 선택
selected_mbti = st.selectbox(
    "👉 MBTI를 선택해봐!",
    list(mbti_data.keys())
)

# 버튼 클릭
if st.button("💖 추천 받기"):

    data = mbti_data[selected_mbti]

    st.subheader(f"🌈 {selected_mbti} 추천 리스트")

    # 책 추천
    st.markdown("## 📚 추천 책 2권")
    for book in data["books"]:
        st.markdown(f"- {book}")

    # 영화 추천
    st.markdown("## 🎬 추천 영화 2편")
    for movie in data["movies"]:
        st.markdown(f"- {movie}")

    st.success("✨ 재미있게 즐겨봐! 취향 저격일지도? 😆")
