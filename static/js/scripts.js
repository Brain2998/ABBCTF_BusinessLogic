$(document).ready(function() {
    generateEquation()
    var taskNumber=0
    $('form').submit(async function(e){
        e.preventDefault();
        var formData=new FormData($('form')[0])
        formData.set('taskNumber',taskNumber)
        var urlFormData=new URLSearchParams(formData).toString();
        var encoder=new TextEncoder();
        var encodedData=encoder.encode(urlFormData)
        var bitArray=sjcl.hash.sha256.hash(urlFormData)
        var hash=sjcl.codec.hex.fromBits(bitArray)
        urlFormData+='&checkSum='+hash
        $.ajax({
            async:true,
            type: "POST",
            url: "/",
            data: btoa(urlFormData),
            cache: false,
			contentType: false,
            processData: false,
            success: function(result) {
                var resultJSON=JSON.parse(result)
                if (resultJSON.hasOwnProperty('flag')){
                    alert('Congratulations! Flag is '+ resultJSON.flag)
                }
                else{
                    taskNumber=10000-parseInt(resultJSON.tasksToSolve)
                    alert(`${resultJSON.result? 'Right': 'Wrong'}! Need to solve ${resultJSON.tasksToSolve} more tasks.`)
                    generateEquation()
                }
            },
            error: function(err){
                alert(`ajax err: ${JSON.stringify(err,null,2)}`);
            }
        });
        
    });
    function generateEquation() {
        $.ajax({
            async: true,
            type: "GET",
            url: "/generateEquation",
            success: function(image){
                $('#equation').attr('src',"data:image/png;base64,"+image)
            },
            error: function(err){
                alert(`ajax err: ${JSON.stringify(err,null,2)}`);
            }
        });
    }
});
