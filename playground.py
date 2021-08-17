import pandas as pd
from page_browser_improvements import page_parser


def df_load(link, num_pages):
    columns = ['Title', 'Summary', 'Area', 'Rooms', 'Price', 'Link']
    df = pd.DataFrame([i for i in page_parser(link, num_pages)], columns=columns)
    df_csv = df.to_csv(index=False)
    return df_csv


def csv_append(link, num_pages):
    with open('database_apartments.csv', 'a', encoding="utf-8") as csv_file:
        return csv_file.write(df_load(link, num_pages))
