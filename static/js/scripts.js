$(document).ready(function() {
    generateEquation()
    var taskNumber=0
    $('form').submit(function(e){
        var formData=new FormData($('form')[0])
        formData.set('taskNumber',taskNumber)
        $.ajax({
            async:true,
            type: "POST",
            url: "/",
            data: formData,
            cache: false,
			contentType: false,
            processData: false,
            success: function(result) {
                var resultJSON=JSON.parse(result)
                if (resultJSON.hasOwnProperty('flag')){
                    alert('Congratulations! Flag is'+ resultJSON.flag)
                }
                else{
                    taskNumber=10000-parseInt(resultJSON.tasksToSolve)
                    alert(`${resultJSON.result? 'Right': 'Wrong'}! Need to solve ${resultJSON.tasksToSolve} more tasks.`)
                    generateEquation()
                }
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
