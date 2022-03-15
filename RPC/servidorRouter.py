from jsonrpclib import Server
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

class MyFuncs:

    def add(self, x, y):
        conn = Server('http://localhost:1007')
        return conn.sum(x, y)

    def substract(self, x, y):
        conn = Server('http://localhost:1008')
        return conn.sub(x, y)

    def mul(self, x, y):
        conn = Server('http://localhost:1009')
        return conn.mul(x, y)

    def div(self, x, y):
        conn = Server('http://localhost:1010')
        return conn.div(x, y)

    def pow(self, x, y):
        conn = Server('http://localhost:1011')
        return conn.pow(x, y)

    def log(self, x, y):
        conn = Server('http://localhost:1012')
        return conn.logarithm(x, y)

def main():
    server = SimpleJSONRPCServer(("localhost", 1006))
    server.register_instance(MyFuncs())
    print("Server is running")
    server.serve_forever()

if __name__ == '__main__':
    main()