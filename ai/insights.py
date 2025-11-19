import os
import pandas as pd


# Exemplo com openai (substitua conforme seu provider/local)
# pip install openai
import openai
openai.api_key = os.getenv('OPENAI_API_KEY')




def gerar_insights_texto(df_hotels):
# sumariza estatísticas básicas e pergunta ao LLM por insights
    resumo = df_hotels.describe(include='all').to_string()
    prompt = f"Você é um analista de turismo. Com base nos dados a seguir, gere insights acionáveis:\n\n{resumo}\n\nEntregue: 1) Tendências, 2) Riscos, 3) Oportunidades, 4) Sugestões de ação."


    resp = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[{'role':'user','content':prompt}],
        max_tokens=800
)


    return resp['choices'][0]['message']['content']


if __name__ == '__main__':
    df = pd.DataFrame([{'preco':100, 'avaliacao':9}, {'preco':200, 'avaliacao':8}])
    print(gerar_insights_texto(df))