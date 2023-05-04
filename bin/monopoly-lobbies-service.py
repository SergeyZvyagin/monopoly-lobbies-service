#!/usr/bin/python3

import argparse
import toml
import logging
import sys

sys.path.append("../lib/python3")

from server import run

def main():
    parser = argparse.ArgumentParser(prog='monopoly-lobbies-service', description="The Monopoly Game's lobbies processing microservice")
    parser.add_argument('-c', '--config', help='path to config file', default='../etc/monopoly-lobbies-service-conf.toml')
    args = parser.parse_args()
    
    config = None
    with open(args.config, 'r') as file:
        config = toml.load(file) 
    
    logging.basicConfig(level=config['Logging']['level'], format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger("LOBBIES_MICROSERVICE")
    
    if config and logger:
        run(config, logger)

if __name__ == '__main__':
    main()
