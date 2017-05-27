import fields

class waypoints:
    def __init__(self, field_holder):
        self.waypoints = []
        self.field_holder = field_holder

    def add_waypoint(self, x, y, strength):
        self.waypoints.append((x, y, strength))
        if len(self.waypoints) == 1:
            self.field_holder.add_field(fields.infinate_constant_attractive_field(fields.fixed_position_tracker(x, y), strength))
            
    def get_waypoint(self):
        return self.waypoints[0]

    def has_waypoint(self):
        return len(self.waypoints) > 0

    def go_to_next_waypoint(self):
        self.waypoints.pop(0)
        self.field_holder.remove_attractive_fields()
        if self.has_waypoint():
            (x, y, strength) = self.get_waypoint()
            self.field_holder.add_field(fields.infinate_constant_attractive_field(fields.fixed_position_tracker(x, y), strength))
