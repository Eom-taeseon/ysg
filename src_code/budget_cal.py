import pandas as pd
import json

class budget_cal:
    def __init__(
            self,
            district: str = None,
            building_type: str = None,
            construct_cost: int = None,
            construct_area: int = None
    ):            
        self.district = district
        self.building_type = building_type
        self.construct_cost = construct_cost
        self.construct_area = construct_area

    def read_budget_percentages(
            self
    ):
        if self.district is None:
            self.district = str(input("지역 이름을 기입해주세요.\n"))
        if self.building_type is None:
            self.building_type = str(input("건물 형태를 입력해주세요. '주상복합' or '공동주택'\n"))

        file_path = f"./src_code/rate/{self.district}.json"

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            # 여기서 바로 building_type으로 접근
            return list(data[self.building_type].items())
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {file_path}")
        except KeyError:
            print(f"'{self.building_type}'은(는) JSON 데이터에 존재하지 않습니다. '주상복합' 또는 '공동주택'으로 입력해주세요.")
        except json.JSONDecodeError:
            print("JSON 형식이 올바르지 않습니다.")
        
        return None  # 오류 발생 시 None 반환
    
    def calculate_Budget_for_projects(self, data):
        if self.construct_cost is None:
            self.construct_cost = int(input("건축비(공사비)를 입력해주세요\n"))

        if self.construct_area is None:
            self.construct_area = int(input("공사 면적을 입력해주세요\n"))
            
        rate__ = self.construct_cost * (1 / data[[0] == '공사비'][1])
        budget__ = [(x[0], int(rate__*x[1])) for x in data]
        df_budget = pd.DataFrame(budget__, columns=['항목', '평단가'])
        df_budget['공사 면적'] = self.construct_area
        df_budget['총액'] = df_budget['평단가'] * self.construct_area
        
        # 시각적 표현만 변경 (원본 데이터는 그대로 유지)
        # df_budget = df_budget.style.format({
        #     '평단가': '{:,} ₩',
        #     '공사 면적': '{:,}',
        #     '총액': '{:,} ₩'
        # })

        return df_budget
        # return pd.DataFrame(budget__)

    def show_percent(self):
        data = self.read_budget_percentages()
        return pd.DataFrame(data, columns=['항목', '비율'])
    
    def __call__(self):
        data = self.read_budget_percentages()
        df = self.calculate_Budget_for_projects(data)

        return df
    
if __name__ == "__main__":
    calculator = budget_cal()
    result = calculator()
    print(result)