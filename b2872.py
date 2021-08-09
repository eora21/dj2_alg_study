import sys

book_num = int(input())
book_list =[int(sys.stdin.readline())]
max_num = book_list[0]

for i in range(1,book_num):
    book_list.append(int(sys.stdin.readline()))

#승훈님이 올려주신 책 목록 한번에 받는 코드

for i in range(len(book_list)-1, -1, -1):
    if book_list[i] == book_num:
        book_num -= 1
print(book_num)