# -*- ecoding: utf-8 -*-
# @ModuleName: chase_db_test
# @Function: 
# @Author: Yufan-tyf
# @Time: 2022/3/23 13:27
import sqlite3
import json
import os
from tqdm import tqdm

os.chdir('../')

def main():
    db_path = '/home/share/other_user/gazp-main/data/database/browser_web/browser_web.sqlite'

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    col = {'name': '名称', 'type': 'text', 'table_name': 'web加速器', 'key': 'web加速器.名称'}
    q = 'select {} from {}'.format(col['name'], col['table_name'])
    cursor.execute(q)
    res = [str(r[0]).split('.')[0] for r in cursor.fetchall()]
    print(res)

if __name__ == '__main__':
    chase_path = './data/chase'
    names = ['tables']

    for file_name in names:
        with open(os.path.join(chase_path, file_name + '.json')) as f:
            chase_table = json.load(f)

