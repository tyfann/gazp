# -*- ecoding: utf-8 -*-
# @ModuleName: content_to_db
# @Function: 
# @Author: Yufan-tyf
# @Time: 2022/4/1 17:50

# -*- ecoding: utf-8 -*-
# @ModuleName: content_to_db
# @Function:
# @Author: Yufan-tyf
# @Time: 2022/3/24 20:56
import json
import os
import sqlite3
import glob
import shutil
from tqdm import tqdm

os.chdir('..')


def generate_sql(sql_len):
    sql = '('
    for i in range(sql_len):
        if i == sql_len - 1:
            sql += '?)'
        else:
            sql += '?, '
    return sql


def db_mv():
    db_path = './data/csgsql/database'
    db = glob.glob(os.path.join(db_path, '*.sqlite'))
    for i in tqdm(range(len(db)), desc='Processing'):
        sql_path = db[i]
        db_name = sql_path.split('/')[-1].split('.')[0]
        os.mkdir(os.path.join(db_path, db_name))
        shutil.move(sql_path, os.path.join(db_path, db_name))

    shutil.copytree(db_path, './data/database')


def generate_db():
    csgsql_path = './data/csgsql'

    with open(os.path.join(csgsql_path, 'db_content.json')) as f:
        csgsql_content = json.load(f)

    if not os.path.exists(os.path.join(csgsql_path, 'database')):
        os.mkdir(os.path.join(csgsql_path, 'database'))

    for single_db in tqdm(csgsql_content, desc='Processing'):
        conn = sqlite3.connect(os.path.join(csgsql_path, 'database', single_db['db_id'] + '.sqlite'))
        cursor = conn.cursor()

        for table in single_db['tables'].keys():
            sql = "create table " + table + "("
            for index, header in enumerate(single_db['tables'][table]['header']):
                if index == len(single_db['tables'][table]['header']) - 1:
                    if single_db['tables'][table]['type'][index] == "number":
                        sql += " " + header + " int"
                    else:
                        sql += " " + header + " " + single_db['tables'][table]['type'][index]
                else:
                    if single_db['tables'][table]['type'][index] == "number":
                        sql += " " + header + " int,"
                    else:
                        sql += " " + header + " " + single_db['tables'][table]['type'][index] + ","
            sql += ");"

            cursor.execute(sql)

            sql = 'insert into ' + table + ' values' + generate_sql(len(single_db['tables'][table]['header']))

            with conn:
                conn.executemany(sql, single_db['tables'][table]['cell'])


if __name__ == '__main__':
    generate_db()
    db_mv()
