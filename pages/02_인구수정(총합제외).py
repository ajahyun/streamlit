import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 파일 불러오기
@st.cache_data
def load_data():
    file_path = 'age2411.csv'
    try:
        data = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        data = pd.read_csv(file_path, encoding='cp949')  # 한글 파일 인코딩 처리
    return data

# 인구 구조 시각화 함수
def plot_population_structure(data, region):
    # 선택한 지역으로 데이터 필터링
    filtered_data = data[data['행정구역'].str.contains(region)]
    if filtered_data.empty:
        st.warning("해당 지역의 데이터가 없습니다. 정확한 지역명을 입력해주세요.")
        return
    
    # 데이터에서 '총합'이나 '총 인구수'를 제외
    population_data = filtered_data.drop(columns=['행정구역']).iloc[0]  # 첫 번째 행 선택
    # '총 인구수', '합계'와 같은 키워드를 포함하는 열 제거
    population_data = population_data[~population_data.index.str.contains("총", na=False)]
    
    # 그래프 그리기
    plt.figure(figsize=(12, 6))
    plt.bar(population_data.index, population_data.values, color='skyblue')
    plt.xticks(rotation=90)
    plt.title(f"{region} 지역의 인구 구조 (총 인구수 제외)")
    plt.xlabel("연령대")
    plt.ylabel("인구 수")
    st.pyplot(plt)

# Streamlit 애플리케이션 UI 구성
st.title("지역별 인구 구조 시각화")
st.write("원하는 지역명을 입력하면 해당 지역의 인구 구조를 확인할 수 있습니다. (총 인구수 제외)")

# 데이터 불러오기
data = load_data()

# 지역 입력 받기
region = st.text_input("지역명을 입력하세요 (예: 서울특별시, 부산광역시):", "")

# 결과 출력
if region:
    st.subheader(f"'{region}' 지역의 인구 구조")
    plot_population_structure(data, region)
else:
    st.info("지역명을 입력하고 Enter를 눌러주세요.")
