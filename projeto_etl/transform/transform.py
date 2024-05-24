import pandas as pd
import sqlite3
from datetime import datetime

class Transform:

    def __init__(self, path) -> None:
        self.path = path

    def create_dataFrame(self) -> pd.DataFrame:
        df = pd.read_json(self.path, lines=True)
        df = self.adjust_dataframe(df)
        df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
        df['_time_stamp'] = datetime.now()
        return df
    
    def adjust_dataframe(self, df:pd.DataFrame) -> pd.DataFrame:
        df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
        df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
        df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
        df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
        df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)
        df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
        df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)
        df['old_price'] = df['old_price_reais'] + df['old_price_centavos']/100
        df['new_price'] = df['new_price_reais'] +  df['new_price_centavos']/100
        df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)
        return df