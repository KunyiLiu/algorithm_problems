class FileNode:
    # similar to TrieNode
    def __init__(self):
        # file/folderName = FileNode()
        self.children = {}
        self.is_file = False
        self.content = []

    def addContent(self, content):
        self.content.append(content)

    def readContent(self):
        return "".join(self.content)

class FileSystem:
    def __init__(self):
        self.root = FileNode()
        
    def ls(self, path: str):
        if path == '/':
            return sorted(self.root.children.keys())

        # if file return the file name;
        # if folder => return the children keys (sorted)
        cur = self.root
        parts = [p for p in path.split("/") if p]

        for p in parts:
            # what if p does not exits
            if p not in cur.children:
                raise ValueError("Path does not exit.")
            cur = cur.children[p]

        if cur.is_file:
            return [parts[-1]]

        return sorted(cur.children.keys())
    
    def _traverse(self, path: str):
        """Navigates the trie and returns the node at the given path."""
        curr = self.root
        if path == "/":
            return curr
        
        # Split by / and filter out empty strings from leading/trailing slashes
        parts = [p for p in path.split("/") if p]
        for part in parts:
            if part not in curr.children:
                curr.children[part] = FileNode()
            curr = curr.children[part]
        return curr

    def mkdir(self, path: str):
        self._traverse(path)

    def addContentToFile(self, filePath: str, content: str):
        cur = self._traverse(filePath)
        cur.is_file = True
        cur.addContent(content)

    def readContentFromFile(self, filePath: str) -> str:
        cur = self._traverse(filePath)
        if not cur.is_file:
            raise 

        return cur.readContent()
