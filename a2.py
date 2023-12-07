import a2_support
import constants
from a2_support import *
from typing import Optional


class Entity:
    id = a2_support.ENTITY

    """
    Abstract base class for any entity. Provides base functionality for all entities in the game.
    """

    def get_class_name(self) -> str:
        """
        Return the class name of this entity’s class.

    Parameters: represent instance access variables in class Entity
    Return:  a string variable i.e'Entity"
        """
        return self.__class__.__name__

    def get_id(self) -> str:
        """
        Return the single character id of this entity’s class.

    Parameters: represent instance access variables in class Entity
    Return: a string variable i.e "E"
        """
        return self.id

    def __str__(self) -> str:
        """
        Return the string representation for this Entity

    Parameters: represent instance access variables in class Entity
    Return: a string representation i.e 'E'
        """
        return str(self.get_id())

    def __repr__(self):
        """
        Return the text that would be required to make a new instance of this class .

    Parameters: represent instance access variables in class Entity
    Return: new instance of this class name i.e 'Entity()'
        """
        return f'{self.get_class_name()}()'


class Plant(Entity):
    id = a2_support.PLANT
    """
    Inherits from Entity
    Plant is an Entity that is planted by the user. A plant has water and health points
    (HP) which start at 10, age starting at 0, and no repellent.
    """

    def __init__(self, name: str):
        """
        Setup default value the plant with a given plant name, water level ,health level,repellent and age.
        """
        self._health_amount = 10
        self._water = 10.0
        self._plant_name = name
        self._plant_repellent = False
        self._plant_age = 0

    def get_name(self) -> str:
        """
        Return name of the plant.

    Parameters: represent instance access variables in class Plant
    Return: a string variable i.e 'Rebutia'
        """
        return self._plant_name

    def get_health(self) -> int:
        """
        Return the plant’s current HP.

    Parameters: represent instance access variables in class Plant
    Return: an integer variable i.e '10'
        """
        return self._health_amount

    def get_water(self) -> float:
        """
        Return the water levels of the plant.

    Parameters: represent instance access variables in class Plant
    Return: an integer variable i.e '10.0'
        """
        return self._water

    def water_plant(self) -> None:
        """
        Add to the plant’s water level by 1.

    Parameters: represent instance access variables in class Plant
    Return: None specific variables
        """
        self._water += 1

    def get_drink_rate(self) -> float:
        """
         Return water drinking rate of the plant

    Parameters: represent instance access variables in class Plant
    Return: a float variable i.e '0.1'
        """
        return PLANTS_DATA.get(self._plant_name).get('drink rate')

    def get_sun_levels(self) -> tuple[int, int]:
        """
        Return the acceptable sun level of the plant with the lower and upper range.

    Parameters: represent instance access variables in class Plant
    Return: a tuple variable
            tuple[0]: integer of sum_lower rate
            tuple[1]: integer of sun_upper rate
        """
        low_sun = PLANTS_DATA.get(self._plant_name).get('sun-lower')
        high_sun = PLANTS_DATA.get(self._plant_name).get('sun-upper')
        sun_level = (low_sun, high_sun)
        return sun_level

    def decrease_water(self, amount: float):
        """
        Decrease the plants' water by a specified amount.

    Parameters: a float variable of amount with given
    Return: a float variable of decreased water rate
        """
        self._water -= amount

    def drink_water(self):
        """
        Reduce water levels by plant’s drink rate. If water levels is zero the plant’s HP
        reduces by 1.

    Parameters: represent instance access variables in class Plant
    Return: the water rate got under this condition
        """
        if self._water == 0:
            self.decrease_health()
        self._water -= self.get_drink_rate()

    def add_health(self, amount: int) -> None:
        """
        Add to the plant’s health levels by a specified amount.

    Parameters: an integer variable of amount with given
    Return: add health rate with given amount
        """
        self._health_amount += amount

    def decrease_health(self, amount: int = 1):
        """
        Decrease the plants' health by a specified amount, decrease by 1 by default.

    Parameters: an integer variable of amount 1
    Return: add health rate by 1
        """
        self._health_amount -= amount

    def set_repellent(self, applied: bool) -> None:
        """
        Apply or remove repellent from plant.

    Parameters: boolean variable applied
    Return: if ture that applied otherwise false
        """
        if applied is True:
            self._plant_repellent = True
        elif applied is False:
            self._plant_repellent = False

    def has_repellent(self) -> bool:
        """
        Return True if the plant has repellent, False otherwise.

    Parameters: represent instance access variables in class Plant
    Return: boolean variable if set repellent return true otherwise false
        """
        if self._plant_repellent is True:
            return True
        else:
            if self._plant_repellent is False:
                return False

    def get_age(self) -> int:
        """
        Return how many days this plant has been planted.

    Parameters: represent instance access variables in class Plant
    Return: get an integer of plant of age i.e ' 1'
        """
        return self._plant_age

    def increase_age(self):
        """
        Increase the number of days this plant has been planted by 1.

    Parameters: represent instance access variables in class Plant
    Return: increase plant age by 1
        """
        self._plant_age += 1

    def is_dead(self) -> bool:
        """
        Return True if the plant’s health is less than or equals to zero, False otherwise.

    Parameters: represent instance access variables in class Plant
    Return: a boolean variable if health_rate lower than 0 return True otherwise False that not dead
        """
        if self._health_amount <= 0:
            return True
        else:
            return False

    def __repr__(self):
        """
        plant format with i.e Plant('Rebutia')

    Parameters: represent instance access variables in class Plant
    Return: Return the textto make a new instance of this class i.e ' Plant('Rebutia')'

        """
        return f"{self.get_class_name()}('{self._plant_name}')"

    @property
    def plant_name(self):
        return self._plant_name


