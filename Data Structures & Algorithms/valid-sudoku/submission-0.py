class Solution:
    def isValidRow(self, board, row_index):
        row=board[row_index] 
        seen=set()
        for num in row:
            if num!='.' and num in seen:
                return False
            seen.add(num)  
        return True      

    def isValidColumn(self, board, column_index): 
        seen=set()
        for row in board:
            num=row[column_index]  
            if  num!='.' and num in seen:
                return False
            seen.add(num)    
        return True  

    def isValidBox(self, board, row_index, column_index):
        seen=set()
        for r in range(3):
            for c in range(3):
                num=board[row_index+r][column_index+c]
                if  num!='.' and num in seen:
                    return False
                seen.add(num)    
        return True                      

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        for row_index in range(9):
            if not self.isValidRow(board, row_index):
                return False
        #column
        for column_index in range(9):
            if not self.isValidColumn(board, column_index):
                return False
        #grid check
        for dr in [0,3,6]:
            for dc in [0,3,6]:
                if not self.isValidBox(board, dr, dc):
                    return False
        return True            



        