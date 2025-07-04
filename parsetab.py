
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN COLON COMMA DIVIDE EQ FLOAT GE GT ID IFELSE INT LBRACKET LE LPAREN LT MINUS NUMFLOAT NUMINT PLUS PRINT RBRACKET READ RPAREN SEMICOLON TIMES WHILEprogram : opt_decls opt_stmtsopt_decls : decl_lst\n| emptydecl_lst : decl SEMICOLON decl_lst\n| decldecl : type COLON id_lstid_lst : ID COMMA id_lst\n| IDtype : INT\n| FLOATstmt : ID ASSIGN expr\n| IFELSE LPAREN expresion RPAREN LBRACKET opt_stmts RBRACKET LBRACKET opt_stmts RBRACKET\n| WHILE LPAREN expresion RPAREN LBRACKET opt_stmts RBRACKET\n| PRINT expr\n| READ IDopt_stmts : stmt_lst\n| emptystmt_lst : stmt SEMICOLON stmt_lst\n| stmtexpr : expr PLUS term\n| expr MINUS term\n| termterm : term TIMES factor\n| term DIVIDE factor\n| factorfactor : LPAREN expr RPARENfactor : IDfactor : NUMINTfactor : NUMFLOATexpresion : expr LT expr\n| expr LE expr\n| expr GT expr\n| expr GE expr\n| expr EQ exprempty : '
    
