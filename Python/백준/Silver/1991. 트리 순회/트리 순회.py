import sys

input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
n = int(input())
nodes = {}

# get_node(): 이미 생성된 노드는 재사용하고, 없으면 새로 만들어 반환
# → 중복 생성 방지 + 모든 노드를 딕셔너리로 관리하기 위함
# 입력 순서가 섞여 있어도 필요한 노드를 한 번만 만들어서 이름(key)으로 쉽게 찾아 쓰게함
def get_node(ch):
    if ch not in nodes:
        nodes[ch] = Node(ch)
    return nodes[ch]

for _ in range(n):
    p, l, r = input().split()
    parent = get_node(p)
    parent.left = None if l == '.' else get_node(l)
    parent.right = None if r == '.' else get_node(r)

root = nodes['A']

def preorder(n, out):
    if not n: return
    out.append(n.value)
    preorder(n.left, out)
    preorder(n.right, out)

def inorder(n, out):
    if not n: return
    inorder(n.left, out)
    out.append(n.value)
    inorder(n.right, out)

def postorder(n, out):
    if not n: return
    postorder(n.left, out)
    postorder(n.right, out)
    out.append(n.value)

pre, ino, post = [], [], []
preorder(root, pre)
inorder(root, ino)
postorder(root, post)

print(''.join(pre))
print(''.join(ino))
print(''.join(post))