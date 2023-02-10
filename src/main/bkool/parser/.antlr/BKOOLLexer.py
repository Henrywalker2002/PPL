# Generated from d:\project\PPL\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("w\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\6")
        buf.write("\fN\n\f\r\f\16\fO\3\r\6\rS\n\r\r\r\16\rT\3\16\6\16X\n")
        buf.write("\16\r\16\16\16Y\3\16\3\16\6\16^\n\16\r\16\16\16_\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\6\23k\n\23\r")
        buf.write("\23\16\23l\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\2\2\27\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27")
        buf.write("\3\2\5\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2{\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\3-\3\2\2\2\5\61\3\2")
        buf.write("\2\2\7\67\3\2\2\2\t>\3\2\2\2\13@\3\2\2\2\rB\3\2\2\2\17")
        buf.write("D\3\2\2\2\21F\3\2\2\2\23H\3\2\2\2\25J\3\2\2\2\27M\3\2")
        buf.write("\2\2\31R\3\2\2\2\33W\3\2\2\2\35a\3\2\2\2\37c\3\2\2\2!")
        buf.write("e\3\2\2\2#g\3\2\2\2%j\3\2\2\2\'p\3\2\2\2)s\3\2\2\2+u\3")
        buf.write("\2\2\2-.\7k\2\2./\7p\2\2/\60\7v\2\2\60\4\3\2\2\2\61\62")
        buf.write("\7h\2\2\62\63\7n\2\2\63\64\7q\2\2\64\65\7c\2\2\65\66\7")
        buf.write("v\2\2\66\6\3\2\2\2\678\7t\2\289\7g\2\29:\7v\2\2:;\7w\2")
        buf.write("\2;<\7t\2\2<=\7p\2\2=\b\3\2\2\2>?\7-\2\2?\n\3\2\2\2@A")
        buf.write("\7/\2\2A\f\3\2\2\2BC\7\61\2\2C\16\3\2\2\2DE\7,\2\2E\20")
        buf.write("\3\2\2\2FG\7?\2\2G\22\3\2\2\2HI\7=\2\2I\24\3\2\2\2JK\7")
        buf.write(".\2\2K\26\3\2\2\2LN\t\2\2\2ML\3\2\2\2NO\3\2\2\2OM\3\2")
        buf.write("\2\2OP\3\2\2\2P\30\3\2\2\2QS\t\3\2\2RQ\3\2\2\2ST\3\2\2")
        buf.write("\2TR\3\2\2\2TU\3\2\2\2U\32\3\2\2\2VX\t\3\2\2WV\3\2\2\2")
        buf.write("XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[]\7\60\2\2\\")
        buf.write("^\t\3\2\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`\34")
        buf.write("\3\2\2\2ab\7*\2\2b\36\3\2\2\2cd\7+\2\2d \3\2\2\2ef\7}")
        buf.write("\2\2f\"\3\2\2\2gh\7\177\2\2h$\3\2\2\2ik\t\4\2\2ji\3\2")
        buf.write("\2\2kl\3\2\2\2lj\3\2\2\2lm\3\2\2\2mn\3\2\2\2no\b\23\2")
        buf.write("\2o&\3\2\2\2pq\13\2\2\2qr\b\24\3\2r(\3\2\2\2st\13\2\2")
        buf.write("\2t*\3\2\2\2uv\13\2\2\2v,\3\2\2\2\b\2OTY_l\4\b\2\2\3\24")
        buf.write("\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    EQUAL = 8
    SEMI = 9
    COMMA = 10
    ID = 11
    INTLIT = 12
    FLOATLIT = 13
    LB = 14
    RB = 15
    LP = 16
    RP = 17
    WS = 18
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'return'", "'+'", "'-'", "'/'", "'*'", 
            "'='", "';'", "','", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "EQUAL", "SEMI", "COMMA", "ID", "INTLIT", "FLOATLIT", "LB", 
            "RB", "LP", "RP", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "EQUAL", "SEMI", "COMMA", "ID", "INTLIT", "FLOATLIT", 
                  "LB", "RB", "LP", "RP", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[18] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


