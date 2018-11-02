# coding=utf-8
# D:/workspace/crawler/taobao




__author__ = 'Hilbert'

__all__ = ['Taobao']

from taobao.taobao_dress.dict import urldict
from multiprocessing import Pool
from taobao.taobao_dress.api import Taobao


if __name__ == '__main__':
    dics = list(urldict.values())
    '''
    一个Pool为一个cpu，自己根据自己的电脑配置修改相应配置，配置高的电脑可以调高配置。
     intel最新出的cpu，也可以一个processes（一个核心）就是一个超线程。
    '''
   # pool = Pool(processes=4)

    for dic in dics:
        print(dic)
        tao = Taobao(dic)
        tao.run()
        '''
        pool.apply_async(tao.run())
        pool.close()
        pool.join()
        '''
    print('--------------******--------------------结束---------------------********---------------------')
