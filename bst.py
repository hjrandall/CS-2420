class Node:
    def __init__ (self,item):
        self.mitem=item
        self.mleft=None
        self.mright=None

class Container:
    def __init__ (self):
        self.mroot=None
    
    def Insert (self,item):
        if self.exists(item):
            return False
        n=Node(item)
        self.mroot=self.insertr(n,self.mroot)
        return True
    def insertr(self,n,current):
        if current is None:
            current=n
        elif n.mitem < current.mitem:
            current.mleft = self.insertr(n,current.mleft)
        else:
            current.mright = self.insertr(n,current.mright)
        return current
    def exists(self,item):
        return self.existsr(item,self.mroot)

    def existsr(self,item,current):
        if current is None:
            return False
        elif current.mitem == item:
            return True 
        elif item < current.mitem:
            return self.existsr(item,current.mleft)
        else:
            return self.existsr(item,current.mright)

    def Retrieve(self,item):
        return self.retriever(item,self.mroot)

    def retriever(self,item,current):
        if current is None:
            return None
        elif current.mitem == item:
            return current.mitem
        elif item< current.mitem :
            return self.retriever(item,current.mleft)
        else:
            return self.retriever(item,current.mright)

    def Traverse(self,callback,data):
        self.traverser(callback,data,self.mroot)
    
    def traverser(self,callback,data,current):
        if current:
            callback(current.mitem,data)
            self.traverser(callback,data,current.mleft)
            self.traverser(callback,data,current.mright)
    def size(self):
        return self.sizer(self.mroot)
    def sizer(self,current):
        if current:
            return 1+ self.sizer(current.mleft)+self.sizer(current.mright)
        else:
            return 0

    def Delete(self,item):
        if self.exists(item)==False:
            return False
        # self.mroot=self.deleter(item,self.mroot)
        # return True
    def deleter(self,item,current):
        if item < current.mitem:
            current.mleft=self.deleter(item, current.mleft)
        elif item > current.mitem:
            current.mright=self.deleter(item, current.mright)
        else:
            if current.mleft == None and current.mright == None: #no child case
                current==None
            elif current.mleft == None and current.mright != None: # 1 right child case
                current=current.mright
            elif current.mleft != None and current.mright == None: # 1 left child case
                current=current.mright
            else: # 2 children
                sucsesor=current.mright
                while sucsesor.mleft:
                    sucsesor=sucsesor.mleft
                current.mitem=sucsesor.mitem
                self.deleter(sucsesor.mitem,current.mright)
        return current


            
            
    