class Item(Entity):
    id = a2_support.ITEM
    """
    Inherits from Entity
    Abstract subclass of Entity which provides base functionality for all items in the game.
    """

    def apply(self, plant: 'Plant') -> None:
        """
        Applies the items effect, if any, to the given plant. Raise NotImplementedError.

    Parameters: the plant of Item
    Return:  raises error applies the item effect
        """
        raise NotImplementedError()


class Water(Item):
    id = a2_support.WATER

    """
    Inherits from Item   
    """

    def apply(self, plant: 'Plant') -> None:
        """
        Adds to plant’s water level by 1 when applied.

    Parameters: the plant of Water
    Return:  Adds to plant’s water level by 1 for applied
        """
        plant.water_plant()


class Fertiliser(Item):
    id = a2_support.FERTILISER
    """
    Inherits from Item
    """

    def apply(self, plant: 'Plant') -> None:
        """
        Adds to plant’s health by 1 when applied

    Parameters: the plant of Fertiliser
    Return:  Adds to plant’s health rate level by 1 for applied
        """
        plant.add_health(1)


class PossumRepellent(Item):
    id = a2_support.POSSUM_REPELLENT
    """
    Inherits from Item
    """

    def apply(self, plant: 'Plant') -> None:
        """
        Cancel a possum attach when applied.

    Parameters: the plant of PossumRepellent
    Return:  Cancel a possum attach for applied
        """
        plant._plant_repellent = True


