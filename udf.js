function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.id = values[0];
    obj.FirstName = values[1];
    obj.LastName = values[2];
    obj.Email = values[3];
    obj.Age = values[4];
    obj.Gender = values[5];
    obj.Location = values[6];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }