import os
import streamlit as st

class web_Business_Cost:
    def __call__(self, budget_cal):
        st.title("정비사업비 추산액 (지출)")

        Type_col, Percent_col = st.columns(2)
        with Type_col:
            with st.container(border = True):
                District_col, BuildingType_col = st.columns(2)
                with District_col:
                    distrct_list = os.listdir("./src_code/rate")
                    distrct_list = [d.split('.')[0] for d in distrct_list]
                    selected_distrct = st.selectbox(
                        "지역을 선택해주세요",
                        distrct_list
                    )
                with BuildingType_col:
                    selected_BuildgingType = st.selectbox(
                        "건물 타입을 선택해주세요",
                        ("주상복합", "공동주택")
                    )
                
                ConstCost = st.number_input("평당 건축 비용을 입력해주세요.", value=0, key = "ConstCost")

                ConstArea = st.number_input("공사 총 면적을 입력해주세요.", value=0, key = "ConstArea")

        with Percent_col:
            # st.rerun()
            df_percent_each_types = budget_cal(selected_distrct, selected_BuildgingType).show_percent()
            st.dataframe(df_percent_each_types, hide_index=True)
                
        df_BudgetCost = budget_cal(selected_distrct, selected_BuildgingType, ConstCost, ConstArea)()
        st.dataframe(df_BudgetCost.style.format({
            '평단가': '{:,} ₩',
            '공사 면적': '{:,}',
            '총액': '{:,} ₩'
        }))

        _, _, _, Total_Cost_Columns = st.columns(4)
        with Total_Cost_Columns:
            st.subheader(f"\t소계 : {df_BudgetCost['총액'].sum()} ₩")
        
        return df_BudgetCost['총액'].sum(), df_BudgetCost['총액'][0]