class Inventory:
    """
    An Inventory contains and manages a collection of items and plant.
    """

    def __init__(self, initial_items: Optional[list[Item]] = None,
                 initial_plants: Optional[list[Plant]] = None) -> None:
        """
        Sets up initial inventory. If no initial_items or initial_plants are provided,
        inventory starts with an empty dictionary for the entities. Otherwise, the initial
        dictionary is set up from the initial_items and initial_plants lists to be a
        dictionary mapping entity names to a list of entity instances with that name.
        """
        self._item_inventory = {}
        self._plant_inventory = {}
        self._white_space = " "

        if initial_items is not None:
            for item in initial_items:
                self.add_entity(item)

        if initial_plants is not None:
            for plant in initial_plants:
                self.add_entity(plant)

    def add_entity(self, entity: Item | Plant) -> None:
        """
        Adds the given item or plant to this inventory’s collection of entities.

    Parameters:
        entity: entity either is Item or Plant
    Return:  add stuffs in either Item or Plant ,if None return None
        """

        if isinstance(entity, Item):
            # new key - add a new list
            if entity.get_id() in self._item_inventory:
                self._item_inventory[entity.get_id()].append(entity)
            else:
                self._item_inventory.update(
                    {entity.get_id(): [entity]})  # key already exists - append to the existing list
        else:
            if isinstance(entity, Plant):
                if entity.get_name() in self._plant_inventory:  # new key - add a new list
                    self._plant_inventory[entity.get_name()].append(entity)
                else:  # key already exists - append to the existing list
                    self._plant_inventory.update({entity.get_name(): [entity]})

    def get_entities(self, entity_type: str) -> dict[str, list[Item | Plant]]:
        """
        Returns the dictionary mapping entity (item or plant) names to the instances of
        the entity with that name in the inventory, respectively.

    Parameters:
        entity_type: a string variable either 'Plant' or 'Item'
    Return: dictionary with their type id (String) and stuffs belongs(List) i.e '{'W': [Water()], 'F': [Fertiliser()]}'
        """

        if entity_type == 'Plant':
            return self._plant_inventory

        else:
            return self._item_inventory

    def remove_entity(self, entity_name: str) -> Optional[Item | Plant]:
        """
        Removes one instance of the entity (item or plant) with the given name from inventory,if one exists.

    Parameters: the name of Item or Plant
    Return: show the instance with given Item or Plant being removed
        """
        if entity_name in self.get_entities('Plant'):
            plant_item = self.get_entities('Plant')[entity_name]
            remove_plant = plant_item.pop()
            if not plant_item:  # not exist just back
                self.get_entities('Plant').pop(entity_name)
            return remove_plant
        if entity_name in self.get_entities('Item'):
            item_item = self.get_entities('Item')[entity_name]
            remove_item = item_item.pop()
            if not item_item:  # not exist just back
                self.get_entities('Item').pop(entity_name)
            return remove_item

    def __str__(self):
        """
        Returns a string containing information about quantities of items available in the inventory.

    Parameters: represent instance access variables in class Inventory
    Return: a string representation i.e ' F: 1 \n Rebutia: 1 \n Monstera: 1 \n FiddleLeafFig: 1 '
        """
        items_plants = list()  # define a list put two strings into one list
        for key_i in self._item_inventory:
            items_l = f"{key_i}:{self._white_space}{len(self._item_inventory.get(key_i))}"
            items_plants.append(items_l)

        for key_p in self._plant_inventory:
            plant_l = f"{key_p}:{self._white_space}{(len(self._plant_inventory.get(key_p)))}"
            items_plants.append(plant_l)

        return '\n'.join(items_plants)

    def __repr__(self):
        """
        Return a string that could be copied and pasted to construct a new Room instance with the same name as
        this Room instance.

    Parameters: represent instance access variables in class Inventory
    Return:
        i.e 'Inventory(initial_items=[Water(), Fertiliser()], initial_plants=[Plant('Rebutia'),
    Plant('Rebutia'), Plant('Monstera')])'
        """

        item_list = []
        for value_items in self._item_inventory.values():  # items list
            for items in value_items:
                item_list.append(items)  # add all values of Items to new list

        plant_list = []
        for values_plant in self._plant_inventory.values():  # plant list
            for plant_items in values_plant:
                plant_list.append(plant_items)  # add all values of Plants to new list

        return f"{self.__class__.__name__}(initial_items={list(item_list)}, initial_plants={list(plant_list)})"


