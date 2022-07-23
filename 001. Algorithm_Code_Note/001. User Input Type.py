# Basic
# [01] A B 2개이상의 변수를 받을떄 (기초)
A, B = map(int, input())
A, B = map(int, open(0))

# [01] A B 2개이상의 변수를 받을떄 (향상)
import sys

A, B = map(int, sys.stdin.readline().split())

# sys는 1개 변수를 받는 경우 개행이 들어가게 된다. rstirp 을 추가하자.
A, B = map(int, sys.stdin.readline().rstrip().split())