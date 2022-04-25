import sys

def dfs(numbers, comb = []):
    if len(comb) + len(numbers) < 6:
        return
    if len(comb) == 6:
        for c in comb:
            print(c, end=' ')
        print()
    for nn in range(len(numbers)):
        if numbers[nn] not in comb:
            # comb.append(numbers[nn])
            dfs(numbers[1+nn:], comb+[numbers[nn]])

# 실패 이유 1
# : 12째 줄에서 comb에 새로운 numbers[nn]원소를 추가한 상태로 재귀함수를 호출하니까
# 함수가 종료된 이후에 원래 함수로 돌아와도 원소가 추가된 comb로 실행
# 따라서 내가 원했던 [1] -> [1,2 ...] / [1] -> [1,3 ...] 이런식으로 실행된 것이 아니라 [1,2,3 ...] 이라는 하나의 결과물만 출력된 것

# 실패 이유 2
# res 리스트를 만들어주고 comb가 길이 6으로 완성되면 if comb not in res, res.append(comb) 이런식으로 중복을 피하려고 했음
# 이 때문에 시간초과 오류가 해결되지 않아서
# 함수가 호출되면 매개변수 numbers를 슬라이싱 해서 재귀함수를 호출하도록 하였음, 이후 len(comb)==6 일때 값을 출력하도록 함(6~8번째 줄)
# 조건에 맞지 않은 numbers에 대해 돌지 않도록 길이가 맞지 않으면 return 하도록 함 (4~5번째 줄)
# 어차피 조합을 찾는 것이니까 이렇게 해도 돌지 않은 경로에 대해서 누락될 우려가 없음



if __name__ == '__main__':
    while True:
        input = sys.stdin.readline()
        numbers = list(map(int, input.split()))
        numbers_ = numbers[1:]
        if len(numbers) == 1 or numbers[0] == '0':
            break
        for nn in range(len(numbers_)):
            dfs(numbers_[1+nn:], [numbers_[nn]])
        print()