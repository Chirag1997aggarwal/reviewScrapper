
$('#showResultBtn').hide();
$('#spin').hide();
process = '<div class="spinner-grow text-info"></div>'


$('#submit').click(function(){
    $('#submit').hide();
    $('#spin').show();

    const data = { productName: $('#productName').val() };
    $.post("/searchReview", data,
        function(data, status){
            data = data['details']
            $('#spin').hide();
            $("#productName").prop('disabled', true);
            $('#showResultBtn').show();
            productList = Object.keys(data);
            for (var i = productList.length - 1; i >= 0; i--) {
                $('#accordion button')[i].innerText = productList[i]
                productData = data[productList[i]]
                alertType = 'success'
                if (parseInt(productData['Over All Rating']) < 3){
                    alertType = 'danger';
                }
                alertStr = '<div class="alert alert-'+alertType+' fade show"> '
                alertStr += '<button type="button" class="close" data-dismiss="alert">&times;</button>'
                alertStr += 'Overall/Average Rating is '+productData["Over All Rating"]+' out of '+productData['Total Reviews & Ratings']
                alertStr += ' </div>';
                $('#accordion .card-body .overview')[i].innerHTML = alertStr;
                for (var j = 0; j < productData['Review List'].length; j++) {
                    // console.log(i, j);
                    colDataList = productData['Review List'][j].map(x=>'<td>'+x+'</td>');
                    row = '<tr>'
                    row += colDataList.reduce((a, b) => a+b)
                    row += '</tr>'
                    // console.log(row);
                    $('#review'+(i+1)+' tbody').append(row);
                }
            }
        }
    );
});