class Pot(Entity):
    id = a2_support.POT
    """
    Pot is an Entity that has growing conditions information and an instance of plant.
    """

    def __init__(self) -> None:

        self._sun_m = None
        self._sun_l = None
        self._evaporation = None
        self._sun_range = None
        self._plant = None
        super().get_class_name()  # Entity's function

    def set_sun_range(self, sun_range: tuple[int, int]) -> None:
        """
        Sets the sun range experienced by the pot.

    Parameters:
        sun_range: tuple variable sun level start from tuple[0] to tuple[1]
    Return: the range of sun level ,None if no set
        """
        self._sun_range = sun_range

    def get_sun_range(self) -> tuple[int, int]:
        """
        Returns the sun range experienced by the pot.

    Parameters: represent sun_range in class Pot
    Return: a tuple variable the range of sun level
        """
        return self._sun_range

    def set_evaporation(self, evaporation: float) -> None:
        """
        Sets the evaporation rate of the pot.

    Parameters:
        evaporation: the float variable of evaporate
    Return: if plant has evaporation show rate otherwise None

        """
        self._evaporation = evaporation

    def get_evaporation(self) -> float:
        """
        Returns the evaporation rate of the pot.

    Parameters: represent evaporation rate in class Pot
    Return: floats of plants evaporation rate

        """
        return self._evaporation

    def put_plant(self, plant: Plant) -> None:
        """
        Adds an instance of a plant to the pot.

    Parameters:
        plant:the plant ready to put
    Return: defined plant need put , otherwise None

        """
        self._plant = plant

    def look_at_plant(self) -> Optional[Plant]:
        """
        Returns the plant in the pot and without removing it.

    Parameters: represent all plants in class Pot
    Return: list of plants on pot , if no plants show None
        """

        return self._plant

    def remove_plant(self) -> Optional[Plant]:
        """
        Returns the plant in the pot and removes it from the pot.

    Parameters: represent all remove plants in class Pot
    Return:list of plants remove from pot , if no plants remove then None
        """
        plant = self.look_at_plant()
        self._plant = None
        return plant  # return to check what plant that removed

    def progress(self) -> None:
        """
        Progress the state of the plant and check if the current plant is suitable in the given
        conditions. Decrease the plant’s water levels based on the evaporation. The health
        of the plant should decrease by 1:
        • If the sun is not in a suitable range
        • If the plant’s water levels is below zero.
        curr_sun_lower <= plant_sun_lower <= curr_sun_upper AND curr_sun_lower <= plant_sun_upper <= curr_sun_upper

    Parameters: represent  plants actions and text  in class Pot
    Return: under some specific conditions of plants

        """
        plant_sun_lower = self.look_at_plant().get_sun_levels()[0]
        plant_sun_upper = self.look_at_plant().get_sun_levels()[1]

        self._plant.decrease_water(self._evaporation + self._plant.get_drink_rate())
        if self.look_at_plant().get_water() <= 0:
            self._plant.decrease_health()

        if self._sun_range[0] not in range(plant_sun_lower, plant_sun_upper) and self._sun_range[1] not in \
                range(plant_sun_lower, plant_sun_upper):
            self._plant.decrease_health()
            if not self.look_at_plant().is_dead():  # only print live plant when sun level not suitable
                print(f"Poor {self.look_at_plant().get_name()} dislikes the sun levels.")
        if self.look_at_plant().get_health() <= 0:
            print(f"{self.look_at_plant().plant_name} is dead")

    def animal_attack(self) -> None:
        """
        Decreases the health of the plant by the animal attack damage dealt if a plant is in the pot .

        Attack should fail if plant has animal repellent. It should not affect the plant’s health .

    Parameters: represent  plants get animal_attack reaction in class Pot
    Return : plants get animal attack reaction , if no animal_attack to plant then None
        """
        if self._plant is not None and self.look_at_plant().has_repellent() is False:
            self.look_at_plant().decrease_health(ANIMAL_ATTACK_DAMAGE)  # in pot no repellent

            print(f"There has been an animal attack! Poor {self.look_at_plant().get_name()}.")
        else:
            if self._plant is not None and self.look_at_plant().has_repellent() is True:  # in pot has repellent
                print(f"There has been an animal attack! But luckily the {self.look_at_plant().get_name()} has "
                      f"repellent.")

    def __str__(self) -> str:
        """
        Return the string representation of this pot.

    Return: i.e 'Pot'
        """
        return str(self.get_class_name())

    def __repr__(self):
        """
        Returns a string that could be used to construct a new instance of Inventory containing the same items as
        self currently contains.

    Return:i.e' Pot()'
        """
        return f"{self.get_class_name()}()"


