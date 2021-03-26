from timeit import Timer
import fibonacci_evaluation
t1 = Timer("fib(20)", "from fibonacci_evaluation import fib")
for i in range(1, 30):
    cmd= "fib("+ str(i) +")"
    t1 = Timer(cmd, "from fibonacci_evaluation import fib")
    time1 = t1.timeit(3)

    cmd = "fibi(" +str(i) +")"
    t2 = Timer(cmd, "from fibonacci_evaluation import fibi")
    time2 =t2.timeit(3)
    print(f"n={i:2d}, fib:{time1:8.6f}, fibi: {time2:7.6f} , time1/time2: {time1/time2:10.2f}")