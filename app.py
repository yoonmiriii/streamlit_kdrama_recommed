import streamlit as st
from streamlit_option_menu import option_menu 
import streamlit.components.v1 as html
from  PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import io
import pickle



from eda import run_eda
from home import run_home
from ml import run_ml

# 차트에 한글 나오게 설정
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')



def main():


    #sidebar
    selectbox_list = ['🏠홈', '📊 드라마 관련 통계', '📺드라마 추천받기']

    st.sidebar.header('내가 좋아하는 드라마와 비슷한 드라마 추천받기', divider='red')
    st.sidebar.image('https://cdn.icon-icons.com/icons2/1261/PNG/512/1496676738-rounded-high-ultra-colour05-television_84626.png')
    st.sidebar.subheader('', divider='red')
    choice_selectbox = st.sidebar.selectbox('메뉴 선택', selectbox_list)
    st.sidebar.title('')
    st.sidebar.title('')
    st.sidebar.title('')
    st.sidebar.title('')
    # st.sidebar.page_link('https://www.kaggle.com/datasets/robertonacu/tmdb-kdramas-2022/data', label='데이터 출처', icon='💾')

    


    if choice_selectbox == selectbox_list[0]:
        st.title('내가 좋아하는 드라마와 비슷한 드라마 찾아줘!🍿')
        run_home()
    

    elif choice_selectbox == selectbox_list[1]:
        st.title('📊 드라마 관련 통계')
        run_eda()

    elif choice_selectbox == selectbox_list[2]:
        st.title('📺 드라마 추천받기')
        run_ml()
    

    


if __name__ == "__main__":
    main()