import streamlit as st


def run_home():
        opening_words = """
        \n

        
        """

        
        st.image('https://cdn.pixabay.com/animation/2023/05/05/07/37/07-37-14-710_512.gif', width=500)
        st.write(opening_words)

        st.subheader('', divider='gray')
        st.page_link('https://www.kaggle.com/datasets/robertonacu/tmdb-kdramas-2022/data', label='**데이터는 Kaggle에 있는 tmdb_kdramas-2022를 이용하였습니다.**', 
                     icon='💾', help='데이터 출처로 이동')
        st.write('https://www.kaggle.com/datasets/robertonacu/tmdb-kdramas-2022/data')
        
