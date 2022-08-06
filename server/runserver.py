import logging
from concurrent import futures

import grpc
import proto.boat_pb2 as boat_pb2
import proto.boat_pb2_grpc as boat_grpc


class PolyVessel(boat_grpc.PolyVesselServicer):

    def Ping(self, request, context):
        return boat_pb2.VesselUpdate(message='hi!')
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    boat_grpc.add_PolyVesselServicer_to_server(PolyVessel(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
