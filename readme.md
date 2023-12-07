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
