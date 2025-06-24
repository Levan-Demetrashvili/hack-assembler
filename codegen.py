import variables as globs
from utilis import safe_int


def code_gen(instruction):
  code = ''
  if instruction['commandType'] == 'A_COMMAND':
    symbol= instruction['symbol']
    number = safe_int(symbol) if safe_int(symbol) is not None else  globs.symbol_table.get(symbol)
    if number == None:
      globs.symbol_table[symbol] = globs.variable_address
      number = globs.variable_address
      globs.variable_address+=1
    code = "0" + "{0:015b}".format(number)
  else:
    code += '111'
    dest = instruction.get("dest") or ""
    dest_bits = ''.join([str(int("A" in dest)),str(int("D" in dest)),str(int("M" in dest))])
    jump_bits = globs.jump_table[instruction["jump"]]
    comp_bits = globs.comp_table[instruction["comp"]]
    code += comp_bits + dest_bits + jump_bits 
    
  return code