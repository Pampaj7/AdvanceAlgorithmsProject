import pandas as pd
import ExeptionCatcherCsv as ecc
import tqdm as tqdm


def check_collab(author_name='Yang Liu'):
    dict = {}
    d = (r"/Users/gianlucagiuliani/Desktop/dblp-all-csv/out-dblp_article.csv")
    df = pd.read_csv(d)
    #df = ecc.read_csv_ignore_errors(d)
    for index, row in tqdm.tqdm(df.iterrows()):
        authors = row['author']

        if isinstance(authors, str):
            authors = authors.split('|')
            if author_name in authors:
                for a in authors:
                    if a != author_name:
                        dict[a] = 0
    return len(dict)
