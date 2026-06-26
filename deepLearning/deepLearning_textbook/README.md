# 딥러닝 완전 입문 교재

이 교재는 딥러닝을 처음 배우는 학습자가 개념을 이해하고, 직접 코드를 실행해보고, 최종적으로 포트폴리오 프로젝트까지 완성할 수 있도록 만든 학습 자료입니다.

전체 목차는 [00_full_table_of_contents.md](./00_full_table_of_contents.md)를 기준으로 관리합니다.

## 진행 방식

- 각 장은 Markdown 교재와 Jupyter Notebook 실습을 함께 제공합니다.
- Markdown은 개념, 비유, 수식 읽는 법, 코드 해설, 과제를 담습니다.
- Notebook은 직접 실행하는 실습용 파일이며, 라이브러리와 메서드에는 초보자용 주석을 충분히 둡니다.
- 이 교재 작업에서는 노트북 실행 여부보다 JSON 정상 여부를 기본 점검 기준으로 삼되, 사용자가 요청한 장은 실행 테스트까지 진행합니다.

## 현재 작성된 장

### 1부. 딥러닝의 아주 기본

1. [딥러닝의 기본 리듬](./01_deeplearning_basic_rhythm.md)
   - 실습: [01_deeplearning_basic_rhythm.ipynb](./notebooks/01_deeplearning_basic_rhythm.ipynb)

2. [아주 작은 수식 읽기](./02_reading_tiny_math.md)
   - 실습: [02_reading_tiny_math.ipynb](./notebooks/02_reading_tiny_math.ipynb)

3. [손실과 학습](./03_loss_and_training.md)
   - 실습: [03_loss_and_training.ipynb](./notebooks/03_loss_and_training.ipynb)

4. [Keras 기본 워크플로우](./04_keras_basic_workflow.md)
   - 실습: [04_keras_basic_workflow.ipynb](./notebooks/04_keras_basic_workflow.ipynb)

4-a. [TensorFlow 저수준 학습 원리](./04_a_tensorflow_low_level_training.md)
   - 실습: [04_a_tensorflow_low_level_training.ipynb](./notebooks/04_a_tensorflow_low_level_training.ipynb)

5. [활성화 함수](./05_activation_functions.md)
   - 실습: [05_activation_functions.ipynb](./notebooks/05_activation_functions.ipynb)

6. [문제 유형과 손실 함수](./06_problem_types_and_loss_functions.md)
   - 실습: [06_problem_types_and_loss_functions.ipynb](./notebooks/06_problem_types_and_loss_functions.ipynb)

7. [EDA와 전처리](./07_eda_and_preprocessing.md)
   - 실습: [07_eda_and_preprocessing.ipynb](./notebooks/07_eda_and_preprocessing.ipynb)

7-a. [KMeans 비지도학습 입문](./07_a_kmeans_unsupervised_intro.md)
   - 실습: [07_a_kmeans_unsupervised_intro.ipynb](./notebooks/07_a_kmeans_unsupervised_intro.ipynb)

### 2부. 표 데이터와 건강 위험 예측

8. [표 데이터 MLP: 심장 질환 위험 예측](./08_tabular_mlp_heart_disease.md)
   - 실습: [08_tabular_mlp_heart_disease.ipynb](./notebooks/08_tabular_mlp_heart_disease.ipynb)

13. [건강 데이터 프로젝트 시작: 당뇨병 위험 예측 Baseline](./13_health_project_diabetes_baseline.md)
   - 실습: [13_health_project_diabetes_baseline.ipynb](./notebooks/13_health_project_diabetes_baseline.ipynb)

14. [임계값, Precision, Recall 이해하기](./14_threshold_precision_recall.md)
   - 실습: [14_threshold_precision_recall.ipynb](./notebooks/14_threshold_precision_recall.ipynb)

