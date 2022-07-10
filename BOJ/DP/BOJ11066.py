# https://www.acmicpc.net/problem/11066
t = int(input().rstrip())
INF = int(10e8)

def solution(chapter, f_size):
    # 현재 테스트 케이스의 파일 사이즈 부분합을 저장하는 리스트 psum
    psum = [0 for _ in range(chapter+1)]
    psum[-1] = sum(f_size)
    # 가장 마지막 원소는 인덱스 처음부터 끝까지의 값의 총합
    # psum을 거꾸로 순환하면서 앞선 인덱스의 파일 사이즈를 빼줌으로써 부분합 계산
    for p in range(chapter-1, 0, -1):
        psum[p] = psum[p+1] - f_size[p]
    # dp[i][j] 는 i 인덱스부터 j 인덱스까지 구할 수 있는 부분합 중 최소의 값
    dp = [[0 for _ in range(chapter+1)] for _ in range(chapter+1)]

    for gap in range(1, chapter):
        # gqp 은 dp[i][j]에서 i 와 j의 간격 (i = 1, j = 3 일 경우 gap = 2)
        # 간격이 작은 것부터 값을 채워야 나중에 dp 값을 불러올 때 제대로 연산이 이뤄짐
        # 예) dp[1][5] 는 dp[2][4], dp[2][5] 등 간격이 더 큰 dp 값이 계산되어 있어야 구할 수 있음
        for start in range(1, chapter-gap+1):
            end = start + gap
            dp[start][end] = INF
            for g in range(start, end):
                # 최소값을 찾기 위해 dp[start][end]에 매우 큰 값(INF)을 미리 저장
                # dp[start][start] + [start+1][end], dp[start][start+1] + dp[start+2][end] ... 등의 최소값을 dp[start][end]에 저장
                dp[start][end] = min(dp[start][end], dp[start][g] + dp[g+1][end])
            # 최소값을 찾아 저장한 후 종료 인덱스까지의 부분합을 저장 (합쳐진 파일을 하나로 합치는데 필요한 비용 추가)
            dp[start][end] += psum[end]
            if start != 1:
                # 시작 인덱스가 1이 아니라면 psum[start-1] 값을 빼줌
                # dp[1][5] 라면 1~5를 합치는데 필요한 부분합 psum[5]를 더하면 끝이지만
                # dp[2][5] 라면 2~5를 합치는데 필요한 부분합만 더해줘야하므로 psum[1]의 값을 빼줘야 함
                dp[start][start+gap] -= psum[start-1]
    print(dp[1][-1])

for _ in range(t):
    chapter = int(input().rstrip())
    f_size = list(map(int, input().split()))
    solution(chapter, f_size)



