import fields

class waypoints:
    def __init__(self, field_holder):
        self.waypoints = []
        self.field_holder = field_holder
        
    def add_waypoint(self, x, y):
        self.waypoints.append((x, y))
        if len(self.waypoints) == 1:
            self.field_holder.add_field(fields.infinate_constant_attractive_field(fields.fixed_position_tracker(x, y), 10))
        
    def get_waypoint(self):
        return self.waypoints[0]
    
    def has_waypoint(self):
        return len(self.waypoints) > 0
    
    def go_to_next_waypoint(self):    
        self.waypoints.pop(0)        
        self.field_holder.remove_attractive_fields()
        if self.has_waypoint():
            (x, y) = self.get_waypoint()
            self.field_holder.add_field(fields.infinate_constant_attractive_field(fields.fixed_position_tracker(x, y), 10))
        
w = waypoints(fields.field_holder())
w.add_waypoint(0, 0)
w.add_waypoint(1, 0)
w.add_waypoint(1, 1)
w.add_waypoint(0, 1)
w.add_waypoint(2, 1)

while w.has_waypoint():
    print(w.get_waypoint())
    fields.draw_field(w.field_holder, -2, -2, 2, 2, 100, 100)
    w.go_to_next_waypoint()