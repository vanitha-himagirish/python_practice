# Return the count of a given substring from a string
def print_cnt_substring(lst,sbstr): 
    p=lst.count(sbstr)
    print(p)
    
a="Emma is good developer. Emma is a writer"
print_cnt_substring(a,"Emma")
