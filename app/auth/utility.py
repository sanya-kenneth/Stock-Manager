from flask import jsonify


def check_admin(*args):
    if args[0][4] is False:
        print(args[0][4])
        return True
       