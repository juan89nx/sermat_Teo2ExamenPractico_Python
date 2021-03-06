
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '40C58D56EB30C470D55E0103473A8A8E'
    
_lr_action_items = {'LEFT_BRACK':([0,8,11,16,20,25,26,29,39,40,],[8,8,8,8,8,8,8,8,8,8,]),'FALSE':([0,8,11,16,20,25,26,29,39,40,],[1,1,1,1,1,1,1,1,1,1,]),'LEFT_PAR':([2,10,],[11,20,]),'RIGHT_BRACE':([1,2,3,5,6,7,9,12,13,17,22,23,27,28,31,32,35,36,38,41,42,],[-10,-12,-13,13,-11,-6,-9,23,-1,-3,-14,-2,-5,-4,-7,-15,-18,-19,-8,-16,-17,]),'EQUALS':([7,],[16,]),'RIGHT_BRACK':([1,2,3,6,7,8,9,13,17,18,19,22,23,27,28,31,32,37,38,],[-10,-12,-13,-11,-6,17,-9,-1,-3,-20,28,-14,-2,-5,-4,-7,-15,-21,-8,]),'NUM':([0,8,11,16,20,25,26,29,39,40,],[6,6,6,6,6,6,6,6,6,6,]),'COMMA':([1,2,3,6,7,9,12,13,17,18,19,21,22,23,27,28,30,31,32,35,36,37,38,41,42,],[-10,-12,-13,-11,-6,-9,24,-1,-3,-20,29,29,-14,-2,-5,-4,29,-7,-15,-18,-19,-21,-8,-16,-17,]),'LEFT_BRACE':([0,8,11,16,20,25,26,29,39,40,],[5,5,5,5,5,5,5,5,5,5,]),'STR':([0,5,8,11,16,20,24,25,26,29,39,40,],[2,14,2,2,2,2,33,2,2,2,2,2,]),'RIGHT_PAR':([1,2,3,6,7,9,11,13,17,18,20,21,22,23,27,28,30,31,32,37,38,],[-10,-12,-13,-11,-6,-9,22,-1,-3,-20,31,32,-14,-2,-5,-4,38,-7,-15,-21,-8,]),'COLON':([14,15,33,34,],[25,26,39,40,]),'BINDINGS':([0,8,11,16,20,25,26,29,39,40,],[7,7,7,7,7,7,7,7,7,7,]),'NULL':([0,8,11,16,20,25,26,29,39,40,],[3,3,3,3,3,3,3,3,3,3,]),'TRUE':([0,8,11,16,20,25,26,29,39,40,],[9,9,9,9,9,9,9,9,9,9,]),'ID':([0,5,8,11,16,20,24,25,26,29,39,40,],[10,15,10,10,10,10,34,10,10,10,10,10,]),'$end':([1,2,3,4,6,7,9,13,17,22,23,27,28,31,32,38,],[-10,-12,-13,0,-11,-6,-9,-1,-3,-14,-2,-5,-4,-7,-15,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'elements':([8,11,20,],[19,21,30,]),'members':([5,],[12,]),'value':([0,8,11,16,20,25,26,29,39,40,],[4,18,18,27,18,35,36,37,41,42,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> value","S'",1,None,None,None),
  ('value -> LEFT_BRACE RIGHT_BRACE','value',2,'p_value','SermatParserCup.py',23),
  ('value -> LEFT_BRACE members RIGHT_BRACE','value',3,'p_value','SermatParserCup.py',24),
  ('value -> LEFT_BRACK RIGHT_BRACK','value',2,'p_value','SermatParserCup.py',25),
  ('value -> LEFT_BRACK elements RIGHT_BRACK','value',3,'p_value','SermatParserCup.py',26),
  ('value -> BINDINGS EQUALS value','value',3,'p_value','SermatParserCup.py',27),
  ('value -> BINDINGS','value',1,'p_value','SermatParserCup.py',28),
  ('value -> ID LEFT_PAR RIGHT_PAR','value',3,'p_value','SermatParserCup.py',29),
  ('value -> ID LEFT_PAR elements RIGHT_PAR','value',4,'p_value','SermatParserCup.py',30),
  ('value -> TRUE','value',1,'p_value_boolNumStrNull','SermatParserCup.py',64),
  ('value -> FALSE','value',1,'p_value_boolNumStrNull','SermatParserCup.py',65),
  ('value -> NUM','value',1,'p_value_boolNumStrNull','SermatParserCup.py',66),
  ('value -> STR','value',1,'p_value_boolNumStrNull','SermatParserCup.py',67),
  ('value -> NULL','value',1,'p_value_boolNumStrNull','SermatParserCup.py',68),
  ('value -> STR LEFT_PAR RIGHT_PAR','value',3,'p_value_str_rules','SermatParserCup.py',73),
  ('value -> STR LEFT_PAR elements RIGHT_PAR','value',4,'p_value_str_rules','SermatParserCup.py',74),
  ('members -> members COMMA STR COLON value','members',5,'p_members_mem_str_val','SermatParserCup.py',87),
  ('members -> members COMMA ID COLON value','members',5,'p_members_mem_id_val','SermatParserCup.py',94),
  ('members -> STR COLON value','members',3,'p_members_str_val','SermatParserCup.py',102),
  ('members -> ID COLON value','members',3,'p_members_id_val','SermatParserCup.py',113),
  ('elements -> value','elements',1,'p_elements','SermatParserCup.py',123),
  ('elements -> elements COMMA value','elements',3,'p_elements','SermatParserCup.py',124),
]
