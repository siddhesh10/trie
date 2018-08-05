import sys
sys.path.insert(0, 'C:/Users/sidd/Desktop/trie/')
import node


class trie:

    def __init__(self):
        self.root=node.node("*")

    def add(self,word):

        temp = self.root
        for char in word:
            found_in_child = False # Search for the character in the children of the present `node
            for child in temp.children:
                if child.char == char:
                # We found it, increase the counter by 1 to keep track that another
                # word has it as well
                    child.counter += 1
                # And point the node to the child that contains this char
                    temp= child
                    found_in_child = True
                    break
        # We did not find it so add a new chlid
            if not found_in_child:
                new_node=node.node(char)
                temp.children.append(new_node)
            # And then point node to the new child
                temp = new_node
        node.word_finished = True


    def search(self,prefix):

        node = self.root
        if not node.children:
            return False

        for char in prefix:
            char_not_found = True
        # Search through all the children of the present `node`
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                # Assign node as the child containing the char and break
                    node = child
                    break
        # Return False anyway when we did not find a char.
            if char_not_found:
                return False
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
        return True
