from Utils import *
import CodeGenerator as cgen
from CodeGenError import *
from MachineCode import JasminCode
from AST import *


class ZCodeType(Type):
    pass

class FuncZType(ZCodeType):
    def __init__(self, name, typ, param):
        self.typ = typ
        self.name = name
        self.param = param
        self.line = 0
    # def __str__(self):
    #     return f"FuncZType(param=[{', '.join(str(i) for i in self.param)}],typ={str(self.typ)},name={self.name},line={self.line})"


class VarZType(ZCodeType):
    def __init__(self, name, typ, index):
        self.typ = typ
        self.name = name
        self.index = index
        self.line = 0
    # def __str__(self):
    #     return f"VarZType(type={self.typ},name={self.name},index={self.index},line={self.line})"

class EmitterPrintoutInterface():
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

class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.jvm = JasminCode()
    def prRed(self, skk): print("\033[91m {}\033[00m".format(skk))

    def prGreen(self, skk): print("\033[92m {}\033[00m".format(skk))

    def prYellow(self, skk): print("\033[93m {}\033[00m" .format(skk))

    def prLightPurple(self, skk): print("\033[94m {}\033[00m" .format(skk))

    def prPurple(self, skk): print("\033[95m {}\033[00m" .format(skk))

    def prCyan(self, skk): print("\033[96m {}\033[00m" .format(skk))

    def prLightGray(self, skk): print("\033[97m {}\033[00m" .format(skk))

    def prBlack(self, skk): print("\033[98m {}\033[00m" .format(skk))
    def getJVMType(self, inType):
        typeIn = type(inType)
        if typeIn is NumberType:
            return "F"
        elif typeIn is BoolType:
            return "Z"
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is ArrayType:
            return "[" * len(inType.size)  + self.getJVMType(inType.eleType)
        elif typeIn is ZCodeType:
            return "LZCodeClass;"
        elif typeIn is VarZType:
            return "None"
        elif typeIn is FuncZType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.param))) + ")" + self.getJVMType(inType.typ) if inType.typ else "None"
        
        return "Ljava/lang/Object;"

    def emitPUSHICONST(self, in_, frame):
        # in: Int or Sring
        # frame: Frame

        frame.push()
        if type(in_) is int:
            i = in_
            if i >= -1 and i <= 5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
        elif type(in_) is str:
            if in_ == "true":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "false":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(int(in_), frame)

    def emitPUSHFCONST(self, in_, frame):
        # in_: String
        # frame: Frame

        f = float(in_)
        frame.push()
        rst = "{0:.4f}".format(f)
        if rst == "0.0" or rst == "1.0" or rst == "2.0":
            return self.jvm.emitFCONST(rst)
        else:
            return self.jvm.emitLDC(in_)

    ''' 
    *    generate code to push a constant onto the operand stack.
    *    @param in the lexeme of the constant
    *    @param typ the type of the constant
    '''

    def emitPUSHCONST(self, in_, typ, frame):
        #& in_: String (giá trị)
        #& typ: Type (kiểu number/string/bool)
        #& frame: Frame
        frame.push()
        if type(typ) is NumberType:
            f = float(in_)
            rst = "{0:.4f}".format(f)
            if rst == "0.0" or rst == "1.0" or rst == "2.0":
                return self.jvm.emitFCONST(rst)
            else:
                return self.jvm.emitLDC(rst)    
        elif type(typ) is StringType:
            return self.jvm.emitLDC(in_)
        elif type(typ) is BoolType:
            if in_:
                return self.jvm.emitICONST(1)
            else:
                return self.jvm.emitICONST(0)
        else:
            raise IllegalOperandException(in_)
    
    ##############################################################

    def emitALOAD(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, index, value -> ...

        frame.pop()
        if type(in_) is BoolType:
            return self.jvm.emitBALOAD()
        elif type(in_) is NumberType:
            return self.jvm.emitFALOAD()
        elif type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))        
        
    def emitASTORE(self, in_, frame):
        #& in_: Type
        #& frame: Frame
        #& ..., arrayref, index, value -> ...

        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is NumberType:
            return self.jvm.emitFASTORE()
        if type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        elif  type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))

    '''    generate the var directive for a local variable.
    *   @param in the index of the local variable.
    *   @param varName the name of the local variable.
    *   @param inType the type of the local variable.
    *   @param fromLabel the starting label of the scope where the variable is active.
    *   @param toLabel the ending label  of the scope where the variable is active.
    '''

    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        # in_: Int
        # varName: String
        # inType: Type
        # fromLabel: Int
        # toLabel: Int
        # frame: Frame

        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    def emitREADVAR(self, name, inType, index, frame):

        frame.push()
        if name == "this":
            return self.jvm.emitALOAD(index)
        elif type(inType) is BoolType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is NumberType:
            return self.jvm.emitFLOAD(index)
        elif type(inType) is StringType:
            return self.jvm.emitALOAD(index)
        elif type(inType) is ArrayType:
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''

    # def emitREADVAR2(self, name, typ, frame):
    #     # name: String
    #     # typ: Type
    #     # frame: Frame
    #     # ... -> ..., value

    #     # frame.push()
    #     raise IllegalOperandException(name)

    '''
    *   generate code to pop a value on top of the operand stack and store it to a block-scoped variable.
    *   @param name the symbol entry of the variable.
    '''

    def emitWRITEVAR(self, name, inType, index, frame):
        #& name: String
        #& inType: Type
        #& index: Int
        #& frame: Frame
        #& ..., value -> ...

        frame.pop()
        if type(inType) is NumberType:
            return self.jvm.emitFSTORE(index)
        elif type(inType) is BoolType:
            return self.jvm.emitISTORE(index)
        elif type(inType) is StringType:
            return self.jvm.emitASTORE(index)
        elif type(inType) is ArrayType:
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)  
        
    ''' generate the second instruction for array cell access
    *
    '''

    # def emitWRITEVAR2(self, name, typ, frame):
    #     # name: String
    #     # typ: Type
    #     # frame: Frame
    #     # ..., value -> ...

    #     # frame.push()
    #     raise IllegalOperandException(name)

    ''' generate the field (static) directive for a class mutable or immutable attribute.
    *   @param lexeme the name of the attribute.
    *   @param in the type of the attribute.
    *   @param isFinal true in case of constant; false otherwise
    '''

    def emitATTRIBUTE(self, lexeme, in_, isFinal = False, value = None):
        # lexeme: String
        # in_: Type
        # isFinal: Boolean
        # value: String

        return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), isFinal)

    def emitGETSTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a static method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''

    def emitINVOKESTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.param))
        if not type(typ.typ) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a special method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''

    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        # lexeme: String
        # in_: Type
        # frame: Frame

        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()

    ''' generate code to invoke a virtual method
    * @param lexeme the qualified name of the method(i.e., class-name/method-name)
    * @param in the type descriptor of the method.
    '''

    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.param))
        frame.pop()
        if not type(typ) is VoidType:
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))

    '''
    *   generate ineg, fneg.
    *   @param in the type of the operands.
    '''

    def emitNEGOP(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., value -> ..., result

        # if type(in_) is IntType:
        #     return self.jvm.emitINEG()
        # else:
        return self.jvm.emitFNEG()

    def emitNOT(self, in_, frame):
        # in_: Type
        # frame: Frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame))
        result.append(self.emitPUSHCONST(True, in_, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST(False, in_, frame))
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)

    def emitF2I(self, frame):
        # frame: Frame
        return '\tf2i\n'
    
    def emitI2F(self, frame):
        # frame: Frame
        return self.jvm.emitI2F()

    '''
    *   generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitADDOP(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "+":
            # if type(in_) is IntType:
            #     return self.jvm.emitIADD()
            # else:
            return self.jvm.emitFADD()
        else:
            # if type(in_) is IntType:
            #     return self.jvm.emitISUB()
            # else:
            return self.jvm.emitFSUB()

    '''
    *   generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitMULOP(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "*":
            # if type(in_) is IntType:
            #     return self.jvm.emitIMUL()
            # else:
            return self.jvm.emitFMUL()
        else:
            # if type(in_) is IntType:
            #     return self.jvm.emitIDIV()
            # else:
            return self.jvm.emitFDIV()

    def emitDIV(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIDIV()

    def emitMOD(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIREM()

    '''
    *   generate iand
    '''

    def emitANDOP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIAND()

    '''
    *   generate ior
    '''

    def emitOROP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIOR()

    def emitREOP(self, op, in_, frame):
        # op: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop()
        frame.pop()
        result.append(self.jvm.emitFCMPL())
        if op == ">":
            result.append(self.jvm.emitIFLE(labelF))
        elif op == ">=":
            result.append(self.jvm.emitIFLT(labelF))
        elif op == "<":
            result.append(self.jvm.emitIFGE(labelF))
        elif op == "<=":
            result.append(self.jvm.emitIFGT(labelF))
        elif op == "!=":
            result.append(self.jvm.emitIFEQ(labelF))
        elif op == "=":
            result.append(self.jvm.emitIFEQ(labelF))   
            result.append(self.emitPUSHCONST(False, BoolType(), frame))
            frame.pop()
            result.append(self.emitGOTO(labelO, frame))
            result.append(self.emitLABEL(labelF, frame))
            result.append(self.emitPUSHCONST(True, BoolType(), frame))
            result.append(self.emitLABEL(labelO, frame)) 
            return ''.join(result)
        result.append(self.emitPUSHCONST(True, BoolType(), frame))
        frame.pop()
        result.append(self.emitGOTO(labelO, frame))
        result.append(self.emitLABEL(labelF, frame))
        result.append(self.emitPUSHCONST(False, BoolType(), frame))
        result.append(self.emitLABEL(labelO, frame))
        return ''.join(result)

    def emitRELOP(self, op, in_, trueLabel, falseLabel, frame):
        # op: String
        # in_: Type
        # trueLabel: Int
        # falseLabel: Int
        # frame: Frame
        # ..., value1, value2 -> ..., result

        result = list()

        frame.pop()
        frame.pop()
        if op == ">":
            result.append(self.jvm.emitIFICMPLE(falseLabel))
            result.append(self.emitGOTO(trueLabel))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(falseLabel))
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(falseLabel))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(falseLabel))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPEQ(falseLabel))
        elif op == "==":
            result.append(self.jvm.emitIFICMPNE(falseLabel))
        result.append(self.jvm.emitGOTO(trueLabel))
        return ''.join(result)

    '''   generate the method directive for a function.
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    '''

    def emitMETHOD(self, lexeme, in_, isStatic, frame):
        # lexeme: String
        # in_: Type
        # isStatic: Boolean
        # frame: Frame

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    '''   generate the end directive for a function.
    '''

    def emitENDMETHOD(self, frame):
        # frame: Frame

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    def getConst(self, ast):
        # ast: Literal
        if type(ast) is IntLiteral:
            return (str(ast.value), IntType())

    '''   generate code to initialize a local array variable.<p>
    *   @param index the index of the local variable.
    *   @param in the type of the local array variable.
    '''

    '''   generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.    
    '''

    '''   generate code to jump to label if the value on top of operand stack is true.<p>
    *   ifgt label
    *   @param label the label where the execution continues if the value on top of stack is true.
    '''

    def emitIFTRUE(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFGT(label)

    '''
    *   generate code to jump to label if the value on top of operand stack is false.<p>
    *   ifle label
    *   @param label the label where the execution continues if the value on top of stack is false.
    '''

    def emitIFFALSE(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFLE(label)

    def emitIFICMPGT(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPLT(label)

    '''   generate code to duplicate the value on the top of the operand stack.<p>
    *   Stack:<p>
    *   Before: ...,value1<p>
    *   After:  ...,value1,value1<p>
    '''

    def emitDUP(self, frame):
        # frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitPOP()

    '''   generate code to exchange an integer on top of stack to a floating-point number.
    '''

    def emitI2F(self, frame):
        # frame: Frame

        return self.jvm.emitI2F()

    ''' generate code to return.
    *   <ul>
    *   <li>ireturn if the type is IntegerType or BooleanType
    *   <li>freturn if the type is RealType
    *   <li>return if the type is null
    *   </ul>
    *   @param in the type of the returned expression.
    '''

    def emitRETURN(self, in_, frame):
        # in_: Type
        # frame: Frame

        # if type(in_) is IntType:
        #     frame.pop()
        #     return self.jvm.emitIRETURN()
        # elif type(in_) is VoidType:
        #     return self.jvm.emitRETURN()

        if type(in_) is BoolType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is NumberType:
            frame.pop()
            return self.jvm.emitFRETURN()
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()
        elif type(in_) is StringType or type(in_) is ArrayType:
            frame.pop()
            return self.jvm.emitARETURN()

    ''' generate code that represents a label	
    *   @param label the label
    *   @return code Label<label>:
    '''

    def emitLABEL(self, label, frame):
        # label: Int
        # frame: Frame

        return self.jvm.emitLABEL(label)

    ''' generate code to jump to a label	
    *   @param label the label
    *   @return code goto Label<label>
    '''

    def emitGOTO(self, label, frame):
        # label: Int
        # frame: Frame

        return self.jvm.emitGOTO(str(label))

    ''' generate some starting directives for a class.<p>
    *   .source MPC.CLASSNAME.java<p>
    *   .class public MPC.CLASSNAME<p>
    *   .super java/lang/Object<p>
    '''

    def emitNEWARRAY(self, in_, frame):
        # frame: Frame
        # in_: Type
        val = ""
        if type(in_) is NumberType:
            val = "float"
        elif type(in_) is BoolType:
            val = "boolean"
        elif type(in_) is StringType:
            return self.emitANEWARRAY(in_, frame)
        return self.jvm.emitNEWARRAY(val)
    
    def emitANEWARRAY(self, in_, frame):
        # frame: Frame
        # in_: Type
        val = ""
        if type(in_) is NumberType:
            val = "float"
        elif type(in_) is BoolType:
            val = "boolean"
        elif type(in_) is StringType:
            val = "java/lang/String"
        elif type(in_) is ArrayType:
            val = self.getJVMType(in_)
        return self.jvm.emitANEWARRAY(val)
    
    def emitMULTIANEWARRAY(self, in_, frame):
        # frame: Frame
        # in_: Type
        if type(in_) is ArrayType:
            dimens = len(in_.size)
            return self.jvm.emitMULTIANEWARRAY(self.getJVMType(in_), str(dimens))
    
    def emitDUP(self, frame):
        # frame: Frame

        frame.push()
        return self.jvm.emitDUP()


    def emitPROLOG(self, name, parent):
        # name: String
        # parent: String
        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER(
            "java/lang/Object" if parent == "" else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        # num: Int

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        # num: Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        """
            Write to .j to translate
        """
        # print("emitEPILOG")
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    ''' print out the code to screen
    *   @param in the code to be printed out
    '''

    def printout(self, in_):
        # in_: String

        self.buff.append(in_)

    def printIndexNew(self):
        return len(self.buff) - 1

    def setType(self, in_):
        if type(in_) is VarZType: typ = self.getJVMType(in_.typ)
        else: typ = self.getJVMType(in_)
        self.buff[in_.line] = self.buff[in_.line].replace("None", typ)
    
    def clearBuff(self):
        self.buff.clear()
