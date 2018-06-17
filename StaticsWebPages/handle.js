var cities;
window.onload=function () {

    var xhttp = new XMLHttpRequest();

    xhttp.onload = function() {
        if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
            //document.getElementById('city').value="";
            //document.getElementById('date').value="";

            var data_string=this.responseText;
            console.log(data_string);
            data = JSON.parse(data_string);

            var x = document.getElementById("city");

            for(var i in data.cities){
                console.log(city)
                var option = document.createElement("option");
                option.text = data.cities[i];
                option.value= data.cities[i];

                x.add(option);
            }


        }
      };

    var url = "http://localhost:9000/cities";
    xhttp.open("GET",url,true);

    xhttp.send();

};



function sendRequest(){
    var city = document.getElementById("city").value
    var date = document.getElementById("date").value

    var xhttp = new XMLHttpRequest();

    xhttp.onload = function() {
        if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
            document.getElementById('city').value="";
            document.getElementById('date').value="";

            var data_string=this.responseText;
            console.log(data_string);
            data = JSON.parse(data_string);
            renderDataView(data);

        }
      };

    var url = "http://localhost:9000/search?city="+city+"&&date="+date;
    xhttp.open("GET",url,true);

    xhttp.send();

}

function renderDataView(data){
    var code_string = "City : "+data.city+"<br>State : "+data.state+"<br>Date : "+data.date+"<br>Petrol Price :"+data.petrol+"<br>Diesel Price : "+data.diesel;
    document.getElementById("display").innerHTML=code_string;


}