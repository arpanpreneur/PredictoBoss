window.onload=function () {

    var xhttp1 = new XMLHttpRequest();

    xhttp1.onload = function() {
        if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
            //document.getElementById('city').value="";
            //document.getElementById('date').value="";

            var data_string=this.responseText;
            console.log(data_string);
            data = JSON.parse(data_string);

            renderDataView(data)





        }
      };

    var url = "../latest";
    xhttp1.open("GET",url,true);

    xhttp1.send();







    var xhttp = new XMLHttpRequest();

    xhttp.onload = function() {
        if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
            //document.getElementById('city').value="";
            //document.getElementById('date').value="";

            var data_string=this.responseText;
            console.log(data_string);
            data = JSON.parse(data_string);

            var city = document.getElementById("city");
            var state= document.getElementById("state");

            for(var i in data.cities){
                console.log(city)
                var option = document.createElement("option");
                option.text = data.cities[i];
                option.value= data.cities[i];

                city.add(option);
            }

            for(var i in data.states){
                console.log(city)
                var option = document.createElement("option");
                option.text = data.states[i];
                option.value= data.states[i];

                state.add(option);
            }


        }
      };

    var url = "../lists";
    xhttp.open("GET",url,true);

    xhttp.send();




};



function sendRequest(){
    var city = document.getElementById("city").value
    var date = document.getElementById("date").value
    var state = document.getElementById("state").value

    var xhttp = new XMLHttpRequest();

    xhttp.onload = function() {
        if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
            //document.getElementById('city').value="";
            //document.getElementById('date').value="";

            var data_string=this.responseText;
            console.log(data_string);
            data = JSON.parse(data_string);
            renderDataView(data);

        }
      };

    var url = "../search";
    var query = "city="+city+"&state="+state+"&date="+date;
    xhttp.open("POST",url,true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(query);

}

function renderDataView(recv_data){


    var code_string = "<table class='table table-hover'>" +
			"<thead>" +
			"<th>Date</th>" +
			"<th>State</th>" +
			"<th>City</th>" +
			"<th>Petrol Price</th>" +
			"<th>Diesel Price</th>" +
			"</thead>";

    data=recv_data.results

    for(i in data){
        //var code_string = code_string+"<hr>"+"<strong>Date : "+data[i].date+"</strong><br>State : "+data[i].state+"<br>City : "+data[i].city+"<br>Petrol Price :"+data[i].petrol+"<br>Diesel Price : "+data[i].diesel;
        var code_string = code_string+"<tr>" +
			"<td>"+data[i].date+
			"<td>"+data[i].state+
			"<td>"+data[i].city+
			"<td>"+data[i].petrol+
			"<td>"+data[i].diesel+
			"</tr>";
    }
    code_string=code_string+"</table>";
    document.getElementById("display").innerHTML=code_string;





}