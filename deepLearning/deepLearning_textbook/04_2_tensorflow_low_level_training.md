# 04-2. TensorFlow 저수준 학습 원리

## 왜 4장 뒤에 이 장을 배우는가

4장에서 우리는 Keras의 기본 흐름을 배웠다.

```text
모델 만들기 -> compile() -> fit() -> predict()
```

이 흐름은 앞으로도 계속 반복된다.
CNN을 배워도, LSTM을 배워도, 결국 대부분의 실습은 이 흐름을 따른다.

그런데 처음 배우는 사람 입장에서는 `fit()`이 조금 이상하게 느껴질 수 있다.

```python
model.fit(x_data, y_data, epochs=200)
```

이 한 줄을 실행했을 뿐인데 모델이 갑자기 좋아진다.
처음에는 `x=5`를 제대로 예측하지 못하던 모델이, 학습 후에는 `11`에 가까운 값을 예측한다.

그럼 질문이 생긴다.

```text
fit() 안에서는 대체 무슨 일이 일어나는 걸까?
```

이 장은 바로 그 질문에 답하기 위한 장이다.
Keras를 버리고 TensorFlow만 쓰자는 뜻이 아니다.
오히려 Keras를 더 잘 이해하기 위해, Keras가 대신 해주던 일을 아주 작은 예제로 직접 펼쳐보는 것이다.

## 이번 장의 목표

이번 장에서는 `y = 2x + 1`이라는 아주 단순한 규칙을 모델이 배우게 한다.

먼저 4장에서는 Keras로 이렇게 했다.

```python
model = Sequential([
    Input(shape=(1,)),
    Dense(1)
])

model.compile(optimizer=SGD(learning_rate=0.01), loss="mse")
model.fit(x_data, y_data, epochs=200)
```

이번 장에서는 `fit()` 내부에서 일어나는 일을 직접 나누어 본다.

```text
1. 현재 w와 b로 예측한다.
2. 예측이 얼마나 틀렸는지 loss를 계산한다.
3. loss를 줄이려면 w와 b를 어느 방향으로 움직여야 하는지 계산한다.
4. w와 b를 조금 수정한다.
5. 이 과정을 여러 번 반복한다.
```

이 다섯 줄이 딥러닝 학습의 가장 안쪽 리듬이다.

## 다시 보는 w와 b

우리가 배우려는 규칙은 다음과 같다.

```text
y = 2x + 1
```

여기서 `2`는 x에 곱해지는 값이고, `1`은 마지막에 더해지는 값이다.
딥러닝에서는 이런 값을 모델이 직접 맞춰간다.

이번 장에서는 다음처럼 부르겠다.

```text
w = x에 곱해지는 값
b = 마지막에 더해지는 값
```

그래서 모델의 예측식은 이렇게 생긴다.

```text
예측값 = w * x + b
```

처음에는 모델이 아무것도 모르기 때문에 `w=0`, `b=0`에서 시작해도 된다.
그러면 처음 예측은 엉망이다.

```text
x = 4
정답 = 9

w = 0, b = 0이라면
예측 = 0 * 4 + 0 = 0
```

많이 틀렸다.
하지만 괜찮다.
학습은 처음부터 잘하는 과정이 아니라, 틀린 것을 보고 조금씩 고치는 과정이다.

## TensorFlow에서 바뀔 수 있는 값: tf.Variable

TensorFlow에서 학습 중 바뀌어야 하는 값은 `tf.Variable`로 만든다.

```python
w = tf.Variable(0.0)
b = tf.Variable(0.0)
```

여기서 중요한 말은 `Variable`이다.
변할 수 있는 값이라는 뜻이다.

일반 숫자 `0.0`은 그냥 숫자다.
하지만 `tf.Variable(0.0)`은 TensorFlow가 학습 중 수정할 수 있는 숫자다.

Keras의 `Dense(1)` 안에도 사실 이런 값들이 들어 있다.
우리가 직접 보지 않았을 뿐이다.

```text
Dense 층 안쪽:
입력에 곱할 값 w
마지막에 더할 값 b
```

4장에서는 Keras가 이 값을 만들어주었다.
이번 장에서는 우리가 직접 만든다.

## loss는 무엇을 알려주는가

3장에서 loss는 모델이 얼마나 틀렸는지 나타내는 숫자라고 했다.

이번 장에서는 MSE를 쓴다.

```text
MSE = 정답과 예측의 차이를 제곱해서 평균낸 값
```

예측이 정답에 가까워질수록 loss는 작아진다.
예측이 정답에서 멀어질수록 loss는 커진다.

그러므로 학습의 목표는 아주 단순하다.

```text
loss를 줄이는 방향으로 w와 b를 바꾼다.
```

## GradientTape는 무엇인가

이제 가장 낯선 단어가 나온다.

```python
with tf.GradientTape() as tape:
    y_pred = predict(x_data)
    loss = mse_loss(y_data, y_pred)
```

`GradientTape`는 이름 그대로 계산 과정을 기록하는 테이프라고 생각하면 된다.

