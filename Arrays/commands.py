if __name__ =="__main__":
    N =int(input())
    my_list=[]

for _ in range(N): 
    command = input().split()
    cmd = command[0]

    if cmd=="insert":
        my_list.insert(int(command[1]),int(command[2]))
    elif cmd=="print":
        print(my_list)
    elif cmd=="remove":
        my_list.remove(int(command[1]))
    elif cmd=="append":
        my_list.append(int(command[1]))
    elif cmd=="sort":
        my_list.sort()
    elif cmd=="pop":
        my_list.pop()
    elif cmd=="reverse":
        my_list.reverse()
