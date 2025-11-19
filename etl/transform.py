import pandas as pd
import re


def limpar_preco(p):
    if p is None: return None
    p = re.sub(r"[^0-9,\.]+", "", p)
    p = p.replace('.', '').replace(',', '.') 
    try:
        return float(p)
    except:
        return None




def transformar_df(df):
    df = df.copy()
    if 'price' in df.columns:
        df['preco'] = df['price'].apply(limpar_preco)
    if 'score' in df.columns:
        df['avaliacao'] = df['score'].str.extract(r"(\d+[\.,]?\d*)")[0]
# normalizar nomes, cidade etc
    return df


if __name__ == '__main__':
# exemplo de uso
    data = [{'hotel':'A','price':'R$ 1.234,56','score':'9.1'}, {'hotel':'B','price':'R$ 899','score':'8'}]
    df = pd.DataFrame(data)
    print(transformar_df(df))