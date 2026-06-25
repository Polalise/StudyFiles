# 딥러닝 완전 입문 교재

이 교재는 딥러닝을 처음 배우는 학습자를 위해 작성한다. 목표는 공식을 외우는 것이 아니라, 딥러닝의 흐름을 이해하고 직접 프로젝트와 포트폴리오로 연결할 수 있게 되는 것이다.

## 진행 방식

- 각 장은 Markdown 교재와 Jupyter Notebook 실습을 함께 제공한다.
- Markdown은 개념, 비유, 수식 읽는 법, 코드 해설, 과제를 담는다.
- Notebook은 직접 실행하는 실습용이며, 라이브러리와 메서드에 충분한 주석을 둔다.
- 이 교재 제작 대화에서는 노트북 코드 실행 검증을 하지 않고, `.ipynb` JSON 정상 여부만 확인한다.

## 현재 작성한 장

1. [01. 딥러닝의 기본 리듬](./01_deeplearning_basic_rhythm.md)
   - 실습: [01_deeplearning_basic_rhythm.ipynb](./notebooks/01_deeplearning_basic_rhythm.ipynb)
2. [02. 아주 작은 수식 읽기](./02_reading_tiny_math.md)
   - 실습: [02_reading_tiny_math.ipynb](./notebooks/02_reading_tiny_math.ipynb)
3. [03. 손실과 학습](./03_loss_and_training.md)
   - 실습: [03_loss_and_training.ipynb](./notebooks/03_loss_and_training.ipynb)
4. [04. Keras 기본 워크플로우](./04_keras_basic_workflow.md)
   - 실습: [04_keras_basic_workflow.ipynb](./notebooks/04_keras_basic_workflow.ipynb)
5. [05. 활성화 함수](./05_activation_functions.md)
   - 실습: [05_activation_functions.ipynb](./notebooks/05_activation_functions.ipynb)
6. [06. 문제 유형과 손실 함수](./06_problem_types_and_loss_functions.md)
   - 실습: [06_problem_types_and_loss_functions.ipynb](./notebooks/06_problem_types_and_loss_functions.ipynb)
7. [07. EDA와 전처리](./07_eda_and_preprocessing.md)
   - 실습: [07_eda_and_preprocessing.ipynb](./notebooks/07_eda_and_preprocessing.ipynb)
8. [08. 표 데이터 MLP: 심장 질환 위험 예측](./08_tabular_mlp_heart_disease.md)
   - 실습: [08_tabular_mlp_heart_disease.ipynb](./notebooks/08_tabular_mlp_heart_disease.ipynb)
9. [09. 이미지 분류와 CNN 입문](./09_image_cnn_digits.md)
   - 실습: [09_image_cnn_digits.ipynb](./notebooks/09_image_cnn_digits.ipynb)
10. [10. 꽃 이미지 CNN 미니 프로젝트](./10_flower_cnn_mini_project.md)
    - 실습: [10_flower_cnn_mini_project.ipynb](./notebooks/10_flower_cnn_mini_project.ipynb)
11. [11. 꽃 CNN 결과 분석과 오답 확인](./11_flower_cnn_error_analysis.md)
    - 실습: [11_flower_cnn_error_analysis.ipynb](./notebooks/11_flower_cnn_error_analysis.ipynb)
12. [12. 전이학습으로 꽃 분류 개선하기](./12_transfer_learning_flower.md)
    - 실습: [12_transfer_learning_flower.ipynb](./notebooks/12_transfer_learning_flower.ipynb)
13. [13. 건강 데이터 프로젝트 시작: 당뇨병 위험 예측 Baseline](./13_health_project_diabetes_baseline.md)
    - 실습: [13_health_project_diabetes_baseline.ipynb](./notebooks/13_health_project_diabetes_baseline.ipynb)
14. [14. 임계값, Precision, Recall 이해하기](./14_threshold_precision_recall.md)
    - 실습: [14_threshold_precision_recall.ipynb](./notebooks/14_threshold_precision_recall.ipynb)
