# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0168\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+")
        buf.write("\7+\u010d\n+\f+\16+\u0110\13+\3,\6,\u0113\n,\r,\16,\u0114")
        buf.write("\3-\3-\3-\5-\u011a\n-\5-\u011c\n-\3-\3-\5-\u0120\n-\3")
        buf.write("-\5-\u0123\n-\3.\3.\3.\3.\3.\3.\7.\u012b\n.\f.\16.\u012e")
        buf.write("\13.\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\60\7\60\u0139\n\60")
        buf.write("\f\60\16\60\u013c\13\60\3\60\3\60\3\61\6\61\u0141\n\61")
        buf.write("\r\61\16\61\u0142\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\7\63\u0150\n\63\f\63\16\63\u0153\13")
        buf.write("\63\3\63\5\63\u0156\n\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\7\64\u0160\n\64\f\64\16\64\u0163\13\64\3\64")
        buf.write("\3\64\3\64\3\64\2\2\65\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W\2Y-[.]/_\60a\61c\62e\63")
        buf.write("g\64\3\2\f\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\5\2\f\f$$^^\t\2))^^ddhhppttvv\3\2\f\f\5\2\n\13")
        buf.write("\16\17\"\"\3\3\f\f\2\u0177\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2Y\3\2\2\2\2[")
        buf.write("\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2")
        buf.write("e\3\2\2\2\2g\3\2\2\2\3i\3\2\2\2\5n\3\2\2\2\7t\3\2\2\2")
        buf.write("\t{\3\2\2\2\13\u0080\3\2\2\2\r\u0087\3\2\2\2\17\u008e")
        buf.write("\3\2\2\2\21\u0092\3\2\2\2\23\u009a\3\2\2\2\25\u009f\3")
        buf.write("\2\2\2\27\u00a3\3\2\2\2\31\u00a9\3\2\2\2\33\u00ac\3\2")
        buf.write("\2\2\35\u00b2\3\2\2\2\37\u00bb\3\2\2\2!\u00be\3\2\2\2")
        buf.write("#\u00c3\3\2\2\2%\u00c8\3\2\2\2\'\u00ce\3\2\2\2)\u00d2")
        buf.write("\3\2\2\2+\u00d6\3\2\2\2-\u00da\3\2\2\2/\u00dd\3\2\2\2")
        buf.write("\61\u00df\3\2\2\2\63\u00e1\3\2\2\2\65\u00e3\3\2\2\2\67")
        buf.write("\u00e5\3\2\2\29\u00e7\3\2\2\2;\u00e9\3\2\2\2=\u00ec\3")
        buf.write("\2\2\2?\u00ef\3\2\2\2A\u00f1\3\2\2\2C\u00f4\3\2\2\2E\u00f6")
        buf.write("\3\2\2\2G\u00f9\3\2\2\2I\u00fd\3\2\2\2K\u0100\3\2\2\2")
        buf.write("M\u0102\3\2\2\2O\u0104\3\2\2\2Q\u0106\3\2\2\2S\u0108\3")
        buf.write("\2\2\2U\u010a\3\2\2\2W\u0112\3\2\2\2Y\u0116\3\2\2\2[\u0124")
        buf.write("\3\2\2\2]\u0132\3\2\2\2_\u0134\3\2\2\2a\u0140\3\2\2\2")
        buf.write("c\u0146\3\2\2\2e\u0149\3\2\2\2g\u0159\3\2\2\2ij\7v\2\2")
        buf.write("jk\7t\2\2kl\7w\2\2lm\7g\2\2m\4\3\2\2\2no\7h\2\2op\7c\2")
        buf.write("\2pq\7n\2\2qr\7u\2\2rs\7g\2\2s\6\3\2\2\2tu\7p\2\2uv\7")
        buf.write("w\2\2vw\7o\2\2wx\7d\2\2xy\7g\2\2yz\7t\2\2z\b\3\2\2\2{")
        buf.write("|\7d\2\2|}\7q\2\2}~\7q\2\2~\177\7n\2\2\177\n\3\2\2\2\u0080")
        buf.write("\u0081\7u\2\2\u0081\u0082\7v\2\2\u0082\u0083\7t\2\2\u0083")
        buf.write("\u0084\7k\2\2\u0084\u0085\7p\2\2\u0085\u0086\7i\2\2\u0086")
        buf.write("\f\3\2\2\2\u0087\u0088\7t\2\2\u0088\u0089\7g\2\2\u0089")
        buf.write("\u008a\7v\2\2\u008a\u008b\7w\2\2\u008b\u008c\7t\2\2\u008c")
        buf.write("\u008d\7p\2\2\u008d\16\3\2\2\2\u008e\u008f\7x\2\2\u008f")
        buf.write("\u0090\7c\2\2\u0090\u0091\7t\2\2\u0091\20\3\2\2\2\u0092")
        buf.write("\u0093\7f\2\2\u0093\u0094\7{\2\2\u0094\u0095\7p\2\2\u0095")
        buf.write("\u0096\7c\2\2\u0096\u0097\7o\2\2\u0097\u0098\7k\2\2\u0098")
        buf.write("\u0099\7e\2\2\u0099\22\3\2\2\2\u009a\u009b\7h\2\2\u009b")
        buf.write("\u009c\7w\2\2\u009c\u009d\7p\2\2\u009d\u009e\7e\2\2\u009e")
        buf.write("\24\3\2\2\2\u009f\u00a0\7h\2\2\u00a0\u00a1\7q\2\2\u00a1")
        buf.write("\u00a2\7t\2\2\u00a2\26\3\2\2\2\u00a3\u00a4\7w\2\2\u00a4")
        buf.write("\u00a5\7p\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7k\2\2\u00a7")
        buf.write("\u00a8\7n\2\2\u00a8\30\3\2\2\2\u00a9\u00aa\7d\2\2\u00aa")
        buf.write("\u00ab\7{\2\2\u00ab\32\3\2\2\2\u00ac\u00ad\7d\2\2\u00ad")
        buf.write("\u00ae\7t\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7c\2\2\u00b0")
        buf.write("\u00b1\7m\2\2\u00b1\34\3\2\2\2\u00b2\u00b3\7e\2\2\u00b3")
        buf.write("\u00b4\7q\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7v\2\2\u00b6")
        buf.write("\u00b7\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7w\2\2\u00b9")
        buf.write("\u00ba\7g\2\2\u00ba\36\3\2\2\2\u00bb\u00bc\7k\2\2\u00bc")
        buf.write("\u00bd\7h\2\2\u00bd \3\2\2\2\u00be\u00bf\7g\2\2\u00bf")
        buf.write("\u00c0\7n\2\2\u00c0\u00c1\7u\2\2\u00c1\u00c2\7g\2\2\u00c2")
        buf.write("\"\3\2\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5\7n\2\2\u00c5")
        buf.write("\u00c6\7k\2\2\u00c6\u00c7\7h\2\2\u00c7$\3\2\2\2\u00c8")
        buf.write("\u00c9\7d\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb\7i\2\2\u00cb")
        buf.write("\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd&\3\2\2\2\u00ce")
        buf.write("\u00cf\7g\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7f\2\2\u00d1")
        buf.write("(\3\2\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7q\2\2\u00d4")
        buf.write("\u00d5\7v\2\2\u00d5*\3\2\2\2\u00d6\u00d7\7c\2\2\u00d7")
        buf.write("\u00d8\7p\2\2\u00d8\u00d9\7f\2\2\u00d9,\3\2\2\2\u00da")
        buf.write("\u00db\7q\2\2\u00db\u00dc\7t\2\2\u00dc.\3\2\2\2\u00dd")
        buf.write("\u00de\7-\2\2\u00de\60\3\2\2\2\u00df\u00e0\7/\2\2\u00e0")
        buf.write("\62\3\2\2\2\u00e1\u00e2\7,\2\2\u00e2\64\3\2\2\2\u00e3")
        buf.write("\u00e4\7\61\2\2\u00e4\66\3\2\2\2\u00e5\u00e6\7\'\2\2\u00e6")
        buf.write("8\3\2\2\2\u00e7\u00e8\7?\2\2\u00e8:\3\2\2\2\u00e9\u00ea")
        buf.write("\7>\2\2\u00ea\u00eb\7/\2\2\u00eb<\3\2\2\2\u00ec\u00ed")
        buf.write("\7#\2\2\u00ed\u00ee\7?\2\2\u00ee>\3\2\2\2\u00ef\u00f0")
        buf.write("\7>\2\2\u00f0@\3\2\2\2\u00f1\u00f2\7>\2\2\u00f2\u00f3")
        buf.write("\7?\2\2\u00f3B\3\2\2\2\u00f4\u00f5\7@\2\2\u00f5D\3\2\2")
        buf.write("\2\u00f6\u00f7\7@\2\2\u00f7\u00f8\7?\2\2\u00f8F\3\2\2")
        buf.write("\2\u00f9\u00fa\7\60\2\2\u00fa\u00fb\7\60\2\2\u00fb\u00fc")
        buf.write("\7\60\2\2\u00fcH\3\2\2\2\u00fd\u00fe\7?\2\2\u00fe\u00ff")
        buf.write("\7?\2\2\u00ffJ\3\2\2\2\u0100\u0101\7]\2\2\u0101L\3\2\2")
        buf.write("\2\u0102\u0103\7_\2\2\u0103N\3\2\2\2\u0104\u0105\7*\2")
        buf.write("\2\u0105P\3\2\2\2\u0106\u0107\7+\2\2\u0107R\3\2\2\2\u0108")
        buf.write("\u0109\7.\2\2\u0109T\3\2\2\2\u010a\u010e\t\2\2\2\u010b")
        buf.write("\u010d\t\3\2\2\u010c\u010b\3\2\2\2\u010d\u0110\3\2\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010fV\3\2\2")
        buf.write("\2\u0110\u010e\3\2\2\2\u0111\u0113\t\4\2\2\u0112\u0111")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0112\3\2\2\2\u0114")
        buf.write("\u0115\3\2\2\2\u0115X\3\2\2\2\u0116\u011b\5W,\2\u0117")
        buf.write("\u0119\7\60\2\2\u0118\u011a\5W,\2\u0119\u0118\3\2\2\2")
        buf.write("\u0119\u011a\3\2\2\2\u011a\u011c\3\2\2\2\u011b\u0117\3")
        buf.write("\2\2\2\u011b\u011c\3\2\2\2\u011c\u0122\3\2\2\2\u011d\u011f")
        buf.write("\t\5\2\2\u011e\u0120\t\6\2\2\u011f\u011e\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123\5W,\2\u0122")
        buf.write("\u011d\3\2\2\2\u0122\u0123\3\2\2\2\u0123Z\3\2\2\2\u0124")
        buf.write("\u012c\7$\2\2\u0125\u012b\n\7\2\2\u0126\u0127\7^\2\2\u0127")
        buf.write("\u012b\t\b\2\2\u0128\u0129\7)\2\2\u0129\u012b\7$\2\2\u012a")
        buf.write("\u0125\3\2\2\2\u012a\u0126\3\2\2\2\u012a\u0128\3\2\2\2")
        buf.write("\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d\3")
        buf.write("\2\2\2\u012d\u012f\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0130")
        buf.write("\7$\2\2\u0130\u0131\b.\2\2\u0131\\\3\2\2\2\u0132\u0133")
        buf.write("\t\t\2\2\u0133^\3\2\2\2\u0134\u0135\7%\2\2\u0135\u0136")
        buf.write("\7%\2\2\u0136\u013a\3\2\2\2\u0137\u0139\n\t\2\2\u0138")
        buf.write("\u0137\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2")
        buf.write("\u013a\u013b\3\2\2\2\u013b\u013d\3\2\2\2\u013c\u013a\3")
        buf.write("\2\2\2\u013d\u013e\b\60\3\2\u013e`\3\2\2\2\u013f\u0141")
        buf.write("\t\n\2\2\u0140\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142")
        buf.write("\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0144\3\2\2\2")
        buf.write("\u0144\u0145\b\61\3\2\u0145b\3\2\2\2\u0146\u0147\13\2")
        buf.write("\2\2\u0147\u0148\b\62\4\2\u0148d\3\2\2\2\u0149\u0151\7")
        buf.write("$\2\2\u014a\u0150\n\7\2\2\u014b\u014c\7^\2\2\u014c\u0150")
        buf.write("\t\b\2\2\u014d\u014e\7)\2\2\u014e\u0150\7$\2\2\u014f\u014a")
        buf.write("\3\2\2\2\u014f\u014b\3\2\2\2\u014f\u014d\3\2\2\2\u0150")
        buf.write("\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u0156\t")
        buf.write("\13\2\2\u0155\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157")
        buf.write("\u0158\b\63\5\2\u0158f\3\2\2\2\u0159\u0161\7$\2\2\u015a")
        buf.write("\u0160\n\7\2\2\u015b\u015c\7^\2\2\u015c\u0160\t\b\2\2")
        buf.write("\u015d\u015e\7)\2\2\u015e\u0160\7$\2\2\u015f\u015a\3\2")
        buf.write("\2\2\u015f\u015b\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0163")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0164\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165\7^\2\2")
        buf.write("\u0165\u0166\n\b\2\2\u0166\u0167\b\64\6\2\u0167h\3\2\2")
        buf.write("\2\22\2\u010e\u0114\u0119\u011b\u011f\u0122\u012a\u012c")
        buf.write("\u013a\u0142\u014f\u0151\u0155\u015f\u0161\7\3.\2\b\2")
        buf.write("\2\3\62\3\3\63\4\3\64\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQ = 28
    ASSIGNINIT = 29
    NE = 30
    LT = 31
    LE = 32
    GT = 33
    GE = 34
    CONCAT = 35
    EQSTRING = 36
    LBRACKET = 37
    RBRACKET = 38
    LPAREN = 39
    RPAREN = 40
    COMMA = 41
    ID = 42
    NUMBER_LIT = 43
    STRING_LIT = 44
    NEWLINE = 45
    COMMENTS = 46
    WS = 47
    ERROR_CHAR = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQ", "ASSIGNINIT", "NE", "LT", 
            "LE", "GT", "GE", "CONCAT", "EQSTRING", "LBRACKET", "RBRACKET", 
            "LPAREN", "RPAREN", "COMMA", "ID", "NUMBER_LIT", "STRING_LIT", 
            "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
                  "ASSIGNINIT", "NE", "LT", "LE", "GT", "GE", "CONCAT", 
                  "EQSTRING", "LBRACKET", "RBRACKET", "LPAREN", "RPAREN", 
                  "COMMA", "ID", "INT", "NUMBER_LIT", "STRING_LIT", "NEWLINE", 
                  "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[44] = self.STRING_LIT_action 
            actions[48] = self.ERROR_CHAR_action 
            actions[49] = self.UNCLOSE_STRING_action 
            actions[50] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[1:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:])
     


