import sys
from parser import parser
from trimmer import trimmer
from codegen import code_gen
from variables import symbol_table

    
def main():
  programName = sys.argv[1].split('/')[-1].split('.')[0]
  instructions = []
  pc = -1
  multi_line_comment = False  
  
  with open(sys.argv[1],"r") as f:
    for line in f:
      (command,multi_line_comment) = trimmer(line,multi_line_comment)
      if not command:
        continue
      if command.startswith('('):
        label = command.split(')')[0].split('(')[1]
        symbol_table[label] = pc + 1
      else:
        pc+=1
        instructions.append(parser(command))
        
  with open(f"./MLcode/{programName}.hack", 'w') as f:
    for instruction in instructions:
      ML_CODE = code_gen(instruction)    
      f.write(ML_CODE + '\n')
      
        

if __name__ == "__main__":
  main()