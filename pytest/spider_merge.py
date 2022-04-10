# -*- ecoding: utf-8 -*-
# @ModuleName: spider_merge
# @Function: 
# @Author: Yufan-tyf
# @Time: 2022/3/15 11:18 AM
import json
import os


def main():
    with open(os.path.join('../data/spider/', 'train.json'), 'rb') as f:
        for ex in json.load(f):
            print(ex)
            break


if __name__ == '__main__':
    main()
    pass
    spider_path = '../data/spider/'
    with open(spider_path + 'train_spider.json') as f:
        train_spider = json.load(f)

    with open(spider_path + 'train_others.json') as f:
        train_other = json.load(f)

    train_spider.extend(train_other)

    with open(spider_path + 'train.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(train_spider, indent=4, separators=(',', ': '), ensure_ascii=False))
