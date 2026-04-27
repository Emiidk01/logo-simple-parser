from SymbolTable import *
from Type import *

class Node:
    def eval(self, env):
        pass

class Numeric(Node):
    def eval(self, env):
        pass

class Logic(Node):
    def eval(self, env):
        pass

class Void(Node):
    def eval(self, env):
        pass

# --- NUMERIC --- #
class Number(Numeric):
    def __init__(self, value):
        self.value = value
    
    def eval(self, env):
        return self.value

class Identifier(Numeric):
    def __init__(self, name, line):
        self.name = name
        self.line = line

    def eval(self, env):
        result = env.lookup(self.name)
        if result != None:
            (_, value) = result
            return value
        else: 
            text = "Line " + str(self.line) + " - " + self.name + " has not been declared"
            raise Exception(text)

class Minus(Numeric):
    def __init__(self, right):
        self.right = right

    def eval(self, env):
        return -1 * float(self.right.eval(env))
    
class Boolean(Logic):
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return self.value
    
class Not(Logic):
    def __init__(self, right):
        self.right = right

    def eval(self, env):
        return not bool(self.right.eval(env))


class Less(Logic):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        left = float(self.left.eval(env))
        right = float(self.right.eval(env))
        return left < right

class LessEq(Logic):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        left = float(self.left.eval(env))
        right = float(self.right.eval(env))
        return left <= right

class Greater(Logic):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        left = float(self.left.eval(env))
        right = float(self.right.eval(env))
        return left > right

class GreaterEq(Logic):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        left = float(self.left.eval(env))
        right = float(self.right.eval(env))
        return left >= right
    
class Equal(Logic):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        return self.left.eval(env) == self.right.eval(env)

class NotEqual(Logic):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        return self.left.eval(env) != self.right.eval(env)
    
class And(Logic):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        return bool(self.left.eval(env)) and bool(self.right.eval(env))

class Or(Logic):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        return bool(self.left.eval(env)) or bool(self.right.eval(env))

class Print(Void):
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        print(self.value.eval(env))

class Assignment(Void):
    def __init__(self, name, value, line):
        self.name = name
        self.value = value
        self.line = line

    def eval(self, env):
        value = self.value.eval(env)
        result = env.set(self.name, None, value)
        if not result:
            text = "Line " + str(self.line) + " - " + self.name + " has not been declared"
            raise Exception(text)
        
class Declaration(Void):
    def __init__(self, name, line):
        self.name = name
        self.line = line
    
    def eval(self, env):
        result = env.insert(self.name)
        if not result:
            text = "Line " + str(self.line) + " - " + self.name + " has already been declared"
            raise Exception(text)

class Add(Numeric):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        left = float(self.left.eval(env))
        right = float(self.right.eval(env))
        return left + right
    
class Subtract(Numeric):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval (self, env):
        left = float(self.left.eval(env))
        right = float(self.right.eval(env))
        return left - right
    
class Multiply(Numeric):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        left = float(self.left.eval(env))
        right = float(self.right.eval(env))
        return left * right
    
class Divide(Numeric):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        left = float(self.left.eval(env))
        right = float(self.right.eval(env))
        if right == 0:
            raise Exception("Cannon divide by zero")
        return left / right

class Mod(Numeric):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        left = int(self.left.eval(env))
        right = int(self.right.eval(env))
        if right == 0:
            raise Exception("Cannon mod by zero")
        return left % right
