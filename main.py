import streamlit as st

# MBTI 유형별 데이터
mbti_data = {
    "INTJ": {
        "job": "전략가, 과학자, 엔지니어, 분석가",
        "match": "INTJ와 잘 맞는 사람은 ENFP나 ENTJ 유형으로, 자유로운 사고를 지닌 사람과 목표 지향적인 파트너입니다.",
    },
    "INTP": {
        "job": "철학자, 개발자, 연구원, 이론가",
        "match": "INTP는 ENTP나 INTP와 잘 맞으며, 논리적이고 지적인 대화를 나눌 수 있는 사람이 좋습니다.",
    },
    "ENTJ": {
        "job": "경영인, 리더, 관리자, 사업가",
        "match": "ENTJ와 잘 맞는 사람은 INTP나 INTJ 유형으로, 체계적이면서도 논리적인 성향을 가진 파트너입니다.",
    },
    "ENTP": {
        "job": "사업가, 혁신가, 마케터, 설계자",
        "match": "ENTP는 INFJ나 INTJ와 잘 맞으며, 창의적이고 열정적인 파트너를 선호합니다.",
    },
    "INFJ": {
        "job": "상담사, 심리학자, 예술가, 작가",
        "match": "INFJ는 ENTP나 ENFP와 잘 맞으며, 이해심이 깊고 따뜻한 사람을 선호합니다.",
    },
    "INFP": {
        "job": "작가, 예술가, 교사, 인도자",
        "match": "INFP는 ENFP나 INFJ와 잘 맞으며, 감성적이고 배려심이 깊은 파트너와 함께합니다.",
    },
    "ENFJ": {
        "job": "리더, 상담사, 교사, 이벤트 기획자",
        "match": "ENFJ는 INFP나 ISFJ와 잘 맞으며, 감정적 지지를 해줄 수 있는 파트너를 선호합니다.",
    },
    "ENFP": {
        "job": "탐험가, 마케터, 연예인, 작가",
        "match": "ENFP는 INTJ나 INFJ와 잘 맞으며, 창의적이고 활발한 파트너를 좋아합니다.",
    },
    "ISTJ": {
        "job": "공무원, 법조인, 관리자, 회계사",
        "match": "ISTJ는 ESTJ나 ISFJ와 잘 맞으며, 신뢰할 수 있고 계획적인 파트너를 선호합니다.",
    },
    "ISFJ": {
        "job": "간호사, 교사, 상담사, 비서",
        "match": "ISFJ는 ESFJ나 ISTJ와 잘 맞으며, 따뜻하고 헌신적인 파트너를 좋아합니다.",
    },
    "ESTJ": {
        "job": "관리자, 사업가, 군인, 조직 리더",
        "match": "ESTJ는 ISTJ나 ESFJ와 잘 맞으며, 책임감 있고 체계적인 파트너를 선호합니다.",
    },
    "ESFJ": {
        "job": "간호사, 교사, 이벤트 기획자, 사회복지사",
        "match": "ESFJ는 ISFJ나 ESTJ와 잘 맞으며, 배려심이 깊고 소통이 원활한 파트너를 좋아합니다.",
    },
    "ISTP": {
        "job": "엔지니어, 파일럿, 탐험가, 수리공",
        "match": "ISTP는 ESTP나 ISFP와 잘 맞으며, 실용적이고 자유로운 파트너를 선호합니다.",
    },
    "ISFP": {
        "job": "예술가, 디자이너, 수의사, 작가",
        "match": "ISFP는 ESFP나 ISTP와 잘 맞으며, 감성적이고 자유로운 파트너와 함께합니다.",
    },
    "ESTP": {
        "job": "사업가, 스포츠 선수, 마케터, 파일럿",
        "match": "ESTP는 ISTP나 ESFP와 잘 맞으며, 에너지 넘치고 활동적인 파트너를 좋아합니다.",
    },
    "ESFP": {
        "job": "연예인, 이벤트 기획자, 가이드, 배우",
        "match": "ESFP는 ISFP나 ESTP와 잘 맞으며, 즐겁고 활발한 파트너를 선호합니다.",
    },
}

# Streamlit 애플리케이션 제목
st.title("MBTI 기반 직업 추천 및 궁합 파트너")

# 사용자에게 MBTI 선택 드롭다운 메뉴 제공
mbti_selected = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    options=list(mbti_data.keys()),
    index=None,
    placeholder="MBTI를 선택해 주세요",
)

# MBTI 선택 시 결과 출력
if mbti_selected:
    st.subheader(f"당신의 MBTI 유형: {mbti_selected}")
    st.write("### 추천 직업")
    st.write(mbti_data[mbti_selected]["job"])
    st.write("### 잘 맞는 사람 유형")
    st.write(mbti_data[mbti_selected]["match"])
else:
    st.write("MBTI를 선택하면 추천 직업과 궁합 파트너가 표시됩니다.")
