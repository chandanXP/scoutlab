$(document).ready(function() {
    $('.page-count').text("1");
    let p = parseInt( $('.page-count').text() );
    if(p==1){
        $('.previous').hide();
    }

    $('.next').click(function() {
        console.log('next click!');
        //to increase the value of page-count on click
        var i = parseInt( $('.page-count').text() );
        i = i + 1;
        $('.page-count').text(i);
        console.log(i)

        $.ajax({
            url: '',
            type: 'GET',
            contentType: 'application/json',
            data: {button_value: $('.page-count').text()},
            success: function(response) {
                if(i == 7){
                    $('.next').hide();
                }else{
                    $('.next').show();
                }
                if(i>1){$('.previous').show();}
            }
        })
    })

    $('.previous').click(function() {
        console.log('previous click!');
        //to decrease the value of page-count on click
        var i = parseInt( $('.page-count').text() );
        i = i - 1;
        $('.page-count').text(i);
        console.log(i)
        $.ajax({
            url: '',
            type: 'GET',
            contentType: 'application/json',
            data: {button_value: $('.page-count').text()},
            success: function(response) {
                if(i == 1){
                    $('.previous').hide();
                }else{
                    $('.previous').show();
                }
                if(i<8){$('.next').show();}
            }
        })
    })
})







