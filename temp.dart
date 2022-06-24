class DartClass {
  Plus_code plus_code;
  List<Results> results;
  String status;

  DartClass({this.plus_code, this.results, this.status});

  DartClass.fromJson(Map<String, dynamic> json) {
    plus_code = json['plus_code'] != null
        ? new Plus_code.fromJson(json['plus_code'])
        : null;
    if (json['results'] != null) {
      results = new List<Results>();
      json['results'].forEach((v) {
        results.add(new Results.fromJson(v));
      });
    }
    status = json['status'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this.plus_code != null) {
      data['plus_code'] = this.plus_code.toJson();
    }
    if (this.results != null) {
      data['results'] = this.results.map((v) => v.toJson()).toList();
    }
    data['status'] = this.status;
    return data;
  }
}

class Plus_code {
  String compound_code;
  String global_code;

  Plus_code({this.compound_code, this.global_code});

  Plus_code.fromJson(Map<String, dynamic> json) {
    compound_code = json['compound_code'];
    global_code = json['global_code'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['compound_code'] = this.compound_code;
    data['global_code'] = this.global_code;
    return data;
  }
}

class Results {
  List<Address_components> address_components;
  String formatted_address;
  Geometry geometry;
  String place_id;
  Plus_code plus_code;
  List<String> types;

  Results(
      {this.address_components, this.formatted_address, this.geometry, this.place_id, this.plus_code, this.types});

  Results.fromJson(Map<String, dynamic> json) {
    if (json['address_components'] != null) {
      address_components = new List<Address_components>();
      json['address_components'].forEach((v) {
        address_components.add(new Address_components.fromJson(v));
      });
    }
    formatted_address = json['formatted_address'];
    geometry =
    json['geometry'] != null ? new Geometry.fromJson(json['geometry']) : null;
    place_id = json['place_id'];
    plus_code = json['plus_code'] != null
        ? new Plus_code.fromJson(json['plus_code'])
        : null;
    types = json['types'].cast<String>();
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this.address_components != null) {
      data['address_components'] =
          this.address_components.map((v) => v.toJson()).toList();
    }
    data['formatted_address'] = this.formatted_address;
    if (this.geometry != null) {
      data['geometry'] = this.geometry.toJson();
    }
    data['place_id'] = this.place_id;
    if (this.plus_code != null) {
      data['plus_code'] = this.plus_code.toJson();
    }
    data['types'] = this.types;
    return data;
  }
}

class Address_components {
  String long_name;
  String short_name;
  List<String> types;

  Address_components({this.long_name, this.short_name, this.types});

  Address_components.fromJson(Map<String, dynamic> json) {
    long_name = json['long_name'];
    short_name = json['short_name'];
    types = json['types'].cast<String>();
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['long_name'] = this.long_name;
    data['short_name'] = this.short_name;
    data['types'] = this.types;
    return data;
  }
}

class Geometry {
  Location location;
  String location_type;
  Viewport viewport;

  Geometry({this.location, this.location_type, this.viewport});

  Geometry.fromJson(Map<String, dynamic> json) {
    location =
    json['location'] != null ? new Location.fromJson(json['location']) : null;
    location_type = json['location_type'];
    viewport =
    json['viewport'] != null ? new Viewport.fromJson(json['viewport']) : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this.location != null) {
      data['location'] = this.location.toJson();
    }
    data['location_type'] = this.location_type;
    if (this.viewport != null) {
      data['viewport'] = this.viewport.toJson();
    }
    return data;
  }
}

class Location {
  double lat;
  double lng;

  Location({this.lat, this.lng});

  Location.fromJson(Map<String, dynamic> json) {
    lat = json['lat'];
    lng = json['lng'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['lat'] = this.lat;
    data['lng'] = this.lng;
    return data;
  }
}

class Viewport {
  Northeast northeast;
  Southwest southwest;

  Viewport({this.northeast, this.southwest});

  Viewport.fromJson(Map<String, dynamic> json) {
    northeast = json['northeast'] != null
        ? new Northeast.fromJson(json['northeast'])
        : null;
    southwest = json['southwest'] != null
        ? new Southwest.fromJson(json['southwest'])
        : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this.northeast != null) {
      data['northeast'] = this.northeast.toJson();
    }
    if (this.southwest != null) {
      data['southwest'] = this.southwest.toJson();
    }
    return data;
  }
}

class Northeast {
  double lat;
  double lng;

  Northeast({this.lat, this.lng});

  Northeast.fromJson(Map<String, dynamic> json) {
    lat = json['lat'];
    lng = json['lng'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['lat'] = this.lat;
    data['lng'] = this.lng;
    return data;
  }
}

class Southwest {
  double lat;
  double lng;

  Southwest({this.lat, this.lng});

  Southwest.fromJson(Map<String, dynamic> json) {
    lat = json['lat'];
    lng = json['lng'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['lat'] = this.lat;
    data['lng'] = this.lng;
    return data;
  }
}

class Plus_code {
  String compound_code;
  String global_code;

  Plus_code({this.compound_code, this.global_code});

  Plus_code.fromJson(Map<String, dynamic> json) {
    compound_code = json['compound_code'];
    global_code = json['global_code'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['compound_code'] = this.compound_code;
    data['global_code'] = this.global_code;
    return data;
  }
}

