
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CLOSE_BRACE CLOSE_BRACKET OPEN_BRACE OPEN_BRACKET SLASH TOKEN_OR_POS_OR_PINYINstatement : expression\n                 | statement expressionsimple_expression : TOKEN_OR_POS_OR_PINYIN SLASH TOKEN_OR_POS_OR_PINYIN\n                         | TOKEN_OR_POS_OR_PINYIN OPEN_BRACE TOKEN_OR_POS_OR_PINYIN CLOSE_BRACE SLASH TOKEN_OR_POS_OR_PINYINexpression : simple_expression\n                  | OPEN_BRACKET statement CLOSE_BRACKET TOKEN_OR_POS_OR_PINYIN'
    
_lr_action_items = {'OPEN_BRACKET':([0,1,2,3,4,6,7,11,13,16,],[4,4,-1,-5,4,-2,4,-3,-6,-4,]),'TOKEN_OR_POS_OR_PINYIN':([0,1,2,3,4,6,7,8,9,10,11,13,15,16,],[5,5,-1,-5,5,-2,5,11,12,13,-3,-6,16,-4,]),'$end':([1,2,3,6,11,13,16,],[0,-1,-5,-2,-3,-6,-4,]),'CLOSE_BRACKET':([2,3,6,7,11,13,16,],[-1,-5,-2,10,-3,-6,-4,]),'SLASH':([5,14,],[8,15,]),'OPEN_BRACE':([5,],[9,]),'CLOSE_BRACE':([12,],[14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,4,],[1,7,]),'expression':([0,1,4,7,],[2,6,2,6,]),'simple_expression':([0,1,4,7,],[3,3,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',69),
  ('statement -> statement expression','statement',2,'p_statement_expr','parser.py',70),
  ('simple_expression -> TOKEN_OR_POS_OR_PINYIN SLASH TOKEN_OR_POS_OR_PINYIN','simple_expression',3,'p_simple_expression_expr','parser.py',97),
  ('simple_expression -> TOKEN_OR_POS_OR_PINYIN OPEN_BRACE TOKEN_OR_POS_OR_PINYIN CLOSE_BRACE SLASH TOKEN_OR_POS_OR_PINYIN','simple_expression',6,'p_simple_expression_expr','parser.py',98),
  ('expression -> simple_expression','expression',1,'p_expression_binop','parser.py',115),
  ('expression -> OPEN_BRACKET statement CLOSE_BRACKET TOKEN_OR_POS_OR_PINYIN','expression',4,'p_expression_binop','parser.py',116),
]
