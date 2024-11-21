from typing import Iterator, Tuple


def _mean_Q(i: Iterator) -> Tuple[float, float]:
    A_0: float = 0
    A: float = A_0
    Q: float = 0
    Q_0: float = Q
    k: float = 0
    for x in i:
        k += 1
        A = A_0 + (x - A_0) / k
        Q = Q_0 + (k - 1) / k * (x - A_0) ** 2
        # Q = Q_0 + (x - A_0) * (x - A)
        Q_0 = Q
        A_0 = A
    return A_0, Q


def mean(i: Iterator) -> float:
    return _mean_Q(i)[0]


def sample_variance(i: Iterator) -> float:
    return _mean_Q(i)[1] / (len(i) - 1)


def population_variance(i: Iterator) -> float:
    return _mean_Q(i)[1] / (len(i))


def population_standard_deviation(i: Iterator) -> float:
    return population_variance(i) ** 0.5


def sample_standard_deviation(i: Iterator) -> float:
    return sample_variance(i) ** 0.5
