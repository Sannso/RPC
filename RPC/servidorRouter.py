from jsonrpclib import Server
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from math import log

class MyFuncs:

    def add(self, x, y):
        conn = Server(("localhost", 1007))
        print(conn.sum(x, y))

    def substract(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x // y

    def pow(self, x, y):
        return x ^ y

    def log(self, x, y):
        return log(x, y)

def main():
    server = SimpleJSONRPCServer(("localhost", 1006))
    server.register_instance(MyFuncs())
    print("Server is running")
    server.serve_forever()

if __name__ == '__main__':
    main()