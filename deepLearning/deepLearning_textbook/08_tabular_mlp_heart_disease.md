# 08. 표 데이터와 MLP: 심장 질환 위험 예측

## 이번 장에서 배울 것

이번 장에서는 표 형태 데이터를 딥러닝 모델에 넣어 이진 분류를 해본다.

사용할 데이터는 다음 파일이다.

```text
C:\work\dataset\diabetes_or_cardiovascular\heart.csv
```

목표는 심장 질환 여부를 예측하는 것이다.

```text
0 = 심장 질환 없음
1 = 심장 질환 있음
```

중요한 표현 주의:

```text
이 모델은 의학적 진단 도구가 아니라, 딥러닝 학습을 위한 교육용 위험 예측 예제다.
```

## 표 데이터란 무엇인가

표 데이터는 행과 열로 이루어진 데이터다.

엑셀 표를 떠올리면 쉽다.

```text
행: 한 사람, 한 샘플, 한 기록
열: 나이, 성별, 혈압, 콜레스테롤 같은 특성
```

심장 질환 데이터에서는 한 행이 한 사람의 건강 기록이다.

## MLP란 무엇인가

MLP는 Multi-Layer Perceptron의 줄임말이다.

쉽게 말하면 Dense 층을 여러 개 쌓은 기본 신경망이다.

```text
입력층 -> Dense -> Dense -> 출력층
```

표 데이터에서는 CNN이나 LSTM보다 MLP가 기본 출발점이 되는 경우가 많다.

## 이번 문제의 유형

이번 문제는 이진 분류다.

```text
심장 질환 있음 / 없음
```

그래서 출력층은 다음처럼 만든다.

```python
Dense(1, activation="sigmoid")
```

손실 함수는 다음을 사용한다.

```python
loss="binary_crossentropy"
```

## 학습 흐름

이번 장의 흐름은 다음과 같다.

```text
1. 데이터 불러오기
2. EDA와 전처리
3. MLP 모델 만들기
4. compile 설정
5. fit으로 학습
6. validation 데이터로 평가
7. 예측 확률을 0/1 라벨로 바꾸기
8. accuracy, confusion matrix, classification report 확인
```

## 확률을 라벨로 바꾸기

sigmoid 출력은 0과 1 사이 값이다.

예:

```text
0.82
```

이 값은 모델이 1일 가능성을 높게 본다는 뜻이다.

보통 기준값 0.5를 사용한다.

```text
0.5 이상 -> 1
0.5 미만 -> 0
```

이 기준값을 threshold라고 한다.

## 평가 지표

이번 장에서는 세 가지를 먼저 본다.

```text
accuracy: 전체 중 맞힌 비율
confusion matrix: 실제/예측 조합 표
classification report: precision, recall, f1-score 요약
```

의료/건강 예제에서는 단순 accuracy만 보면 부족하다. 나중에는 recall과 precision도 중요하게 다룬다.

이번 장에서는 먼저 결과를 읽는 첫 감각을 만드는 것이 목표다.

## 이번 장에서 반드시 기억할 문장

```text
표 데이터 이진 분류의 기본 출발점은 MLP, sigmoid 출력층, binary_crossentropy 손실이다.
```

## 확인 질문

1. MLP는 무엇인가?
2. 이번 문제는 회귀, 이진 분류, 다중 분류 중 무엇인가?
3. 이진 분류 출력층에는 어떤 활성화 함수를 쓰는가?
4. `binary_crossentropy`는 어떤 문제에 쓰는가?
5. sigmoid 출력 0.8은 어떻게 해석할 수 있는가?

## 과제

1. 은닉층 뉴런 수를 16에서 32로 바꿔 결과를 비교해보라.
2. epoch 수를 20, 50으로 바꿔 손실 그래프를 비교해보라.
3. threshold를 0.5가 아니라 0.6으로 바꾸면 예측 결과가 어떻게 달라지는지 확인해보라.

