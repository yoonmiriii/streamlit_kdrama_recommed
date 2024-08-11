import joblib
import pandas as pd
import streamlit as st
import sklearn

def run_ml():
    try:
        # 데이터 로드
        df = pd.read_csv('./data/series.csv')

        # 모델 및 데이터 로드
        cv = joblib.load('./model/cv_model.pkl')
        similarity = joblib.load('./model/similarity_matrix.pkl')
        main_df = joblib.load('./model/main_df.pkl')

        # 'original_name' 및 'poster_img_url' 컬럼 추가
        main_df = pd.merge(main_df, df[['name', 'original_name', 'poster_img_url']], on='name', how='left')
        main_df['poster_img_url'] = main_df['poster_img_url'].fillna('no_image.jpg')

        def recommend(original_name):
            # 원래 이름을 기반으로 'name'을 찾음
            selected_name = main_df[main_df["original_name"] == original_name]["name"].values[0]
            df_index = main_df[main_df["name"] == selected_name].index[0]
            distances = similarity[df_index]
            
            # 추천 리스트 생성
            df_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
            
            # 추천된 드라마 이름을 원래 이름으로 변환
            return [(main_df.iloc[i[0]]["original_name"], main_df.iloc[i[0]]["poster_img_url"]) for i in df_list]

        # Streamlit 앱
        # 'original_name'을 선택하는 selectbox
        original_name_list = main_df['original_name'].unique()
        selected_original_name = st.selectbox('좋아하는 드라마 선택해 주세요.', original_name_list)

        if st.button('추천받기'):
            with st.spinner('Generating recommendations...'):
                recommendations = recommend(selected_original_name)
                st.write('선택하신 드라마와 비슷한 드라마는..')
                for drama, img_url in recommendations:
                    st.write(drama)
                    st.image(img_url, width=200)  # 이미지 크기를 적절히 조절하세요.
    except FileNotFoundError as e:
        st.error(f"파일을 찾을 수 없습니다: {e}")
    except ImportError as e:
        st.error(f"필요한 라이브러리를 찾을 수 없습니다: {e}. `scikit-learn`을 설치해 보세요.")
    except Exception as e:
        st.error(f"문제가 발생했습니다: {e}")




# print(sklearn.__version__)
