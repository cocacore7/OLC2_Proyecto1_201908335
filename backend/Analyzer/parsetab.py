
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDDleftORRleftNOTTleftIGUALDISTINTOleftMAYORMENORMAYORIGUALMENORIGUALleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOleftPOTENCIAANDD CHAR COMA CORDER CORIZQ DECIMAL DISTINTO DIVISION DOSPT ENTERO FALSO FUNCTION ID IGUAL IGUALIGUAL LLAVEDER LLAVEIZQ MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MODULO MULTIPLICACION NOTT NULO ORR PARDER PARIZQ POTENCIA PRINT PRINTLN PTCOMA RBOOL RCHAR RELSE RFLOAT RIF RINT RSTRING RWHILE STRING VERDADEROinitial : instructionsinstructions : instructions instruction\n                    | instruction\n    instruction  : p_print \n                    | p_println\n                    | declaration\n                    | function\n                    | callFuncSt\n                    | whileSt\n                    | ifSt\n    empty :p_print : PRINT PARIZQ exp PARDER PTCOMA\n    p_println : PRINTLN PARIZQ exp PARDER PTCOMA\n    declaration  : ID IGUAL exp PTCOMA\n                    | ID IGUAL exp DOSPT DOSPT typeDef PTCOMA\n    function : FUNCTION ID parametersFunc DOSPT typeDef block\n    parametersFunc   : PARIZQ parameters PARDER\n                        | PARIZQ PARDER\n    callFuncSt   : ID parametersCallFunc PTCOMA\n    parameters   : parameters COMA parameter\n                    | parameter\n    parameter    : ID DOSPT typeDef\n    parametersCallFunc   : PARIZQ listValues PARDER\n                            | PARIZQ PARDER\n    block    : LLAVEIZQ instructions LLAVEDER\n                | LLAVEIZQ LLAVEDER\n    whileSt  : RWHILE PARIZQ exp PARDER block \n     ifSt  : RIF PARIZQ exp PARDER block elseSt\n    elseSt   : RELSE block\n                | ifSt\n    decArray : CORIZQ CORDER\n                | empty \n    listValues   : listValues COMA exp\n                    | exp\n    typeDef  : RINT\n                | RFLOAT\n                | RSTRING\n                | RCHAR\n                | RBOOL\n    exp  : exp MAS exp\n            | exp MENOS exp\n            | exp MULTIPLICACION exp\n            | exp DIVISION exp\n            | exp POTENCIA exp\n            | exp MODULO exp\n            | exp MAYOR exp\n            | exp MENOR exp\n            | exp IGUALIGUAL exp\n            | exp MAYORIGUAL exp\n            | exp MENORIGUAL exp\n            | exp DISTINTO exp\n            | exp ANDD exp\n            | exp ORR exp\n            | NOTT exp\n    exp : PARIZQ exp PARDERexp  : ENTERO\n    exp  : DECIMAL\n    exp  : STRING\n    exp  : CHAR\n    exp  : VERDADERO\n    exp  : FALSO\n    exp  : NULO\n    exp  : ID\n            | ID listArray\n    exp : CORIZQ listValues CORDERlistArray    : listArray  CORIZQ exp CORDER \n                    | CORIZQ exp CORDER\n    '
    