class Room:
    def __init__(self, name):
        """
        Set up an empty room of given room name
        """
        self._room_name = name
        self._name_room_items = ROOM_LAYOUTS.get(name)
        self._pot_position = ROOM_LAYOUTS.get(name).get('Position')
        self._position = {}
        self._class_name = self.__class__.__name__
        self._pots_position = {0: Pot(), 1: Pot(), 2: Pot(), 3: Pot()}

    def init_positions(self):
        """
        Set up an empty room of given room name. Note: Make use of constants.py.

    Parameters: represent plants in Room
    Return:set initial position of plants
        """
        for num_position, point in enumerate(ROOM_LAYOUTS.get(self._room_name).get('positions').values()):
            self._position[num_position] = point

        return self._position

    def get_plants(self) -> dict[int, Plant | None]:
        """
        Return the Plant instances in this room. with the keys being the positions and value
        being the corresponding plant, None if no plant is in the position.

    Parameters: represent plants in Room
    Return: a dictionary variable of plants and with their position
        """
        keys = self.init_positions().keys()
        room_plant = dict.fromkeys(keys)  # dictionary with initial position's key

        for k in self.init_positions().keys():
            if self._pots_position.get(k).look_at_plant() is not None:
                room_plant.update({k: self._pots_position.get(k).look_at_plant()})
            else:
                room_plant.update({k: None})  # none to change the value to none of it position

        return room_plant

    def get_number_of_plants(self) -> int:
        """
        Return the total number of live plants in the room.

    Parameters: represent number of live plants in Room
    Return: integer of number of live plants exist
        """
        num = 0
        for key in self.get_plants():
            if self.get_plants().get(key) is not None and not self.get_plants().get(key).is_dead():  # count live plants
                num += 1
            return num

    def add_pots(self, pots: dict[int, Pot]) -> None:
        """
        Add a pots to the room. Each key corresponds to a position in the room, with each
        value being an instance of a pot.
    Parameters:
        pots: a dictionary variable that pot should be added in which position
    Return : add pots by key corresponds to a position in room ,otherwise None
        """
        for pot_key, value in pots.items():
            self._pots_position.update({pot_key: value})

    def get_pots(self) -> dict[int, Pot]:
        """
        Return all pots within the room.

    Parameters: represent number of pots in Room
    Return: a dictionary variable get all pots with their position in room
        """
        return self._pots_position

    def get_pot(self, position: int) -> Pot:
        """
        Return the Pot instance at the given position.

    Parameters:
        position: integer of position
    Return: the pot with given position
        """
        return self._pots_position.get(position)

    def add_plant(self, position: int, plant: Plant):
        """
       Add a plant instance to Pot at a given position if no plant exist at that position. Do
       nothing if a plant is already there. The given position can be 0, 1, 2, or 3.

    Parameters:
        position: integer of position that plant should be added into
        plant: the plants should be added
    Return:
        plants add the given position
        """
        position_pot = self.get_pot(position)
        if position_pot.look_at_plant() is None:  # no plant exist put plant in any empty pot
            return position_pot.put_plant(plant)

    def get_name(self) -> str:
        """
        Return the name of this room instance.

    Parameters: represent room name
    Return :string of room name
        """
        return self._room_name

    def remove_plant(self, position: int) -> Plant | None:
        """
        Return a Plant at a given position from a Pot, None if no plant exists.

    Parameters:
        position : integer of plant needs to be removed in this position
    Return:
        Removes the plant from a pot at the given position.
        """
        if self.get_pot(position).look_at_plant() is not None:  # remove not empty plant
            return self.get_pot(position).remove_plant()
        else:
            return None  # no plant exist no remove required

    def progress_plant(self, pot: Pot) -> bool:
        """
        Return True if pot is not empty and triggers a given pot to check on plant condition and plant to age.
        False if pot is empty.

    Parameters:
        pot: the pots that plant put in
        """
        if pot.look_at_plant() is None:  # no plant exist
            return False
        else:
            pot.progress()
            pot.look_at_plant().increase_age()  # check on plant condition and plant to age for future function
            return True

    def progress_plants(self) -> None:
        """
        Trigger the pots to check on plant conditions and plants to age.

    Parameters: represent progress_plants
        """
        for num_position in self._pots_position:
            self.progress_plant(self._pots_position[num_position])

    def __str__(self) -> str:
        """
        Return the string representation of this room.i.e 'Bedroom'
        """
        return str(self._room_name)

    def __repr__(self) -> str:
        """
        Return a string that could be copied and pasted to construct a new Room instance i.e'Room('Bedroom')'
        """
        return f"{self._class_name}('{self._room_name}')"


