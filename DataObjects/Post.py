class Post:
    def __init__(self,id,seller,model,year,color,distance,image,price,description):
        self._id = id
        self._seller = seller
        self._model = model
        self._year = year
        self._color = color
        self._distance_driven = distance
        self._image = image
        self._price = price
        self._description = description

    @property
    def id(self):
        return self._id;

    @property
    def seller(self):
        return self._seller;

    @property
    def model(self):
        return self._model;

    @property
    def year(self):
        return self._year;

    @property
    def color(self):
        return self._color;

    @property
    def distance_driven(self):
        return self._distance_driven;

    @property
    def image(self):
        return self._image;

    @property
    def price(self):
        return self._price;

    @property
    def description(self):
        return self._description;
