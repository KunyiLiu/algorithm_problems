class ThroneInheritance:
    def __init__(self, kingName: str):
        self.family = {kingName: []}
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        # Add the child to the parent's list
        self.family[parentName].append(childName)
        # Initialize the child's own branch
        self.family[childName] = []

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        
        # Standard Recursive Preorder Traversal
        def dfs(current_person):
            if current_person not in self.dead:
                res.append(current_person)
            
            for child in self.family[current_person]:
                dfs(child)
        
        dfs(self.king)
        return res
