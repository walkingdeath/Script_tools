import psutil
import time
# 定义一个进程列表
process_lst = []

def getProcess(pid):

    # 获取当前系统所有进程id列表
    all_pids  = psutil.pids()

    # 遍历所有进程，名称匹配的加入process_lst
    # for pid in all_pids:
    #     p = psutil.Process(pid)
    #     if (p.name() == pName):
    #         process_lst.append(p)
    for pid in all_pids:
        if(pid == 5540):
            p = psutil.Process(pid)
            process_lst.append(p)
    return process_lst

# 获取进程名位Python的进程对象列表
process_lst = getProcess(5540)

# 获取内存利用率：
for process_instance in process_lst:
    print(process_instance.memory_percent())

# 获取cpu利用率：
for process_instance in process_lst:
    process_instance.cpu_percent(None)

time.sleep(2)
for process_instance in process_lst:
    print(process_instance.cpu_percent(None))


