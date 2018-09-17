import retrying


@retry
def shit(byn):
    for i in range(byn):
        print(i)
        assert i == 0


if __name__ == '__main__':
    shit(3)
