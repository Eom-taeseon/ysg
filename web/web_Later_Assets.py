import os
import streamlit as st

class web_Later_Assets:
    def __init__(
            self,
            mem_union   :int    = None,
            avg_cost    :int    = None,
            avg_area    :int    = None,
            total_area  :int    = None
    ):
        self.union = {
            "인원 수": mem_union,       # 조합원 수
            "평단가": int(avg_cost * 0.85),   # 평단가
            "공급면적": avg_area,   # 평균 공급면적
            "총액" : int((avg_cost * 0.85) * (avg_area) * mem_union)
        }
        self.general = {
            "인원 수": "-",
            "평단가": int(avg_cost),
            "공급면적": total_area - (avg_area * mem_union),
            "총액": int(int(avg_cost) * (total_area - (avg_area * mem_union)))
        }

        self.house = [self.union, self.general]

    def __call__(self):
        st.title("종후자산(수입)")

        Type_col, Percent_col = st.columns(2)
        with Type_col:
            with st.container(border = True):
                District_col, BuildingType_col = st.columns(2)
                with District_col:
                    distrct_list = os.listdir("./code/rate")
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
                
                ConstCost = st.number_input("평당 건축 비용을 입력해주세요.", value=None)

                ConstArea = st.number_input("공사 총 면적을 입력해주세요.", value=None)

        with Percent_col:
            # st.rerun()
            df_percent_each_types = budget_cal(selected_distrct, selected_BuildgingType).show_percent()
            st.dataframe(df_percent_each_types, hide_index=True)
                
        df_BudgetCost = budget_cal(selected_distrct, selected_BuildgingType, ConstCost, ConstArea)()
        st.dataframe(df_BudgetCost)