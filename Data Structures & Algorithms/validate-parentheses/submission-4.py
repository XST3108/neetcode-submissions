class Solution:
    def isValid(self, s: str) -> bool:



        #1. stack的初始化怎么搞，一般不初始化吗，直接for循环往里加？
        stack = []

        if not s:
            return True


        for i in range(len(s)):
            #string字符串也能这样遍历吗，s【0】拿元素可以吗

            #如果是左括号，就无脑加入stack，右括号，就弹出栈顶，如果能匹配，就continue，如果不能 False，最终stack空 return True

            if s[i] in ['(','{','[']:
                stack.append(s[i])

                #continue和break都是跨过上面的if，到for的下一个是吗
            else:
                if not stack:
                    return False

                top_stack = stack.pop()
                
                if s[i] == ')':
                    if top_stack != '(':
                        return False
                    
                if s[i] == '}':
                    if top_stack != '{':
                        return False
                
                if s[i] == ']':
                    if top_stack !='[':
                        return False

        if not stack:
            return True
        return False
                    
                    
                        






























    #     1. 输入的是一个string
    #     2. 怎么实例化一个stack，那么我用到了这个stack，实例出了一个stack，是不是要用On的复杂度去存储这个stack
    #     3. 遍历string的话，应该是for吧，但是有判断条件啊，就是发现是右括号了


    # stack = []

    
        