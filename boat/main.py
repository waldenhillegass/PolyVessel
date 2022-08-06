# this main function is to be started when the boat is powered on.


from operator import imod
from time import sleep
import grpc
import proto.boat_pb2 as boat_pb2
import proto.boat_pb2_grpc as boat_pb2_grpc

def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = boat_pb2_grpc.PolyVesselStub(channel)
        response = stub.Ping(boat_pb2.PingHello(boatID="hello!"))
        print("Greeter client received: " + response.message)



if __name__ == "__main__":
   main()