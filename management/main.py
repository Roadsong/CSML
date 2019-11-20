import os
import sys
import request_queue


def main():
    cv_q = request_queue.ClientRequestQueue("opencv")
    print("Initiate Opencv Queue.")
    print(cv_q.maxsize)

    dynet_q = request_queue.ClientRequestQueue("dynet", 100)
    print("Initiate DyNet Queue.")
    print(dynet_q.maxsize)
    
    dlib_q = request_queue.ClientRequestQueue("dlib", 100)
    print("Initiate Dlib Queue.")
    print(dlib_q.maxsize)


if __name__ == "__main__":
    main()