14-a. [Autoencoder 이상 탐지](./14_a_autoencoder_anomaly_detection.md)
   - 실습: [14_a_autoencoder_anomaly_detection.ipynb](./notebooks/14_a_autoencoder_anomaly_detection.ipynb)

15. [당뇨병 예측 모델 개선과 실험 관리](./15_experiment_management_diabetes.md)
   - 실습: [15_experiment_management_diabetes.ipynb](./notebooks/15_experiment_management_diabetes.ipynb)

16. [당뇨병 예측 모델 해석하기](./16_interpreting_diabetes_model.md)
   - 실습: [16_interpreting_diabetes_model.ipynb](./notebooks/16_interpreting_diabetes_model.ipynb)

16-a. [PCA와 SHAP 입문](./16_a_pca_shap_intro.md)
   - 실습: [16_a_pca_shap_intro.ipynb](./notebooks/16_a_pca_shap_intro.ipynb)

17. [당뇨병 위험 예측 함수 만들기](./17_diabetes_prediction_function.md)
   - 실습: [17_diabetes_prediction_function.ipynb](./notebooks/17_diabetes_prediction_function.ipynb)

18. [당뇨병 예측 프로젝트 포트폴리오 문서 만들기](./18_diabetes_project_portfolio.md)
   - 실습: [18_diabetes_project_portfolio.ipynb](./notebooks/18_diabetes_project_portfolio.ipynb)

18-a. [Streamlit 데모 입문](./18_a_streamlit_demo_intro.md)
   - 실습: [18_a_streamlit_demo_intro.ipynb](./notebooks/18_a_streamlit_demo_intro.ipynb)

### 3부. 이미지 분류와 CNN

9. [이미지 분류와 CNN 입문](./09_image_cnn_digits.md)
   - 실습: [09_image_cnn_digits.ipynb](./notebooks/09_image_cnn_digits.ipynb)

9-a. [Fashion-MNIST CNN 퀴즈](./09_a_fashion_mnist_cnn_quiz.md)
   - 실습: [09_a_fashion_mnist_cnn_quiz.ipynb](./notebooks/09_a_fashion_mnist_cnn_quiz.ipynb)

10. [꽃 이미지 CNN 미니 프로젝트](./10_flower_cnn_mini_project.md)
   - 실습: [10_flower_cnn_mini_project.ipynb](./notebooks/10_flower_cnn_mini_project.ipynb)

11. [꽃 CNN 결과 분석과 오답 확인](./11_flower_cnn_error_analysis.md)
   - 실습: [11_flower_cnn_error_analysis.ipynb](./notebooks/11_flower_cnn_error_analysis.ipynb)

12. [전이학습으로 꽃 분류 개선하기](./12_transfer_learning_flower.md)
   - 실습: [12_transfer_learning_flower.ipynb](./notebooks/12_transfer_learning_flower.ipynb)

12-a. [GAN 입문](./12_a_gan_intro.md)
   - 실습: [12_a_gan_intro.ipynb](./notebooks/12_a_gan_intro.ipynb)

12-1. [객체 탐지와 YOLO 입문](./12_1_object_detection_yolo.md)
   - 실습: [12_1_object_detection_yolo.ipynb](./notebooks/12_1_object_detection_yolo.ipynb)

12-2. [YOLO 실제 실행 입문](./12_2_yolo_practical_intro.md)
   - 실습: [12_2_yolo_practical_intro.ipynb](./notebooks/12_2_yolo_practical_intro.ipynb)

### 4부. PM10 환경/건강 시계열 예측

19. [PM10 시계열 데이터 입문](./19_pm10_time_series_intro.md)
   - 실습: [19_pm10_time_series_intro.ipynb](./notebooks/19_pm10_time_series_intro.ipynb)

20. [PM10 데이터를 LSTM 입력 모양으로 만들기](./20_pm10_lstm_dataset.md)
   - 실습: [20_pm10_lstm_dataset.ipynb](./notebooks/20_pm10_lstm_dataset.ipynb)