class OutDoor(Room):
    def progress_plant(self, pot: Pot) -> bool:
        """
        Checks to see if an animal attack has occurred.

    Parameters:
          pot: the pot that plant progress
    Return: boolean variable:
        True if pot is not empty and triggers a given pot to check on plant condition and plant to age.
        False if pot is empty.
        """

        if super().progress_plant(pot):  # check if true or not above functions did this job
            if dice_roll():  # if pot is empty or not check attack
                pot.animal_attack()
        return super().progress_plant(pot)


def load_house(filename: str) -> tuple[list[tuple[Room, str]], dict[str, int]]:
    """ Reads a file and creates a dictionary of all the Rooms.
    
    Parameters:
        filename: The path to the file
    
    Return:
        A tuple containing 
            - a list of all Room instances amd their room name,
            - and a dictionary containing plant names and number of plants
    """
    rooms = []
    plants = {}
    items = {}
    room_count = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('Room'):
                _, _, room = line.partition(' - ')
                name, room_number = room.split(' ')
                room_number = int(room_number)
                if room_count.get(name) is None:
                    room_count[name] = 0
                room_count[name] += 1
                if ROOM_LAYOUTS.get(name).get('room_type') == 'Room':
                    room = Room(name)
                elif ROOM_LAYOUTS.get(name).get('room_type') == 'OutDoor':
                    room = OutDoor(name)
                rooms.append((room, name[:3] + str(room_count[name])))
                row_index = 0

            elif line.startswith('Plants'):
                _, _, plant_names = line.partition(' - ')
                plant_names = plant_names.split(',')
                for plant in plant_names:
                    plant = plant.split(' ')
                    plants[plant[0]] = int(plant[1])

            elif line.startswith('Items'):
                _, _, item_names = line.partition(' - ')
                item_names = item_names.split(',')
                for item in item_names:
                    item = item.split(' ')
                    items[item[0]] = int(item[1])

            elif len(line) > 0 and len(rooms) > 0:
                pots = line.split(',')
                positions = {}
                for index, pot in enumerate(pots):
                    sun_range, evaporation_rate, plant_name = pot.split('_')
                    pot = Pot()
                    if plant_name != 'None':
                        pot.put_plant(Plant(plant_name))
                    sun_lower, sun_upper = sun_range.split('.')
                    pot.set_evaporation(float(evaporation_rate))
                    pot.set_sun_range((int(sun_lower), int(sun_upper)))
                    positions[index] = pot
                rooms[-1][0].add_pots(positions)
                row_index += 1

    return rooms, plants, items


