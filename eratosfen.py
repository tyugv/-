#решето эратосфена

import numpy as np
import matplotlib.pyplot as plt
import time

def generator(int_start, int_end, step):
    if (int_start>int_end):
        print('Некорректные входные данные')
        exit()
    iter = int_start
    while iter<=int_end:
        yield iter
        iter += step

def Eratosfen(N):
    bool_vec = np.ones(N+1)
    bool_vec[0:2] = 0
    i = 2
    while (i**2 <= N):
        if (bool_vec[i]):
            bool_vec[i**2:N+1:i] = 0
        i+=1
    return np.where(bool_vec)


def main():
    times = []
    for n in generator(500000,5000000,500000):
        sum_time = 0
        for _ in range(20):
            start_time = time.time()
            Eratosfen(n)
            sum_time += time.time() - start_time
        times.append(sum_time/20)

    N = np.arange(500000,5500000,500000)
    plt.plot(N, times, c = 'r')
    plt.title('Время выполнения алгоритма от N')
    plt.xlabel('N')
    plt.ylabel('Время (секунды)')
    plt.show()

    plt.plot(N, N*np.log(np.log(N)), c = 'b')
    plt.title('f(n) = n * log(log(n)))')
    plt.xlabel('n')
    plt.ylabel('f(n)')
    plt.show()
    

   

if __name__ == "__main__":
    main()
