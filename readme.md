## About

**Factorize Numbers with Different Approaches in Python**

This project demonstrates various methods for factorizing numbers in Python, including synchronous and asynchronous approaches.

**Features:**

* **Factorizes a list of integers.**
* **Calculates the prime factors of each number.**
* **Supports both synchronous and asynchronous execution.**
* **Measures and displays execution time.**

**Usage:**

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```
or
```bash
pip3 install -r requirements.txt
```

2. **Run the script:**

```bash
python main.py
```
or
```bash
python3 main.py
```

3. **Output:**

The script will print the following information:

* Time taken for synchronous factorization
* Time taken for asynchronous factorization with different number of processes
* Time taken for asynchronous factorization using ProcessPoolExecutor

**Script Breakdown:**

* **`factorize` function:**
    * Takes a list of integers as input.
    * Calculates the prime factors of each number.
    * Returns a list of lists containing the prime factors for each number.
* **`_init_logging` function:**
    * Initializes logging with a custom format.
* **`main` function:**
    * Defines a list of numbers to factorize.
    * Measures and compares the execution time of different approaches:
        * Synchronous factorization using a loop.
        * Asynchronous factorization using `Pool` with different number of processes.
        * Asynchronous factorization using `ProcessPoolExecutor`.
    * Prints the results to the console.

**Additional Notes:**

* This script uses the `multiprocessing` module for asynchronous execution.
* The script utilizes logging to track the progress and performance.
* The script can be easily extended to support other types of calculations.

**License:**

This project is licensed under the MIT License.

**Code Structure:**

The code is divided into two main files:

* `factorize.py`: Contains the `factorize` function for calculating prime factors.
* `main.py`: Contains the main script that performs the execution and prints the results.

### Results

<details>
<summary>macOS</summary>

Python 3.11.6, MacBook Air M1
 
```commandline
2023-12-07 21:22:12,497 INFO Sync calculations
2023-12-07 21:22:12,497 DEBUG Start time: 1701976932.497167
2023-12-07 21:22:12,497 DEBUG pid=11257, numbers=(128,)
2023-12-07 21:22:12,497 DEBUG pid=11257, numbers=(255,)
2023-12-07 21:22:12,497 DEBUG pid=11257, numbers=(99999,)
2023-12-07 21:22:12,500 DEBUG pid=11257, numbers=(10651060,)
2023-12-07 21:22:12,794 DEBUG pid=11257, numbers=(12345678,)
2023-12-07 21:22:13,131 DEBUG pid=11257, numbers=(73967205,)
2023-12-07 21:22:15,147 DEBUG End time: 1701976935.1471791
2023-12-07 21:22:15,147 DEBUG Time: 2.650174856185913
2023-12-07 21:22:15,147 INFO -------------------------
2023-12-07 21:22:15,147 INFO Async calculations Pool with 1 processes
2023-12-07 21:22:15,147 DEBUG Start time: 1701976935.147379
2023-12-07 21:22:15,190 DEBUG pid=11262, numbers=(128,)
2023-12-07 21:22:15,190 DEBUG pid=11262, numbers=(255,)
2023-12-07 21:22:15,190 DEBUG pid=11262, numbers=(99999,)
2023-12-07 21:22:15,193 DEBUG pid=11262, numbers=(10651060,)
2023-12-07 21:22:15,486 DEBUG pid=11262, numbers=(12345678,)
2023-12-07 21:22:15,823 DEBUG pid=11262, numbers=(73967205,)
2023-12-07 21:22:17,835 DEBUG End time: 1701976937.835097
2023-12-07 21:22:17,835 DEBUG Time: 2.687864065170288
2023-12-07 21:22:17,835 INFO -------------------------
2023-12-07 21:22:17,835 INFO Async calculations Pool with 2 processes
2023-12-07 21:22:17,835 DEBUG Start time: 1701976937.835268
2023-12-07 21:22:17,873 DEBUG pid=11263, numbers=(128,)
2023-12-07 21:22:17,873 DEBUG pid=11263, numbers=(99999,)
2023-12-07 21:22:17,873 DEBUG pid=11264, numbers=(255,)
2023-12-07 21:22:17,873 DEBUG pid=11264, numbers=(10651060,)
2023-12-07 21:22:17,876 DEBUG pid=11263, numbers=(12345678,)
2023-12-07 21:22:18,169 DEBUG pid=11264, numbers=(73967205,)
2023-12-07 21:22:20,185 DEBUG End time: 1701976940.185152
2023-12-07 21:22:20,185 DEBUG Time: 2.3500239849090576
2023-12-07 21:22:20,185 INFO -------------------------
2023-12-07 21:22:20,185 INFO Async calculations Pool with 3 processes
2023-12-07 21:22:20,185 DEBUG Start time: 1701976940.185317
2023-12-07 21:22:20,225 DEBUG pid=11265, numbers=(128,)
2023-12-07 21:22:20,225 DEBUG pid=11267, numbers=(255,)
2023-12-07 21:22:20,225 DEBUG pid=11266, numbers=(99999,)
2023-12-07 21:22:20,225 DEBUG pid=11265, numbers=(10651060,)
2023-12-07 21:22:20,225 DEBUG pid=11267, numbers=(12345678,)
2023-12-07 21:22:20,228 DEBUG pid=11266, numbers=(73967205,)
2023-12-07 21:22:22,251 DEBUG End time: 1701976942.2518559
2023-12-07 21:22:22,251 DEBUG Time: 2.0666708946228027
2023-12-07 21:22:22,252 INFO -------------------------
2023-12-07 21:22:22,252 INFO Async calculations Pool with 4 processes
2023-12-07 21:22:22,252 DEBUG Start time: 1701976942.252012
2023-12-07 21:22:22,289 DEBUG pid=11271, numbers=(128,)
2023-12-07 21:22:22,289 DEBUG pid=11268, numbers=(255,)
2023-12-07 21:22:22,289 DEBUG pid=11271, numbers=(99999,)
2023-12-07 21:22:22,289 DEBUG pid=11269, numbers=(10651060,)
2023-12-07 21:22:22,289 DEBUG pid=11270, numbers=(12345678,)
2023-12-07 21:22:22,290 DEBUG pid=11268, numbers=(73967205,)
2023-12-07 21:22:24,316 DEBUG End time: 1701976944.316226
2023-12-07 21:22:24,316 DEBUG Time: 2.064349889755249
2023-12-07 21:22:24,316 INFO -------------------------
2023-12-07 21:22:24,316 INFO Async calculations Pool with 5 processes
2023-12-07 21:22:24,316 DEBUG Start time: 1701976944.316385
2023-12-07 21:22:24,356 DEBUG pid=11273, numbers=(128,)
2023-12-07 21:22:24,356 DEBUG pid=11273, numbers=(255,)
2023-12-07 21:22:24,356 DEBUG pid=11273, numbers=(99999,)
2023-12-07 21:22:24,356 DEBUG pid=11276, numbers=(10651060,)
2023-12-07 21:22:24,359 DEBUG pid=11273, numbers=(12345678,)
2023-12-07 21:22:24,360 DEBUG pid=11275, numbers=(73967205,)
2023-12-07 21:22:26,385 DEBUG End time: 1701976946.385707
2023-12-07 21:22:26,385 DEBUG Time: 2.0694689750671387
2023-12-07 21:22:26,385 INFO -------------------------
2023-12-07 21:22:26,385 INFO Async calculations Pool with 6 processes
2023-12-07 21:22:26,385 DEBUG Start time: 1701976946.3858812
2023-12-07 21:22:26,423 DEBUG pid=11277, numbers=(128,)
2023-12-07 21:22:26,423 DEBUG pid=11277, numbers=(255,)
2023-12-07 21:22:26,423 DEBUG pid=11277, numbers=(99999,)
2023-12-07 21:22:26,431 DEBUG pid=11277, numbers=(10651060,)
2023-12-07 21:22:26,431 DEBUG pid=11278, numbers=(12345678,)
2023-12-07 21:22:26,433 DEBUG pid=11280, numbers=(73967205,)
2023-12-07 21:22:28,460 DEBUG End time: 1701976948.4602299
2023-12-07 21:22:28,460 DEBUG Time: 2.074467658996582
2023-12-07 21:22:28,460 INFO -------------------------
2023-12-07 21:22:28,460 INFO Async calculations Pool with 7 processes
2023-12-07 21:22:28,460 DEBUG Start time: 1701976948.460373
2023-12-07 21:22:28,507 DEBUG pid=11287, numbers=(128,)
2023-12-07 21:22:28,507 DEBUG pid=11287, numbers=(255,)
2023-12-07 21:22:28,507 DEBUG pid=11287, numbers=(99999,)
2023-12-07 21:22:28,509 DEBUG pid=11284, numbers=(10651060,)
2023-12-07 21:22:28,510 DEBUG pid=11283, numbers=(12345678,)
2023-12-07 21:22:28,510 DEBUG pid=11287, numbers=(73967205,)
2023-12-07 21:22:30,543 DEBUG End time: 1701976950.5431318
2023-12-07 21:22:30,543 DEBUG Time: 2.0829010009765625
2023-12-07 21:22:30,543 INFO -------------------------
2023-12-07 21:22:30,543 INFO Async calculations Pool with 8 processes
2023-12-07 21:22:30,543 DEBUG Start time: 1701976950.543301
2023-12-07 21:22:30,597 DEBUG pid=11296, numbers=(128,)
2023-12-07 21:22:30,597 DEBUG pid=11296, numbers=(255,)
2023-12-07 21:22:30,597 DEBUG pid=11296, numbers=(10651060,)
2023-12-07 21:22:30,597 DEBUG pid=11295, numbers=(99999,)
2023-12-07 21:22:30,599 DEBUG pid=11291, numbers=(12345678,)
2023-12-07 21:22:30,602 DEBUG pid=11290, numbers=(73967205,)
2023-12-07 21:22:32,633 DEBUG End time: 1701976952.633313
2023-12-07 21:22:32,633 DEBUG Time: 2.090146780014038
2023-12-07 21:22:32,633 INFO -------------------------
2023-12-07 21:22:32,633 INFO Async calculations Pool with default processes
2023-12-07 21:22:32,680 DEBUG pid=11298, numbers=(128,)
2023-12-07 21:22:32,680 DEBUG pid=11298, numbers=(255,)
2023-12-07 21:22:32,680 DEBUG pid=11298, numbers=(99999,)
2023-12-07 21:22:32,684 DEBUG pid=11301, numbers=(10651060,)
2023-12-07 21:22:32,686 DEBUG pid=11298, numbers=(12345678,)
2023-12-07 21:22:32,690 DEBUG pid=11302, numbers=(73967205,)
2023-12-07 21:22:34,722 DEBUG End time: 1701976954.722056
2023-12-07 21:22:34,722 DEBUG Time: 2.0887370109558105
2023-12-07 21:22:34,722 INFO -------------------------
2023-12-07 21:22:34,722 INFO Async calculations ProcessPoolExecutor with 8 processes
2023-12-07 21:22:34,722 DEBUG Start time: 1701976954.722232
2023-12-07 21:22:34,761 DEBUG pid=11307, numbers=(128,)
2023-12-07 21:22:34,761 DEBUG pid=11307, numbers=(255,)
2023-12-07 21:22:34,761 DEBUG pid=11307, numbers=(99999,)
2023-12-07 21:22:34,764 DEBUG pid=11307, numbers=(10651060,)
2023-12-07 21:22:34,769 DEBUG pid=11312, numbers=(12345678,)
2023-12-07 21:22:34,770 DEBUG pid=11311, numbers=(73967205,)
2023-12-07 21:22:36,815 DEBUG End time: 1701976956.815424
2023-12-07 21:22:36,815 DEBUG Time: 2.093296766281128
2023-12-07 21:22:36,815 INFO -------------------------
```
</details>
<details>
<summary>Windows 11</summary>
Python 3.11.6, PC with i5-8500T

```commandline
2023-12-07 19:47:57,590 INFO Sync calculations
2023-12-07 19:47:57,590 DEBUG Start time: 1701971277.5909872
2023-12-07 19:47:57,590 DEBUG pid=4888, numbers=(128,)
2023-12-07 19:47:57,590 DEBUG pid=4888, numbers=(255,)
2023-12-07 19:47:57,590 DEBUG pid=4888, numbers=(99999,)
2023-12-07 19:47:57,597 DEBUG pid=4888, numbers=(10651060,)
2023-12-07 19:47:58,292 DEBUG pid=4888, numbers=(12345678,)
2023-12-07 19:47:59,097 DEBUG pid=4888, numbers=(73967205,)
2023-12-07 19:48:03,856 DEBUG End time: 1701971283.856276
2023-12-07 19:48:03,857 DEBUG Time: 6.266256332397461
2023-12-07 19:48:03,857 INFO -------------------------
2023-12-07 19:48:03,857 INFO Async calculations Pool with 1 processes
2023-12-07 19:48:03,857 DEBUG Start time: 1701971283.857476
2023-12-07 19:48:03,982 DEBUG pid=9200, numbers=(128,)
2023-12-07 19:48:03,982 DEBUG pid=9200, numbers=(255,)
2023-12-07 19:48:03,982 DEBUG pid=9200, numbers=(99999,)
2023-12-07 19:48:03,988 DEBUG pid=9200, numbers=(10651060,)
2023-12-07 19:48:04,685 DEBUG pid=9200, numbers=(12345678,)
2023-12-07 19:48:05,489 DEBUG pid=9200, numbers=(73967205,)
2023-12-07 19:48:10,298 DEBUG End time: 1701971290.298842
2023-12-07 19:48:10,298 DEBUG Time: 6.441365957260132
2023-12-07 19:48:10,298 INFO -------------------------
2023-12-07 19:48:10,298 INFO Async calculations Pool with 2 processes
2023-12-07 19:48:10,298 DEBUG Start time: 1701971290.298842
2023-12-07 19:48:10,422 DEBUG pid=8260, numbers=(128,)
2023-12-07 19:48:10,422 DEBUG pid=8260, numbers=(255,)
2023-12-07 19:48:10,422 DEBUG pid=8260, numbers=(99999,)
2023-12-07 19:48:10,424 DEBUG pid=3168, numbers=(10651060,)
2023-12-07 19:48:10,429 DEBUG pid=8260, numbers=(12345678,)
2023-12-07 19:48:11,131 DEBUG pid=3168, numbers=(73967205,)
2023-12-07 19:48:15,852 DEBUG End time: 1701971295.8524418
2023-12-07 19:48:15,852 DEBUG Time: 5.553599834442139
2023-12-07 19:48:15,852 INFO -------------------------
2023-12-07 19:48:15,852 INFO Async calculations Pool with 3 processes
2023-12-07 19:48:15,852 DEBUG Start time: 1701971295.8524418
2023-12-07 19:48:15,981 DEBUG pid=9680, numbers=(128,)
2023-12-07 19:48:15,981 DEBUG pid=9680, numbers=(255,)
2023-12-07 19:48:15,981 DEBUG pid=9680, numbers=(99999,)
2023-12-07 19:48:15,987 DEBUG pid=9924, numbers=(10651060,)
2023-12-07 19:48:15,989 DEBUG pid=10540, numbers=(12345678,)
2023-12-07 19:48:15,989 DEBUG pid=9680, numbers=(73967205,)
2023-12-07 19:48:20,744 DEBUG End time: 1701971300.7448838
2023-12-07 19:48:20,744 DEBUG Time: 4.892441987991333
2023-12-07 19:48:20,744 INFO -------------------------
2023-12-07 19:48:20,744 INFO Async calculations Pool with 4 processes
2023-12-07 19:48:20,744 DEBUG Start time: 1701971300.7448838
2023-12-07 19:48:20,893 DEBUG pid=9612, numbers=(128,)
2023-12-07 19:48:20,894 DEBUG pid=9612, numbers=(255,)
2023-12-07 19:48:20,894 DEBUG pid=9612, numbers=(99999,)
2023-12-07 19:48:20,895 DEBUG pid=1972, numbers=(10651060,)
2023-12-07 19:48:20,901 DEBUG pid=9612, numbers=(12345678,)
2023-12-07 19:48:20,901 DEBUG pid=9260, numbers=(73967205,)
2023-12-07 19:48:25,753 DEBUG End time: 1701971305.7538316
2023-12-07 19:48:25,753 DEBUG Time: 5.008947849273682
2023-12-07 19:48:25,753 INFO -------------------------
2023-12-07 19:48:25,753 INFO Async calculations Pool with 5 processes
2023-12-07 19:48:25,753 DEBUG Start time: 1701971305.7538316
2023-12-07 19:48:25,896 DEBUG pid=3248, numbers=(128,)
2023-12-07 19:48:25,896 DEBUG pid=3248, numbers=(255,)
2023-12-07 19:48:25,896 DEBUG pid=3248, numbers=(99999,)
2023-12-07 19:48:25,896 DEBUG pid=6640, numbers=(10651060,)
2023-12-07 19:48:25,904 DEBUG pid=3248, numbers=(12345678,)
2023-12-07 19:48:25,904 DEBUG pid=6912, numbers=(73967205,)
2023-12-07 19:48:30,761 DEBUG End time: 1701971310.7613432
2023-12-07 19:48:30,761 DEBUG Time: 5.007511615753174
2023-12-07 19:48:30,761 INFO -------------------------
2023-12-07 19:48:30,761 INFO Async calculations Pool with 6 processes
2023-12-07 19:48:30,761 DEBUG Start time: 1701971310.7613432
2023-12-07 19:48:30,910 DEBUG pid=6792, numbers=(128,)
2023-12-07 19:48:30,910 DEBUG pid=6792, numbers=(255,)
2023-12-07 19:48:30,910 DEBUG pid=6792, numbers=(99999,)
2023-12-07 19:48:30,913 DEBUG pid=9300, numbers=(10651060,)
2023-12-07 19:48:30,918 DEBUG pid=6792, numbers=(12345678,)
2023-12-07 19:48:30,922 DEBUG pid=6140, numbers=(73967205,)
2023-12-07 19:48:35,697 DEBUG End time: 1701971315.696248
2023-12-07 19:48:35,697 DEBUG Time: 4.935904264450073
2023-12-07 19:48:35,697 INFO -------------------------
2023-12-07 19:48:35,697 INFO Async calculations Pool with default processes
2023-12-07 19:48:35,846 DEBUG pid=8020, numbers=(128,)
2023-12-07 19:48:35,846 DEBUG pid=8020, numbers=(255,)
2023-12-07 19:48:35,846 DEBUG pid=8020, numbers=(99999,)
2023-12-07 19:48:35,849 DEBUG pid=9572, numbers=(10651060,)
2023-12-07 19:48:35,853 DEBUG pid=8020, numbers=(12345678,)
2023-12-07 19:48:35,857 DEBUG pid=4844, numbers=(73967205,)
2023-12-07 19:48:40,626 DEBUG End time: 1701971320.6263378
2023-12-07 19:48:40,626 DEBUG Time: 4.929090261459351
2023-12-07 19:48:40,626 INFO -------------------------
2023-12-07 19:48:40,626 INFO Async calculations ProcessPoolExecutor with 6 processes
2023-12-07 19:48:40,626 DEBUG Start time: 1701971320.6263378
2023-12-07 19:48:40,773 DEBUG pid=2612, numbers=(128,)
2023-12-07 19:48:40,773 DEBUG pid=2612, numbers=(255,)
2023-12-07 19:48:40,773 DEBUG pid=2612, numbers=(99999,)
2023-12-07 19:48:40,780 DEBUG pid=2612, numbers=(10651060,)
2023-12-07 19:48:40,787 DEBUG pid=8704, numbers=(12345678,)
2023-12-07 19:48:40,787 DEBUG pid=8012, numbers=(73967205,)
2023-12-07 19:48:45,557 DEBUG End time: 1701971325.5571349
2023-12-07 19:48:45,557 DEBUG Time: 4.930797100067139
2023-12-07 19:48:45,557 INFO -------------------------

```
</details>

<details>
<summary>Ubuntu 20.04</summary>

Python 3.11.6, PC with i5-8500T

```commandline

```
</details>