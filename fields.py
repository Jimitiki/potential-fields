import math
import random
import sys

#class vector:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y

class field_holder:
    def __init__(self):
        self.fields = []
        
    def get_field(self, x, y):
        result_field_x = 0.0
        result_field_y = 0.0
        for field in self.fields:
            (field_x, field_y) = field.get_field(x, y)
            result_field_x += field_x
            result_field_y += field_y
        return (result_field_x, result_field_y)
    
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
        power = self.strength * (diff / self.size)
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

class constant_clockwise_tangential_field:
    def __init__(self, position_tracker, size, strength):
        self.position_tracker = position_tracker
        self.size = size
        self.strength = strength
    
    def get_field(self, x, y):
        (px, py) = self.position_tracker.get_position()        
        dy = y - py
        dx = x - px
        angle = math.atan2(dy, dx)                
        angle += math.pi / 2
        mag = math.sqrt(dy * dy + dx * dx)        
        if mag > self.size:
            return (0.0, 0.0)
        return (self.strength * math.cos(angle), self.strength * math.sin(angle))
        
class constant_counterclockwise_tangential_field:
    def __init__(self, position_tracker, size, strength):
        self.position_tracker = position_tracker
        self.size = size
        self.strength = strength
    
    def get_field(self, x, y):
        (px, py) = self.position_tracker.get_position()        
        dy = y - py
        dx = x - px
        angle = math.atan2(dy, dx)                
        angle -= math.pi / 2
        mag = math.sqrt(dy * dy + dx * dx)        
        if mag > self.size:
            return (0.0, 0.0)
        return (self.strength * math.cos(angle), self.strength * math.sin(angle))
        
class linear_clockwise_tangential_field:
    def __init__(self, position_tracker, size, strength):
        self.position_tracker = position_tracker
        self.size = size
        self.strength = strength
    
    def get_field(self, x, y):
        (px, py) = self.position_tracker.get_position()        
        dy = y - py
        dx = x - px
        angle = math.atan2(dy, dx)                
        angle += math.pi / 2
        mag = math.sqrt(dy * dy + dx * dx)        
        diff = self.size - mag
        if diff < 0:
            return (0.0, 0.0)
        power = self.strength * (diff / self.size)
        return (power * math.cos(angle), power * math.sin(angle))
        
class linear_counterclockwise_tangential_field:
    def __init__(self, position_tracker, size, strength):
        self.position_tracker = position_tracker
        self.size = size
        self.strength = strength
    
    def get_field(self, x, y):
        (px, py) = self.position_tracker.get_position()        
        dy = y - py
        dx = x - px
        angle = math.atan2(dy, dx)                
        angle -= math.pi / 2
        mag = math.sqrt(dy * dy + dx * dx)        
        diff = self.size - mag
        if diff < 0:
            return (0.0, 0.0)
        power = self.strength * (diff / self.size)
        return (power * math.cos(angle), power * math.sin(angle))
        
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
        
def draw_field(fields, min_x, min_y, max_x, max_y, res_x, res_y):
    y = min_y    
    while y < max_y:
        x = min_x
        while x < max_x:
            (field_x, field_y) = fields.get_field(x, y)
            if abs(field_x) > abs(field_y):
                if field_x > 0:
                    sys.stdout.write('>')
                else:                
                    sys.stdout.write('<')
            else:
                if field_y > 0:
                    sys.stdout.write('v')
                else:
                    sys.stdout.write('^')                    
            x += (max_x - min_x) / (1.0 * res_x)
        print('')
        y += (max_y - min_y) / (1.0 * res_y)

f = field_holder()
f.add_field(infinate_constant_attractive_field(fixed_position_tracker(0, 0), 5))
f.add_field(linear_clockwise_tangential_field(fixed_position_tracker(0, 5), 5, 10))
draw_field(f, -10, -10, 10, 10, 100, 100)