class Model:
    """
    This is the model class that the controller uses to understand and mutate the house
state. The model keeps track of multiple Room instances and an inventory.
    """

    def __init__(self, house_file: str):
        """
        Sets up the model from the given house_file, which is a path to a file containing
house information (e.g. houses/house1.txt).
        """
        self._days = 1
        self._house_file = house_file
        rooms, plants, items_i = load_house(house_file)
        self._room_dict = {}
        self._room_list_house = list()
        for room_t in rooms:  # to {'Bal1': OutDoor('Balcony'), 'Bed1': Room('Bedroom')}
            self._room_dict.update({room_t[1]: room_t[0]})
        for room_l in rooms:
            self._room_list_house.append(room_l[0])  # get list of all rooms
        # set_up initial_items
        self._ini_items = list()
        # set_up initial_plants
        self._ini_plants = list()
        self._plants_name = list()
        for k_name in PLANTS_DATA:  # get plants name
            self._plants_name.append(k_name)

        for key, values in items_i.items():  # initial items
            if key == 'F':
                for f in range(values):
                    self._ini_items.append(Fertiliser())
            if key == 'W':
                for w in range(values):
                    self._ini_items.append(Water())

            if key == 'R':
                for r in range(values):
                    self._ini_items.append(PossumRepellent())

        for plant_key, plant_values in plants.items():  # initial plants
            for p_i in range(len(PLANTS_DATA)):
                if plant_key == self._plants_name[p_i]:
                    for p_j in range(plant_values):
                        self._ini_plants.append(Plant(plant_key))

        self._inventory = Inventory(self._ini_items, self._ini_plants)
        self._num_plants = 0
        if self._days == 1:
            self.start_num_plants = self.get_number_of_plants_alive()

    def get_rooms(self) -> dict[str, Room]:
        """
        Returns all rooms with room name as keys with a corresponding room instance.

    Parameters: represent rooms in Model
    Return : a dictionary contains dict[str, Room]:
    all rooms with room name as keys with a corresponding room instance
        """
        return self._room_dict  # {'Bal1': OutDoor('Balcony'), 'Bed1': Room('Bedroom')}

    def get_all_rooms(self) -> list[Room]:
        """
        a list of all the room instances.

    Parameters: represent all rooms in Model
    Return : list of all room in model
        """
        return self._room_list_house  # [OutDoor('Balcony'), Room('Bedroom')]

    def get_inventory(self) -> Inventory:

        """
        Returns the inventory

    Parameters: represent inventory in Model
        """
        return self._inventory

    def get_days_past(self) -> int:
        """
        Returns the number of days since the start.

    Parameters: represent plants that past days in Model
        """
        return self._days

    def next(self, applied_items: list[tuple[str, int, Item]]) -> None:
        """
        Move to the next day, if there are items in the list of applied items (room name,
        position, item to be applied) then apply all affects. Add fertiliser and possum
        repellent to the inventory every 3 days. Progress all plants in all rooms.

    Parameters:
        applied_items: list of applied items (str(room name),int(position),Item)to be applied
    Return : applied items (str(room name),int(position),Item) in next day
        """

        for items_app in applied_items:
            if items_app[2] is not None:  # remove Item if exist just keep Plants
                items_app[2].apply(self.get_rooms().get(items_app[0]).get_pot(items_app[1]).look_at_plant())
                self.get_inventory().remove_entity(str(items_app[2]))
        if self._days % 3 == 0:  # In every 3 days
            self.get_inventory().add_entity((Fertiliser()))  # Add fertiliser
            self.get_inventory().add_entity(PossumRepellent())  # Add possum repellent
        for room in self.get_all_rooms():
            room.progress_plants()
        self._days += 1  # next day

    def move_plant(self, from_room_name: str, from_position: int,
                   to_room_name: str, to_position: int) -> None:
        """
        Move a plant from a room at a given position to a room with the given position.

    Parameters:
        from_position: the position of plant need to move
        from_room_name: the room  name of plant current stay
        to_position: the position that plant need to be moved
        to_room_name: the room name that plant should go
    Return : a plant from a room at a given position to a room with the given position, otherwise None
        """
        plant = self.get_rooms()[from_room_name].get_pot(from_position).look_at_plant()
        if plant is not None:
            self.get_rooms()[from_room_name].remove_plant(from_position)
        to_position_pot = self.get_rooms()[to_room_name].get_pot(to_position)
        # add plant in empty pot
        if to_position_pot.look_at_plant() is None:
            self.get_rooms()[to_room_name].add_plant(to_position, plant)

    def plant_plant(self, plant_name: str, room_name: str,
                    position: int) -> None:
        """
        Plant a plant in a room at a given position.

    Parameters:
        plant_name: plants' name  to plant
        room_name: plants need to plant in which room 's name
        position: plants need to plant which position
    Return : Plant a plant in a room at a given position , otherwise None
        """
        plant = Plant(plant_name)  # get plant from plant_name
        rooms_model = self.get_rooms()
        if rooms_model is not None:
            room = rooms_model.get(room_name)  # get room name
            room.add_plant(position, plant)  # add plant in exist room

    def swap_plant(self, from_room_name: str, from_position: int,
                   to_room_name: str, to_position: int) -> None:
        """
        Swap the two plants from a room at a given position to a room with the given position.

    Parameters:
         from_position: the position that one plants current stay
         from_room_name: the room that one plant current stay
         to_position: the  position that another plants current stay
         to_room_name:the  room that another plants current stay
    Return : the plant position swap

        """
        to_plant_name = self.get_rooms().get(to_room_name).get_pot(to_position).look_at_plant().get_name()
        self.get_rooms().get(to_room_name).remove_plant(to_position)  # remove plant of to_position to none
        self.move_plant(from_room_name, from_position, to_room_name, to_position)  # switch plant position
        self.plant_plant(to_plant_name, from_room_name, from_position)  # put to_position_plant in swap position

    def get_number_of_plants_alive(self) -> int:
        """
        Get the number of plants that are alive in all rooms.

    Parameters: represent number of live plants in Model
    Return : the number of plants that are alive in all rooms
        """
        self._num_plants = 0
        for all_room_model in self.get_all_rooms():
            self._num_plants += all_room_model.get_number_of_plants()  # get all live plants
        return self._num_plants

    def has_won(self) -> bool:
        """
        Return True if number of plants alive > 50% of number from start of the 15-day period. And 15 days has passed.
        """

        if self.get_days_past() >= 15:
            plant_remain = self.get_number_of_plants_alive()
            if self.start_num_plants * 0.5 < plant_remain:
                return True
        return False

    def has_lost(self) -> bool:
        """
        Return True if number of plants alive < 50% of number from start of the 15 days period.
        """
        if self.has_won():
            return False
        return True

    def __str__(self):
        """
        Returns the text required to construct a new instance of Model with the same game file used to construct self.
        """
        # str(model) == "Model('houses/house2.txt')"
        return str(f"{self.__class__.__name__}('{self._house_file}')")

    def __repr__(self):
        """
        Does the same thing as __str__.
        """
        # repr(model) == "Model('houses/house2.txt')"
        return f"{self.__class__.__name__}('{self._house_file}')"


