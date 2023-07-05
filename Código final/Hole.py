class Hole:
    def __init__(self, name, x, y, radius):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius

    def isPointInside(self, point_x, point_y):
            dist_x = point_x - self.x if point_x > self.x else self.x - point_x
            dist_y = point_y - self.y if point_y > self.y else self.y - point_y

            distance = dist_x**2 + dist_y**2

            if distance < self.radius**2:
                return True
            else:
                return False
            
    def areCirclesSuperimposed(self, point_x, point_y, radius):
        dist_x = point_x - self.x if point_x > self.x else self.x - point_x
        dist_y = point_y - self.y if point_y > self.y else self.y - point_y

        distance = dist_x**2 + dist_y**2
        somme_rayons = radius + self.radius

        if distance <= somme_rayons**2:
            return True
        else:
            return False
