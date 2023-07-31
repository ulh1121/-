from collections import deque
def solution(order):
    answer =0
    stack=deque([])
    length=len(order)
    k=0
    for i in range(length):
        if order[k]!=i+1:
            stack.appendleft(i+1)
            continue;
            
        k+=1
        answer+=1
        
        while(len(stack)>0 and stack[0]==order[k]):
            stack.popleft();
            k+=1
            answer+=1       
        
    return answer
