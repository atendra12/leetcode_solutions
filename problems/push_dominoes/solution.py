class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        domino = list(dominoes)
        q = deque()
        for index, item in enumerate(domino):
            if item != '.':
                q.append((index, item))
        
        while q:
            index, item = q.popleft()
            if item == 'L' and index - 1 > -1 and domino[index -1] == '.':
                q.append((index -1, 'L'))
                domino[index - 1] = 'L'
            elif item == 'R':
                if index + 1 < len(domino) and domino[index + 1] == '.':
                    if index + 2 < len(domino) and domino[index + 2] == 'L':
                        q.popleft()
                    else:
                        q.append((index + 1, 'R'))
                        domino[index + 1] = 'R'
        
        return "".join(domino)



            