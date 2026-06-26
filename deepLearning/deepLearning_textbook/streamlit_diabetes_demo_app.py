import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Diabetes Risk Demo",
    page_icon="",
    layout="centered",
)

st.title("당뇨병 위험 예측 데모")

st.caption(
    "이 앱은 학습용 포트폴리오 데모입니다. "
    "의학적 진단이나 치료 판단에 사용할 수 없습니다."
)

st.subheader("입력값")

# 실제 프로젝트에서는 학습 때 사용한 feature_names와 같은 순서를 사용해야 한다.
# 여기서는 데모 구조를 보여주기 위해 일부 대표 입력만 사용한다.
age = st.slider("Age", min_value=18, max_value=100, value=45)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
high_bp = st.selectbox("High Blood Pressure", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
high_chol = st.selectbox("High Cholesterol", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
physical_activity = st.selectbox("Physical Activity", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

input_df = pd.DataFrame([{
    "Age": age,
    "BMI": bmi,
    "HighBP": high_bp,
    "HighChol": high_chol,
    "PhysActivity": physical_activity,
}])

st.write("입력 확인")
st.dataframe(input_df, use_container_width=True)

if st.button("예측하기"):
    # 실제 프로젝트에서는 이 부분을 17장에서 만든 예측 함수로 바꾼다.
    #
    # 예시:
    # model = keras.models.load_model("diabetes_model.keras")
    # scaler = joblib.load("diabetes_scaler.joblib")
    # feature_names = joblib.load("feature_names.joblib")
    # score = predict_diabetes_risk(input_df, model, scaler, feature_names)
    #
    # 지금은 앱 구조를 보여주기 위한 임시 점수 계산식이다.
    risk_score = (
        0.15
        + 0.004 * (age - 18)
        + 0.018 * max(bmi - 20, 0)
        + 0.14 * high_bp
        + 0.10 * high_chol
        - 0.06 * physical_activity
    )
    risk_score = min(max(risk_score, 0.0), 1.0)

    threshold = 0.50
    predicted_class = int(risk_score >= threshold)

    st.metric("예측 점수", f"{risk_score:.2f}")

    if predicted_class == 1:
        st.warning("모델 기준상 위험 점수가 높게 계산되었습니다.")
    else:
        st.success("모델 기준상 위험 점수가 낮게 계산되었습니다.")

    st.info(
        "이 결과는 학습용 예시입니다. "
        "실제 의료 판단은 전문가 상담과 검사를 통해 이루어져야 합니다."
    )

st.divider()
st.write("포트폴리오 설명 예시")
st.markdown(
    "- 노트북에서 학습한 모델을 사용자 입력 기반 데모로 확장하는 흐름을 보여줍니다.\n"
    "- 실제 배포 시에는 저장된 모델, scaler, feature order를 함께 불러와야 합니다.\n"
    "- 건강 관련 결과는 진단이 아니라 예측 점수로 표현해야 합니다."
)
