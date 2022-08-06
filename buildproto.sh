# Make sure you have python's version of protobuf installed.
# install via apt or brew

rm -rf ./server/proto
rm -rf ./boat/proto

mkdir -p ./server/proto
mkdir -p ./boat/proto

python -m grpc_tools.protoc -I . --python_out=./server/proto --grpc_python_out=./server/proto boat.proto
python -m grpc_tools.protoc -I . --python_out=./boat/proto --grpc_python_out=./boat/proto boat.proto