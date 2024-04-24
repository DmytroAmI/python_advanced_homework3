import funcs
import pandas as pd

if __name__ == '__main__':
    funcs.create_or_overwrite_csv('task7.csv')
    funcs.update_csv('task7.csv')
    print(pd.read_csv('task7.csv'))
    print("JSON:\n", funcs.convert_to_json('task7.csv'))
    print("XML:\n", funcs.convert_to_xml('task7.csv'))

