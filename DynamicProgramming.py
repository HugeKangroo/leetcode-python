'''
@Author: your name
@Date: 2020-03-30 10:52:46
@LastEditTime: 2020-03-31 10:21:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/DynamicProgramming.py
'''

def DP(row,column):
    row_num = len(row)
    col_num = len(column)
    grid =[ [ -float("inf") for i in range(col_num) ] for j in range(row_num)]
    paths = [[ [] for i in range(col_num) ] for j in range(row_num)]
    for i in range(row_num):
        for j in range(col_num):
            item = row[i]
            name,cost,value = item
            spare = column[j][1] - cost
            if spare < 0:
                # cur item can not fit in
                if i >= 1:
                    grid[i][j] = grid[i-1][j] # previous row
                    paths[i][j] += paths[i-1][j]
                else:
                    grid[i][j] = -float("inf")
            elif spare == 0:
                # can fit only for cur item
                if grid[i-1][j] is not None and i >=1:
                    grid[i][j] = value if value > grid[i-1][j] else grid[i-1][j]
                    paths[i][j] += [name] if value > grid[i-1][j] else paths[i-1][j]
                else:
                    grid[i][j] = value
                    paths[i][j] += [name] 
            else:#spare >= 1
                if i >= 1:
                    if grid[i-1][j] is not None and  grid[i-1][spare-1] is not None:
                        grid[i][j] = grid[i-1][j] if grid[i-1][j] > value + grid[i-1][spare-1] else value + grid[i-1][spare-1]
                        paths[i][j] += paths[i-1][j] if grid[i-1][j] > value + grid[i-1][spare-1] else [name] + paths[i-1][spare-1]

                    elif grid[i-1][j] is not None and grid[i-1][spare-1] is None:
                        grid[i][j] = value if value > grid[i-1][j] else grid[i-1][j]
                        paths[i][j] += [name] if value > grid[i-1][j] else paths[i-1][j]
                        
                    elif grid[i-1][j] is  None and grid[i-1][spare-1] is not None:
                        grid[i][j] = value if value > grid[i-1][spare-1] else grid[i-1][spare-1]
                        paths[i][j] += [name] if value > grid[i-1][spare-1] else paths[i-1][spare-1]

                        
                    elif grid[i-1][j] is None and grid[i-1][spare-1] is None:
                        grid[i][j] = value
                        paths[i][j] += [name]

                    else:
                        raise Exception("logic error.")
                else:
                    grid[i][j] = value
                    paths[i][j] += [name]
    return grid,paths



if __name__ == "__main__":
    table = [["water",3,10],["book",1,3],["food",2,9],["jack",2,5],["camera",1,6]]
    
    volume = [ [i,i+1] for i in range(6)]
    # values = [10,3,9,5,6]
    res = DP(table,volume)
    findItem(res,table,volume)