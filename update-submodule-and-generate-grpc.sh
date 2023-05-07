#!/bin/bash
cd lib/protos
git pull origin main
cd ..
python -m grpc_tools.protoc -I ./protos --python_out=./python3 --grpc_python_out=./python3 ./protos/UsersMicroservice.proto
python -m grpc_tools.protoc -I ./protos --python_out=./python3 --grpc_python_out=./python3 ./protos/LobbiesMicroservice.proto
