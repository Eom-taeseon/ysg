import os
import streamlit as st

class web_Later_Assets:
    def __call__(self, Later_Assets_House, Later_Assets_Arcade):
        st.title("종후자산 (수입)")
        st.header("공동주택")
        total_area_cols, union_cols, area_cols, cost_cols = st.columns(4)
        with total_area_cols:
            total_area = st.number_input("공급면적 소계(평)를 입력해주세요.", value = 0, key='total_area_cols')
        with union_cols:
            mem_union = st.number_input("조합원 수를 입력해주세요.", value = 0, key='mem_union')
        with area_cols:
            avg_area = st.number_input("평균 공급면적(평)을 입력해주세요.", value = 0, key='avg_area')
        with cost_cols:
            avg_cost = st.number_input("일반 분양가를 입력해주세요.", value = 0, key='avg_cost')
       
        df_house = Later_Assets_House(mem_union, avg_cost, avg_area, total_area)()
        st.dataframe(df_house.style.format({
            '인원수': '{:,}',
            '평단가': '{:,} ₩',
            '공급면적 (평)': '{:,}',
            '총 공급면적 (평)': '{:,}',
            '총액': '{:,} ₩'
        }))

        st.header("상가시설")
        arcade_area_cols, arcade_union_cols, arcade_gen_cols, arcade_cost_cols = st.columns(4)
        with arcade_area_cols:
            arcade_area = st.number_input("상가 공급면적 소계(m²)를 입력해주세요.", value = 0, key='arcade_area')
        with arcade_union_cols:
            arcade_union = st.number_input("조합원 수를 입력해주세요.", value = 100, key="arcade_union")
        with arcade_gen_cols:
            arcade_gen = st.number_input("분양 일반 인원수를 입력해주세요.", value = 348, key="arcade_gen")
        with arcade_cost_cols:
            arcade_cost = st.number_input("평단가를 입력해주세요.", value = 4000, key=arcade_cost_cols)

        df_arcade = Later_Assets_Arcade(arcade_area, arcade_union, arcade_gen, arcade_cost)()
        st.dataframe(df_arcade.style.format({
            '인원 수': '{:,}',
            '평단가': '{:,} ₩',
            '공급면적 (m²)': '{:,}',
            '공급면적 (평)': '{:,}',
            '총액': '{:,} ₩'
        }))

        _, _, _, Total_Cost_Columns = st.columns(4)
        with Total_Cost_Columns:
            total_cost = df_house['총액'].sum() + (df_arcade['총액'].sum()/2)
            st.subheader(f"\t소계 : {int(total_cost)} ₩")

        return int(total_cost)