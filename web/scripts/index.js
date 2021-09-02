const sendLoadDialog = async function() {
    let value = await eel.getWordFile()()
    return value
}

const renderFields = function(fieldsArray){

    if(fieldsArray.length<1){
        alert("Select a file with mergefields")
        return
    }

    $("#formFields").html("")

    $.each(fieldsArray, function( index, value ) {
        let inputField = `<input class="form-control my-1" type="text" placeholder="${value}" required/>` 
        $("#formFields").append(inputField);
    });

}

const sendWordProcess = async function(fileName) {
    let value = await eel.processWordFile(fileName)()
    renderFields(value)
}

const sendGenerateFile = async function(fileName,data,outputFile) {
    await eel.generateWordFile(fileName,data,outputFile)()
    alert("File Created Successfully!")
}

$(document).ready(function(){

    //window.resizeTo(400,800);

    $("#formWordFile").click(function(){
        let rvalue = sendLoadDialog()
        rvalue.then((a) => {
            if(a!="")
                $("#inputWordFile").val(a)
            else{
                alert("Select a doc file!")
                $("#formFields").html("")
                $("#inputWordFile").val("")
            }
        });
    })

    $("#processWordFile").click(function(){
        if($("#inputWordFile").val()!="")
            sendWordProcess($("#inputWordFile").val())
        else{
            alert("Select a doc file!")
        }
    })

    $("#generateFileForm").submit(function(){

        if($( "div#formFields > input.form-control.my-1" ).length < 1){
            alert("Process a word file!")
            return
        }

        let data = {}

        $( "div#formFields > input.form-control.my-1" ).each(function() {
            data[$(this).attr("placeholder")]=$(this).val()
        });

        sendGenerateFile($("#inputWordFile").val(),data,$("#outputFileName").val())

    })

   
    $("#resetWordFile").click(function(){
        location.reload();
    })
    
});