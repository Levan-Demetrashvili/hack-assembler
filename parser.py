def parser(command):
  fields = ["commandType", "symbol", "dest", "comp", "jump"]
  command_dict = dict.fromkeys(fields)

  if command.startswith('@'):
    #* A-insctruction
    command_dict['commandType'] = 'A_COMMAND'
    address = command.split('@')[1]
    command_dict['symbol'] = address
  else: 
    #* C-insctruction
    command_dict['commandType'] = 'C_COMMAND'
    command_dict['dest'] = command.split('=')[0] if '=' in command else None
    command_dict['jump'] = command.split(';')[1] if ';' in command else None
    line = command.split('=')[1] if '=' in command else command
    command_dict['comp'] = line.split(';')[0] if ';' in line else line
  return command_dict
    