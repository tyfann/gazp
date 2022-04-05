# -*- ecoding: utf-8 -*-
# @ModuleName: assertion_test
# @Function: 
# @Author: Yufan-tyf
# @Time: 2022/4/2 19:14

if __name__ == '__main__':
    try:
        assert 1 == 2
    except AssertionError as e:
        print('assertion error in parse_sql', e)
    except ValueError as e:
        print('valueerror', e)