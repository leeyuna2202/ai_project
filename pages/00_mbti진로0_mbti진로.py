import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천",
    page_icon="✨",
    layout="centered"
)

# MBTI별 진로 데이터
career_data = {
    "INTJ": [
        {
            "job": "🧠 데이터 사이언티스트",
            "major": "컴퓨터공학과, 통계학과",
            "personality": "논리적이고 분석적인 사람",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "🚀 전략 컨설턴트",
            "major": "경영학과, 경제학과",
            "personality": "계획 세우기를 좋아하는 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "INTP": [
        {
            "job": "💻 프로그래머",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "호기심 많고 아이디어가 풍부한 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🔬 연구원",
            "major": "물리학과, 화학과",
            "personality": "탐구를 좋아하는 사람",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],
    "ENTJ": [
        {
            "job": "🏢 CEO",
            "major": "경영학과",
            "personality": "리더십이 강한 사람",
            "salary": "평균 연봉 약 7,000만원"
        },
        {
            "job": "📈 마케팅 매니저",
            "major": "광고홍보학과",
            "personality": "목표 지향적인 사람",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],
    "ENTP": [
        {
            "job": "🎤 크리에이터",
            "major": "미디어학과",
            "personality": "창의적이고 활동적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "💡 스타트업 창업가",
            "major": "경영학과",
            "personality": "도전을 즐기는 사람",
            "salary": "평균 연봉 다양함 😆"
        }
    ],
    "INFJ": [
        {
            "job": "🩺 상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "✍️ 작가",
            "major": "국문학과",
            "personality": "상상력이 풍부한 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],
    "INFP": [
        {
            "job": "🎨 디자이너",
            "major": "디자인학과",
            "personality": "감수성이 풍부한 사람",
            "salary": "평균 연봉 약 4,300만원"
        },
        {
            "job": "📚 웹소설 작가",
            "major": "문예창작과",
            "personality": "창의적인 사람",
            "salary": "평균 연봉 다양함 ✨"
        }
    ],
    "ENFJ": [
        {
            "job": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람을 돕는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🎯 HR 전문가",
            "major": "경영학과",
            "personality": "소통을 잘하는 사람",
            "salary": "평균 연봉 약 5,200만원"
        }
    ],
    "ENFP": [
        {
            "job": "🎬 방송 PD",
            "major": "방송영상학과",
            "personality": "열정적이고 아이디어가 많은 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "📱 SNS 마케터",
            "major": "광고홍보학과",
            "personality": "트렌드에 민감한 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "ISTJ": [
        {
            "job": "⚖️ 공무원",
            "major": "행정학과",
            "personality": "책임감이 강한 사람",
            "salary": "평균 연봉 약 4,800만원"
        },
        {
            "job": "🏦 회계사",
            "major": "회계학과",
            "personality": "꼼꼼한 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "ISFJ": [
        {
            "job": "💉 간호사",
            "major": "간호학과",
            "personality": "배려심이 깊은 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🏫 사회복지사",
            "major": "사회복지학과",
            "personality": "따뜻한 성격의 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],
    "ESTJ": [
        {
            "job": "📊 경영 관리자",
            "major": "경영학과",
            "personality": "체계적인 사람",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "job": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각하는 사람",
            "salary": "평균 연봉 약 5,200만원"
        }
    ],
    "ESFJ": [
        {
            "job": "🎀 승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 사교적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🏥 병원 코디네이터",
            "major": "보건행정학과",
            "personality": "배려심이 좋은 사람",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],
    "ISTP": [
        {
            "job": "🔧 엔지니어",
            "major": "기계공학과",
            "personality": "문제 해결을 좋아하는 사람",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "🛠 자동차 정비사",
            "major": "자동차공학과",
            "personality": "손재주가 좋은 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "ISFP": [
        {
            "job": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "예술 감각이 뛰어난 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "🎵 작곡가",
            "major": "실용음악과",
            "personality": "감성적인 사람",
            "salary": "평균 연봉 다양함 🎶"
        }
    ],
    "ESTP": [
        {
            "job": "🏀 스포츠 트레이너",
            "major": "체육학과",
            "personality": "활동적인 사람",
            "salary": "평균 연봉 약 4,300만원"
        },
        {
            "job": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "도전 정신이 강한 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "ESFP": [
        {
            "job": "🎤 연예인",
            "major": "연극영화과",
            "personality": "에너지가 넘치는 사람",
            "salary": "평균 연봉 다양함 🌟"
        },
        {
            "job": "🎉 이벤트 플래너",
            "major": "관광경영학과",
            "personality": "사람들과 어울리는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 4,300만원"
        }
    ]
}

# 제목
st.title("✨ MBTI 진로 추천 프로그램")
st.write("너의 MBTI에 딱 맞는 직업을 추천해줄게 😎")

# MBTI 선택
mbti = st.selectbox(
    "👉 너의 MBTI를 선택해봐!",
    list(career_data.keys())
)

# 버튼
if st.button("🔍 진로 추천 받기"):

    st.subheader(f"🎯 {mbti} 유형 추천 진로")

    careers = career_data[mbti]

    for idx, career in enumerate(careers, start=1):
        st.markdown(f"""
        ---
        ## {idx}. {career['job']}

        📚 **추천 학과**  
        {career['major']}

        💖 **잘 어울리는 성격**  
        {career['personality']}

        💰 **평균 연봉**  
        {career['salary']}
        """)

    st.success("✨ 미래의 멋진 너를 응원할게! 🚀")
