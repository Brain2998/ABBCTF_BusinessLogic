$(document).ready(function() {
    generateEquation()
    $('form').submit(function(e){
        $.ajax({
            async:true,
            type: "POST",
            url: "/",
            data: new FormData($('form')[0]),
            cache: false,
			contentType: false,
            processData: false,
            success: function(result) {
                alert(result)
                generateEquation()
            }
        });
        e.preventDefault();
    });
    function generateEquation() {
        $.ajax({
            async: true,
            type: "GET",
            url: "/generateEquation",
            success: function(image){
                $('#equation').attr('src',"data:image/png;base64,"+image)
            }
        });
    }
});
