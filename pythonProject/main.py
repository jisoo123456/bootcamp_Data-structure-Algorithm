## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__(self) :
		self.data = None
		self.link = None

def printNodes(start):
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link  #다음 노드로 이동
		print(current.data, end = ' ')
	print()

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]


## 메인 코드 부분 ##
if __name__ == "__main__":

	node = Node()		# 첫 번째 노드(pre를 선언해야하기떄문에 첫번째 노드 먼저지정)
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node  #이 부분이 없으면 피카츄만 출력됨(연결이 안되기 때문)
		memory.append(node)

	printNodes(head)
	print(memory)  #memory가 리스트지만 그 안에 내용들이 객체이기 때문에 리스트 출력이 안됨 -> 해결방법 매직매소드