class GardenSim:
    """
    """

    def __init__(self, house_file: str, view: View):
        """
        Creates a new GardenSim house with the given view and a new Model instantiated using the given house_file.
        """
        self.file = house_file
        self._model_garden = Model(house_file)
        self._view = view
        self.input = ['ls', 'm', 'p', 'w', 'a', 's', 'rm', 'n']

    def play(self):
        """ Executes the entire game until a win or loss occurs. """
        while True:
            user_move_input = input('Enter a Move:').split()

            if user_move_input[0] in self.input:
                if len(user_move_input) == 1 and user_move_input[0] == 'ls':
                    self._view.display_rooms(self._model_garden.get_rooms())
                if len(user_move_input) == 3 and user_move_input[0] == 'ls':
                    self._view.display_room_position_information({self._model_garden.get_rooms().get(
                        user_move_input[1]), self._model_garden.get_rooms().
                    get(user_move_input[1]).get_pot(user_move_input[2])},
                        user_move_input[2], self._model_garden.get_rooms().
                    get(user_move_input[1]).get_plants())
                if len(user_move_input) == 5 and user_move_input[0] == 'm':
                    self._model_garden.move_plant(user_move_input[1], int(user_move_input[2]),
                                                  user_move_input[3], int(user_move_input[4]))
                if len(user_move_input) == 4 and user_move_input[0] == 'p':
                    self._model_garden.plant_plant(user_move_input[1], user_move_input[2], int(user_move_input[3]))
                if len(user_move_input) == 3 and user_move_input[0] == 'w':
                    self._model_garden.get_rooms().get(user_move_input[1]).get_pot(int(user_move_input[2])). \
                        look_at_plant().water_plant()
                if len(user_move_input) == 4 and user_move_input[0] == 'a':
                    self._model_garden.get_inventory().add_entity(self._model_garden.get_inventory().add_entity())

            else:
                print(f'move not found : {user_move_input[0]}')
                self._view.draw(self._model_garden.get_all_rooms())

        pass


def main():
    """ Entry-point to gameplay """
    view = View()
    house_file = input('Enter house file: ')
    garden_gnome = GardenSim(house_file, view)
    garden_gnome.play()


if __name__ == '__main__':
    main()
