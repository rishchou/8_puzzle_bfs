
# @File - Project-1.py
# @Brief - Planning project-1 to fins solution of 8-puzzle algorithm using brute force approach
# @Authors - Rishabh Choudhary

import sys
import copy
import collections
import numpy as np

# Define goal state
goalState=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

#Define global variables
startState = []
Nodes = []
NodeInfo = []
NodePath = []
node_id = 1
totalNodes = 0
visited = set()


# Define Node class for each node of the tree
class Node:
	def __init__(self,startNode=None,nodeID=None, parentID=None):
		self.state=startNode
		self.ID = nodeID
		self.parentID = parentID
	
	# Expand current node in each possible direction (up, down, left, right)
	def expandNode(self,parent,visited,totalNodes=None):
		children=[]
		global node_id
		global NodeInfo
		x_,y_= None,None
		for i in range(0,3):
			for j in range(0,3):
				if(parent.state[i][j]==0):
					x_=i
					y_=j
					break
			if x_ is not None:
				break

		#move left
		if y_ is not 0 : 
			child=Node(copy.deepcopy(parent.state),None,parent.ID)
			child.state[x_][y_-1],child.state[x_][y_]=child.state[x_][y_],child.state[x_][y_-1]
			# If expanded node is not present in visited nodes, append to children list
			if (self.toString(child.state) not in visited):
				totalNodes+=1
				#Increment node id
				node_id+=1
				child.ID =node_id				
				children.append(child)

		# move right
		if y_ is not 2:  
			#create child node using parent
			child = Node(copy.deepcopy(parent.state),None,parent.ID)
			child.state[x_][y_+1], child.state[x_][ y_] = child.state[x_][y_], child.state[x_][y_+1]
			# If expanded node is not present in visited nodes, append to children list
			if (self.toString(child.state) not in visited):
				totalNodes+=1
				#Increment node id
				node_id+=1
				child.ID =node_id				
				children.append(child)

		# move up
		if x_ is not 0:  
			#create child node using parent
			child = Node(copy.deepcopy(parent.state),None,parent.ID)
			child.state[x_-1][y_], child.state[x_][ y_] = child.state[x_][y_], child.state[x_-1][y_]
			# If expanded node is not present in visited nodes, append to children list
			if (self.toString(child.state) not in visited):
				#Increment node id
				node_id+=1
				child.ID =node_id				
				children.append(child)

		# move down
		if x_ is not 2:  
			#create child node using parent
			child = Node(copy.deepcopy(parent.state),None,parent.ID)
			child.state[x_ + 1][y_], child.state[x_][y_] = child.state[x_][y_], child.state[x_ + 1][y_]
			# If expanded node is not present in visited nodes, append to children list
			if (self.toString(child.state) not in visited):
				totalNodes+=1
				#Increment node id
				node_id+=1
				child.ID =node_id				
				children.append(child)

		return children,totalNodes

	#Utility function to convert Node params to string for writing in file
	def node2string(self, s2s):
		s = ''
		for i in s2s:
			for j in i:
				s += str(j) + " "
		return s

	#Function to check goal state with current state and backtrace the Nodepath to from goal to initial state
	def isGoalState(self, currentNode):

		global NodePath
		if(self.toString(currentNode.state) == self.toString(goalState)):

			#print(Nodes)
			#print(NodeInfo)
			print("Total nodes visited:",len(NodeInfo))
			n_id = currentNode.ID-1
			p_id = currentNode.parentID-1

			#Append nodes and their parents in backward fashion as seen in nodeinfo
			NodePath.append(Nodes[NodeInfo[n_id][0]-1])
			NodePath.append(Nodes[NodeInfo[n_id][1]-1])
			while p_id != 0:
				n_id = p_id
				NodePath.append(Nodes[NodeInfo[n_id][1]-1])
				p_id = NodeInfo[n_id][1] -1

			print("NodePath: ")	
			NodePath.reverse()
			for elem in NodePath:
				print(elem)

			self.writeOutput(Nodes,1)
			self.writeOutput(NodeInfo,2)
			self.writeOutput(NodePath,3)	
			flag = 1
		else:
			flag = 0

		return flag	
			
	# Utility function to write into Nodes, NodeInfo and NodePath file	
	def writeOutput(self, fileName, flag):

		if flag == 1:

			f_op = open('Nodes.txt', 'w')
			for i in range(0, len(fileName)):
				t_nodes = fileName[i].transpose()
				string_val = self.node2string(t_nodes)
				f_op.write("%s \n" % string_val)
			f_op.close()

		if flag == 2:
			f_op = open('NodesInfo.txt', 'w')
			for i in range(0, len(fileName)):
				for j in range(0, 3):
					string_val = fileName[i][j]
					f_op.write("%s " % string_val)
				f_op.write("\n")
			f_op.close()

		if flag == 3:

			f_op = open('NodePath.txt', 'w')
			for i in range(0, len(fileName)):
				t_nodes = fileName[i].transpose()
				string_val = self.node2string(t_nodes)
				f_op.write("%s \n" % string_val)
			f_op.close()
	
	#Converting a state to string for storage in set
	def toString(self,State):
		s=''
		for i in State:
			for j in i:
				s+=str(j)
		return s
		
	#Breadth first search algorithm for 8-puzzle
	def breadth_first_search(self):

		global node_id
		global Nodes
		global totalNodes
		matrix = []

		#Take user input for initial state
		for i in range(3):
		    matrix.append(list(map(int, input().rstrip().split())))
		startState = np.array(matrix)

		if(self.toString(startState) == self.toString(goalState)):
			print("Initial Node is equal to Goal Node, exiting")
			return

		maxListSize=536870912
		
		# Intialize a queue for storing nodes at same level
		q = collections.deque()
		startNode = Node(startState, node_id,0)
		
		# Add the current node to the queue
		q.append(startNode)
		flag = 0
		while (q):
			if len(q)>maxListSize:
				maxListSize=len(q)
			
			currentNode = q.popleft()
			
			# Add the current node to the lists
			Nodes.append(currentNode.state)
			stateString = self.toString(currentNode.state)
			NodeInfo.append([currentNode.ID, currentNode.parentID, 0])
			visited.add(stateString)
			
			ret = self.isGoalState(currentNode)
			if ret == 1:
				print ("Goal state reached")
				break
			# Expand the current node and put in queue  
			tchilds,totalNodes=self.expandNode(currentNode, visited,totalNodes)
			q.extend(tchilds)# Adding the expanded chidrens to the list
		
		if(ret == 0):
			print("No solution found")
			return
				
# Main function to handle user input
#Ask for input and parse it


def main():

	#Parsing the input format to the required format for processing in python.
	print ("Please input the  Start state in the form of 2D matrix with 3 elements in each row and space between elements:")
		
	obj = Node()
	obj.breadth_first_search()

	


if __name__ == "__main__":
	main()