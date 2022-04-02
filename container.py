import node
class Container:
    def __init__ (self):
        self.mFirst=None
        
    def Exists(self,item):
        current = self.mFirst
        while current:
            if current.mItem==item:
                return True
            current=current.mNext
        return False

    def Insert(self,item):
        if self.Exists(item):
            return False
        else:
            self.mFirst=node.Node(item,self.mFirst)
            return True

    def Traverse(self,callback,data):
        current=self.mFirst
        while current:
            callback(current.mItem,data)
            current=current.mNext
        return

    def Delete(self,item):
        if not self.Exists(item):
            return False
        current=self.mFirst
        if current.mItem==item:
            self.mFirst=current.mNext
            return True
        while not current.mNext.mItem==item:
            current= current.mNext
        current.mNext=current.mNext.mNext
        return True
    def Retrieve(self,item):
        current = self.mFirst
        while current:
            if current.mItem==item:
                return current.mItem
            current=current.mNext
        return None
    def size(self):
        counter=0
        current=self.mFirst
        while current:
            counter+=1
            current=current.mNext
        return counter
