# サブモジュールをインポートする
from station_search import station_serch
from introduction_to_Station import introduction_to_Station

import streamlit as st
import pandas as pd
import numpy as np
import datetime
import streamlit as st
from streamlit_folium import st_folium 
import folium

# ページの設定：広いレイアウトを使用
st.set_page_config(layout="wide")


# サイドバー設定
with st.sidebar:
    st.write("## 勤務地入力:")  
    target_Station1 = st.text_input("勤務地①の駅",'',key='target_Station1')
    allowable_time1 = st.text_input("許容できる時間",'',key='allowable_time1')
    target_Station2 = st.text_input("勤務地②",'',key='target_Station2')
    allowable_time2 = st.text_input("許容できる時間",'',key='allowable_time2')

    st.write("## 駅近（徒歩5分以内）に必要な施設:")  
    # リストの項目
    items = ['ジム', 'サウナ', 'カフェ', 'コンビニ', 'スーパー']

    # チェックボックスの選択状態を管理するための辞書
    selected_items = {}

    # チェックボックスを表示
    for item in items:
        selected_items[item] = st.checkbox(item, key=item)

    if st.button("駅検索"):
        # 検索実行
        station_df = station_serch()
        st.session_state.station_df = station_df


if 'station_df' in st.session_state:
    st.write("### 候補駅一覧:")  # タイトル行
    # ページネーションを設定
    page_size = 10
    total_pages = (len(st.session_state.station_df) + page_size - 1) // page_size
    page_number = st.number_input('ページ番号', min_value=1, max_value=total_pages, value=1, step=1) - 1
    start_index = page_number * page_size
    end_index = min(start_index + page_size, len(st.session_state.station_df))
    displayed_df = st.session_state.station_df.iloc[start_index:end_index]

    # タイトル行の常時表示
    title_row = st.session_state.station_df.iloc[0]
    title_cols = st.columns([2, 2, 2, 2, 2, 2, 2, 2])
    title_cols[0].write('**駅名**')
    title_cols[1].write('**主要路線**')
    title_cols[2].write('**区**')
    title_cols[3].write('**①までの時間**')
    title_cols[4].write('**②までの時間**')
    title_cols[5].write('**平均賃料**')
    title_cols[6].write('**候補物件数**')


    for i, row in displayed_df.iterrows():
        index = start_index + i  # 元のデータフレームでのインデックス位置
        cols = st.columns([2, 2, 2, 2, 2, 2, 2, 2])
        cols[0].write(row['station_name'])
        cols[1].write(row['main_line'])
        cols[2].write(row['ward'])
        cols[3].write(row['time_to_target1'])
        cols[4].write(row['time_to_target2'])
        cols[5].write(row['average_rent'])
        cols[6].write(row['num_properties'])
        if cols[7].button("選択", key=f"select_{index}"):  # キーにインデックスを追加
            st.session_state.selected_station = row['station_name']
    
    if 'selected_station' in st.session_state:
        st.write("### 選択した駅の紹介:") 
        introduction_text = introduction_to_Station()
        st.write(introduction_text)

        st.write("### この駅の物件情報:") 
        tab_map, tab_lists = st.tabs(["地図で表示", "一覧で表示"])
        with tab_map:
            map = folium.Map(location=[35.5378631,139.5951104], zoom_start=10)
            st_folium(map, width = 1000, height = 500)
        with lists:
            st.write("aaa")