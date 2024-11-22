import time
import random

if __name__ == "__main__":
    random.seed(time.time())
    lst = [random.randint(0, 20) for _ in range(10)]
    print(*lst) # 1 1 8 1 0 3 8 2 9 4