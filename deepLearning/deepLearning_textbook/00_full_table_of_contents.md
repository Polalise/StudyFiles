# 딥러닝 완전 입문 교재 전체 목차

이 목차는 Markdown 교재와 Jupyter Notebook 실습을 함께 보기 위한 기준 문서입니다. 번호가 `a`로 붙은 장과 `12-1`, `12-2`는 원본 흐름에서 빠지기 쉬운 내용을 보강하기 위해 추가한 연결형 부록 장입니다.

## 1부. 딥러닝의 아주 기본

1. [딥러닝의 기본 리듬](./01_deeplearning_basic_rhythm.md)
   - 실습: [01_deeplearning_basic_rhythm.ipynb](./notebooks/01_deeplearning_basic_rhythm.ipynb)
   - 입력, 예측, 손실, 학습, 가중치의 기본 흐름

2. [아주 작은 수식 읽기](./02_reading_tiny_math.md)
   - 실습: [02_reading_tiny_math.ipynb](./notebooks/02_reading_tiny_math.ipynb)
   - 딥러닝에서 자주 만나는 기호와 수식 읽는 법

3. [손실과 학습](./03_loss_and_training.md)
   - 실습: [03_loss_and_training.ipynb](./notebooks/03_loss_and_training.ipynb)
   - 손실 함수, 학습 방향, 오차를 줄이는 감각

4. [Keras 기본 워크플로우](./04_keras_basic_workflow.md)
   - 실습: [04_keras_basic_workflow.ipynb](./notebooks/04_keras_basic_workflow.ipynb)
   - `Sequential`, `Input`, `Dense`, `compile`, `fit`, `predict`

4-a. [TensorFlow 저수준 학습 원리](./04_a_tensorflow_low_level_training.md)
   - 실습: [04_a_tensorflow_low_level_training.ipynb](./notebooks/04_a_tensorflow_low_level_training.ipynb)
   - `fit()` 내부에서 일어나는 예측, 손실 계산, 기울기 계산, 가중치 업데이트

5. [활성화 함수](./05_activation_functions.md)
   - 실습: [05_activation_functions.ipynb](./notebooks/05_activation_functions.ipynb)
   - sigmoid, tanh, ReLU, softmax의 역할

6. [문제 유형과 손실 함수](./06_problem_types_and_loss_functions.md)
   - 실습: [06_problem_types_and_loss_functions.ipynb](./notebooks/06_problem_types_and_loss_functions.ipynb)
   - 회귀, 이진 분류, 다중 분류와 손실 함수 매칭

7. [EDA와 전처리](./07_eda_and_preprocessing.md)
   - 실습: [07_eda_and_preprocessing.ipynb](./notebooks/07_eda_and_preprocessing.ipynb)
   - 데이터 확인, 결측치, 스케일링, 데이터 누출 주의

7-a. [KMeans 비지도학습 입문](./07_a_kmeans_unsupervised_intro.md)
   - 실습: [07_a_kmeans_unsupervised_intro.ipynb](./notebooks/07_a_kmeans_unsupervised_intro.ipynb)
   - 정답 `y`가 없을 때 데이터를 묶어보는 기본 비지도학습

## 2부. 표 데이터와 건강 위험 예측

8. [표 데이터 MLP: 심장 질환 위험 예측](./08_tabular_mlp_heart_disease.md)
   - 실습: [08_tabular_mlp_heart_disease.ipynb](./notebooks/08_tabular_mlp_heart_disease.ipynb)
   - 표 데이터 이진 분류와 MLP 기본 구조

13. [건강 데이터 프로젝트 시작: 당뇨병 위험 예측 Baseline](./13_health_project_diabetes_baseline.md)
   - 실습: [13_health_project_diabetes_baseline.ipynb](./notebooks/13_health_project_diabetes_baseline.ipynb)
   - 당뇨병 위험 예측 baseline, 스케일링, confusion matrix

14. [임계값, Precision, Recall 이해하기](./14_threshold_precision_recall.md)
   - 실습: [14_threshold_precision_recall.ipynb](./notebooks/14_threshold_precision_recall.ipynb)
   - threshold, precision, recall, F1, FN/FP 해석

14-a. [Autoencoder 이상 탐지](./14_a_autoencoder_anomaly_detection.md)
   - 실습: [14_a_autoencoder_anomaly_detection.ipynb](./notebooks/14_a_autoencoder_anomaly_detection.ipynb)
   - reconstruction error와 threshold로 이상 데이터를 판단하는 흐름

