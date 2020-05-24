
class BSTNode:
   def __init__(self, data):
      self.data = data
      self.left= None
      self. right = None
      #set data
      
count = 0
class BST:
   def __init__(self,root = None):
      self.root = root

   def searchRec(self,root, data):
      if not root:
         return None
      if root.data == data:
         return root
      if root.data > data:
         return search(root.left,data)
      return search(root.right,data)

   def search(self,root,data):
      if not root:
         return None
      while (root != None):
         if root.data == data:
            return root
         if root.data> data:
            root = root.left
         else:
            root = root.right
      return None
            

   def findmin(self,root):
      if not root:
         return NOne
      if root.left == None:
         return root
      return self.findmin(root.left)

   def findmin2(self,root):
      if not root:
         return None
      while root.left != None:
         root = root.left
      return root.data

   def findmax(self,root):
      if not root:
         return root
      if root.right == None:
         return root
      if root.right != None:
         return self.findmax(root.right)
      
   def findmax2(self,root):
      if not root:
         return None
      while root.right != None:
         root = root.right
      return root.data

   def rangePrinter(self,root,A,B):
      if not root:
         return None
      if root.data >= A:
         self.rangePrinter(root.left,A,B)
      if A <= root.data <= B:
         print(root.data)
      if root.data <= B:
         self.rangePrinter(root.right,A,B)
         
   def inorder(self,root):
      if not root:
         return
      self.inorder(root.left)
      print(root.data)
      self.inorder(root.right)

   def inorderDesc(self,root):
      if not root:
         return
      self.inorderDesc(root.right)
      print(root.data)
      self.inorderDesc(root.left)

   def kthSmallest(self,root,k):
      global count
      if not root:
         return
      l = self.kthSmallest(root.left,k)
      if l:
         return l
      
      count = count + 1
      if count == k:
         return root
      return self.kthSmallest(root.right,k)
   
   def lca(self,root,A,B):
      if not root:
         return root
      if A < root.data and B < root.data:   
         l = self.lca(root.left,A,B)
         if l:
            return l
      if A <= root.data <= B:
         return root
      if A > root.data and B > root.data:
         return self.lca(root.right,A,B)
      
      
      
node1 = BSTNode(6);node2 = BSTNode(2);node3 = BSTNode(10);node4 = BSTNode(2);
node5 = BSTNode(15);node6 = BSTNode(4);node7 = BSTNode(12);node8 = BSTNode(3);
node9 = BSTNode(5);
 
node1.left = node2; node1.right = node3
node2.right = node6; node6.left= node8;node6.right=node9
node3.right=node5;node5.left = node7

bt = BST(node1)
print("SEARCH 12 in BINARY SEARCH TREE")
print(bt.search(node1,12))

print("-"*50)

print("FINDS MIN OF BINARY SEARCH TREE USING RECURSIVE FUNCTION ")
result = (bt.findmin(node1).data)
print(result)

print("-"*50)

print("FINDS MIN OF BINARY SEARCH TREE")
print(bt.findmin2(node1))

print("-"*50)

print("FIND MAX OF BINARY SEARCH TREE USING RECURSIVE FUNCTION")
result2 = bt.findmax(node1)
print(result2.data)

print("-"*50)

print("FIND MAX OF BINARY SEARCH TREE")
print(bt.findmax2(node1))

print("-"*50)

print("FIND THE RANGE OF ELEMENTS BETWEEN 2 NUMBERS")
print(bt.rangePrinter(node1,4,11))

print("-"*50)

print("PRINTS THE INORDER TREE TRAVERSAL ALGORITHM OF THE GIVEN TREE")
print(bt.inorder(node1))

print("-"*50)

print("PRINTS THE DESCENDING INORDER TREE TRAVERSAL ALGORITHM OF THE GIVEN TREE")
print(bt.inorderDesc(node1))

print("-"*50)

print("FINDS THE KTH SMALLEST ELEMENT")
result3 = bt.kthSmallest(node1,7)
print(result3.data)

print("-"*50)

print("FINDS THE LEAST COMMON ANCESTOR OF 2 GIVEN ELEMENTS")
result4 = bt.lca(node1,4,10)
print(result4.data)
