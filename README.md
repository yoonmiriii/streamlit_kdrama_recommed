![header](https://capsule-render.vercel.app/api?text=Getting%20drama%20recommend!&fontSize=40&width=100)
<br>
<br>
<br>

# 파일이름 : streamlit_kdrama_recommend
> ## 내가 좋아하는 드라마와 비슷한 드라마 추천받기

 > ### &#129321; 내가 재미있게 본 드라마와 비슷한 스타일의 또 다른 드라마들을 10개 추천받을 수 있다.

 > #### 한국 드라마는 국내외를 막론하고 큰 인기를 얻고 있습니다. 특히 넷플릭스와 같은 스트리밍 플랫폼을 통해 언제든지 원하는 시간에 드라마를 자유롭게 시청할 수 있게 되면서 한국 드라마의 인기는 더욱 치솟았습니다. 하지만 한 드라마의 마지막 회를 보고 난 후, 다음에 무엇을 볼지 결정하는 것은 언제나 고민입니다. 그 고민을 덜어드리겠습니다.


---

|인터프리터 언어|데이터분석|웹 대시보드 Tool|플랫폼|배포|
|:------:|:------:|:---------:|:-----:|:--------:|
|<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>|<img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white /">|<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>|<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>|<img src="https://img.shields.io/badge/Streamlit%20Sharing-FF9900?style=for-the-badge">|

---
**작업순서**<br>
    데이터 주제 선정 ➡︎ 라이브러리 및 데이터 불러오기 ➡︎ 데이터 확인하기 ➡︎ 전처리, 변수 변환하기 ➡︎ Matplotlib로 차트 그리기 ➡︎모델링 및 예측하기 ➡︎ 예측 모델 평가하기 ➡︎ Python 프레임워크 Streamlit으로 웹 대시보드 개발 ➡︎ Streamlit Sharing 배포

---
<br>
<br>

:pencil: 데이터 주제 선정 
-
재미있게 본 드라마를 마지막 회까지 본 후, 비슷한 느낌을 이어갈 드라마를 찾는 것은 항상 어려운 일입니다. 많은 드라마 목록 중에서 어떤 드라마를 선택해야 할지 결정하는 것은 큰 고민이었습니다. 비슷한 스타일의 드라마를 선택하더라도, 첫 회를 보면서 내가 찾던 스타일이 아닌 것 같아 종료하고 다른 드라마를 찾아보는 과정을 반복하게 되었습니다. 이러한 고민을 겪는 분들을 위해 이 프로젝트를 진행하게 되었습니다.
  
<br>

:pencil: 데이터 전처리
-
- 데이트 분석을 위한 pandas, numpy 라이브러리를 이용했습니다.
- 텍스트 처리에 필요한 nltk 라이브러리를 이용했습니다.
- 텍스트 표준화를 위해 nltk 라이브러리의 PorterStemmer 클래스를 불러와서 사용했습니다.
- 문서 내 단어의 빈도를 계산하여 벡터 형태롤 변환해 주는 사이킷런의 CountVectorizer 클래스를 불러와서 사용했습니다.
- 두 벡터 간의 코사인 유사도를 계산하여 벡터간의 유사성을 측정해 주는 사이킷런의 cosine_similarity 함수를 불러와서 사용했습니다.
- 드라마 관련 csv 파일안에 장르, 방송사, 배우/감독 정보는 숫자화 되어 있고, 각각의 정보는 다른 csv 파일로 저장되어 있어서,
각각의 파일들을 다른 변수로 저장해서 사용했습니다.
- 데이터 프레임을 파악하기 위해, head()를 이용하여 5열을 확인해 보았습니다.
- info()를 이용하여 각 컬럼의 데이터 타임과 null 값이 있는지 확인해 보았습니다.
- shpe를 이용하여 데이트 프레임의 행과 열의 크기를 확인해 보았습니다.
- columns를 이용하여 어떤 컬럼들이 있는지 확인해 보았습니다.
- 컬럼을 확인한 후, 예측 시 필요한 컬럼들로 데이트 프레임을 새로 만들었습니다.
- 가중 평가 점수 계산: 평점과 평점 수를 기반으로 가중 평가 점수를 계산하여 드라마의 신뢰성을 평가하였습니다. 평가 수 대비 평점으로 인기도를 측정했습니다.
- ID 변환: 숫자로 된 장르와 방송사 정보를 실제 값으로 변환하였습니다 (예: 장르 `18`을 `Drama`, 방송사 `213`을 `Netflix`).
- 데이터 클렌징: null 값을 dropna()를 사용하여 삭제하였으며, 문자열을 쉼표와 공백으로 분리한 후 불필요한 공백을 제거하여 데이터를 정리하였습니다.
- 태그 컬럼 생성: 배우, 줄거리, 장르 컬럼을 묶어 하나의 태그 컬럼을 생성하였습니다. 리스트 형태의 값을 문자열로 변환하고, 소문자로 변환하여 텍스트 분석을 가능하게 하였습니다.

<br>

:pencil: 데이터 시각화
-
- 인기도 순위 시각화: `popularity` 컬럼을 기준으로 드라마를 정렬하고, 수평 막대 그래프(barh)를 사용하여 인기 순위를 시각화하였습니다.
- y축을 뒤집어 가장 인기 있는 드라마가 상단에 위치하도록 설정하였습니다.
- 가중 평가 점수 시각화: 가중 평가 점수에 따른 드라마를 시각화하고, `popularity` 컬럼과 비교하여 결과를 분석하였습니다.
- 방송사별 방영된 드라마 수는 수평 막대 그래프(barh)로 나타내고, y축을 뒤집어서 가장 많은 드라마를 방영한 방송사가 상단에 오도록 했습니다.
- 파일에는 외국 방송사까지 포함되어 있어 우리나라 방송사들만 리스트로 만들어 시각화 했습니다.
- 장르별 드라마 수의 비율은 파이차트로 나타냈습니다.
- 적은 양의 데이터를 차지하는 장르들은 etc로 묶어서 표에서 겹쳐지는 부분이 없도록 했습니다.
- 에피소드 수와 시청시간의 관계는 산점도로 나타냈습니다.
- 그래프에 격자(grid)를 추가하여 데이터 포인트를 쉽게 비교할 수 있도록 했습니다.
- 감독별 제작한 드라마 수는 기본 막대 그래프(plot)으로 했습니다.
- 감독 수를 표에 다 넣을 수 없어서 상위 10명만 표로 나타냈습니다.
- 배우별 드라마 출연 횟수도 기본 막대 그래프(plot)로 나태내고, y축을 반전 시켜 출연 횟수가 가장 많은 배우가 상단에 오도록 했습니다.
- 연도별 방영된 드라마 수는 bar 차트로 나타냈습니다.

 

<br>

:pencil: 모델링 및 예측하기
-
- 텍스트 벡터화: CountVectorizer를 사용하여 전처리된 텍스트 데이터를 벡터화하였습니다.
- 영어의 의미 없는 단어들을 제거하기 위해 stop_words="english"를 설정하였습니다.
- 유사도 계산: 벡터화된 데이터를 사용하여 코사인 유사도를 계산하였습니다. 이를 통해 드라마 간의 유사성을 측정하고 추천할 수 있는 기능을 구현하였습니다.
- 추천 시스템은 유사도 기분으로 추천하도록 했습니다.
- 유사도 기반 추천: 특정 드라마와 유사한 10개의 드라마를 추천하는 함수를 작성하였습니다.
- 추천 함수는 입력된 드라마의 인덱스를 찾아 유사도를 계산하고, 유사도가 높은 드라마 10개의 이름을 출력합니다.
- 모델 및 데이터 저장: joblib 라이브러리를 사용하여 텍스트 데이터를 벡터화하는 모델, 드라마 간의 유사도 행렬, 드라마 정보를 담고 있는 데이터 프레임을 파일로 저장하였습니다.

<br>

:pencil: Streamlit Sharing 배포
-
- GitHub에 새 repository를 생성하고, VSCode와 GitHub repository를 연동시켜 주었습니다.
- VSCode에서 작업한 코드를 깃허브에 commit & push해 주었습니다.
- Streamlit Sharing에 GitHub 계정으로 로그인 했습니다.
- Streamlit Sharing에서 깃허브 repository URL을 넣고, 실행하려는 파일을 선택( app.py)해주었습니다.
- 변경 사항이 생길 때마다 commit & push하면, 자동으로 웹 대시보드가 업데이트 되는 것을 확인할 수 있었습니다.

[이슈 및 해결방법]
- 이슈 : 로컬에서 잘 돌아가던 웹이, 배포 후 `ModuleNotFoundError`가 발생되었습니다.
- 해결방법 : requirements.txt 파일을 추가하여, 필요한 패키지들을 넣어 주었습니다.
 <br>
<br>
<br>

> **데이터 출처**<br><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" /><br>
series.csv 파일
 <https://www.kaggle.com/datasets/robertonacu/tmdb-kdramas-2022/data><br>
    
> **웹 페이지**<br><https://appkdramarecommed-6edkvalzivzb9efbwxvdsg.streamlit.app/>    


 
