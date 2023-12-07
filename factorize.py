import logging
from multiprocessing import current_process


def factorize(*numbers):
    logging.debug(f"pid={current_process().pid}, {numbers=}")
    results = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        results.append(factors)
    return results


# def factorize(*numbers):
#    return (
#      [i for i in range(1, numb+1) if not(numb % i)]
#      or [numb] for numb in numbers
#    )


# def factorize_async(*numbers):
#     return [i for i in range(1, numbers + 1) if numbers % i == 0]

def _init_logging(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s'):
    logger = logging.getLogger()
    logger.setLevel(level)
    formatter = logging.Formatter(format)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


def main():
    pass


if __name__ == '__main__':
    main()
