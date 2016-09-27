from city_model import CityModel


# For the time being, the city will be our Gazebo world
class City(CityModel):
    def __init__(self, name=None):
        super(City, self).__init__(name)
        self.ground_plane = None
        self.roads = []
        self.blocks = []
        self.buildings = []

    def add_ground_plane(self, ground_plane):
        self.ground_plane = ground_plane

    def add_road(self, road):
        self.roads.append(road)

    def add_block(self, block):
        self.blocks.append(block)

    def add_building(self, building):
        self.buildings.append(building)

    def template(self):
        return """
        <?xml version="1.0" ?>
        <sdf version="1.5">
          <world name="{{model.name}}">
            <include>
              <uri>model://sun</uri>
            </include>
            {{model.ground_plane.to_sdf()}}
            {% for road in model.roads %}
              {{road.to_sdf()}}
            {% endfor %}
            {% for block in model.blocks %}
              {{block.to_sdf()}}
            {% endfor %}
            {% for building in model.buildings %}
              {{building.to_sdf()}}
            {% endfor %}
          </world>
        </sdf>"""