15. [당뇨병 예측 모델 개선과 실험 관리](./15_experiment_management_diabetes.md)
   - 실습: [15_experiment_management_diabetes.ipynb](./notebooks/15_experiment_management_diabetes.ipynb)
   - EarlyStopping, Dropout, 실험 결과표, 최종 모델 선택

16. [당뇨병 예측 모델 해석하기](./16_interpreting_diabetes_model.md)
   - 실습: [16_interpreting_diabetes_model.ipynb](./notebooks/16_interpreting_diabetes_model.ipynb)
   - permutation importance, 입력 변수 실험, 인과와 해석 구분

16-a. [PCA와 SHAP 입문](./16_a_pca_shap_intro.md)
   - 실습: [16_a_pca_shap_intro.ipynb](./notebooks/16_a_pca_shap_intro.ipynb)
   - 차원 축소와 모델 설명 도구의 역할 구분

17. [당뇨병 위험 예측 함수 만들기](./17_diabetes_prediction_function.md)
   - 실습: [17_diabetes_prediction_function.ipynb](./notebooks/17_diabetes_prediction_function.ipynb)
   - 모델, scaler, feature order 저장과 예측 함수

18. [당뇨병 예측 프로젝트 포트폴리오 문서 만들기](./18_diabetes_project_portfolio.md)
   - 실습: [18_diabetes_project_portfolio.ipynb](./notebooks/18_diabetes_project_portfolio.ipynb)
   - README 초안, 한계, 개선 방향, 발표용 요약

18-a. [Streamlit 데모 입문](./18_a_streamlit_demo_intro.md)
   - 실습: [18_a_streamlit_demo_intro.ipynb](./notebooks/18_a_streamlit_demo_intro.ipynb)
   - 노트북 결과를 포트폴리오용 입력/예측 데모로 연결

## 3부. 이미지 분류와 CNN

9. [이미지 분류와 CNN 입문](./09_image_cnn_digits.md)
   - 실습: [09_image_cnn_digits.ipynb](./notebooks/09_image_cnn_digits.ipynb)
   - 이미지 배열, CNN, 합성곱과 풀링 입문

9-a. [Fashion-MNIST CNN 퀴즈](./09_a_fashion_mnist_cnn_quiz.md)
   - 실습: [09_a_fashion_mnist_cnn_quiz.ipynb](./notebooks/09_a_fashion_mnist_cnn_quiz.ipynb)
   - MNIST 다음 단계로 이미지 CNN 분류 복습

10. [꽃 이미지 CNN 미니 프로젝트](./10_flower_cnn_mini_project.md)
   - 실습: [10_flower_cnn_mini_project.ipynb](./notebooks/10_flower_cnn_mini_project.ipynb)
   - 폴더 기반 이미지 데이터셋, CNN 학습, 모델 저장

11. [꽃 CNN 결과 분석과 오답 확인](./11_flower_cnn_error_analysis.md)
   - 실습: [11_flower_cnn_error_analysis.ipynb](./notebooks/11_flower_cnn_error_analysis.ipynb)
   - confusion matrix, 클래스별 정확도, 오답 이미지 확인

12. [전이학습으로 꽃 분류 개선하기](./12_transfer_learning_flower.md)
   - 실습: [12_transfer_learning_flower.ipynb](./notebooks/12_transfer_learning_flower.ipynb)
   - MobileNetV2, `include_top=False`, feature extractor

12-a. [GAN 입문](./12_a_gan_intro.md)
   - 실습: [12_a_gan_intro.ipynb](./notebooks/12_a_gan_intro.ipynb)
   - 이미지를 분류하는 모델에서 이미지를 생성하는 모델로 확장

12-1. [객체 탐지와 YOLO 입문](./12_1_object_detection_yolo.md)
   - 실습: [12_1_object_detection_yolo.ipynb](./notebooks/12_1_object_detection_yolo.ipynb)
   - 이미지 분류와 객체 탐지 차이, bounding box, YOLO 개념

12-2. [YOLO 실제 실행 입문](./12_2_yolo_practical_intro.md)
   - 실습: [12_2_yolo_practical_intro.ipynb](./notebooks/12_2_yolo_practical_intro.ipynb)
   - 사전학습 YOLO 모델 호출, box/class/confidence 읽기

## 4부. PM10 환경/건강 시계열 예측

19. [PM10 시계열 데이터 입문](./19_pm10_time_series_intro.md)
   - 실습: [19_pm10_time_series_intro.ipynb](./notebooks/19_pm10_time_series_intro.ipynb)
   - PM10 데이터 읽기, 날짜 변환, 지표 선택, 이동평균

