# 12-3. GAN 입문

## 왜 12장 뒤에 이 장을 배우는가

9장부터 12장까지 우리는 이미지 모델을 배웠다.

```text
9장: CNN으로 숫자 이미지 분류
10장: CNN으로 꽃 이미지 분류
11장: CNN 결과와 오답 분석
12장: 전이학습으로 꽃 분류 개선
```

지금까지의 목표는 모두 같았다.

```text
이미지를 보고, 그 이미지가 무엇인지 맞히기
```

즉 분류였다.

이번 장에서는 이미지 문제를 다른 방향에서 본다.

```text
이미지를 보고 맞히는 모델
-> 이미지를 새로 만들어내는 모델
```

이렇게 데이터를 새로 만들어내는 모델을 생성 모델이라고 부른다.
GAN은 대표적인 생성 모델 중 하나다.

이 장은 GAN을 깊게 학습시키는 장이 아니다.
CPU 환경에서 GAN을 제대로 오래 학습시키기는 부담이 크다.
대신 GAN의 핵심 구조를 이해하는 데 집중한다.

## GAN이란 무엇인가

GAN은 Generative Adversarial Network의 줄임말이다.

```text
Generative = 생성하는
Adversarial = 서로 경쟁하는
Network = 신경망
```

한국어로는 보통 생성적 적대 신경망이라고 부른다.

말이 어렵지만 핵심은 단순하다.
GAN에는 두 모델이 있다.

```text
Generator: 가짜 데이터를 만들어내는 모델
Discriminator: 진짜와 가짜를 구분하는 모델
```

Generator는 위조범처럼 가짜 이미지를 만든다.
Discriminator는 감별사처럼 이미지가 진짜인지 가짜인지 판단한다.

처음에는 Generator가 만든 이미지가 엉망이다.
Discriminator도 처음에는 잘 구분하지 못한다.

학습이 진행되면 둘은 서로 경쟁한다.

```text
Generator: 더 진짜 같은 이미지를 만들려고 한다.
Discriminator: 진짜와 가짜를 더 잘 구분하려고 한다.
```

이 경쟁을 통해 Generator가 점점 더 그럴듯한 이미지를 만들도록 학습하는 것이 GAN의 기본 아이디어다.

## 분류 모델과 GAN의 차이

CNN 분류 모델은 이미지를 입력으로 받고, 클래스 확률을 출력한다.

```text
입력: 이미지
출력: 이 이미지는 꽃이다, 숫자 3이다, 운동화다
```

GAN의 Generator는 방향이 다르다.

```text
입력: 무작위 숫자 묶음 noise
출력: 이미지
```

즉 Generator는 이미지가 아닌 숫자 벡터에서 출발한다.
그 숫자 벡터를 조금씩 이미지 모양으로 바꾸어간다.

이번 노트북에서는 Generator가 다음 일을 하게 만든다.

```text
길이 100짜리 noise
-> 7x7 작은 특징 덩어리
-> 14x14 이미지 비슷한 것
-> 28x28 흑백 이미지
```

여기서 28x28은 MNIST 같은 작은 흑백 이미지 크기다.

## noise는 무엇인가

GAN에서 noise는 무작위 숫자 묶음이다.

```text
noise = [-0.3, 1.2, 0.7, ...]
```

처음에는 이 숫자들이 아무 의미 없어 보인다.
하지만 Generator는 이 noise를 재료처럼 사용한다.

비유하면 찰흙 덩어리와 비슷하다.
찰흙 자체는 아직 컵도 아니고 접시도 아니다.
하지만 만드는 사람이 어떻게 빚느냐에 따라 다른 물건이 된다.

Generator는 noise를 받아 이미지처럼 보이는 결과를 만든다.

## Conv2DTranspose는 무엇인가

CNN 분류 모델에서는 `Conv2D`를 사용했다.
`Conv2D`는 이미지에서 특징을 찾는다.

GAN의 Generator에서는 `Conv2DTranspose`라는 층이 자주 쓰인다.

