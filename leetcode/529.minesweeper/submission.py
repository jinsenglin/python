class Solution(object):
    def _yield_adj_pos(self, board, click):
        pos_y = click[0]
        pos_x = click[1]
        
        top_y = 0
        bottom_y = len(board)-1
        #print('DEBUG: bottom_y = {0}'.format(bottom_y))
        
        left_x = 0
        right_x = len(board[0])-1
        #print('DEBUG: right_x = {0}'.format(right_x))
        
        for y in [pos_y-1, pos_y, pos_y+1]:
            for x in [pos_x-1, pos_x, pos_x+1]:
                if y >= top_y and y <= bottom_y and x >= left_x and x <= right_x:
                    if y == pos_y and x == pos_x:
                        pass
                    else:
                        yield [y, x]
    
    
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
        pos_y = click[0]
        pos_x = click[1]
        
        top_y = 0
        bottom_y = len(board)-1
        #print('DEBUG: bottom_y = {0}'.format(bottom_y))
        
        left_x = 0
        right_x = len(board[0])-1
        #print('DEBUG: right_x = {0}'.format(right_x))
        
        if board[pos_y][pos_x] == 'M':
            board[pos_y][pos_x] = 'X'
            return board
        elif board[pos_y][pos_x] == 'E':
            num = 0
            for adj_pos in self._yield_adj_pos(board, click):
                adj_y = adj_pos[0]
                adj_x = adj_pos[1]
                # print('DEBUG: adj_y = {0} and adj_x = {1}'.format(adj_y, adj_x))
                if board[adj_y][adj_x] == 'M':
                   num += 1
            
            if num == 0:
                board[pos_y][pos_x] = 'B'
                
                # TODO: reveal adjustments
                for adj_pos in self._yield_adj_pos(board, click):
                    self.updateBoard(board, adj_pos)
            else:
                board[pos_y][pos_x] = '{0}'.format(num)
        else:
            return board
        
        return board
