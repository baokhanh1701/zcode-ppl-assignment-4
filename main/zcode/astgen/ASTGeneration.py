from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *
from functools import reduce

class ASTGeneration(ZCodeVisitor):
    
###^ declared declared declared declared

    #* program: ( NEWLINE)* list_declared EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))

    #* list_declared: declared  list_declared | declared; 
    def visitList_declared(self, ctx:ZCodeParser.List_declaredContext):
        if ctx.list_declared():
            return [self.visit(ctx.declared())] + self.visit(ctx.list_declared())
        return [self.visit(ctx.declared())]

    #* declared: function | variables ignore;
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        if ctx.variables():
            return self.visit(ctx.variables())
        elif ctx.function():
            return self.visit(ctx.function())

    #* variables: implicit_var | keyword_var | implicit_dynamic; 
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        if ctx.implicit_var():
            return self.visit(ctx.implicit_var())
        elif ctx.keyword_var():
            return self.visit(ctx.keyword_var())
        return self.visit(ctx.implicit_dynamic())

    #* implicit_var: VAR ID ASSIGNINIT expression;
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return VarDecl(Id(ctx.ID().getText()), None, "var", self.visit(ctx.expression()))

    #* keyword_var: type_prime ID (LBRACKET list_NUMBER_LIT RBRACKET)? (ASSIGNINIT expression)?;
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        expr = None
        if ctx.expression(): expr = self.visit(ctx.expression())
        
        typ = self.visit(ctx.type_prime())        
        if ctx.list_NUMBER_LIT(): typ = ArrayType(self.visit(ctx.list_NUMBER_LIT()) , typ)
        
        return VarDecl(Id(ctx.ID().getText()), typ, None, expr)

    #* implicit_dynamic: DYNAMIC ID (ASSIGNINIT expression)?;
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        if ctx.expression():
            return VarDecl(Id(ctx.ID().getText()), None, "dynamic", self.visit(ctx.expression()))
        return VarDecl(Id(ctx.ID().getText()), None, "dynamic", None)

    #* type_prime: BOOL | NUMBER | STRING;
    def visitType_prime(self, ctx:ZCodeParser.Type_primeContext):
        if ctx.BOOL():
            return BoolType()
        elif ctx.NUMBER():
            return NumberType()
        return StringType()

    #* list_NUMBER_LIT: NUMBER_LIT COMMA list_NUMBER_LIT | NUMBER_LIT;
    def visitList_NUMBER_LIT(self, ctx:ZCodeParser.List_NUMBER_LITContext):
        if ctx.getChildCount() == 1:
            return [float(ctx.NUMBER_LIT().getText())]
        return [float(ctx.NUMBER_LIT().getText())] + self.visit(ctx.list_NUMBER_LIT())

    #* function: FUNC ID LPAREN prameters_list? RPAREN  (ignore? return_statement | ignore? block_statement | ignore);
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        statement = None
        if ctx.return_statement():
            statement = self.visit(ctx.return_statement())
        elif ctx.block_statement():
            statement = self.visit(ctx.block_statement())
            
        prameters_list =  []
        if ctx.prameters_list():
            prameters_list = self.visit(ctx.prameters_list())
        
        return FuncDecl(Id(ctx.ID().getText()), prameters_list, statement)

    #* prameters_list: prameters COMMA prameters_list | prameters;
    def visitPrameters_list(self, ctx:ZCodeParser.Prameters_listContext):
        if ctx.prameters_list():
            return [self.visit(ctx.prameters())] + self.visit(ctx.prameters_list())
        return [self.visit(ctx.prameters())]
        
    #* prameters: type_prime ID | type_prime ID LBRACKET list_NUMBER_LIT RBRACKET;
    def visitPrameters(self, ctx:ZCodeParser.PrametersContext):
        if ctx.getChildCount() == 2:
            return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.type_prime()), None, None)
        return VarDecl(Id(ctx.ID().getText()), ArrayType(self.visit(ctx.list_NUMBER_LIT()) , self.visit(ctx.type_prime())), None, None)
        
    
