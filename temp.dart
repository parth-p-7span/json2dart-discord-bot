class Glossary {
   String title;
   Glossdiv GlossDiv;

   Glossary({this.title,this.GlossDiv});

   Glossary.fromJson(Map<String, dynamic> json) {
      title = json['title'];
      GlossDiv = json['GlossDiv'] != null ? new Glossdiv.fromJson(json['GlossDiv']) : null;
   }

   Map<String, dynamic> toJson() {
      final Map<String, dynamic> data = new Map<String, dynamic>();
      data['title'] = this.title;
      if (this.GlossDiv != null){
         data['GlossDiv'] = this.GlossDiv.toJson();
      }
      return data;
   }
}

class Glossdiv {
   String title;
   Glosslist GlossList;

   Glossdiv({this.title,this.GlossList});

   Glossdiv.fromJson(Map<String, dynamic> json) {
      title = json['title'];
      GlossList = json['GlossList'] != null ? new Glosslist.fromJson(json['GlossList']) : null;
   }

   Map<String, dynamic> toJson() {
      final Map<String, dynamic> data = new Map<String, dynamic>();
      data['title'] = this.title;
      if (this.GlossList != null){
         data['GlossList'] = this.GlossList.toJson();
      }
      return data;
   }
}

class Glosslist {
   Glossentry GlossEntry;

   Glosslist({this.GlossEntry});

   Glosslist.fromJson(Map<String, dynamic> json) {
      GlossEntry = json['GlossEntry'] != null ? new Glossentry.fromJson(json['GlossEntry']) : null;
   }

   Map<String, dynamic> toJson() {
      final Map<String, dynamic> data = new Map<String, dynamic>();
      if (this.GlossEntry != null){
         data['GlossEntry'] = this.GlossEntry.toJson();
      }
      return data;
   }
}

class Glossentry {
   String ID;
   String SortAs;
   String GlossTerm;
   String Acronym;
   String Abbrev;
   Glossdef GlossDef;
   String GlossSee;

   Glossentry({this.ID,this.SortAs,this.GlossTerm,this.Acronym,this.Abbrev,this.GlossDef,this.GlossSee});

   Glossentry.fromJson(Map<String, dynamic> json) {
      ID = json['ID'];
      SortAs = json['SortAs'];
      GlossTerm = json['GlossTerm'];
      Acronym = json['Acronym'];
      Abbrev = json['Abbrev'];
      GlossDef = json['GlossDef'] != null ? new Glossdef.fromJson(json['GlossDef']) : null;
      GlossSee = json['GlossSee'];
   }

   Map<String, dynamic> toJson() {
      final Map<String, dynamic> data = new Map<String, dynamic>();
      data['ID'] = this.ID;
      data['SortAs'] = this.SortAs;
      data['GlossTerm'] = this.GlossTerm;
      data['Acronym'] = this.Acronym;
      data['Abbrev'] = this.Abbrev;
      if (this.GlossDef != null){
         data['GlossDef'] = this.GlossDef.toJson();
      }
      data['GlossSee'] = this.GlossSee;
      return data;
   }
}

class Glossdef {
   String para;
   List<String> GlossSeeAlso;

   Glossdef({this.para,this.GlossSeeAlso});

   Glossdef.fromJson(Map<String, dynamic> json) {
      para = json['para'];
      GlossSeeAlso = json['GlossSeeAlso'].cast<String>();
   }

   Map<String, dynamic> toJson() {
      final Map<String, dynamic> data = new Map<String, dynamic>();
      data['para'] = this.para;
      data['GlossSeeAlso'] = this.GlossSeeAlso;
      return data;
   }
}

