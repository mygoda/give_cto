#coding = UTF-8
import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 
#this is first question
def del_repeat(LB):
    for x in LB:
        while LB.count(x)>1:
            del LB[LB.index(x)]
    return LB
#test function
print del_repeat([1,[1,2,3],1])
