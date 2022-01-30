q = list()
e = list()
list_avg = list()
n = int(input())
for k in range(n):
    c = input().split()
    if c[0] == "reset":
        a = int(c[1])
    elif c[0] == "new":
        print("ticket", a)
        q.append(a)
        e.append(c[1])
        a += 1
    elif c[0] == "next":
        p = q.pop(0)
        e1 = e.pop(0)
        print("call", p)
    elif c[0] == "order":
        print("qtime", p , int(c[1]) - int(e1))
        list_avg.append(int(c[1]) - int(e1))
    elif c[0] == "avg_qtime":
        total_time = 0
        for i in list_avg:
            total_time += int(i)
        print("avg_qtime", total_time/len(list_avg))
