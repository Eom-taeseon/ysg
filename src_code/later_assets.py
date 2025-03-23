import pandas as pd

class Later_Assets_House:
    def __init__(
            self,
            mem_union   :int    = 0,
            avg_cost    :int    = 0,
            avg_area    :int    = 0,
            total_area  :int    = 0
    ):
        # 조합원 정보
        self.mem_union = mem_union
        self.avg_cost_union = avg_cost * 0.85
        self.avg_area_union = avg_area
        self.total_cost_union = self.avg_cost_union * self.avg_area_union * self.mem_union

        # 일반
        self.avg_cost_gen = avg_cost
        self.total_area_gen = total_area - (avg_area * mem_union)
        self.total_cost_gen = avg_cost * self.total_area_gen

        self.union = {
            "인원수": self.mem_union,       # 조합원 수
            "평단가": int(self.avg_cost_union),   # 평단가
            "공급면적 (평)": self.avg_area_union,   # 평균 공급면적
            "총 공급면적 (평)": self.mem_union * self.avg_area_union,
            "총액" : int(self.total_cost_union)
        }
        self.general = {
            "인원수": 0,
            "평단가": int(avg_cost),
            "공급면적 (평)": int(self.total_area_gen),
            "총 공급면적 (평)": int(self.total_area_gen),
            "총액": int(self.total_cost_gen)
        }

        self.df_house = pd.DataFrame([self.union, self.general], index=['조합원', '일반'])

    # def calcualte_df(self):
    #     if self.

    def __call__(self):
        df_house = self.df_house.style.format({
            '인원수': '{:,}',
            '평단가': '{:,} ₩',
            '공급면적 (평)': '{:,}',
            '총 공급면적 (평)': '{:,}',
            '총액': '{:,} ₩'
        })
        return self.df_house
    
class Later_Assets_Arcade:
    def __init__(
            self,
            arcade_area    :int    = 0,
            arcade_union   :int    = 0,
            arcade_gen     :int    = 0,
            arcade_cost    :int    = 0,
    ):
        # 조합원 정보
        self.num_union = arcade_union
        # self.avg_cost_union = arcade_cost
        # self.avg_area_union = float(arcade_area) / 3.3
        # self.total_cost_union = arcade_cost * arcade_area

        # 일반
        self.num_gen = arcade_gen
        # self.avg_cost_gen = arcade_cost
        # self.total_area_gen = float(arcade_area) / 3.3
        # self.total_cost_gen = arcade_cost * arcade_area

        # 공통 
        self.avg_cost = arcade_cost
        self.total_area = float(arcade_area) / 3.3
        self.total_cost = arcade_cost * arcade_area

        self.union = {
            "인원수": self.num_union,       # 조합원 수
            "평단가": int(self.avg_cost),   # 평단가
            "공급면적 (m²)": int(arcade_area),   # 평균 공급면적
            "공급면적 (평)": int(self.total_area),
            "총액" : int(self.total_cost)
        }
        self.general = {
            "인원수": self.num_gen,
            "평단가": int(self.avg_cost),   # 평단가
            "공급면적 (m²)": int(arcade_area),   # 평균 공급면적
            "공급면적 (평)": int(self.total_area),
            "총액" : int(self.total_cost)
        }

        self.df_arcade = pd.DataFrame([self.union, self.general], index=['조합원', '일반'])

    # def calcualte_df(self):
    #     if self.

    def __call__(self):
        df_arcade = self.df_arcade.style.format({
            '인원 수': '{:,}',
            '평단가': '{:,} ₩',
            '공급면적 (m²)': '{:,}',
            '공급면적 (평)': '{:,}',
            '총액': '{:,} ₩'
        })
<<<<<<< HEAD
        return self.df_arcade
=======
        return df_arcade
>>>>>>> 6b2b165fab979acbd01221a3c0be14a9d4da7cf5
