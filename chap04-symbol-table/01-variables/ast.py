###########################################################
# Abstract Syntax Tree and Visitor Pattern Implementation
###########################################################

from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "Abstract method not implemented."

###########################################################
# AbstractNode -- Abstract Node of AST
###########################################################
class AbstractNode:
    __metaclass__ = ABCMeta

    @abstractmethod
    def accept(self, visitor):
        raise NotImplementedError(NOT_IMPLEMENTED)

    def __init__(self, token):
        self.token = token
        self.children = []

    def addChild(self, node):
        self.children.append(node)

###########################################################
# AbstractNodeVisitor -- Abstract Visitor of Node
###########################################################
class AbstractNodeVisitor:
    __metaclass__ = ABCMeta

    def visit(self, node):
        if isinstance(node, BinaryExpressionNode):
            return self.visitBinaryExpressionNode(node)
        elif isinstance(node, IntegerNode):
            return self.visitIntegerNode(node)
        elif isinstance(node, UnaryExpressionNode):
            return self.visitUnaryExpressionNode(node)
        elif isinstance(node, IdentifierNode):
            return self.visitIdentifierNode(node)
        elif isinstance(node, StatementListNode):
            return self.visitStatementListNode(node)

    @abstractmethod
    def visitBinaryExpressionNode(self, node):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitIntegerNode(self, node):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitUnaryExpressionNode(self, node):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitIdentifierNode(self, node):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def visitStatementListNode(self, node):
        raise NotImplementedError(NOT_IMPLEMENTED)

###########################################################
# BinaryExpressionNode -- AST Node of Expression
###########################################################
class BinaryExpressionNode(AbstractNode):
    def accept(self, visitor):
        return visitor.visit(self)

###########################################################
# IntegerNode -- AST Node of Integer
###########################################################
class IntegerNode(AbstractNode):
    def accept(self, visitor):
        return visitor.visit(self)

###########################################################
# UnaryExpressionNode -- AST Node of Unary Expression
###########################################################
class UnaryExpressionNode(AbstractNode):
    def accept(self, visitor):
        return visitor.visit(self)

###########################################################
# IdentifierNode -- AST Node of Variable
###########################################################
class IdentifierNode(AbstractNode):
    def accept(self, visitor):
        return visitor.visit(self)

###########################################################
# StatementListNode -- AST Node of Statement List
###########################################################
class StatementListNode(AbstractNode):
    def accept(self, visitor):
        return visitor.visit(self)

###########################################################
# PrintVisitor
###########################################################
class PrintVisitor(AbstractNodeVisitor):
    def visitBinaryExpressionNode(self, node):
        for child in node.children:
            child.accept(self)
        print(node.token)

    def visitIntegerNode(self, node):
        print(node.token)

    def visitUnaryExpressionNode(self, node):
        for child in node.children:
            child.accept(self)
        print('{token} (Unary)'.format(token = node.token))

    def visitIdentifierNode(self, node):
        print(node.token)

    def visitStatementListNode(self, node):
        for child in node.children:
            child.accept(self)
        print(node.token)

###########################################################
# Top-level script tests
###########################################################
if __name__ == '__main__':
    # AST of '3 * 2 + 5'
    operand1 = IntegerNode('3')
    operand2 = IntegerNode('2')
    operand3 = IntegerNode('5')

    mult = BinaryExpressionNode('*')
    root = BinaryExpressionNode('+')

    mult.addChild(operand1)
    mult.addChild(operand2)

    root.addChild(mult)
    root.addChild(operand3)

    visitor = PrintVisitor();
    root.accept(visitor)
