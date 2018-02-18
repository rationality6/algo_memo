# import requests
#
# url = "https://jsonmock.hackerrank.com/api/movies/search/?Title=spiderman"
#
# response = requests.get(url)
# resp = response.json()
# print(resp.data)


def solution(N):
    if N % 2 != 0:
        print("Weird")
    else:
        if 2 <= N and N <= 5:
            print('Not Weird')
        elif 6 <= N and N <= 20:
            print("Weird")
        elif 20 < N:
            print("Not Weird")


# solution(3)
# solution(24)
solution(18)
