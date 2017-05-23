import math
import random

#class vector:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y

class field_holder:
    def __init__(self):
        self.fields = []
        
    def get_field(self, x, y):
        result_field = (0.0, 0.0)
        for field in self.fields:
            result_field += field.get_field(x, y)
        return result_field
    
    def add_field(self, field):
        self.fields.append(field)
            
    
class linear_repulsive_field:
    def __init__(self, position_tracker, size, strength):
        self.position_tracker = position_tracker
        self.size = size
        self.strength = strength
    
    def get_field(self, x, y):    
        (px, py) = self.position_tracker.get_position()        
        dy = y - py
        dx = x - px
        angle = math.atan2(dy, dx)                
        mag = math.sqrt(dy * dy + dx * dx)        
        diff = self.size - mag
        if diff < 0:
            return (0.0, 0.0)
        power = self.strength * (diff / size)
        return (power * math.cos(angle), power * math.sin(angle))

class constant_repulsive_field:
    def __init__(self, position_tracker, size, strength):
        self.position_tracker = position_tracker
        self.size = size
        self.strength = strength
    
    def get_field(self, x, y):    
        (px, py) = self.position_tracker.get_position()        
        dy = y - py
        dx = x - px
        angle = math.atan2(dy, dx)                
        mag = math.sqrt(dy * dy + dx * dx)        
        if mag > self.size:
            return (0.0, 0.0)
        return (self.strength * math.cos(angle), self.strength * math.sin(angle))
    
class infinate_constant_attractive_field:
    def __init__(self, position_tracker, strength):
        self.position_tracker = position_tracker
        self.strength = strength       
       
    def get_field(self, x, y):
        (px, py) = self.position_tracker.get_position()        
        dy = y - py
        dx = x - px
        angle = math.atan2(dy, dx)                
        return (-self.strength * math.cos(angle), -self.strength * math.sin(angle))        

class random_field:
    def __init__(self, strength):
        self.strength = strength       
       
    def get_field(self, x, y):
        angle = random.random() * 2 * math.pi
        return (self.strength * math.cos(angle), self.strength * math.sin(angle))        

class fixed_position_tracker:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_position(self):
        return (self.x, self.y)        
        
class variable_position_tracker:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_position(self):
        return (self.x, self.y)        

    def set_postion(self, x, y):
        self.x = x
        self.y = y        
        
