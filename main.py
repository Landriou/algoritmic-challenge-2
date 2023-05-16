from trie import *
from doublelinkedlist import *

def encriptar(documento,niveles):
    T = Trie()
    currentnode = documento.head
    while currentnode != None:
        trie_insert(T,currentnode.value)
        currentnode = currentnode.nextNode
    L = LinkedList()
    recorridoTrie(T.root,String(""),L)
    imprimirlista(L)
    for i in range(len(niveles)):
        L = traverseAmplitude(T,niveles[i])
        inverseValues(L)
    L = LinkedList()
    recorridoTrie(T.root,String(""),L)
    imprimirlista(L)

def inverseValues(DL):
    currentnode = DL.head
    reversenode = DL.tail
    size = length(DL)//2
    for i in range(size):
        headvalue = currentnode.value.value.key
        reversevalue = reversenode.value.value.key
        currentnode.value.value.key = reversevalue
        reversenode.value.value.key = headvalue
        currentnode = currentnode.nextNode
        reversenode = reversenode.previousNode

def traverseAmplitude(T,wantedlvl):
    nivel = 0
    L = DoubleLinkedList()
    traverselvl(T.root,nivel,L,wantedlvl)
    return L    
    
def traverselvl(node,nivel,L,wantedlevel):
    currentnode = None
    if node.children != None:
        currentnode = node.children.head
    while currentnode != None:
        if nivel == wantedlevel: # Imprimo la palabra si es end of word
            D_add(L,currentnode)
        traverselvl(currentnode.value,nivel+1,L,wantedlevel)
        currentnode = currentnode.nextNode
    
documento = LinkedList()
add(documento,"kotlyn")
add(documento,"swift")
add(documento,"android")
add(documento,"ios")

A = Array(2,0)
A[0] = 2
A[1] = 3

encriptar(documento,A)