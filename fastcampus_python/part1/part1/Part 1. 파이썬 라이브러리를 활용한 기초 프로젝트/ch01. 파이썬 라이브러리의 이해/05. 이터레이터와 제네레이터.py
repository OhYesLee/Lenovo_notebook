def client_count(total_client):
    n = 1
    for num in range(total_client):
        print(f'{n} 번째 고객님 입장하십시오!')
        n += 1
        yield


if __name__ == "__main__":
    mygen = client_count(100)

    next(mygen)
    next(mygen)
    next(mygen)