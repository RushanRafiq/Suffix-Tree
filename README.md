# Suffix-Tree
In computer science, a suffix tree (also called PAT tree or, in an earlier form, position tree) is a compressed trie containing all the suffixes of the given text as their keys and positions in the text as their values.
# Descriptions About Functions
 1. First it create a tree containing all possible suffixes of a string with terminating character '$'
 2. Then followpath functions checks if the given string follow each node and edge for path
 3. Substring fuction check if the given string follows the path then it is a substring of suffix
 4. CheckSuffix check if the given string is a suffix or not 
 5. IsPalindrome Function checks that palindrom exist or not
 6. Similarly CheckSuffixPalindrome checks if suffixes of given string has palindrome or not and similarly LongestPlaindrome function Checks which suffix is a longest palindrome
 7. addSuffix will add new word ni suffixes of string(similar word would not effect the tree because all possible suffixes are already exist and having similar edges,nodes in that tree (because adding new suffix always check if the path already exist or not if it does then keeps follow untill it has to create a new node for new path) but diffirent word would effect changes in tree)
 8. Print function will print all possible suffixes of string
 # How to Call Functions
 First Initialize class with an object and then use that object to call all functions of that class
 1. c=SuffixTree('aabbaa') 'Pass a string as a parameter it would create tree of all possibble suffixes'
 2. print(c.Substring('ba')) 'Check if given parameter is substring or not'
 3. print(c.CheckSuffix('baa')) 'Check if given parameter is suffix or not'
 4. c.Print() 'It Print all possible suffixes of the given string'
 5. c.addSuffix('Rushan') 'Adding word to existing tree for suffixes(Adding same word will effect none as discussed above)'
 6. print(c.Substring('aaRus')) 'Again check for Substring after adding new word'
 7. print(c.CheckSuffix('aaRushan')) 'Check that the given parameter is a suffix after adding word'
 8. c.Print() 'It Print all possible suffixes of the given string after adding new word in it'
 9. print(c.IsPalindrome('Maam')) 'Checks if Plaindrome exist or not (Palindrome exist only in words having length equal or greater than 2 E.g 'Maam')'
 10. print(c.CheckSuffixPalindrome()) 'Checks is suffixes of string are Palindrome or not'
 11. print(c.LongestPalindrome()) 'Checks the Longest Suffix Palindrome'