_lr_action_items = {'PRINT':([0,2,3,4,5,6,7,8,9,10,17,40,69,81,99,111,112,117,120,121,122,124,126,127,128,],[11,11,-3,-4,-5,-6,-7,-8,-9,-10,-2,-19,-14,-12,-13,-27,11,-16,11,-26,-28,-30,-15,-25,-29,]),'PRINTLN':([0,2,3,4,5,6,7,8,9,10,17,40,69,81,99,111,112,117,120,121,122,124,126,127,128,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,-2,-19,-14,-12,-13,-27,12,-16,12,-26,-28,-30,-15,-25,-29,]),'ID':([0,2,3,4,5,6,7,8,9,10,14,17,18,19,20,22,24,25,26,28,37,40,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,69,72,81,96,99,109,111,112,117,120,121,122,124,126,127,128,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,23,-2,36,36,36,36,36,36,36,36,36,-19,77,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-14,36,-12,36,-13,77,-27,13,-16,13,-26,-28,-30,-15,-25,-29,]),'FUNCTION':([0,2,3,4,5,6,7,8,9,10,17,40,69,81,99,111,112,117,120,121,122,124,126,127,128,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-2,-19,-14,-12,-13,-27,14,-16,14,-26,-28,-30,-15,-25,-29,]),'RWHILE':([0,2,3,4,5,6,7,8,9,10,17,40,69,81,99,111,112,117,120,121,122,124,126,127,128,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-2,-19,-14,-12,-13,-27,15,-16,15,-26,-28,-30,-15,-25,-29,]),'RIF':([0,2,3,4,5,6,7,8,9,10,17,40,69,81,99,111,112,113,117,120,121,122,124,126,127,128,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-2,-19,-14,-12,-13,-27,16,16,-16,16,-26,-28,-30,-15,-25,-29,]),'$end':([1,2,3,4,5,6,7,8,9,10,17,40,69,81,99,111,117,121,122,124,126,127,128,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-19,-14,-12,-13,-27,-16,-26,-28,-30,-15,-25,-29,]),'LLAVEDER':([3,4,5,6,7,8,9,10,17,40,69,81,99,111,112,117,120,121,122,124,126,127,128,],[-3,-4,-5,-6,-7,-8,-9,-10,-2,-19,-14,-12,-13,-27,121,-16,127,-26,-28,-30,-15,-25,-29,]),'PARIZQ':([11,12,13,15,16,18,19,20,22,23,24,25,26,28,37,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,72,96,],[18,19,22,24,25,26,26,26,26,45,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'IGUAL':([13,],[20,]),'NOTT':([18,19,20,22,24,25,26,28,37,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,72,96,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'ENTERO':([18,19,20,22,24,25,26,28,37,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,72,96,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'DECIMAL':([18,19,20,22,24,25,26,28,37,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,72,96,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'STRING':([18,19,20,22,24,25,26,28,37,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,72,96,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'CHAR':([18,19,20,22,24,25,26,28,37,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,72,96,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'VERDADERO':([18,19,20,22,24,25,26,28,37,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,72,96,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'FALSO':([18,19,20,22,24,25,26,28,37,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,72,96,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'NULO':([18,19,20,22,24,25,26,28,37,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,72,96,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'CORIZQ':([18,19,20,22,24,25,26,28,36,37,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,72,96,115,125,],[37,37,37,37,37,37,37,37,66,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,96,37,37,37,-67,-66,]),'PTCOMA':([21,29,30,31,32,33,34,35,36,39,42,49,64,65,68,71,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,103,104,105,106,107,115,116,125,],[40,-56,-57,-58,-59,-60,-61,-62,-63,69,-24,81,-54,-64,99,-23,-55,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-65,-35,-36,-37,-38,-39,-67,126,-66,]),'PARDER':([22,27,29,30,31,32,33,34,35,36,38,41,43,45,46,47,48,64,65,74,76,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,101,103,104,105,106,107,115,118,119,125,],[42,49,-56,-57,-58,-59,-60,-61,-62,-63,68,71,-34,75,78,79,80,-54,-64,108,-21,-55,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-65,-33,-35,-36,-37,-38,-39,-67,-20,-22,-66,]),'MAS':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[50,-56,-57,-58,-59,-60,-61,-62,-63,50,50,50,50,50,50,50,-64,-55,-40,-41,-42,-43,-44,-45,50,50,50,50,50,50,50,50,50,-65,50,50,-67,-66,]),'MENOS':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[51,-56,-57,-58,-59,-60,-61,-62,-63,51,51,51,51,51,51,51,-64,-55,-40,-41,-42,-43,-44,-45,51,51,51,51,51,51,51,51,51,-65,51,51,-67,-66,]),'MULTIPLICACION':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[52,-56,-57,-58,-59,-60,-61,-62,-63,52,52,52,52,52,52,52,-64,-55,52,52,-42,-43,-44,-45,52,52,52,52,52,52,52,52,52,-65,52,52,-67,-66,]),'DIVISION':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[53,-56,-57,-58,-59,-60,-61,-62,-63,53,53,53,53,53,53,53,-64,-55,53,53,-42,-43,-44,-45,53,53,53,53,53,53,53,53,53,-65,53,53,-67,-66,]),'POTENCIA':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[54,-56,-57,-58,-59,-60,-61,-62,-63,54,54,54,54,54,54,54,-64,-55,54,54,54,54,-44,54,54,54,54,54,54,54,54,54,54,-65,54,54,-67,-66,]),'MODULO':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[55,-56,-57,-58,-59,-60,-61,-62,-63,55,55,55,55,55,55,55,-64,-55,55,55,-42,-43,-44,-45,55,55,55,55,55,55,55,55,55,-65,55,55,-67,-66,]),'MAYOR':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[56,-56,-57,-58,-59,-60,-61,-62,-63,56,56,56,56,56,56,56,-64,-55,-40,-41,-42,-43,-44,-45,-46,-47,56,-49,-50,56,56,56,56,-65,56,56,-67,-66,]),'MENOR':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[57,-56,-57,-58,-59,-60,-61,-62,-63,57,57,57,57,57,57,57,-64,-55,-40,-41,-42,-43,-44,-45,-46,-47,57,-49,-50,57,57,57,57,-65,57,57,-67,-66,]),'IGUALIGUAL':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[58,-56,-57,-58,-59,-60,-61,-62,-63,58,58,58,58,58,58,-54,-64,-55,-40,-41,-42,-43,-44,-45,-46,-47,58,-49,-50,-51,-52,-53,58,-65,58,58,-67,-66,]),'MAYORIGUAL':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[59,-56,-57,-58,-59,-60,-61,-62,-63,59,59,59,59,59,59,59,-64,-55,-40,-41,-42,-43,-44,-45,-46,-47,59,-49,-50,59,59,59,59,-65,59,59,-67,-66,]),'MENORIGUAL':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[60,-56,-57,-58,-59,-60,-61,-62,-63,60,60,60,60,60,60,60,-64,-55,-40,-41,-42,-43,-44,-45,-46,-47,60,-49,-50,60,60,60,60,-65,60,60,-67,-66,]),'DISTINTO':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[61,-56,-57,-58,-59,-60,-61,-62,-63,61,61,61,61,61,61,61,-64,-55,-40,-41,-42,-43,-44,-45,-46,-47,61,-49,-50,-51,61,61,61,-65,61,61,-67,-66,]),'ANDD':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[62,-56,-57,-58,-59,-60,-61,-62,-63,62,62,62,62,62,62,-54,-64,-55,-40,-41,-42,-43,-44,-45,-46,-47,62,-49,-50,-51,-52,-53,62,-65,62,62,-67,-66,]),'ORR':([27,29,30,31,32,33,34,35,36,38,39,43,46,47,48,64,65,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[63,-56,-57,-58,-59,-60,-61,-62,-63,63,63,63,63,63,63,-54,-64,-55,-40,-41,-42,-43,-44,-45,-46,-47,63,-49,-50,-51,63,-53,63,-65,63,63,-67,-66,]),'DOSPT':([29,30,31,32,33,34,35,36,39,44,64,65,70,75,77,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,108,115,125,],[-56,-57,-58,-59,-60,-61,-62,-63,70,73,-54,-64,100,-18,110,-55,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-65,-17,-67,-66,]),'COMA':([29,30,31,32,33,34,35,36,41,43,64,65,67,74,76,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,101,103,104,105,106,107,115,118,119,125,],[-56,-57,-58,-59,-60,-61,-62,-63,72,-34,-54,-64,72,109,-21,-55,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-65,-33,-35,-36,-37,-38,-39,-67,-20,-22,-66,]),'CORDER':([29,30,31,32,33,34,35,36,43,64,65,67,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,114,115,125,],[-56,-57,-58,-59,-60,-61,-62,-63,-34,-54,-64,98,-55,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,115,-65,-33,125,-67,-66,]),'RINT':([73,100,110,],[103,103,103,]),'RFLOAT':([73,100,110,],[104,104,104,]),'RSTRING':([73,100,110,],[105,105,105,]),'RCHAR':([73,100,110,],[106,106,106,]),'RBOOL':([73,100,110,],[107,107,107,]),'LLAVEIZQ':([78,79,102,103,104,105,106,107,123,],[112,112,112,-35,-36,-37,-38,-39,112,]),'RELSE':([113,121,127,],[123,-26,-25,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'initial':([0,],[1,]),'instructions':([0,112,],[2,120,]),'instruction':([0,2,112,120,],[3,17,3,17,]),'p_print':([0,2,112,120,],[4,4,4,4,]),'p_println':([0,2,112,120,],[5,5,5,5,]),'declaration':([0,2,112,120,],[6,6,6,6,]),'function':([0,2,112,120,],[7,7,7,7,]),'callFuncSt':([0,2,112,120,],[8,8,8,8,]),'whileSt':([0,2,112,120,],[9,9,9,9,]),'ifSt':([0,2,112,113,120,],[10,10,10,124,10,]),'parametersCallFunc':([13,],[21,]),'exp':([18,19,20,22,24,25,26,28,37,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,72,96,],[27,38,39,43,46,47,48,64,43,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,101,114,]),'listValues':([22,37,],[41,67,]),'parametersFunc':([23,],[44,]),'listArray':([36,],[65,]),'parameters':([45,],[74,]),'parameter':([45,109,],[76,118,]),'typeDef':([73,100,110,],[102,116,119,]),'block':([78,79,102,123,],[111,113,117,128,]),'elseSt':([113,],[122,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> initial","S'",1,None,None,None),
  ('initial -> instructions','initial',1,'p_initial','Gramatica.py',182),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','Gramatica.py',189),
  ('instructions -> instruction','instructions',1,'p_instructions','Gramatica.py',190),
  ('instruction -> p_print','instruction',1,'p_instruction','Gramatica.py',200),
  ('instruction -> p_println','instruction',1,'p_instruction','Gramatica.py',201),
  ('instruction -> declaration','instruction',1,'p_instruction','Gramatica.py',202),
  ('instruction -> function','instruction',1,'p_instruction','Gramatica.py',203),
  ('instruction -> callFuncSt','instruction',1,'p_instruction','Gramatica.py',204),
  ('instruction -> whileSt','instruction',1,'p_instruction','Gramatica.py',205),
  ('instruction -> ifSt','instruction',1,'p_instruction','Gramatica.py',206),
  ('empty -> <empty>','empty',0,'p_empty','Gramatica.py',211),
  ('p_print -> PRINT PARIZQ exp PARDER PTCOMA','p_print',5,'p_print','Gramatica.py',216),
  ('p_println -> PRINTLN PARIZQ exp PARDER PTCOMA','p_println',5,'p_println','Gramatica.py',221),
  ('declaration -> ID IGUAL exp PTCOMA','declaration',4,'p_declaration','Gramatica.py',227),
  ('declaration -> ID IGUAL exp DOSPT DOSPT typeDef PTCOMA','declaration',7,'p_declaration','Gramatica.py',228),
  ('function -> FUNCTION ID parametersFunc DOSPT typeDef block','function',6,'p_function','Gramatica.py',237),
  ('parametersFunc -> PARIZQ parameters PARDER','parametersFunc',3,'p_parametersFunc','Gramatica.py',242),
  ('parametersFunc -> PARIZQ PARDER','parametersFunc',2,'p_parametersFunc','Gramatica.py',243),
  ('callFuncSt -> ID parametersCallFunc PTCOMA','callFuncSt',3,'p_callFuncSt','Gramatica.py',251),
  ('parameters -> parameters COMA parameter','parameters',3,'p_parameters','Gramatica.py',257),
  ('parameters -> parameter','parameters',1,'p_parameters','Gramatica.py',258),
  ('parameter -> ID DOSPT typeDef','parameter',3,'p_parameter','Gramatica.py',267),
  ('parametersCallFunc -> PARIZQ listValues PARDER','parametersCallFunc',3,'p_parametersCallFunc','Gramatica.py',272),
  ('parametersCallFunc -> PARIZQ PARDER','parametersCallFunc',2,'p_parametersCallFunc','Gramatica.py',273),
  ('block -> LLAVEIZQ instructions LLAVEDER','block',3,'p_block','Gramatica.py',282),
  ('block -> LLAVEIZQ LLAVEDER','block',2,'p_block','Gramatica.py',283),
  ('whileSt -> RWHILE PARIZQ exp PARDER block','whileSt',5,'p_whileSt','Gramatica.py',292),
  ('ifSt -> RIF PARIZQ exp PARDER block elseSt','ifSt',6,'p_ifSt','Gramatica.py',298),
  ('elseSt -> RELSE block','elseSt',2,'p_elseSt','Gramatica.py',303),
  ('elseSt -> ifSt','elseSt',1,'p_elseSt','Gramatica.py',304),
  ('decArray -> CORIZQ CORDER','decArray',2,'p_decArray','Gramatica.py',313),
  ('decArray -> empty','decArray',1,'p_decArray','Gramatica.py',314),
  ('listValues -> listValues COMA exp','listValues',3,'p_listValues','Gramatica.py',324),
  ('listValues -> exp','listValues',1,'p_listValues','Gramatica.py',325),
  ('typeDef -> RINT','typeDef',1,'p_typeDef','Gramatica.py',334),
  ('typeDef -> RFLOAT','typeDef',1,'p_typeDef','Gramatica.py',335),
  ('typeDef -> RSTRING','typeDef',1,'p_typeDef','Gramatica.py',336),
  ('typeDef -> RCHAR','typeDef',1,'p_typeDef','Gramatica.py',337),
  ('typeDef -> RBOOL','typeDef',1,'p_typeDef','Gramatica.py',338),
  ('exp -> exp MAS exp','exp',3,'p_exp_aritmetica','Gramatica.py',348),
  ('exp -> exp MENOS exp','exp',3,'p_exp_aritmetica','Gramatica.py',349),
  ('exp -> exp MULTIPLICACION exp','exp',3,'p_exp_aritmetica','Gramatica.py',350),
  ('exp -> exp DIVISION exp','exp',3,'p_exp_aritmetica','Gramatica.py',351),
  ('exp -> exp POTENCIA exp','exp',3,'p_exp_aritmetica','Gramatica.py',352),
  ('exp -> exp MODULO exp','exp',3,'p_exp_aritmetica','Gramatica.py',353),
  ('exp -> exp MAYOR exp','exp',3,'p_exp_aritmetica','Gramatica.py',354),
  ('exp -> exp MENOR exp','exp',3,'p_exp_aritmetica','Gramatica.py',355),
  ('exp -> exp IGUALIGUAL exp','exp',3,'p_exp_aritmetica','Gramatica.py',356),
  ('exp -> exp MAYORIGUAL exp','exp',3,'p_exp_aritmetica','Gramatica.py',357),
  ('exp -> exp MENORIGUAL exp','exp',3,'p_exp_aritmetica','Gramatica.py',358),
  ('exp -> exp DISTINTO exp','exp',3,'p_exp_aritmetica','Gramatica.py',359),
  ('exp -> exp ANDD exp','exp',3,'p_exp_aritmetica','Gramatica.py',360),
  ('exp -> exp ORR exp','exp',3,'p_exp_aritmetica','Gramatica.py',361),
  ('exp -> NOTT exp','exp',2,'p_exp_aritmetica','Gramatica.py',362),
  ('exp -> PARIZQ exp PARDER','exp',3,'p_exp_agrupacion','Gramatica.py',398),
  ('exp -> ENTERO','exp',1,'p_exp_valor_entero','Gramatica.py',402),
  ('exp -> DECIMAL','exp',1,'p_exp_valor_decimal','Gramatica.py',407),
  ('exp -> STRING','exp',1,'p_exp_valor_string','Gramatica.py',412),
  ('exp -> CHAR','exp',1,'p_exp_valor_char','Gramatica.py',417),
  ('exp -> VERDADERO','exp',1,'p_exp_valor_verdadero','Gramatica.py',422),
  ('exp -> FALSO','exp',1,'p_exp_valor_falso','Gramatica.py',427),
  ('exp -> NULO','exp',1,'p_exp_valor_nulo','Gramatica.py',432),
  ('exp -> ID','exp',1,'p_exp_variable','Gramatica.py',437),
  ('exp -> ID listArray','exp',2,'p_exp_variable','Gramatica.py',438),
  ('exp -> CORIZQ listValues CORDER','exp',3,'p_exp_array','Gramatica.py',446),
  ('listArray -> listArray CORIZQ exp CORDER','listArray',4,'p_list_array','Gramatica.py',450),
  ('listArray -> CORIZQ exp CORDER','listArray',3,'p_list_array','Gramatica.py',451),
]
