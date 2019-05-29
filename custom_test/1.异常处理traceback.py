import traceback


def f1():
    print(123)
    int('adf')


def run():
    try:
        ret = f1()
        print(ret)
    except Exception as e:
        err_msg= traceback.format_exc()
        print('错误信息')


run()
