import sys
sys.path.insert(0, 'C:/Users/sidd/Desktop/trie/')
import trie



keys = ["the","a","there","anaswe","any",
            "by","their"]



t = trie.trie()


for key in keys:
    t.add(key)


print(t.search("ab"))
