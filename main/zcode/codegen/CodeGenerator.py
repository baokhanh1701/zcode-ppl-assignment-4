from Emitter import *
from functools import reduce
from AST import *
from Frame import Frame
from abc import ABC
from Visitor import *



class Access():
    def __init__(self, frame, symbol, is_at_left, is_type=True, is_first=False):
        self.is_at_left = is_at_left
        self.is_first = is_first
        self.frame = frame
        self.symbol = symbol
        self.is_type = is_type

class CodeGenerator:
    def gen(self, ast, path):
        gc = CodeGenVisitor(ast, path)
        gc.visit(ast, None)


class CodeGenVisitor(BaseVisitor):
    def __init__(self, ast_tree, path):
        self.ast_tree = ast_tree
        self.function = None
        self.Return = False
        self.array_cell = ""
        self.list_of_func = []
        self.path = path
        self.class_name = "ZCodeClass"
        self.emit = Emitter(self.path + "/" + self.class_name + ".j")

    def visitFuncZType(self, ast, param): 
        typ = ast.typ if ast.typ else ast
        return None, typ 

    def visitVarZType(self, ast, param): 
        typ = ast.typ if ast.typ else ast
        return None, typ 

    def prRed(self, skk): print("\033[91m {}\033[00m".format(skk))

    def prGreen(self, skk): print("\033[92m {}\033[00m".format(skk))

    def prYellow(self, skk): print("\033[93m {}\033[00m" .format(skk))

    def prLightPurple(self, skk): print("\033[94m {}\033[00m" .format(skk))

    def prPurple(self, skk): print("\033[95m {}\033[00m" .format(skk))

    def prCyan(self, skk): print("\033[96m {}\033[00m" .format(skk))

    def prLightGray(self, skk): print("\033[97m {}\033[00m" .format(skk))

    def prBlack(self, skk): print("\033[98m {}\033[00m" .format(skk))

    def compareTypeInDecl(self, lhs, rhs, o):
        _, rhs_type = self.visit(rhs, Access(o.frame, o.symbol, False, False))
        _, lhs_type = self.visit(lhs, Access(o.frame, o.symbol, True, False))
        if isinstance(lhs_type, ZCodeType):
            lhs_type.typ = rhs_type
            self.emit.setType(lhs_type)
        elif isinstance(rhs_type, ZCodeType):
            rhs_type.typ = lhs_type
            self.emit.setType(rhs_type)

    def printoutVisit(self, visitor):
        self.emit.printout(
            self.visit(visitor)[0]
        )
    
    def printoutEmitMethod(self, lexeme, in_, isStatic, frame):
        self.emit.printout(
            self.emit.emitMETHOD(lexeme, in_, isStatic, frame)
        )

    def printoutEmitLabel(self, label, frame):
        self.emit.printout(
            self.emit.emitLABEL(label, frame)
        )

    def printoutEmitAttribute(self, lexeme, in_, isFinal, value):
        self.emit.printout(
            self.emit.emitATTRIBUTE(lexeme, in_, isFinal, value)
        )

    def printoutEmitVar(self,  in_, varName, inType, fromLabel, toLabel, frame):
        self.emit.printout(
            self.emit.emitVAR(in_, varName, inType, fromLabel, toLabel, frame)
        )

    def printoutEmitReadVar(self, name, inType, index, frame):
        self.emit.printout(
            self.emit.emitREADVAR(name, inType, index, frame)
        )

    def printoutEmitInvokeSpecial(self, frame,   lexeme=None, in_=None):
        self.emit.printout(
            self.emit.emitINVOKESPECIAL(frame, lexeme, in_)
        )
        
    def printoutEmitEndMethod(self, frame):
        self.emit.printout(
            self.emit.emitENDMETHOD(frame)
        )
        
    def printoutEmitReturn(self, in_, frame):
        self.emit.printout(
            self.emit.emitRETURN(in_, frame)
        )

    def printoutEmitNewArray(self, in_, frame):
        self.emit.printout(
            self.emit.emitNEWARRAY(in_, frame)
        )
    
    def printoutEmitF2I(self, frame):
        self.emit.printout(
            self.emit.emitF2I(frame)
        )

    def printoutEmitPutStatic(self, lexeme, in_, frame):
        self.emit.printout(
            self.emit.emitPUTSTATIC(lexeme, in_, frame)
        )
    
    def printoutEmitMultiANewArray(self, in_, frame):
        self.emit.printout(
            self.emit.emitMULTIANEWARRAY(in_, frame)
        )
    
    def printoutEmitGoto(self, label, frame):
        self.emit.printout(
            self.emit.emitGOTO(label, frame)
        )
    def printoutEmitInvokeStatic(self, lexeme, _in, frame):
        self.emit.printout(
            self.emit.emitINVOKESTATIC(lexeme, _in, frame)
        )
    
    def printoutEmitIfFalse(self, label, frame):
        self.emit.printout(
            self.emit.emitIFFALSE(label, frame)
        )
    
    def printoutEmitIfTrue(self, label, frame):
        self.emit.printout(
            self.emit.emitIFTRUE(label, frame)
        )
    def initiatorEndProcess(self, frame):
        self.printoutEmitReturn(VoidType(), frame)
        self.printoutEmitLabel(frame.getEndLabel(), frame)
        self.printoutEmitEndMethod(frame)

    def programInitiator(self, init_code, frame, class_name):
        self.printoutEmitMethod("<init>", FuncZType(
            init_code, VoidType(), []), False, frame)
        frame.enterScope(True)
        self.printoutEmitLabel(frame.getStartLabel(), frame)
        self.printoutEmitVar(frame.getNewIndex(
        ), "this", ZCodeType(), frame.getStartLabel(), frame.getEndLabel(), frame)
        self.printoutEmitReadVar("this", class_name, 0, frame)
        self.printoutEmitInvokeSpecial(frame)
        self.initiatorEndProcess(frame)
        frame.exitScope()

    def programCLInitiator(self, clinit_code, frame, class_name, Symbol, ast):
        self.printoutEmitMethod(
            "<" + clinit_code + ">", FuncZType(clinit_code, VoidType(), []), True, frame)
        frame.enterScope(True)
        one = 1
        zero = 0
        self.printoutEmitLabel(frame.getStartLabel(), frame)
        for var in ast.decl:
            name = var.name.name
            class_dir = class_name + "." + name
            if (type(var) is VarDecl) and (type(var.varType) is ArrayType):
                if len(var.varType.size) == one:
                    self.printoutVisit(NumberLiteral(var.varType.size[zero]), Access(frame, Symbol, False))
                    self.printoutEmitF2I(frame)
                    self.printoutEmitNewArray(var.varType.eleType, frame)
                    self.printoutEmitPutStatic(class_dir, var.varType, frame)
                
                elif len(var.varType.size) != one:
                    for i in var.varType.size:
                        self.printoutVisit(NumberLiteral(i), Access(frame, Symbol, False))
                        self.printoutEmitF2I(frame)
                    self.printoutEmitMultiANewArray(var.varType, frame)
                    self.printoutEmitPutStatic(class_dir, var.varType, frame)
            
            elif type(var) is VarDecl and var.varInit is not None:
                self.visit(Assign(var.name, var.varInit),
                            Access(frame, Symbol, False))
        self.initiatorEndProcess(frame)
        frame.exitScope()

    def programMainIntiator(self, main_code, frame, Main, Symbol, function):
        one = 1
        self.printoutEmitMethod(main_code, FuncZType(main_code, VoidType(), [
                                ArrayType([one], StringType())]), True, frame)
        frame.enterScope(True)
        self.printoutEmitLabel(frame.getStartLabel(), frame)
        self.printoutEmitVar(frame.getNewIndex(), "args", ArrayType(
            [], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame)
        self.function = function
        self.visit(Main.body, Access(frame, Symbol, False))
        self.initiatorEndProcess(frame)
        frame.exitScope()

    def visitProgram(self, ast: Program, o):
        # self.prGreen("visitProgram")
        Symbol = [[]]
        Main = None
        function = None
        init_code = "init"
        clinit_code = "clinit"
        java_lang_object = "java.lang.Object"
        self.emit.printout(self.emit.emitPROLOG(
            self.class_name, java_lang_object))

        for item in ast.decl:
            item_name = item.name.name
            if type(item) is VarDecl:
                Symbol[0].append(VarZType(item_name, item.varType, -1))
                self.printoutEmitAttribute(
                    item_name, item.varType if item.varType else Symbol[0][-1], False, self.class_name)
                Symbol[0][-1].line = self.emit.printIndexNew()

            elif type(item) is FuncDecl and item.body is not None:
                self.list_of_func += [FuncZType(item_name,
                                                None, [i.varType for i in item.param])]
                if item_name == "main":
                    function = self.list_of_func[-1]
                    Main = item

        frame = Frame("<init>", VoidType)
        self.programInitiator(init_code, frame, self.class_name)
                
        frame = Frame("<clinit>", VoidType)
        self.programCLInitiator(clinit_code, frame, self.class_name, Symbol, ast)

        zero = 0
        one = 1
        counter = zero
        for item in ast.decl:
            if (type(item) is FuncDecl) :
                if (item.body is not None):
                    if (item.name.name != "main"):
                        self.function = self.list_of_func[counter]
                        self.visit(item, Symbol)
            if type(item) is FuncDecl and item.body is not None:
                counter += one

        frame = Frame("main", VoidType)
        self.programMainIntiator("main", frame, Main, Symbol, function)
        
        self.emit.emitEPILOG()

    def visitVarDecl(self, ast: VarDecl, o):
        # self.prGreen("VarDecl: " + str(ast))
        frame = o.frame
        idx = frame.getNewIndex()
        start_label = frame.getStartLabel()
        end_label = frame.getEndLabel()
        name = ast.name.name
        var_type = ast.varType
        self.printoutEmitVar(idx, name, var_type, start_label, end_label, frame)
        o.symbol[0].append(VarZType(name, var_type, idx))
        o.symbol[0][-1].line = self.emit.printIndexNew()
        if ast.varInit is not None:
            self.visit(Assign(ast.name, ast.varInit), Access(frame, o.symbol, False))

    def visitFuncDecl(self, ast, Symbol):
        # self.prGreen("visitFuncDecl: " + str(ast))
        self.Return = False
        name = ast.name.name
        frame = Frame(name, VoidType)

        self.printoutEmitMethod(name, self.function, True, frame)
        
        self.function.line = self.emit.printIndexNew()
        frame.enterScope(True)
        start_label = frame.getStartLabel()
        end_label = frame.getEndLabel()
        self.printoutEmitLabel(start_label, frame)
        typeParam = []
        for param in ast.param:
            param_name = param.name.name
            index = frame.getNewIndex()
            typeParam += [VarZType(param_name, param.varType, index)]
            self.printoutEmitVar(index, param_name, param.varType, start_label, end_label, frame)
        self.visit(ast.body, Access(frame, [typeParam] + Symbol, False))
        self.printoutEmitReturn(VoidType(), frame)
        self.printoutEmitLabel(end_label, frame)
        if not self.Return:
            self.printoutEmitReturn(VoidType(), frame)
            self.compareTypeInDecl(self.function, VoidType(), Access(frame, Symbol, False))
        self.printoutEmitEndMethod(frame)
        frame.exitScope()

    def visitId(self, ast, o):
        # print("visitId", ast)
        frame = o.frame
        Symbol = o.symbol
        localized = -1
        # print("o.is_type: ", o.is_type)
        # print("o.is_at_left: ", o.is_at_left)
        # if o.is_type:
        for symbol in Symbol:
            for item in symbol:
                # print("item: ", item)
                if item.name == ast.name:
                    if item.index == localized:
                        # print(o)
                        if o.is_at_left:
                            return self.emit.emitPUTSTATIC(self.class_name + "." + item.name, item.typ, frame), item.typ
                        else:
                            return self.emit.emitGETSTATIC(self.class_name + "." + item.name, item.typ, frame), item.typ
                    else:
                        if o.is_at_left:
                            return self.emit.emitWRITEVAR(item.name, item.typ, item.index, frame), item.typ
                        else:
                            return self.emit.emitREADVAR(item.name, item.typ, item.index, frame), item.typ

    def visitCallExpr(self, ast, o):
        frame = o.frame
        # print("visitCallExpr")
        name = ast.name.name
        lexeme = f"io/{name}"
        if name == "readBool":
            if o.is_type:
                return None, BoolType()
            return self.emit.emitINVOKESTATIC(lexeme, FuncZType(name, BoolType(), []), frame), BoolType()
        elif name == "readString":
            if o.is_type:
                return None, StringType()
            return self.emit.emitINVOKESTATIC(lexeme, FuncZType(name, StringType(), []), frame), StringType()
        elif name == "readNumber":
            if o.is_type:
                return None, NumberType()
            return self.emit.emitINVOKESTATIC(lexeme, FuncZType(name, NumberType(), []), frame), NumberType()
        
        function = None
        for item in self.list_of_func:
            if item.name == ast.name.name:
                function = item

        emit_arg = ""
        for item in range(len(function.param)):
            arg, _ = self.visit(ast.args[item], o)
            # print("emit_arg: ", emit_arg)
            emit_arg += arg
        return emit_arg + self.emit.emitINVOKESTATIC(self.class_name + "/" + function.name, FuncZType(function.name, function.typ, function.param), o.frame), function.typ

    def visitCallStmt(self, ast, o):
        # print("visitCallStmt", ast)
        name = ast.name.name
        if name in ["writeNumber", "writeBool", "writeString"]:
            if name == "writeNumber":
                self.compareTypeInDecl(NumberType(), ast.args[0], o)
            elif name == "writeBool":
                self.compareTypeInDecl(BoolType(), ast.args[0], o)
            elif name == "writeString":
                self.compareTypeInDecl(StringType(), ast.args[0], o)
            args_code, args_type = self.visit(ast.args[0], o)
            # print("argsType:", args_type)

            self.emit.printout(args_code)

            self.printoutEmitInvokeStatic(f"io/{name}", FuncZType(name, VoidType(), [args_type]), o.frame)
            return
        else:
            args_type_list = []
            for arg in ast.args:
                args_code, args_type = self.visit(arg, o)
                self.emit.printout(args_code)
                args_type_list.append(args_type)
                
            self.printoutEmitInvokeStatic(f"{self.class_name}/{name}", FuncZType(name, VoidType(), args_type_list), o.frame)
    def visitReturn(self, ast: Return, o):
        # self.prGreen("visitReturn")
        self.Return = True
        frame = o.frame
        if ast.expr:
            retCode, retType = self.visit(
                ast.expr, Access(frame, o.symbol, False, True))
            # print("retType: ", retType)
            # print("retCode: ", retCode)
            # if not type(retType) is VoidType:
            # expCode, _ = self.visit(ast.expr, Access(frame, o.symbol, False, True))
            self.compareTypeInDecl(self.function, retType, o)
            self.emit.printout(retCode)
            self.printoutEmitReturn(retType, frame)
        else:
            self.compareTypeInDecl(self.function, VoidType(), o)            
            self.printoutEmitReturn(VoidType(), frame)
    def visitAssign(self, ast: Assign, o):
        # self.prGreen("visitAssign:" + str(ast))
        rhs, _ = self.visit(ast.rhs, Access(o.frame, o.symbol, False))
        lhs, _ = self.visit(ast.lhs, Access(o.frame, o.symbol, True))
        self.emit.printout(rhs + lhs)

    def visitBlock(self, ast, o):
        symbolnew = [[]] + o.symbol
        o.frame.enterScope(False)
        self.printoutEmitLabel(o.frame.getStartLabel(), o.frame)
        for item in ast.stmt:
            self.visit(item, Access(o.frame, symbolnew, False))
        self.printoutEmitLabel(o.frame.getEndLabel(), o.frame)
        o.frame.exitScope()

    def visitBinaryOp(self, ast: BinaryOp, o):
        lhs, _ = self.visit(ast.left, o)
        rhs, _ = self.visit(ast.right, o)
        java_lang_string_equals = f"java/lang/String/equals"
        java_lang_string_concat = f"java/lang/String/concat"
        tmp = lhs + rhs
        if (ast.op in ["+", "-"]):
            return tmp + self.emit.emitADDOP(ast.op, NumberType(), o.frame), NumberType()
        elif (ast.op in ["*", "/"]):
            return tmp + self.emit.emitMULOP(ast.op, NumberType(), o.frame), NumberType()
        elif (ast.op in ["and"]):
            return tmp + self.emit.emitANDOP(o.frame), BoolType()
        elif (ast.op in ["or"]):
            return tmp + self.emit.emitOROP(o.frame), BoolType()
        elif (ast.op in ["=="]):
            return tmp + self.emit.emitINVOKEVIRTUAL(java_lang_string_equals, FuncZType("equals", BoolType(), [None]), o.frame), BoolType()
        elif (ast.op in ["..."]):
            return tmp + self.emit.emitINVOKEVIRTUAL(java_lang_string_concat, FuncZType("concat", StringType(), [StringType()]), o.frame), StringType()
        elif (ast.op in ["%"]):
            lhs += self.emit.emitF2I(o.frame)
            rhs += self.emit.emitF2I(o.frame)
            tmp = lhs + rhs
            return tmp + self.emit.emitMOD(o.frame) + self.emit.emitI2F(o.frame), NumberType()
        elif (ast.op in [">", "<", ">=", "=", "!=", "<="]):
            return tmp + self.emit.emitREOP(ast.op, NumberType(), o.frame), BoolType()

    def visitUnaryOp(self, ast: UnaryOp, o):
        operand, _ = self.visit(ast.operand, o)
        if (ast.op in ["not"]):
            return operand + self.emit.emitNOT(BoolType(), o.frame), BoolType()
        elif (ast.op in ["-"]):
            return operand + self.emit.emitNEGOP(NumberType(), o.frame), NumberType()

    def visitIf(self, ast: If, o):
        # pass
        self.compareTypeInDecl(BoolType(), ast.expr, o)        
        for item in ast.elifStmt:
            self.compareTypeInDecl(BoolType(), item[0], o)        
        frame = o.frame
        exp, exp_type = self.visit(ast.expr, Access(frame, o.symbol, False))
        else_label = frame.getNewLabel()
        exit_label = frame.getNewLabel()
        end_if_label = frame.getNewLabel()

        self.emit.printout(exp)
        if len(ast.elifStmt) > 0:
            self.printoutEmitIfFalse(end_if_label, o.frame)
        else:
            self.printoutEmitIfFalse(else_label, o.frame)
        self.visit(ast.thenStmt, o)
        self.printoutEmitGoto(exit_label, o.frame)
        self.printoutEmitLabel(end_if_label, o.frame)
        # if len(ast.elifStmt) > 0:
        #     for elif_decl in ast.elifStmt:
        #         elif_label = frame.getNewLabel()
        #         expr = elif_decl[0]
        #         stmt = elif_decl[1]
                
        #         expr_code, expr_type = self.visit(expr, o)
        #         self.emit.printout(self.emit.emitLABEL(elif_label, o.frame))
                
        #         self.prRed(expr_code)
        #         self.prRed(expr_type)
        #         self.emit.printout(expr_code)
        #         # self.emit.printout(self.emit.emitIFFALSE(end_elif_label, o.frame))
                
        #         stmt_code, stmt_type = self.visit(stmt, o)
        #         self.prRed(stmt_code)
        #         self.prRed(stmt_type)
        #         self.emit.printout(stmt_code)
        #         self.emit.printout(self.emit.emitGOTO(exit_label, o.frame))

        self.printoutEmitGoto(exit_label, o.frame)
        self.printoutEmitLabel(else_label, o.frame)
        
        if ast.elseStmt:
            self.visit(ast.elseStmt, o)
        self.printoutEmitLabel(exit_label, o.frame)

    def visitFor(self, ast: For, o):
        # self.prGreen("visitFor")
        name = ast.name
        cond_expr = ast.condExpr
        upd_expr = ast.updExpr
        self.compareTypeInDecl(NumberType(), name, o)
        self.compareTypeInDecl(BoolType(), cond_expr, o)
        self.compareTypeInDecl(NumberType(), upd_expr, o)

        self.visit(ast.name, o)
        frame = o.frame
        enter_loop = o.frame.getNewLabel()
        # self.prPurple(enter_loop)
        frame.enterLoop()
        continue_label = o.frame.getContinueLabel()
        break_label = o.frame.getBreakLabel()
        self.printoutEmitLabel(enter_loop, o.frame)
        exp, exp_type = self.visit(cond_expr, Access(o.frame, o.symbol, False))
        # self.prRed(exp)
        # self.prRed(exp_type)
        self.emit.printout(exp)
        self.printoutEmitIfTrue(break_label, o.frame)
        self.visit(ast.body, o)
        self.printoutEmitLabel(continue_label, o.frame)
        self.visit(Assign(ast.name, BinaryOp('+', ast.name,
                    ast.updExpr)), Access(frame, o.symbol, False))
        # self.visit(ast.updExpr, o)
        self.printoutEmitGoto(enter_loop, o.frame)
        self.printoutEmitLabel(break_label, o.frame)
        frame.exitLoop()

    def visitContinue(self, ast, o):
        self.printoutEmitGoto(o.frame.getContinueLabel(), o.frame)

    def visitBreak(self, ast, o):
        self.printoutEmitGoto(o.frame.getBreakLabel(), o.frame)
    def visitNumberLiteral(self, ast, o):
        # print("visitNumberLiteral:", ast)
        emitted = self.emit.emitPUSHCONST(ast.value, NumberType(), o.frame)
        return emitted, NumberType()

    def visitBooleanLiteral(self, ast, o):
        emmitted = self.emit.emitPUSHCONST(ast.value, BoolType(), o.frame)
        return emmitted, BoolType()
    # if o.is_type else None

    def visitStringLiteral(self, ast, o):
        emmitted = self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o.frame)
        return emmitted, StringType()

    def visitArrayType(self, ast, param): return None, ast
    def visitNumberType(self, ast, param): return None, NumberType()
    def visitVoidType(self, ast, param): return None, VoidType()
    def visitBoolType(self, ast, param): return None, BoolType()
    def visitStringType(self, ast, param): return None, StringType()
