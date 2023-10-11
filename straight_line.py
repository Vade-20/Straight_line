import re
from fractions import Fraction


class Line_2D:
    def __init__(self,line:str):
        self.line = line.lower().strip().replace(' ','')
        if not self.is_linear_equation_int_2_var():
            raise Exception("Please enter a linear equation with x and y as its variables.")
         
        self.constant = self.__find_constant()
        self.x = self.__sum_of_var_x()
        self.y = self.__sum_of_var_y()
        self.slope = Fraction(self.x,self.y) if self.y != 0 else 'Not Defined'
    
    
    def __sum_of_var_x(self):
        real_value_1 = 0
        real_value_2 = 0 
        line_1,line_2 = self.line.split('=')
        value = re.findall(r'([-]?[\d]*)(x)',line_1)
        for i in value:
                if i[0]=='':
                    real_value_1 += 1
                elif i[0]=='-':
                    real_value_1 -= 1
                else:
                    real_value_1 += int(i[0])
                    
        value = re.findall(r'([-]?[\d]*)(x)',line_2)
        for i in value:
                if i[0]=='':
                    real_value_2 += 1
                elif i[0]=='-':
                    real_value_2 -= 1
                else:
                    real_value_2 += int(i[0])
        return real_value_1-real_value_2
    
    
    def __sum_of_var_y(self):
        real_value_1 = 0
        real_value_2 = 0 
        line_1,line_2 = self.line.split('=')
        value = re.findall(r'([-]?[\d]*)(y)',line_1)
        for i in value:
                if i[0]=='':
                    real_value_1 += 1
                elif i[0]=='-':
                    real_value_1 -= 1
                else:
                    real_value_1 += int(i[0])
                    
        value = re.findall(r'([-]?[\d]*)(y)',line_2)
        for i in value:
                if i[0]=='':
                    real_value_2 += 1
                elif i[0]=='-':
                    real_value_2 -= 1
                else:
                    real_value_2 += int(i[0])
        return real_value_1-real_value_2
    
    def __find_constant(self):
        line_1,line_2 = self.line.split('=')
        
        constant_1 = re.findall(r"[-]?[\d]+(?![a-z])\b",line_1)
        constant_1 = sum(list(map(int,constant_1)))
        
        constant_2 = re.findall(r"[-]?[\d]+(?![a-z])\b",line_2)
        constant_2 = sum(list(map(int,constant_2)))
        return constant_1-constant_2
                    
    def is_linear_equation_int_2_var(self):
        if '=' not in self.line:
            return False  
        for i in self.line:
            if i.isalpha() and i not in ['x','y']:
                return False
            elif not i.isalnum() and i not in ['+','-','=']:
                return False
        for i in ['++','--','==']:
            if i in self.line:
                return False
        return True
    

a = Line_2D('y=10+10x')
print(a.constant)
print(a.x)
print(a.y)
print(a.line)
print(a.slope)
