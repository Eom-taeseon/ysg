import os

import streamlit as st
import pandas as pd
import numpy as np

from src_code.budget_cal import *
from src_code.later_assets import *
from web.web_Business_Cost import *
from web.web_Later_Assets import *

st.set_page_config(
    page_title="예시건 - 종합건축사 사무소",
    page_icon="./web/src/logo/icon.png",  # 이모지를 사용한 아이콘 변경
    layout="wide",
    initial_sidebar_state="expanded"
)

cost_tab, asset_tab, eval_tab = st.tabs(["사업비 산정", "종후자산", "종전 자산 평가"])

with cost_tab:
    total_input, construct_cost = web_Business_Cost()(budget_cal)
with asset_tab:
    total_output = web_Later_Assets()(Later_Assets_House, Later_Assets_Arcade)
with eval_tab:
    st.title("종전 자산 평가")
    input_col, show_col = st.columns(2)
    with input_col:
        with st.container(border = True):
            official_price = st.number_input("지역 평균공시지가", value = 0, key="official_price")
            union_num = st.number_input("조합원 수", value = 0, key = "union_num")
            cost_per_area = st.number_input("조합원 별 땅값(평당)", value = 0, key = "cost_per_area")

    with show_col:
        with st.container(border = True):
            try:
                avg_official_price = official_price / union_num
            except:
                avg_official_price = "-"

            total_input__ = total_input - construct_cost - (union_num * cost_per_area)
            md = f"""
##### 조합원 수 {union_num}명일 때 지역 공시지가 평균 : {avg_official_price}
##### 수입 (분양 수입) = {total_input__}
###### ※ 수식 : 사업비 산정 총액 - 사업비 산정(공사비) 총액 - (조합원 수 * 조합원 별 땅값(평당))
"""

            st.markdown(md)

    # official_price_col, union_num_col, cost_per_area_col = st.columns(3)
    # with official_price_col:
    #     official_price = st.number_input("지역 평균공시지가", value = 0, key="official_price")
    # with union_num_col:
    #     union_num = st.number_input("조합원 수", value = 0, key = "union_num")
    # with cost_per_area_col:
        # cost_per_area = st.number_input("조합원 별 땅 값(평 당)", value = 0, key = "cost_per_area")

    st.title("수익성 분석 항목")
    try:
        fin_rate = ((total_input - total_output) / (official_price*2.0)) * 100
    except:
        fin_rate = "-"
    md = f"""
### 비례율 : {fin_rate} %
"""
    st.markdown(md)
