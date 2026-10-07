from tools_manager import execute_tool
from tools import read_text_file

print(execute_tool("What time is it?"))

print(execute_tool("Roll a dice"))

print(execute_tool("Generate a password"))

print(execute_tool("Explain Python"))
text=read_text_file("data/noteffs.txt")
print(text)
