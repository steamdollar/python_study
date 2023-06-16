몇 가지 모르는 컨샙들이 나와서 정리해둔 파일..

머신 러닝과 최적화의 맥락에서 cost function, loss function은

모델이 x, y의 관계를 평가하는데 있어 얼마나 오차가 있는지를 측정하는 함수이다.

모델에 있어 최선의 파라미터들을 찾는 프로세스에서 사용된다.

(e.g. 선형 희귀의 weight)

실제 값과 예상값의 차이로 정의 되는데, 훈련 과정에서 이를 최소화 해야 한다.

1. Cost function : cost function은 loss funtion의 한 종류이다. 동일한 의미로 종종 사용되긴 하지만,

문맥상의 약간의 차이가 있다.

Cost function은 보통 모든 학습 샘플의 error의 측정이고, 

loss function은 하나의 학습 샘플에 대한 에러의 측정이다.

예를 들어 선형 희귀에서 cost function은 Mean Squared Error(MSE) 이며,

이는 예측, 실제값의 차이의 제곱의 평균이고, 수식으로 표현하면

J = (1/2m) Σ(y_pred - y-actual)^2 (m은 학습 자료의 갯수)

//

2. Loss function : 학습 과정의 현 반복에서 얼마나 모델이 잘 작동하는지를 측정한다.

분류 과정에서 예측된 값(y_pred)과 실제 레이블(y_actual) 사이의 불일치를 측정하게 되는데, 

예를 들어 이진 분류에서 일반적인 loss function은 log loss이다. (logistic loss나 cross-entropy loss라고도 함)

Loss Function (L) = - (y_actual * log(y_pred) + (1 - y_actual) * log(1 - y_pred))

//

cost, loss function 모두 최적화를 위해 사용한다. 

학습의 목표는 이 둘을 최소화 하는 것.

물론 이 둘의 최소화한다는 목표가 같을 뿐 둘은 다른 개념이므로 헷갈리지 않게 주의한다.