_lr_action_items = {'ID':([0,2,3,4,5,16,17,19,20,21,22,23,27,32,33,34,40,41,42,43,45,47,48,49,50,51,58,59,65,70,],[-35,13,-2,-3,-5,28,31,34,13,28,28,28,28,-4,-6,-8,28,28,28,28,34,28,28,28,28,28,-7,13,13,13,]),'IFELSE':([0,2,3,4,5,20,32,33,34,58,59,65,70,],[-35,14,-2,-3,-5,14,-4,-6,-8,-7,14,14,14,]),'WHILE':([0,2,3,4,5,20,32,33,34,58,59,65,70,],[-35,15,-2,-3,-5,15,-4,-6,-8,-7,15,15,15,]),'PRINT':([0,2,3,4,5,20,32,33,34,58,59,65,70,],[-35,16,-2,-3,-5,16,-4,-6,-8,-7,16,16,16,]),'READ':([0,2,3,4,5,20,32,33,34,58,59,65,70,],[-35,17,-2,-3,-5,17,-4,-6,-8,-7,17,17,17,]),'$end':([0,1,2,3,4,5,9,10,11,12,24,25,26,28,29,30,31,32,33,34,35,36,53,54,55,56,57,58,69,72,],[-35,0,-35,-2,-3,-5,-1,-16,-17,-19,-14,-22,-25,-27,-28,-29,-15,-4,-6,-8,-18,-11,-20,-21,-23,-24,-26,-7,-13,-12,]),'INT':([0,18,],[7,7,]),'FLOAT':([0,18,],[8,8,]),'SEMICOLON':([5,12,24,25,26,28,29,30,31,33,34,36,53,54,55,56,57,58,69,72,],[18,20,-14,-22,-25,-27,-28,-29,-15,-6,-8,-11,-20,-21,-23,-24,-26,-7,-13,-12,]),'COLON':([6,7,8,],[19,-9,-10,]),'RBRACKET':([10,11,12,24,25,26,28,29,30,31,35,36,53,54,55,56,57,59,65,66,67,69,70,71,72,],[-16,-17,-19,-14,-22,-25,-27,-28,-29,-15,-18,-11,-20,-21,-23,-24,-26,-35,-35,68,69,-13,-35,72,-12,]),'ASSIGN':([13,],[21,]),'LPAREN':([14,15,16,21,22,23,27,40,41,42,43,47,48,49,50,51,],[22,23,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'NUMINT':([16,21,22,23,27,40,41,42,43,47,48,49,50,51,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'NUMFLOAT':([16,21,22,23,27,40,41,42,43,47,48,49,50,51,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'PLUS':([24,25,26,28,29,30,36,38,44,53,54,55,56,57,60,61,62,63,64,],[40,-22,-25,-27,-28,-29,40,40,40,-20,-21,-23,-24,-26,40,40,40,40,40,]),'MINUS':([24,25,26,28,29,30,36,38,44,53,54,55,56,57,60,61,62,63,64,],[41,-22,-25,-27,-28,-29,41,41,41,-20,-21,-23,-24,-26,41,41,41,41,41,]),'LT':([25,26,28,29,30,38,53,54,55,56,57,],[-22,-25,-27,-28,-29,47,-20,-21,-23,-24,-26,]),'LE':([25,26,28,29,30,38,53,54,55,56,57,],[-22,-25,-27,-28,-29,48,-20,-21,-23,-24,-26,]),'GT':([25,26,28,29,30,38,53,54,55,56,57,],[-22,-25,-27,-28,-29,49,-20,-21,-23,-24,-26,]),'GE':([25,26,28,29,30,38,53,54,55,56,57,],[-22,-25,-27,-28,-29,50,-20,-21,-23,-24,-26,]),'EQ':([25,26,28,29,30,38,53,54,55,56,57,],[-22,-25,-27,-28,-29,51,-20,-21,-23,-24,-26,]),'RPAREN':([25,26,28,29,30,37,39,44,53,54,55,56,57,60,61,62,63,64,],[-22,-25,-27,-28,-29,46,52,57,-20,-21,-23,-24,-26,-30,-31,-32,-33,-34,]),'TIMES':([25,26,28,29,30,53,54,55,56,57,],[42,-25,-27,-28,-29,42,42,-23,-24,-26,]),'DIVIDE':([25,26,28,29,30,53,54,55,56,57,],[43,-25,-27,-28,-29,43,43,-23,-24,-26,]),'COMMA':([34,],[45,]),'LBRACKET':([46,52,68,],[59,65,70,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'opt_decls':([0,],[2,]),'decl_lst':([0,18,],[3,32,]),'empty':([0,2,59,65,70,],[4,11,11,11,11,]),'decl':([0,18,],[5,5,]),'type':([0,18,],[6,6,]),'opt_stmts':([2,59,65,70,],[9,66,67,71,]),'stmt_lst':([2,20,59,65,70,],[10,35,10,10,10,]),'stmt':([2,20,59,65,70,],[12,12,12,12,12,]),'expr':([16,21,22,23,27,47,48,49,50,51,],[24,36,38,38,44,60,61,62,63,64,]),'term':([16,21,22,23,27,40,41,47,48,49,50,51,],[25,25,25,25,25,53,54,25,25,25,25,25,]),'factor':([16,21,22,23,27,40,41,42,43,47,48,49,50,51,],[26,26,26,26,26,26,26,55,56,26,26,26,26,26,]),'id_lst':([19,45,],[33,58,]),'expresion':([22,23,],[37,39,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> opt_decls opt_stmts','program',2,'p_program','SitProb.py',115),
  ('opt_decls -> decl_lst','opt_decls',1,'p_opt_decls','SitProb.py',119),
  ('opt_decls -> empty','opt_decls',1,'p_opt_decls','SitProb.py',120),
  ('decl_lst -> decl SEMICOLON decl_lst','decl_lst',3,'p_decl_lst','SitProb.py',126),
  ('decl_lst -> decl','decl_lst',1,'p_decl_lst','SitProb.py',127),
  ('decl -> type COLON id_lst','decl',3,'p_decl','SitProb.py',131),
  ('id_lst -> ID COMMA id_lst','id_lst',3,'p_id_lst','SitProb.py',141),
  ('id_lst -> ID','id_lst',1,'p_id_lst','SitProb.py',142),
  ('type -> INT','type',1,'p_type','SitProb.py',150),
  ('type -> FLOAT','type',1,'p_type','SitProb.py',151),
  ('stmt -> ID ASSIGN expr','stmt',3,'p_stmt','SitProb.py',158),
  ('stmt -> IFELSE LPAREN expresion RPAREN LBRACKET opt_stmts RBRACKET LBRACKET opt_stmts RBRACKET','stmt',10,'p_stmt','SitProb.py',159),
  ('stmt -> WHILE LPAREN expresion RPAREN LBRACKET opt_stmts RBRACKET','stmt',7,'p_stmt','SitProb.py',160),
  ('stmt -> PRINT expr','stmt',2,'p_stmt','SitProb.py',161),
  ('stmt -> READ ID','stmt',2,'p_stmt','SitProb.py',162),
  ('opt_stmts -> stmt_lst','opt_stmts',1,'p_opt_stmts','SitProb.py',192),
  ('opt_stmts -> empty','opt_stmts',1,'p_opt_stmts','SitProb.py',193),
  ('stmt_lst -> stmt SEMICOLON stmt_lst','stmt_lst',3,'p_stmt_lst','SitProb.py',197),
  ('stmt_lst -> stmt','stmt_lst',1,'p_stmt_lst','SitProb.py',198),
  ('expr -> expr PLUS term','expr',3,'p_expr','SitProb.py',208),
  ('expr -> expr MINUS term','expr',3,'p_expr','SitProb.py',209),
  ('expr -> term','expr',1,'p_expr','SitProb.py',210),
  ('term -> term TIMES factor','term',3,'p_term','SitProb.py',220),
  ('term -> term DIVIDE factor','term',3,'p_term','SitProb.py',221),
  ('term -> factor','term',1,'p_term','SitProb.py',222),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor_expr','SitProb.py',235),
  ('factor -> ID','factor',1,'p_factor_id','SitProb.py',241),
  ('factor -> NUMINT','factor',1,'p_factor_numint','SitProb.py',249),
  ('factor -> NUMFLOAT','factor',1,'p_factor_numfloat','SitProb.py',254),
  ('expresion -> expr LT expr','expresion',3,'p_expresion','SitProb.py',260),
  ('expresion -> expr LE expr','expresion',3,'p_expresion','SitProb.py',261),
  ('expresion -> expr GT expr','expresion',3,'p_expresion','SitProb.py',262),
  ('expresion -> expr GE expr','expresion',3,'p_expresion','SitProb.py',263),
  ('expresion -> expr EQ expr','expresion',3,'p_expresion','SitProb.py',264),
  ('empty -> <empty>','empty',0,'p_empty','SitProb.py',273),
]
