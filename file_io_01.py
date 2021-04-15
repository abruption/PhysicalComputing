# File io
# 파일 객체 = open(파일 경로, 읽기 모드)
# w : 쓰기모드, r : 읽기모드, a : 이어쓰기 모드
# 파일을 닫을 때 파일객체.close()

fp = open('war_flower.txt', 'w')
print('고니', file=fp)    # 실제 쓰기
print('정마담', file=fp)    # 실제 쓰기
print('아귀', file=fp)    # 실제 쓰기
fp.write('너구리')      # 실제 쓰기
fp.close()


# 파일 읽기
fp = open('wf.txt', 'r')
lines = fp.readlines()  # 파일을 1행 단위의 리스트 원소로 리턴
for line in lines:
    #print(line.rstrip('\n'))    # Option 1
    #print(line.strip('\n'))     # Option 2
    print(line[0:-1])            # Option 3

# for line in fp:   # 파일을 라인단위로 읽어 print에서 end 옵션으로 줄바꿈을 없애는 방법
#     print(line, end=' ')
fp.close()


# with
with open('wf.txt') as fp:
    lines = fp.readlines()  # 파일을 1행 단위의 리스트 원소로 리턴
    for line in lines:
        print(line[:-1])     