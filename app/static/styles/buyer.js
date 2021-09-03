

$("#inputbuyerstate").change(function(){
  var StateSelected = $(this).val();
  $.ajax({
    type: "POST",
    url: "/buyergetdatabystate",
    data: JSON.stringify(StateSelected),
    contentType: "application/json",
    dataType: 'json',
    success: function(result) {
    //   console.log("Result:");
      console.log(result);
      table(result);
    } 
  });

});




function table(data){
    var htmlstring='<table style="background-color:white;" class="table table-hover  text-center"><thead><tr><th scope="col">ID</th>'+
                                              '<th scope="col">STATE</th>'+
                                              '<th scope="col">DISTRICT</th>'+
                                              '<th scope="col">CROP</th>'+
                                              '<th scope="col">CROP MINIMUM PRICE(IN RUPEES.)</th>'+
                                              '<th scope="col">AVAILABLE CROP QUANTITY(IN TONNES)</th>'+
                                              '<th scope="col"></th>'+
                                              '</tr></thead><tbody>'

    for (var property in data) {
        var crop=data[property]['CROP'];
        var farmid=data[property]['FARM_ID'];
        htmlstring+='<tr id="'+data[property]['UNIQUE_ID'] +'">'+
                        '<th scope="row">'+ data[property]['UNIQUE_ID']+'</th>'+
                        '<td>'+ data[property]['STATE'] +'</td>'+
                        '<td>'+ data[property]['DISTRICT'] +'</td>'+
                        '<td>'+ data[property]["CROP"] +'</td>'+
                        '<td>'+ data[property]['CROP_MIN_PRICE'] +'</td>'+
                        '<td>'+ data[property]['CROP_MIN_PRICE']+'</td>'+ 
                        '<td><button type="button" class="btn btn-md btn-primary" onclick=' +'"changedata('+ property + ",'"+crop+"'," + farmid+ ","+ data[property]['CROP_MIN_PRICE'] + ","+ data[property]['CROP_MIN_PRICE']+ ")"+'"' + 'data-bs-toggle="modal" data-bs-target="#staticBackdrop">Buy</button></td>'+                           
                    '</tr>'
        }
    htmlstring += '</tbody></table>'
    $("#datafromfarmer").html(htmlstring);

}

$(document).ready(function(){
    fetch("/buyergetdata")
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log(data)
        table(data);
    });
});

function changedata(no,crop,farmid,min_price,max_qty){
    // console.log("hello");
    // console.log(no,crop);
    $("#reference_id").val(no);
    $("#inputcropbuyer").val(crop);
    $("#farmid").val(farmid);
    $("#pricebuyer").attr({
        "min" : min_price
     });
    $("#qtybuyer").attr({
        "max" : max_qty,        // substitute your own
     });


}

$(document).ready(function(){
    fetch("/approvedcrop")
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log(data)
        var htmlstring='<table style="background-color:white;" class="table table-hover  text-center"><thead><tr><th scope="col">ID</th>'+
                                              '<th scope="col">CROP</th>'+
                                              '<th scope="col">PRICE IN WHICH PURCHASED</th>'+
                                              '<th scope="col">CROP QTY CONFIRMED</th>'+
                                              '<th scope="col">PHONE NUMBER</th>'+
                                              '</tr></thead><tbody>'
        
        for (var property in data) {
            // console.log('${property}: ${object[property]}');
            htmlstring+='<tr id="'+data[property]['UNIQUE_ID'] +'">'+
                            '<th scope="row">'+ data[property]['FARM_CROP_ID']+'</th>'+
                            '<td>'+ data[property]['CROP'] +'</td>'+
                            '<td>'+ data[property]['PRICE'] +'</td>'+
                            '<td>'+ data[property]['CROP_QUANTITY'] +'</td>'+
                            '<td>'+ data[property]['PH_NO'] +'</td>'+ 
                                                     
                        '</tr>'
          }
        htmlstring += '</tbody></table>'
        $("#approvedcrop").html(htmlstring);

    });
});

$(document).ready(function(){
    fetch("/for_approval")
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log(data)
        var htmlstring='<table style="background-color:white;" class="table table-hover  text-center"> <thead><tr><th scope="col">ID</th>'+
                                              '<th scope="col">CROP</th>'+
                                              '<th scope="col">PRICE IN WHICH PURCHASED</th>'+
                                              '<th scope="col">CROP QTY</th>'+
                                              '<th scope="col">PHONE NUMBER</th>'+
                                              '</tr></thead><tbody>'
        
        for (var property in data) {
            // console.log('${property}: ${object[property]}');
            htmlstring+='<tr id="'+data[property]['UNIQUE_ID'] +'">'+
                            '<th scope="row">'+ data[property]['FARM_CROP_ID']+'</th>'+
                            '<td>'+ data[property]['CROP'] +'</td>'+
                            '<td>'+ data[property]['PRICE'] +'</td>'+
                            '<td>'+ data[property]['CROP_QUANTITY'] +'</td>'+
                            '<td>'+ data[property]['PH_NO'] +'</td>'+ 
                                                     
                        '</tr>'
          }
        htmlstring += '</tbody></table>'
        $("#for_approval").html(htmlstring);

    });
});