20. [PM10 데이터를 LSTM 입력 모양으로 만들기](./20_pm10_lstm_dataset.md)
   - 실습: [20_pm10_lstm_dataset.ipynb](./notebooks/20_pm10_lstm_dataset.ipynb)
   - window, `(samples, timesteps, features)`, MinMaxScaler

21. [LSTM으로 PM10 다음 시간 예측하기](./21_pm10_lstm_forecasting.md)
   - 실습: [21_pm10_lstm_forecasting.ipynb](./notebooks/21_pm10_lstm_forecasting.ipynb)
   - LSTM 회귀 모델, MAE/RMSE, `inverse_transform`

21-a. [RNN, LSTM, GRU, BiLSTM 비교](./21_a_rnn_lstm_gru_bilstm_comparison.md)
   - 실습: [21_a_rnn_lstm_gru_bilstm_comparison.ipynb](./notebooks/21_a_rnn_lstm_gru_bilstm_comparison.ipynb)
   - 같은 window 데이터로 순환 모델 계열 비교

22. [PM10 예측: LSTM과 단순 Baseline 비교하기](./22_pm10_baseline_comparison.md)
   - 실습: [22_pm10_baseline_comparison.ipynb](./notebooks/22_pm10_baseline_comparison.ipynb)
   - naive baseline, mean baseline, LSTM 비교

23. [PM10 다변량 LSTM: PM2.5 함께 사용하기](./23_pm10_multivariate_lstm.md)
   - 실습: [23_pm10_multivariate_lstm.ipynb](./notebooks/23_pm10_multivariate_lstm.ipynb)
   - PM10 + PM2.5 다변량 입력, `(samples, 24, 2)`

24. [PM10 시계열 예측 프로젝트 포트폴리오 문서 만들기](./24_pm10_project_portfolio.md)
   - 실습: [24_pm10_project_portfolio.ipynb](./notebooks/24_pm10_project_portfolio.ipynb)
   - PM10 프로젝트 README 초안과 발표용 요약

## 5부. 경제 시계열 예측

25. [경제 시계열 프로젝트 시작: API로 데이터 가져오기](./25_economic_time_series_api_intro.md)
   - 실습: [25_economic_time_series_api_intro.ipynb](./notebooks/25_economic_time_series_api_intro.ipynb)
   - FRED API, `.env`, JSON 응답, 경제 지표 CSV 저장

26. [경제 시계열 예측용 데이터셋 만들기](./26_economic_forecasting_dataset.md)
   - 실습: [26_economic_forecasting_dataset.ipynb](./notebooks/26_economic_forecasting_dataset.ipynb)
   - `target_next_cpi`, lag feature, 미래 정보 누출 방지

27. [경제 시계열 예측: MLP와 LSTM 비교하기](./27_economic_mlp_lstm_comparison.md)
   - 실습: [27_economic_mlp_lstm_comparison.ipynb](./notebooks/27_economic_mlp_lstm_comparison.ipynb)
   - lag MLP, window LSTM, MAE/RMSE 비교

28. [경제 시계열 예측 프로젝트 포트폴리오 문서 만들기](./28_economic_project_portfolio.md)
   - 실습: [28_economic_project_portfolio.ipynb](./notebooks/28_economic_project_portfolio.ipynb)
   - API 수집, target 설계, 모델 비교, 한계 정리

## 6부. 최종 정리

29. [최종 로드맵: 상황에 맞게 딥러닝을 고르는 법](./29_final_roadmap_and_model_selection.md)
   - 실습: [29_final_roadmap_and_model_selection.ipynb](./notebooks/29_final_roadmap_and_model_selection.ipynb)
   - 문제 유형별 모델 선택, 대표 포트폴리오 프로젝트 선택, 최종 체크리스트

## 추천 학습 순서

1. 처음부터 차례대로 1장부터 7장까지 기본기를 먼저 익힌다.
2. 프로젝트 중심 학습이 필요하면 13장부터 18-a장까지 당뇨병 프로젝트를 완성한다.
3. 이미지 확장이 필요하면 9장부터 12-2장까지 CNN, 전이학습, GAN, YOLO 흐름을 확인한다.
4. 시계열 확장이 필요하면 19장부터 24장까지 PM10 프로젝트를 진행한다.
5. 경제 데이터 프로젝트가 필요하면 25장부터 28장까지 API 기반 경제 시계열 프로젝트를 진행한다.
6. 마지막으로 29장에서 본인 포트폴리오에 가장 맞는 프로젝트 방향을 선택한다.
