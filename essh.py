import sys
import argparse
import os


def help():
    print("============================Command Help=========================")
    print("\t[host] required host, essh example.com")
    print("\t[-h] more help")
    print("\tmust be install sshpass tools. brew install sshpass")
    print("\tsshpass install path to /usr/local/bin/sshpass, and  password path : ~/.ssh/public_pass")
    print("============================Command Help=========================")
    sys.exit(2)


def dossh(args):
    os.system("/usr/local/bin/sshpass -f ~/.ssh/public_pass ssh -p22 j-luoxiaoguang@"+str(args.host))


# /usr/local/bin/sshpass -f ~/.ssh/public_pass -p xxxx ssh -p22 xxxxx@xxxxx
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="input host", type=str)

    if len(sys.argv) < 2:
        help()

    # try:
    args = parser.parse_args()
    if args.host is None:
        help()
        sys.exit(2)

    dossh(args)
    # except:
    #     help()
    #     sys.exit(2)
