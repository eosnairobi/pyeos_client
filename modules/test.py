"""
this a fake main. just to test the code.

Note: this file will be deleted.
"""
from NodeosConnect import RequestHandlerAPI
from EOSChainApi import ChainAPI


if __name__ == '__main__':

    conn = RequestHandlerAPI(base_url='http://167.99.15.249:8888', headers={"Accept": "application/json"})
    chainapi = ChainAPI(connection_session=conn)
    print(chainapi.get_info().text)