이름이 길지만 역할은 이렇게 생각하면 된다.

```text
Conv2D: 이미지 크기를 줄여가며 특징을 찾는다.
Conv2DTranspose: 작은 특징 덩어리를 키워 이미지 모양으로 만든다.
```

정확한 수학은 나중에 배워도 된다.
지금은 방향 감각이 중요하다.

분류 CNN은 이미지를 점점 작게 압축해 판단한다.
Generator는 작은 벡터를 점점 키워 이미지로 만든다.

## Discriminator는 무엇인가

Discriminator는 분류 모델과 비슷하다.
이미지를 입력으로 받고 하나의 점수를 출력한다.

```text
입력: 이미지
출력: 진짜처럼 보이는 정도
```

그래서 Discriminator 안에는 익숙한 층들이 들어간다.

```text
Conv2D
LeakyReLU
Dropout
Flatten
Dense
```

즉 지금까지 배운 CNN 지식은 GAN에서도 사라지지 않는다.
Generator와 Discriminator를 이해하는 바탕이 된다.

## GAN 학습이 어려운 이유

일반 분류 모델은 목표가 비교적 단순하다.

```text
정답 라벨을 맞히면 된다.
```

GAN은 두 모델이 동시에 움직인다.

```text
Generator가 좋아지면 Discriminator는 더 어려워진다.
Discriminator가 너무 강하면 Generator가 배울 기회를 잃을 수 있다.
Discriminator가 너무 약하면 Generator가 엉터리 이미지를 만들어도 속일 수 있다.
```

그래서 GAN 학습은 불안정할 수 있다.
입문 단계에서는 “GAN은 구조가 중요하고 학습은 까다롭다”는 정도만 기억해도 충분하다.

## 이 장의 실습 범위

이번 장의 노트북은 CPU 환경을 고려해 전체 GAN을 오래 학습하지 않는다.
대신 다음을 확인한다.

```text
1. Generator 구조 만들기
2. noise를 넣어 28x28 이미지 모양 출력 확인하기
3. Discriminator 구조 만들기
4. Generator 출력 이미지를 Discriminator에 넣어보기
5. Generator loss와 Discriminator loss의 의미 확인하기
```

이미지가 잘 만들어지는 것을 목표로 하지 않는다.
아직 학습하지 않은 Generator 출력은 당연히 이상하게 보인다.

목표는 구조를 이해하는 것이다.

## 이번 장에서 반드시 기억할 문장

```text
GAN은 가짜 이미지를 만드는 Generator와 진짜/가짜를 구분하는 Discriminator가 서로 경쟁하며 학습하는 생성 모델이다.
```

하나 더 기억하자.

```text
분류 CNN은 이미지를 보고 정답을 고르고, GAN의 Generator는 noise에서 이미지를 만들어낸다.
```

## 확인 질문

1. GAN의 두 구성 요소는 무엇인가?
2. Generator는 무엇을 입력으로 받고 무엇을 출력하는가?
3. Discriminator는 무엇을 입력으로 받고 무엇을 판단하는가?
4. `Conv2D`와 `Conv2DTranspose`의 방향 차이를 말로 설명해보라.
5. GAN 학습이 일반 분류보다 불안정할 수 있는 이유는 무엇인가?

## 과제

### 과제 1. 역할 설명하기

다음 두 문장을 완성하라.

```text
Generator는 ______를 입력으로 받아 ______를 만든다.
Discriminator는 ______가 진짜인지 가짜인지 판단한다.
```

### 과제 2. 구조 읽기

노트북에서 `generator.summary()`와 `discriminator.summary()`를 보고 다음을 적어보라.

```text
Generator의 최종 출력 모양은 무엇인가?
Discriminator의 최종 출력 개수는 몇 개인가?
```

### 과제 3. 왜 아직 이상한 이미지인가

학습하지 않은 Generator가 만든 이미지는 왜 의미 있는 숫자나 옷처럼 보이지 않는지 설명해보라.
