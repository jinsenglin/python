import copy

class Solution(object):
    def _eval_postfix(self, postfix):
        stack = []

        for ch in postfix:
            if ch not in ['+', '-', '*', '/']:
                stack.append(ch)
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()
                if ch == '+':
                    stack.append(float(left_operand) + float(right_operand))
                elif ch == '-':
                    stack.append(float(left_operand) - float(right_operand))
                elif ch == '*':
                    stack.append(float(left_operand) * float(right_operand))
                elif ch == '/':
                    # TODO to handle ZeroDivisionError
                    stack.append(float(left_operand) / float(right_operand))

        value = stack.pop()
        return value

    
    def _ch_greater_than_op_in_the_stack(self, ch, stack):
        if len(stack) == 0:
            return True
        elif stack[len(stack)-1] == '(':
            return True
        elif ch in ['*', '/'] and stack[len(stack)-1] in ['+', '-']:
            return True
        else:
            return False
        
    
    def _infix_to_postfix(self, infix):
        stack = []
        postfix = []

        for i in xrange(0, len(infix)):
            ch = infix[i]
            if ch not in ['+', '-', '*', '/', '(', ')']:
                postfix.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch in ['+', '-', '*', '/']:
                while not self._ch_greater_than_op_in_the_stack(ch, stack):
                    op = stack.pop()
                    postfix.append(op)
                stack.append(ch)
            elif ch == ')':
                while True:
                    op = stack.pop()
                    if op == '(':
                        break
                    else:
                        postfix.append(op)

        while len(stack) > 0:
            postfix.append(stack.pop())

        return ''.join(postfix)
    
    def _new_expression_r(self, exp, mask):
        left_oprand = ''
        op = ''
        right_oprand = ''
        index = len(mask)-1;
        new_exp = []
        
        while index > -1:
            if index == len(mask)-1:
                left_oprand = exp[index*2+1-1]
                op = exp[index*2+1]
                right_oprand = exp[index*2+1+1]
            else:
                op = exp[index*2+1]
                left_oprand = exp[index*2+1-1]

            if mask[index] == '1':
                right_oprand = '({0}{1}{2})'.format(left_oprand, op, right_oprand)
            else:
                new_exp.insert(0, right_oprand)
                new_exp.insert(0, op)
                right_oprand = left_oprand

            index -= 1

        new_exp.insert(0, right_oprand)
        return ''.join(new_exp)
    

    def _new_expression(self, exp, mask):
        left_oprand = ''
        op = ''
        right_oprand = ''
        index = 0;
        new_exp = []
        
        while index < len(mask):
            if index == 0:
                left_oprand = exp[index*2+1-1]
                op = exp[index*2+1]
                right_oprand = exp[index*2+1+1]
            else:
                op = exp[index*2+1]
                right_oprand = exp[index*2+1+1]
            
            if mask[index] == '1':
                left_oprand = '({0}{1}{2})'.format(left_oprand, op, right_oprand)
            else:
                new_exp.append(left_oprand)
                new_exp.append(op)
                left_oprand = right_oprand

            index += 1

        new_exp.append(left_oprand)
        return ''.join(new_exp)
    
    
    def _yield_possible_ops(self):
        for op in ['+', '-', '*', '/']:
            yield '{0}'.format(op)
    
    
    def _yield_possible_expressions(self, nums):
        if len(nums) == 1:
            yield '{0}'.format(nums[0])
        else:
            for num in nums:
                nums_clone = copy.copy(nums)
                nums_clone.remove(num)
                for op in self._yield_possible_ops():
                    for sub_exp in self._yield_possible_expressions(nums_clone):
                        yield '{0}{1}{2}'.format(num, op, sub_exp)

                        
    def _yield_possible_flags(self):
        for flag in [0, 1]:
            yield '{0}'.format(flag)
            
            
    def _yield_possible_masks(self, n):
        if n == 2:
            for i in self._yield_possible_flags():
                yield '{0}'.format(i)
        else:
            for i in self._yield_possible_flags():
                for j in self._yield_possible_masks(n-1):
                    yield '{0}{1}'.format(i, j)
                    
                
    def _yield_possible_expressions_with_possible_masks(self, nums):
        for exp in self._yield_possible_expressions(nums):
            for mask in self._yield_possible_masks(len(nums)):
                yield(self._new_expression(exp, mask))
                yield(self._new_expression_r(exp, mask))
                
                
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        for exp in self._yield_possible_expressions_with_possible_masks(nums):
            value = 0
            
            try:
                postfix = self._infix_to_postfix(exp)
                value = self._eval_postfix(postfix)
                # print('DEBUG: {0} -> {1} = {2}'.format(exp, postfix, value))
            except ZeroDivisionError:
                pass
            
            if value == 24:
                return True
            
        return False
