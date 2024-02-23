import sys

if __name__ == "__main__":
    argument = sys.argv
    del argument[0]     # 맨 앞에 있는 아규먼트는 파일명이기 때문에 불필요해서 삭제함
    print('arguments: {}'.format(argument))

    num = argument[0]

    test = f"/Users/leo/Downloads/dragonball/part01/book{num}"
    print('test: ', test)