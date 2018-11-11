class String :
    def __init__(self):
        temp=int(raw_input("How much elements there is going to be?"))
        self.brackets=[]
        for i in range (0,temp):
            self.brackets.append(raw_input())
    def is_matched(self):
        new_brackets=[]
        for i in range(0,len(self.brackets)):
            if self.brackets[i]=="(" or self.brackets[i]=="[" or self.brackets[i]=="{" or self.brackets[i]==")" or self.brackets[i]=="]" or self.brackets[i]=="}":
                new_brackets.append(self.brackets[i])
        if len(new_brackets) % 2 != 0:
            return False

        opening = ("(", "[", "{")
        closing = (")", "]", "}")
        mapping = {opening[0]: closing[0],
                   opening[1]: closing[1],
                   opening[2]: closing[2]}

        if new_brackets[0] in closing:
            return False

        if new_brackets[-1] in opening:
            return False

        closing_queue = []
        for letter in new_brackets:
            if letter in opening:
                closing_queue.append(mapping[letter])
            elif letter in closing:
                if not closing_queue:
                    return False

                if closing_queue[-1] == letter:
                    closing_queue.pop()
                else:
                    return False

        return True
class Sorting:

    def createStack(self):
        stack = []
        return stack
    def isEmpty(self,stack=0):
        if stack==0:
            stack=stack
        return len(stack) == 0

    def push(self,stack, item):
        stack.append(item)

    def pop(self,stack):
        if (self.isEmpty(stack)):
            print("Stack Underflow ")
            exit(1)

            return stack.pop()
    def top(self,stack=0):
        if stack==0:
            stack=stack
        p = len(stack)
        return stack[p - 1]

    def prints(self):
        for i in range(len(self.stack) - 1, -1, -1):
            print(self.stack[i])
        print()
    def sortStack(self,stack):
        tmpStack=stack
        while (self.isEmpty(stack) == False):
            tmp = self.top(stack)
            stack.pop()

            while (self.isEmpty(tmpStack) == False and  int(self.top(tmpStack)) > int(tmp)):
                self.push(stack, self.top(tmpStack))
                tmpStack.pop()

            self.push(stack,tmp)

        return tmpStack
def main():
    queue=String()
    if queue.is_matched():
        print("It's true")
    else :
        print("It's false")
    print("Now we are starting sorting algorithm")
    sort=Sorting()
    stak=sort.createStack()
    for i in range(1,int(raw_input("How many times do you want to input a number?"))):
        sort.push(stak,raw_input("Input number,please"))
    sorted=sort.sortStack(stak)
    for i in range(0,len(sorted)):
        print(sorted[i]+"\n")
        print(sorted[i]+"\n")
main()