21. [LSTM으로 PM10 다음 시간 예측하기](./21_pm10_lstm_forecasting.md)
   - 실습: [21_pm10_lstm_forecasting.ipynb](./notebooks/21_pm10_lstm_forecasting.ipynb)

21-a. [RNN, LSTM, GRU, BiLSTM 비교](./21_a_rnn_lstm_gru_bilstm_comparison.md)
   - 실습: [21_a_rnn_lstm_gru_bilstm_comparison.ipynb](./notebooks/21_a_rnn_lstm_gru_bilstm_comparison.ipynb)

22. [PM10 예측: LSTM과 단순 Baseline 비교하기](./22_pm10_baseline_comparison.md)
   - 실습: [22_pm10_baseline_comparison.ipynb](./notebooks/22_pm10_baseline_comparison.ipynb)

23. [PM10 다변량 LSTM: PM2.5 함께 사용하기](./23_pm10_multivariate_lstm.md)
   - 실습: [23_pm10_multivariate_lstm.ipynb](./notebooks/23_pm10_multivariate_lstm.ipynb)

24. [PM10 시계열 예측 프로젝트 포트폴리오 문서 만들기](./24_pm10_project_portfolio.md)
   - 실습: [24_pm10_project_portfolio.ipynb](./notebooks/24_pm10_project_portfolio.ipynb)

### 5부. 경제 시계열 예측

25. [경제 시계열 프로젝트 시작: API로 데이터 가져오기](./25_economic_time_series_api_intro.md)
   - 실습: [25_economic_time_series_api_intro.ipynb](./notebooks/25_economic_time_series_api_intro.ipynb)

26. [경제 시계열 예측용 데이터셋 만들기](./26_economic_forecasting_dataset.md)
   - 실습: [26_economic_forecasting_dataset.ipynb](./notebooks/26_economic_forecasting_dataset.ipynb)

27. [경제 시계열 예측: MLP와 LSTM 비교하기](./27_economic_mlp_lstm_comparison.md)
   - 실습: [27_economic_mlp_lstm_comparison.ipynb](./notebooks/27_economic_mlp_lstm_comparison.ipynb)

28. [경제 시계열 예측 프로젝트 포트폴리오 문서 만들기](./28_economic_project_portfolio.md)
   - 실습: [28_economic_project_portfolio.ipynb](./notebooks/28_economic_project_portfolio.ipynb)

### 6부. 최종 정리

29. [최종 로드맵: 상황에 맞게 딥러닝을 고르는 법](./29_final_roadmap_and_model_selection.md)
   - 실습: [29_final_roadmap_and_model_selection.ipynb](./notebooks/29_final_roadmap_and_model_selection.ipynb)

## 추가된 보강 장 요약

- 4-a: TensorFlow 저수준 학습 원리
- 7-a: KMeans 비지도학습 입문
- 9-a: Fashion-MNIST CNN 퀴즈
- 12-a: GAN 입문
- 12-1: 객체 탐지와 YOLO 입문
- 12-2: YOLO 실제 실행 입문
- 14-a: Autoencoder 이상 탐지
- 16-a: PCA와 SHAP 입문
- 18-a: Streamlit 데모 입문
- 21-a: RNN, LSTM, GRU, BiLSTM 비교

## 실습 준비

노트북 실행에는 아래 패키지가 필요합니다.

```text
numpy
pandas
matplotlib
scikit-learn
keras
tensorflow
jupyter
streamlit
ultralytics
shap
```

`streamlit`, `ultralytics`, `shap`은 일부 보강 장에서만 사용합니다. 설치되어 있지 않아도 해당 장의 노트북은 가능한 범위에서 설명 또는 대체 예시를 제공하도록 구성했습니다.

## 확정 프로젝트 축

1. 건강/의료 위험 예측 프로젝트
2. 이미지 분류와 객체 탐지 확장 프로젝트
3. PM10 환경/건강 시계열 예측 프로젝트
4. 경제 시계열 예측 프로젝트
