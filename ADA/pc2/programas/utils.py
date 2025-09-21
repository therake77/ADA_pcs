class Node:
    key = None
    left = None
    right = None
    def __init__(self,key=None,left=None,right=None) -> None:
        if(key is not None):
            self.key = key
        if(left is not None):
            self.left = left
        if(right is not None):
            self.right = right
        pass

class Tree:
    root:Node
    def __init__(self,root=None) -> None:
        if(root is not None):
            self.root = root
        else:
            pass
    def printAsList(self,labels=None) -> str:
        q = Queue()
        q.enqueue(self.root)
        if(labels is not None):
            s = f"{labels[self.root.key]} "
        else:
            s = f"{self.root.key} "
        while(q.length() > 0):
            r = q.dequeue()
            if (r.left is None and r.right is None):
                continue
            elif(r.left is not None):
                q.enqueue(r.left)
                if(labels is not None):
                    s+=f"{labels[r.left.key]} "
                else:    
                    s+=f"{r.left.key} "
            else:
                s+="None "
            if(r.right is not None):
                q.enqueue(r.right)
                if(labels is not None):
                    s+=f"{labels[r.right.key]} "
                else:    
                    s+=f"{r.right.key} "
            else:
                s+="None "
        return s


class Stack:
    stack = []
    def __init__(self) -> None:
        pass
    def push(self,key):
        if(key is not None):
            self.stack.append(key)

    def pop(self):
        if(len(self.stack)>0):
            return self.stack.pop()
        raise ValueError
    def length(self):
        return len(self.stack)

class Queue:
    queue = []
    def __init__(self) -> None:
        pass
    
    def enqueue(self,key)->None:
        self.queue.insert(0,key)

    def dequeue(self):
        if(len(self.queue)>0):
            return self.queue.pop()
        raise ValueError
    def length(self)->int:
        return len(self.queue)