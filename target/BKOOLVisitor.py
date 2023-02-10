# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decllist.
    def visitDecllist(self, ctx:BKOOLParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl.
    def visitDecl(self, ctx:BKOOLParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idenlist.
    def visitIdenlist(self, ctx:BKOOLParser.IdenlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcdecl.
    def visitFuncdecl(self, ctx:BKOOLParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameter.
    def visitParameter(self, ctx:BKOOLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paralist.
    def visitParalist(self, ctx:BKOOLParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paraprime.
    def visitParaprime(self, ctx:BKOOLParser.ParaprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmllist.
    def visitStmllist(self, ctx:BKOOLParser.StmllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignstmt.
    def visitAssignstmt(self, ctx:BKOOLParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#callstmt.
    def visitCallstmt(self, ctx:BKOOLParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnstmt.
    def visitReturnstmt(self, ctx:BKOOLParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operator.
    def visitOperator(self, ctx:BKOOLParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subexpr.
    def visitSubexpr(self, ctx:BKOOLParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprlist.
    def visitExprlist(self, ctx:BKOOLParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprime.
    def visitExprime(self, ctx:BKOOLParser.ExprimeContext):
        return self.visitChildren(ctx)



del BKOOLParser