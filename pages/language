import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- 데이터 정의 ---

language_data = {
    "Python": {
        "특징": [
            "문법이 간결하고 배우기 쉬움",
            "방대한 라이브러리 지원",
            "인터프리터 방식"
        ],
        "사용 용도": [
            "데이터 과학, AI, 웹 개발, 자동화 스크립트"
        ],
        "장점": [
            "생산성 높음",
            "다양한 분야에 사용 가능",
            "커뮤니티와 자료가 풍부함"
        ],
        "단점": [
            "속도가 느림",
            "모바일 앱 개발에는 비선호"
        ],
        "코드 예제": '''# 리스트의 합 구하기
numbers = [1, 2, 3, 4, 5]
print("합:", sum(numbers))'''
    },
    "JavaScript": {
        "특징": [
            "웹 프론트엔드의 핵심 언어",
            "동적 타입, 인터프리터 언어",
            "Node.js로 백엔드도 가능"
        ],
        "사용 용도": [
            "웹 프론트엔드/백엔드 개발",
            "하이브리드 앱 개발"
        ],
        "장점": [
            "브라우저에서 바로 실행 가능",
            "생태계가 크고 활발함"
        ],
        "단점": [
            "동적 타입으로 오류가 런타임에 발생",
            "초보자에게 비직관적인 부분이 있음"
        ],
        "코드 예제": '''// 배열의 합 구하기
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((a, b) => a + b);
console.log("합:", sum);'''
    },
    "Java": {
        "특징": [
            "정적 타입, 객체지향 언어",
            "JVM 기반으로 플랫폼 독립적",
            "비교적 안정적이고 구조적"
        ],
        "사용 용도": [
            "기업용 백엔드 시스템",
            "안드로이드 앱 개발"
        ],
        "장점": [
            "성능이 좋고 확장성이 큼",
            "강력한 타입 시스템"
        ],
        "단점": [
            "코드가 장황할 수 있음",
            "런타임이 무거울 수 있음"
        ],
        "코드 예제": '''// 배열의 합 구하기
int[] numbers = {1, 2, 3, 4, 5};
int sum = 0;
for (int num : numbers) {
    sum += num;
}
System.out.println("합: " + sum);'''
    },
    "C++": {
        "특징": [
            "절차지향 + 객체지향",
            "시스템 프로그래밍에 적합",
            "복잡하지만 강력함"
        ],
        "사용 용도": [
            "게임 개발, 시스템/드라이버, 성능 요구 높은 애플리케이션"
        ],
        "장점": [
            "빠르고 효율적",
            "하드웨어 제어 가능"
        ],
        "단점": [
            "학습 난이도 높음",
            "메모리 관리 부담"
        ],
        "코드 예제": '''// 배열의 합 구하기
#include <iostream>
using namespace std;

int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    int sum = 0;
    for (int i = 0; i < 5; ++i) {
        sum += numbers[i];
    }
    cout << "합: " << sum << endl;
    return 0;
}'''
    },
}

# 인기 순위 (가상의 예시 값)
popularity_data = pd.DataFrame({
    "언어": ["Python", "JavaScript", "Java", "C++"],
    "인기도 점수": [95, 92, 85, 78]
})

# --- Streamlit 앱 UI ---

st.set_page_config(page_title="프로그래밍 언어 설명기", page_icon="🧠")
st.title("🧠 프로그래밍 언어 특징 & 인기 시각화")

# 인기 순위 시각화
st.subheader("📊 인기 순위 비교")

fig, ax = plt.subplots()
ax.bar(popularity_data["언어"], popularity_data["인기도 점수"], color="skyblue")
ax.set_ylabel("인기도 점수 (100점 만점)")
ax.set_ylim(0, 100)
st.pyplot(fig)

# 언어 선택
st.subheader("💡 언어별 특징 보기")

language = st.selectbox("언어를 선택하세요", list(language_data.keys()))
info = language_data[language]

st.markdown(f"### 🔍 {language}의 특징")
st.markdown("\n".join(f"- {f}" for f in info["특징"]))

st.markdown("### 🔧 사용 용도")
st.markdown("\n".join(f"- {f}" for f in info["사용 용도"]))

st.markdown("### ✅ 장점")
st.markdown("\n".join(f"- {f}" for f in info["장점"]))

st.markdown("### ⚠️ 단점")
st.markdown("\n".join(f"- {f}" for f in info["단점"]))

# 코드 예제
st.markdown("### 🧑‍💻 코드 예제")
st.code(info["코드 예제"], language=language.lower())
