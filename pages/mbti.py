import streamlit as st

# MBTI 유형별 특징 및 추천 직업 데이터
mbti_data = {
    "ISTJ": {
        "특징": "현실적이고 체계적이며 신뢰할 수 있는 성격입니다. 계획적이고 책임감이 강해 주어진 일을 끝까지 해내는 유형입니다.",
        "추천 직업": ["회계사", "공무원", "데이터 분석가", "법률 전문가", "엔지니어"]
    },
    "ISFJ": {
        "특징": "헌신적이고 따뜻하며 조화를 중요시하는 성격입니다. 타인을 돌보는 데 뛰어나며 세심하고 성실합니다.",
        "추천 직업": ["간호사", "교사", "사회복지사", "사서", "상담사"]
    },
    "INFJ": {
        "특징": "통찰력 있고 직관적이며 타인을 돕고자 하는 성향이 강합니다. 공감 능력이 뛰어나며 깊은 관계를 선호합니다.",
        "추천 직업": ["심리상담사", "작가", "교수", "인사 전문가", "예술가"]
    },
    "INTJ": {
        "특징": "독립적이고 전략적이며 비전을 가지고 문제를 해결하는 성향입니다. 계획을 세우고 목표를 이루는 데 능숙합니다.",
        "추천 직업": ["경영 컨설턴트", "소프트웨어 개발자", "과학자", "변호사", "데이터 과학자"]
    },
    "ESTJ": {
        "특징": "현실적이고 리더십이 강하며 체계적으로 일을 처리하는 유형입니다. 목표 달성을 위해 노력합니다.",
        "추천 직업": ["경영자", "군인", "공무원", "프로젝트 매니저", "은행원"]
    },
    "ESFJ": {
        "특징": "따뜻하고 사교적이며 타인과의 관계를 중요시합니다. 조화를 추구하며 타인을 돕는 데 능숙합니다.",
        "추천 직업": ["간호사", "교사", "인사 전문가", "이벤트 코디네이터", "상담사"]
    },
}

# 혈액형별 특징 데이터
blood_type_data = {
    "A형": "꼼꼼하고 신중하며 계획을 세우는 것을 좋아합니다. 배려심이 많고 예의 바른 성격입니다.",
    "B형": "자유롭고 창의적이며 자신만의 길을 가는 성향이 강합니다. 즉흥적이고 열정적입니다.",
    "O형": "활발하고 사교적이며 리더십이 뛰어납니다. 자신감이 넘치며 목표 지향적입니다.",
    "AB형": "이해력이 뛰어나고 이성적이지만 때로는 감성적인 면을 보여줍니다. 독특하고 창의적입니다."
}

# Streamlit 애플리케이션 구성
st.title("MBTI 유형과 혈액형 비교 프로그램")
st.write("MBTI 유형과 혈액형을 선택하면 각각의 특징을 비교해볼 수 있습니다!")

# 사용자 입력 받기
selected_mbti = st.selectbox("MBTI 유형을 선택하세요:", options=list(mbti_data.keys()))
selected_blood_type = st.selectbox("혈액형을 선택하세요:", options=list(blood_type_data.keys()))

# 선택한 MBTI 유형과 혈액형 특징 보여주기
if selected_mbti:
    st.subheader(f"**{selected_mbti}** 유형의 특징")
    st.write(mbti_data[selected_mbti]["특징"])
    
    st.subheader("추천 직업")
    jobs = mbti_data[selected_mbti]["추천 직업"]
    st.write(", ".join(jobs))

if selected_blood_type:
    st.subheader(f"**{selected_blood_type}**의 특징")
    st.write(blood_type_data[selected_blood_type])

# MBTI와 혈액형 요약 비교
if selected_mbti and selected_blood_type:
    st.subheader("MBTI와 혈액형 비교")
    st.write(f"**{selected_mbti}** 유형의 특징: {mbti_data[selected_mbti]['특징']}")
    st.write(f"**{selected_blood_type}** 혈액형의 특징: {blood_type_data[selected_blood_type]}")