15. [15. 당뇨병 예측 모델 개선과 실험 관리](./15_experiment_management_diabetes.md)
    - 실습: [15_experiment_management_diabetes.ipynb](./notebooks/15_experiment_management_diabetes.ipynb)
16. [16. 당뇨병 예측 모델 해석하기](./16_interpreting_diabetes_model.md)
    - 실습: [16_interpreting_diabetes_model.ipynb](./notebooks/16_interpreting_diabetes_model.ipynb)
17. [17. 당뇨병 위험 예측 함수 만들기](./17_diabetes_prediction_function.md)
    - 실습: [17_diabetes_prediction_function.ipynb](./notebooks/17_diabetes_prediction_function.ipynb)
18. [18. 당뇨병 예측 프로젝트 포트폴리오 문서 만들기](./18_diabetes_project_portfolio.md)
    - 실습: [18_diabetes_project_portfolio.ipynb](./notebooks/18_diabetes_project_portfolio.ipynb)
19. [19. PM10 시계열 데이터 입문](./19_pm10_time_series_intro.md)
    - 실습: [19_pm10_time_series_intro.ipynb](./notebooks/19_pm10_time_series_intro.ipynb)
20. [20. PM10 데이터를 LSTM 입력 모양으로 만들기](./20_pm10_lstm_dataset.md)
    - 실습: [20_pm10_lstm_dataset.ipynb](./notebooks/20_pm10_lstm_dataset.ipynb)
21. [21. LSTM으로 PM10 다음 시간 예측하기](./21_pm10_lstm_forecasting.md)
    - 실습: [21_pm10_lstm_forecasting.ipynb](./notebooks/21_pm10_lstm_forecasting.ipynb)
22. [22. PM10 예측: LSTM과 단순 Baseline 비교하기](./22_pm10_baseline_comparison.md)
    - 실습: [22_pm10_baseline_comparison.ipynb](./notebooks/22_pm10_baseline_comparison.ipynb)
23. [23. PM10 다변량 LSTM: PM2.5 함께 사용하기](./23_pm10_multivariate_lstm.md)
    - 실습: [23_pm10_multivariate_lstm.ipynb](./notebooks/23_pm10_multivariate_lstm.ipynb)
24. [24. PM10 시계열 예측 프로젝트 포트폴리오 문서 만들기](./24_pm10_project_portfolio.md)
    - 실습: [24_pm10_project_portfolio.ipynb](./notebooks/24_pm10_project_portfolio.ipynb)
25. [25. 경제 시계열 프로젝트 시작: API로 데이터 가져오기](./25_economic_time_series_api_intro.md)
    - 실습: [25_economic_time_series_api_intro.ipynb](./notebooks/25_economic_time_series_api_intro.ipynb)
26. [26. 경제 시계열 예측용 데이터셋 만들기](./26_economic_forecasting_dataset.md)
    - 실습: [26_economic_forecasting_dataset.ipynb](./notebooks/26_economic_forecasting_dataset.ipynb)
27. [27. 경제 시계열 예측: MLP와 LSTM 비교하기](./27_economic_mlp_lstm_comparison.md)
    - 실습: [27_economic_mlp_lstm_comparison.ipynb](./notebooks/27_economic_mlp_lstm_comparison.ipynb)
28. [28. 경제 시계열 예측 프로젝트 포트폴리오 문서 만들기](./28_economic_project_portfolio.md)
    - 실습: [28_economic_project_portfolio.ipynb](./notebooks/28_economic_project_portfolio.ipynb)

## 실습 준비

노트북 실행에는 아래 패키지가 필요하다.

```text
numpy
pandas
matplotlib
scikit-learn
keras
tensorflow
jupyter
```

현재 교재는 CPU 환경에서도 따라올 수 있도록 작은 예제부터 시작한다.

## 확정 프로젝트 축

1. 꽃 이미지 CNN 미니 프로젝트
2. 건강/의료 위험 예측 프로젝트
3. 환경/건강 PM10 시계열 예측 프로젝트
4. 경제 시계열 예측 프로젝트
