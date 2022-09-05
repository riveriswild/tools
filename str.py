# takes a column, returns row delimited by ','

my_str = []
with open("doc_str.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    my_str.append(stripped_line)
    
print(my_str)
