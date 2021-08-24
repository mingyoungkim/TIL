# BigData

## 영화 평점 빅 데이터 이용

### 개요

> python

- 다양한 라이브러리를 사용할 수 있어서 python언어 사용
-  Sparse matrix(회소 행렬)형태의 데이터를 array에 zero값들까지 그대로 저장하면 메모리도 많이 필요하고 수해 시간도 오래 걸림
- Python의 numpy 라이브러리의 행렬 연산과 scipy 라이브러리의 sparse matrix format을 사용하면서 reshape과 broadcasting 기법을 이용해 효율적으로 코딩



> 단계

1. K-nearest neighbor (KNN) 알고리즘
2. Matrix factorization 알고리즘
3. Matrix factorization + PLSI 알고리즘

- 빅데이터마이닝에서 많이 쓰이는 기술인 Preobabilistic Modeling 기술 습득
- 영화 평점과 영화에 대한 다른 텍스트 정보도 이용하는 알고리즘 구현
- 오픈 소스 기반의 웹 어플리케이션 프레임워크인 Diango 이용



> Anaconda

- free and open-source distribution of the Python
- 유용한 특정 패키지들을 포함하고 있다.



### Django

> 흐름도

- 클라이언트 요청은 django 프로젝트 디렉토리 안의 urls.py에 전달

- urls.py에서 요청을 views.py로 보내고 저장되어 있는 데이터가 필요하면

  models.py에서 가져와 templates로 보내면 클라이언트에게 응답하게 됨

- 

