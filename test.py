'''
zxfeng
'''

import docker
from pprint import pprint
 
def main():
    '''
    main
    '''
    client = docker.from_env()
    data = client.services.get("deploy-demo_nginx")
    pprint(data)
    pprint(data.attrs)


if __name__ == "__main__":
    main()