비유하면 주방 CCTV와 비슷하다.
요리가 망쳤을 때, 어떤 순서로 재료를 넣었는지 다시 보려면 기록이 필요하다.

TensorFlow도 마찬가지다.
loss가 계산된 뒤에 TensorFlow는 이런 질문을 해야 한다.

```text
loss가 커진 원인을 w에서 찾을 수 있을까?
loss가 커진 원인을 b에서 찾을 수 있을까?
w를 올려야 loss가 줄어들까, 내려야 줄어들까?
b를 올려야 loss가 줄어들까, 내려야 줄어들까?
```

이 질문에 답하려면 loss가 계산되기까지의 과정이 기록되어 있어야 한다.
그 기록을 해주는 도구가 `GradientTape`다.

## gradient는 무엇인가

`gradient`는 처음 들으면 어려운 말이다.
여기서는 이렇게 이해하면 충분하다.

```text
gradient = loss를 줄이기 위해 값을 어느 방향으로 움직여야 하는지 알려주는 신호
```

정확히 말하면 gradient는 기울기다.
하지만 지금은 기울기라는 수학 단어보다, 방향 신호라고 이해하는 편이 좋다.

예를 들어 현재 `w`가 너무 작아서 예측이 계속 낮게 나온다면, TensorFlow는 대략 이런 신호를 만든다.

```text
w를 올려야 loss가 줄어들 것 같다.
```

반대로 `w`가 너무 크다면 이런 신호가 나온다.

```text
w를 내려야 loss가 줄어들 것 같다.
```

이 신호를 계산하는 코드가 다음이다.

```python
gradients = tape.gradient(loss, [w, b])
```

## optimizer는 무엇을 하는가

gradient가 방향 신호라면, optimizer는 실제로 값을 움직이는 역할을 한다.

```python
optimizer.apply_gradients(zip(gradients, [w, b]))
```

이 코드는 이런 뜻이다.

```text
방금 계산한 gradient를 보고,
w와 b를 loss가 줄어드는 방향으로 조금 수정해라.
```

여기서 `조금`이 중요하다.
한 번에 너무 크게 움직이면 정답을 지나쳐버릴 수 있다.
한 번에 너무 작게 움직이면 학습이 너무 느리다.

그 조금의 크기를 정하는 값이 `learning_rate`다.

```python
optimizer = tf.optimizers.SGD(learning_rate=0.01)
```

`learning_rate=0.01`은 한 번에 아주 조금씩 고치겠다는 뜻이다.

## Keras fit()과 직접 학습 루프 비교

이제 Keras의 `fit()`과 직접 학습 루프를 나란히 놓고 보자.

Keras에서는 이렇게 썼다.

```python
model.fit(x_data, y_data, epochs=200)
```

직접 쓰면 대략 이렇게 된다.

```python
for step in range(200):
    with tf.GradientTape() as tape:
        y_pred = predict(x_data)
        loss = mse_loss(y_data, y_pred)

    gradients = tape.gradient(loss, [w, b])
    optimizer.apply_gradients(zip(gradients, [w, b]))
```

즉 `fit()`은 이 반복 작업을 대신 해주는 편리한 함수다.

그래서 앞으로 실습에서는 계속 Keras를 써도 된다.
다만 이제는 `fit()`을 볼 때 이런 그림을 떠올릴 수 있어야 한다.

```text
fit() 안쪽에서는
예측 -> loss 계산 -> gradient 계산 -> 가중치 수정
이 반복된다.
```

## 이번 장에서 반드시 기억할 문장

```text
Keras의 fit()은 예측, loss 계산, gradient 계산, 가중치 수정을 반복해서 모델을 학습시킨다.
```

그리고 하나 더 기억하자.

```text
tf.Variable은 학습 중 바뀌는 값이고, GradientTape는 loss가 줄어드는 방향을 계산하기 위해 계산 과정을 기록한다.
```

## 확인 질문

1. Keras의 `fit()` 안에서는 어떤 일이 반복되는가?
2. `tf.Variable`은 일반 숫자와 무엇이 다른가?
3. `GradientTape`는 왜 필요한가?
4. gradient를 “방향 신호”라고 부를 수 있는 이유는 무엇인가?
5. `learning_rate`가 너무 크면 어떤 일이 생길 수 있을까?

## 과제

### 과제 1. 말로 설명하기

다음 문장을 완성하라.

```text
fit()은 모델이 예측하고, ______를 계산하고, ______를 계산한 뒤,
w와 b 같은 값을 조금씩 수정하는 과정을 반복한다.
```

### 과제 2. learning_rate 바꿔보기

노트북에서 `learning_rate`를 다음 값으로 바꿔보라.

```text
0.001
0.01
0.1
```

각각 loss가 어떻게 변하는지 관찰하라.

### 과제 3. 시작값 바꿔보기

`w`와 `b`의 시작값을 바꿔보라.

```python
w = tf.Variable(5.0)
b = tf.Variable(-3.0)
```

시작값이 달라도 학습이 정답에 가까워지는지 확인하라.
