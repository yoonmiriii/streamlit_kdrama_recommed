import streamlit as st


def run_home():
        opening_words = """
        \n한국 드라마는 국내외를 막론하고 큰 인기를 얻고 있습니다.
        \n코로나 팬데믹 동안 많은 사람들이 집에서 다양한 미디어를 활용하며 시간을 보냈고, BTS의 글로벌 인기와 맞물려 한류 열풍이 아이돌을 넘어 한국 드라마까지 확산되었습니다. 
        \n특히 넷플릭스와 같은 스트리밍 플랫폼을 통해 언제든지 원하는 시간에 드라마를 자유롭게 시청할 수 있게 되면서 한국 드라마의 인기는 더욱 치솟았습니다.
        \n
        \n하지만 한 드라마의 마지막 회를 보고 난 후, 다음에 무엇을 볼지 결정하는 것은 언제나 고민입니다.
        \n이 앱은 그 고민을 덜어드리기 위해 개발되었습니다.
        \n여러분이 좋아할 만한 드라마를 선택하면, 그 드라마와 비슷한 스타일의 다른 드라마를 추천해드립니다.
   
        """
        st.write('Streamlit으로 웹 대시보드를 만들었고, Matplotllib의 차트로 드라마의 분포 순위를 나타냈으며, "CountVectorizer"로 텍스트 데이터를 수치형 데이터로 변환 / "cosine_similarity"로 드라마 간의 유사도를 계산하여 추천하도록 만들었습니다.')
        
        st.image('https://cdn.pixabay.com/animation/2023/05/05/07/37/07-37-14-710_512.gif', width=500)
        st.write(opening_words)

        st.subheader('', divider='gray')
        st.page_link('https://www.kaggle.com/datasets/robertonacu/tmdb-kdramas-2022/data', label='**데이터는 Kaggle에 있는 tmdb_kdramas-2022를 이용하였습니다.**', 
                     icon='💾', help='데이터 출처로 이동')
        st.write('https://www.kaggle.com/datasets/robertonacu/tmdb-kdramas-2022/data')
        
