import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="공공데이터 상관관계 분석기", layout="wide")

st.title("📊 공공데이터 자동 상관관계 분석기")

st.markdown("""
1. 공공데이터 CSV 파일을 업로드하거나,  
2. CSV 파일 URL을 넣으면  
→ 컬럼 목록을 보여주고,  
→ X축 / Y축 컬럼을 고르면  
→ 그래프 + 상관계수를 자동 계산해주는 도구입니다.
""")

# -------------------
# 1. 데이터 불러오기
# -------------------
st.sidebar.header("데이터 불러오기")

upload_option = st.sidebar.radio(
    "데이터 입력 방식 선택",
    ("CSV 파일 업로드", "CSV URL 입력"),
)

df = None

if upload_option == "CSV 파일 업로드":
    uploaded_file = st.sidebar.file_uploader("CSV 파일 선택", type=["csv"])
    if uploaded_file is not None:
        # 인코딩 문제 있으면 encoding 매개변수 조정 가능 (e.g. "cp949", "euc-kr")
        df = pd.read_csv(uploaded_file)
elif upload_option == "CSV URL 입력":
    url = st.sidebar.text_input("CSV 파일 URL 입력")
    if url and st.sidebar.button("URL에서 불러오기"):
        try:
            df = pd.read_csv(url)
        except Exception as e:
            st.sidebar.error(f"데이터 불러오기 오류: {e}")

# -------------------
# 2. 데이터 미리보기
# -------------------
if df is None:
    st.info("⬆️ 왼쪽 사이드바에서 CSV를 업로드하거나 URL을 입력하세요.")
    st.stop()

st.subheader("데이터 미리보기")
st.write("행/열 수:", df.shape)
st.dataframe(df.head())

st.subheader("컬럼 정보")
col_info = pd.DataFrame({
    "컬럼명": df.columns,
    "데이터 타입": [str(dtype) for dtype in df.dtypes]
})
st.table(col_info)

# 숫자형 컬럼만 추출
numeric_cols = df.select_dtypes(include="number").columns.tolist()

if len(numeric_cols) < 2:
    st.warning("숫자형 컬럼이 2개 이상 있어야 상관관계 분석이 가능합니다.")
    st.stop()

# -------------------
# 3. X/Y 컬럼 선택
# -------------------
st.subheader("분석할 변수 선택")

col1, col2 = st.columns(2)

with col1:
    x_col = st.selectbox("X축에 사용할 숫자형 컬럼", numeric_cols)
with col2:
    y_col = st.selectbox("Y축에 사용할 숫자형 컬럼", [c for c in numeric_cols if c != x_col])

# 결측치 제거
plot_df = df[[x_col, y_col]].dropna()

if plot_df.empty:
    st.warning("선택한 두 컬럼에 유효한 데이터가 없습니다(모두 결측).")
    st.stop()

# -------------------
# 4. 그래프 그리기
# -------------------
st.subheader("산점도 및 추세선")

fig = px.scatter(
    plot_df,
    x=x_col,
    y=y_col,
    trendline="ols",  # 간단한 회귀선
    title=f"{x_col} vs {y_col}"
)
st.plotly_chart(fig, use_container_width=True)

# -------------------
# 5. 상관계수 계산
# -------------------
st.subheader("상관관계 분석")

corr_value = plot_df[x_col].corr(plot_df[y_col])  # 피어슨 상관계수

def interpret_corr(r: float) -> str:
    ar = abs(r)
    if ar < 0.1:
        return "거의 상관관계 없음"
    elif ar < 0.3:
        return "약한 상관관계"
    elif ar < 0.5:
        return "보통 수준의 상관관계"
    elif ar < 0.7:
        return "꽤 강한 상관관계"
    else:
        return "매우 강한 상관관계"

st.metric(
    label=f"{x_col} - {y_col} 피어슨 상관계수",
    value=f"{corr_value:.3f}",
    delta=interpret_corr(corr_value),
)

st.markdown(f"""
- **양수(+)**이면: `{x_col}`이 증가할수록 `{y_col}`도 함께 증가하는 경향  
- **음수(-)**이면: `{x_col}`이 증가할수록 `{y_col}`은 감소하는 경향  
- |r| 값이 클수록(1에 가까울수록) 두 변수의 선형 관계가 강합니다.
""")

# -------------------
# 6. 전체 상관계수 매트릭스 (옵션)
# -------------------
with st.expander("📌 숫자형 컬럼 전체 상관계수 매트릭스 보기"):
    corr_matrix = df[numeric_cols].corr()
    st.dataframe(corr_matrix.style.background_gradient(axis=None))

