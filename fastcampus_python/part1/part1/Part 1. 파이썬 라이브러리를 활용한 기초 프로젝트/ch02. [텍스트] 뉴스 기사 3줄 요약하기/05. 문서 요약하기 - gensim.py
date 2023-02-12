from gensim.summarization.summarizer import summarize
import pandas as pd
import numpy as np


if __name__ == "__main__":
    # 데이터 불러오기
    df = pd.read_csv('Book_test.csv')
    df = df.iloc[0:100]
    df.reset_index(inplace=True)

    # 전체 데이터 적용
    df['extract'] = df.passage.apply(lambda x : summarize(x, ratio=0.4))

    # 시각화
    for i in range(0, 1):
        random_number = np.random.randint(0, 100, size=1)
        print("=" * 120)
        print(f'{random_number[0]}' + ' 번째 문장 \n')
        print('원문: \n\n' + df['passage'][random_number[0]] + '\n\n')
        print('AI 요약: \n\n' + df['summary'][random_number[0]] + '\n\n')
        print('Gensim 요약: \n\n' + df['extract'][random_number[0]] + '\n\n')