###^ Expression Expression Expression Expression
    #* expression: expression1 CONCAT expression1  | expression1; 
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1()[0]) 

        op = ctx.CONCAT().getText()
        left = self.visit(ctx.expression1()[0])
        right = self.visit(ctx.expression1()[1])
        return BinaryOp(op, left, right)
    
    #* expression1: expression2 (EQ | EQSTRING | NE | LT | LE | GT | GE) expression2 | expression2;
    def visitExpression1(self, ctx:ZCodeParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2()[0])
        
        op = ''
        if ctx.EQ():
            op = ctx.EQ().getText()
        elif ctx.EQSTRING():
            op = ctx.EQSTRING().getText()
        elif ctx.NE():
            op = ctx.NE().getText()
        elif ctx.LT():
            op = ctx.LT().getText()
        elif ctx.LE():
            op = ctx.LE().getText()
        elif ctx.GT():
            op = ctx.GT().getText()
        elif ctx.GE():
            op = ctx.GE().getText()

        left = self.visit(ctx.expression2()[0])
        right = self.visit(ctx.expression2()[1])
        return BinaryOp(op, left, right)

    #* expression2: expression2 (AND | OR) expression3 | expression3   
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        
        op = ''
        if ctx.AND():
            op = ctx.AND().getText()
        elif ctx.OR():
            op = ctx.OR().getText()

        left = self.visit(ctx.expression2())
        right = self.visit(ctx.expression3())
        return BinaryOp(op, left, right)

    #* expression3: expression3 (ADD | SUB) expression4 | expression4.
    def visitExpression3(self, ctx:ZCodeParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())

        op = ''
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()

        left = self.visit(ctx.expression3())
        right = self.visit(ctx.expression4())
        return BinaryOp(op, left, right)

    #* expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        
        op = ''
        if ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()            

        left = self.visit(ctx.expression4())
        right = self.visit(ctx.expression5())
        return BinaryOp(op, left, right)

    #* expression5: NOT expression5 | expression6;
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        
        op = ctx.NOT().getText()
        right = self.visit(ctx.expression5())
        return UnaryOp(op, right)

    #* expression6: (SUB | ADD) expression6 | expression7;
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        
        op = ''
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()
        
        right = self.visit(ctx.expression6())
        return UnaryOp(op, right)

    #* expression7: (ID | ID LPAREN index_operators? RPAREN) LBRACKET index_operators  RBRACKET  | expression8;
    def visitExpression7(self, ctx:ZCodeParser.Expression7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression8())
        elif ctx.getChildCount() == 4:
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.index_operators()[0]))
        elif len(ctx.index_operators()) == 2:
            return ArrayCell(CallExpr(Id(ctx.ID().getText()), self.visit(ctx.index_operators()[0])), self.visit(ctx.index_operators()[1]))
        return ArrayCell(CallExpr(Id(ctx.ID().getText()), []), self.visit(ctx.index_operators()[0]))
    
    #* expression8: ID  | literal | LPAREN expression RPAREN | ID LPAREN index_operators? RPAREN;
    def visitExpression8(self, ctx:ZCodeParser.Expression8Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        elif ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.index_operators():
            return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.index_operators()))
        return CallExpr(Id(ctx.ID().getText()), [])

    #* index_operators: expression COMMA index_operators | expression;
    def visitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.index_operators())     
    
    # #* literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        if ctx.NUMBER_LIT():
            return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        return ArrayLiteral(self.visit(ctx.array_literal()))
        
    #* array_literal: LBRACKET index_operators?  RBRACKET;
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        if ctx.index_operators():
            return self.visit(ctx.index_operators())
        return []


###^ Statements Statements Statements Statements

    #* statement: (declaration_statement | assignment_statement | if_statement | for_statement | break_statement   | continue_statement | return_statement  | call_statement | block_statement);
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        if ctx.declaration_statement():
            return self.visit(ctx.declaration_statement())
        elif ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.call_statement():
            return self.visit(ctx.call_statement())
        elif ctx.block_statement():
            return self.visit(ctx.block_statement())


    #* declaration_statement: variables ignore;
    def visitDeclaration_statement(self, ctx:ZCodeParser.Declaration_statementContext):
        return self.visit(ctx.variables())


    #* assignment_statement : lhs ASSIGNINIT expression ignore;
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expression()))

    

    #* FOR ID UNTIL expression BY expression ignore? statement;
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return For(Id(ctx.ID().getText()),
                       self.visit(ctx.expression()[0]),
                       self.visit(ctx.expression()[1]),
                       self.visit(ctx.statement()))

    #* break_statement      : BREAK ignore;
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return Break()

    #* continue_statement   : CONTINUE  ignore;
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return Continue()

    #* return_statement     : RETURN expression? ignore;
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return(None)

    #* call_statement       : ID LPAREN  index_operators? RPAREN ignore;
    def visitCall_statement(self, ctx:ZCodeParser.Call_statementContext):
        if ctx.index_operators():
            return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.index_operators()))
        return CallStmt(Id(ctx.ID().getText()), [])

    #* block_statement      : BEGIN ignore statement_list END ignore;
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return Block(self.visit(ctx.statement_list()))

    #* lhs: ID LBRACKET index_operators  RBRACKET | ID;
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.index_operators():
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.index_operators()))
        return Id(ctx.ID().getText())
        

    #* statement_list: statement statement_list | ; 
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        if ctx.getChildCount() == 0: return []
        return [self.visit(ctx.statement())] + self.visit(ctx.statement_list())

    #* if_statement : IF LPAREN expression RPAREN ignore? statement elif_list (ELSE ignore? statement )?;
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        if not ctx.ELSE():
            return If(self.visit(ctx.expression()),
                          self.visit(ctx.statement()[0]),
                          self.visit(ctx.elif_list()),None)
        return If(self.visit(ctx.expression()),
                    self.visit(ctx.statement()[0]),
                    self.visit(ctx.elif_list()),self.visit(ctx.statement()[1]))    
        
    #* elif_list:ELIF LPAREN expression RPAREN ignore? statement elif_list | ;
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        if ctx.getChildCount() == 0: return []
        return [(self.visit(ctx.expression()), self.visit(ctx.statement()))] + self.visit(ctx.elif_list())

    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return None