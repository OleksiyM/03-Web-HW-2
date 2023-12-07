import logging
from time import time
from multiprocessing import Pool, cpu_count
from concurrent.futures import ProcessPoolExecutor
from factorize import factorize, _init_logging


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')

    numbers = [128, 255, 99999, 10651060, 12345678, 73967205]

    start = time()
    logging.info("Sync calculations")
    logging.debug(f'Start time: {start}')
    for i in numbers:
        factorize(i)

    # factorize(128, 255, 99999, 10651060)

    logging.debug(f'End time: {time()}')
    logging.debug(f'Time: {time() - start}')
    logging.info("-" * 25)

    # async
    max_processes_number = cpu_count()
    processes_number = 1
    while processes_number <= max_processes_number:
        start = time()
        logging.info(
            f"Async calculations Pool with {processes_number} processes")
        logging.debug(f'Start time: {start}')

        with Pool(initializer=_init_logging, processes=processes_number) as pool:
            pool.map(factorize, numbers)
        logging.debug(f'End time: {time()}')
        logging.debug(f'Time: {time() - start}')
        logging.info("-" * 25)
        processes_number += 1

    # async
    start = time()
    logging.info(f"Async calculations Pool with default processes")
    with Pool(initializer=_init_logging) as p:
        results = p.map(factorize, numbers)

    logging.debug(f'End time: {time()}')
    logging.debug(f'Time: {time() - start}')
    logging.info("-" * 25)

    # async
    start = time()
    logging.info(
        f"Async calculations ProcessPoolExecutor with {max_processes_number} processes")
    logging.debug(f'Start time: {start}')
    with ProcessPoolExecutor(initializer=_init_logging, max_workers=max_processes_number) as executor:
        executor.map(factorize, numbers)

    logging.debug(f'End time: {time()}')
    logging.debug(f'Time: {time() - start}')
    logging.info("-" * 25)


if __name__ == '__main__':
    main()
