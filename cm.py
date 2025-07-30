class state:
    def __init__(self,missionaries,cannibals,boat):
        self.missionaries=missionaries
        self.cannibals=cannibals
        self.boat=boat
    def __eq__(self,other):
        return (self.missionaries==other.missionaries and self.cannibals==other.cannibals and self.boat==other.boat)
    def __hash__(self):
        return hash((self.missionaries, self.cannibals,self.boat))
    def is_valid(state):
        if state.missionaries < state.cannibals and state.missionaries > 0:
            return False
        if (3 - state.missionaries) < (3 - state.cannibals) and (3 - state.missionaries) > 0:
            return False
        return True
    def get_successor(boss):
        successor=[]
        if boss.boat==0:
            for i in range(1,3):
                for j in range (3):
                    if state.is_valid(state(boss.missionaries-i,boss.cannibals-j+1,1)):
                        successor.append(state(boss.missionaries-i,boss.cannibals-j+1,1))
        for i in range(1,3):
            for j in range(3):
                if state.is_valid(state(boss.missionaries+i,boss.cannibals+j,0)):
                    successor.append(state(boss.missionaries+i,boss.cannibals+j,0))
        return [successor]
    def dfs(start,target):
        visited=set()
        frontier=[]
        frontier.append([start])
        while frontier:
            path=frontier.pop(0)
            brstate=path[-1]
            if brstate==target:
                return path
            if brstate not in visited:
                visited.add(brstate)
            for next_state in state.get_successor(brstate)[0]:
                if next_state not in visited:
                    frontier.append(path+[next_state])
        return None
    def print_solution(path):
        print("Solution")
        for i, brstate in enumerate(path):
            print(f"Step {i+1}:Left Bank:{brstate.missionaries},{brstate.cannibals},Right Bank:{3-brstate.missionaries},{3-brstate.cannibals}")
    def main():
        start=state(3,3,0)
        end=state(0,0,1)
        path=state.dfs(start,end)
        if path:
            state.print_solution(path)
if __name__=="__main__":  # fix: correct __name__ check
    state.main()
        
    