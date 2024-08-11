from matplotlib import font_manager
import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from collections import Counter
# from matplotlib import font_manager, rc


def translate_ids_to_names(main_df, target_column, target_df):
    for index, value in main_df[target_column].items():
        new_values = []
        if not pd.isna(value):
            values = value.split(", ")
            for element in values:
                id = int(element)
                name = target_df.loc[target_df["tmdb_id"] == id, "name"].values
                if name.size > 0:
                    new_values.append(name[0])
            if new_values:
                new_values = ", ".join(new_values)
                main_df.at[index, target_column] = new_values
            else:
                main_df.at[index, target_column] = None

def run_eda():
    df_series = pd.read_csv('./data/series.csv')
    df_genres = pd.read_csv('./data/genres.csv')
    df_networks = pd.read_csv('./data/networks.csv')
    df_people = pd.read_csv('./data/people.csv')

    # IDs를 실제 값으로 변환
    translate_ids_to_names(df_series, "genres_ids", df_genres)
    translate_ids_to_names(df_series, "networks_ids", df_networks)
    translate_ids_to_names(df_series, "directors_ids", df_people)
    translate_ids_to_names(df_series, "cast_ids", df_people) 
    
    st.dataframe(df_series)
    st.write(df_series.describe())

    if st.button('연도별 방영된 드라마 수 그래프 보기', help='클릭해주세요.', use_container_width=True):
        air_series = pd.to_datetime(df_series['airing_date'])
        air_series = air_series.dt.year.value_counts().sort_index()
        
        fig1 = plt.figure()   # figure 객체 생성해줘야 오류 메세지 안 생김
        plt.bar(air_series.index, air_series.values, color='green')
        plt.xlabel('Year')
        plt.ylabel('Number of dramas')
        plt.title('Number of dramas aired by year')
        plt.xticks(rotation=45)
        plt.grid(axis='y')  # y축에 그리드 추가
        st.pyplot(fig1)

    if st.button('방송사별 방영된 드라마 수 그래프 보기', help='클릭해주세요.', use_container_width=True):
        search_words = ['Netflix', 'Wavve', 'ENA', 'tvN', 'jTBC', 'OCN', 'SBS', 'KBS2', 'KBS1', 'MBC', 'Olleh TV', 'Disney+', 'Channel A', 'TV Chosun', 'MBN', 'YouTube', 'Tooniverse', 'Coupang Play']
        
        counts = {}
        for word in search_words:
            counts[word] = df_series[df_series['networks_ids'].str.contains(word, case=False, na=False)].shape[0]
        
        counts_sorted = dict(sorted(counts.items(), key=lambda item: item[1], reverse=False))
        
        fig2 = plt.figure(figsize=(12, 8))
        plt.barh(list(counts_sorted.keys()), list(counts_sorted.values()), color='skyblue')
        plt.xlabel('Number of dramas')
        plt.ylabel('Broadcasting companies')
        plt.title('Number of dramas aired by broadcaster')
        plt.grid(axis='x')  # x축에 그리드 추가
        st.pyplot(fig2)

    if st.button('에피소드 수와 시청 시간', help='클릭해주세요.', use_container_width=True):
        fig3 = plt.figure(figsize=(10, 6))

        # 에피소드 수와 시청 시간 시각화
        Q1 = df_series[['number_of_episodes', 'episode_run_time']].quantile(0.25)
        Q3 = df_series[['number_of_episodes', 'episode_run_time']].quantile(0.75)
        IQR = Q3 - Q1

        # 이상치 필터링
        filtered_df = df_series[
            (df_series['number_of_episodes'] >= (Q1['number_of_episodes'] - 1.5 * IQR['number_of_episodes'])) &
            (df_series['number_of_episodes'] <= (Q3['number_of_episodes'] + 1.5 * IQR['number_of_episodes'])) &
            (df_series['episode_run_time'] >= (Q1['episode_run_time'] - 1.5 * IQR['episode_run_time'])) &
            (df_series['episode_run_time'] <= (Q3['episode_run_time'] + 1.5 * IQR['episode_run_time']))
        ]

        # 시각화
        if not filtered_df.empty:
            sb.scatterplot(x='number_of_episodes', y='episode_run_time', data=filtered_df)
            plt.title('The number of episodes and the duration of the drama')
            plt.xlabel('Number of episodes')
            plt.ylabel('Broadcast time (minutes)')
            plt.grid(True)
            st.pyplot(fig3)
        else:
            st.write("유효한 데이터가 없어 시각화를 수행할 수 없습니다.")

    if st.button('감독별 제작한 드라마 수 그래프 보기', help='클릭해주세요.', use_container_width=True):
        director_counts = df_series[df_series['directors_ids'] != ''].groupby('directors_ids').size().sort_values(ascending=False).head(10)

        fig4 = plt.figure(figsize=(12, 8))
        director_counts.plot(kind='bar')
        plt.title('Number of dramas produced by director (Top10)')
        plt.xlabel('Directors')
        plt.ylabel('Number of dramas')
        plt.xticks(rotation=45)
        st.pyplot(fig4)

    
    if st.button('배우별 드라마 출연 횟수 그래프 보기', help='클릭해주세요.', use_container_width=True):
        cast_counts = df_series['cast_ids'].str.split(',').explode().str.strip().value_counts()

        # 상위 30명 캐스트만 추출
        top_cast = cast_counts.head(30)

        fig5, ax = plt.subplots(figsize=(12, 20))
        top_cast.plot(kind='barh', ax=ax)
        ax.set_title('Number of appearances in dramas by actor (Top 30)')
        ax.set_xlabel('Number of dramas')
        ax.set_ylabel('Actor/Actress')
        ax.invert_yaxis()  # 순서 뒤집기 (가장 많은 것이 위에 오도록)
        st.pyplot(fig5)


    if st.button('장르별 드라마 수 비율 그래프 보기', help='클릭해주세요.', use_container_width=True):
        # 각 장르 단어의 등장 횟수 세기
        genre_counts = Counter()

        # 데이터에서 각 행을 읽어와서 장르 단어를 분리하고 카운트하기
        for i in df_series['genres_ids']:
            genres = i.split(', ')
            for genre in genres:
                genre_counts[genre.strip()] += 1

        # 상위 10개 장르와 나머지 장르 추출
        top_genres = genre_counts.most_common(10)
        top_labels = [genre[0] for genre in top_genres]
        top_sizes = [genre[1] for genre in top_genres]

        # 나머지 장르를 'etc'로 묶기
        other_count = sum(count for genre, count in genre_counts.items() if genre not in top_labels)
        top_labels.append('etc')
        top_sizes.append(other_count)

        # 파이차트 그리기
        fig8 = plt.figure(figsize=(10, 8))
        plt.pie(top_sizes, labels=top_labels, autopct='%1.1f%%', startangle=30, wedgeprops={'width':0.7})
        plt.axis('equal')  # 원 모양으로 조정
        plt.title('Percentage of dramas by genre')
        st.pyplot(fig8)

    st.subheader('장르에 해당하는 드라마를 보여드립니다')
    column_list = ['선택해주세요', 'Drama', 'Crime', 'Mystery', 'Action & Adventure', 'Sci-Fi & Fantasy', 'Comedy', 'Family', 'War & Politics', 'Soap', 'History', 'Romance', 'Reality', 'Kids', 'Animation', 'Documentary']

    my_choice = st.selectbox('장르를 선택하세요', column_list)
            
    if my_choice == column_list[0]:
        st.text('')
    else:
        genre_drama = df_series[df_series['genres_ids'].str.contains(my_choice, case=False, na=False)]
        if not genre_drama.empty:
            st.write(f'{my_choice} 장르에 속하는 드라마:')
            for name in genre_drama['original_name']:
                st.text(name)  # 줄별로 출력

    
