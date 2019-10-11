$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "http://localhost:5000/state",
        crossDomain: true,
        success: function(result){
            changeLook(result.heating);
            $("body").show();
            console.log(result);
        } 
    })
    
    $("#checkbox").change(function() {
        changeLook(this.checked);
        console.log(this.checked);
        $.ajax({
            type: "POST",
            url: "http://localhost:5000/state",
            crossDomain: true,
            data: JSON.stringify({"heating": this.checked}),
            contentType: 'application/json',
            success: function(result){}
        })
    })
})

function changeLook(state) {
    if (state === false) {
        $("#emoji").html("❄");
        $("body").animate({backgroundColor: "#1E90FF"}); //dodgerblue
        $("#checkbox").prop("checked", false);
    } else if (state === true) {
        $("#emoji").html("🔥");
        $("body").animate({backgroundColor: "#FF7F50"}); //coral
        $("#checkbox").prop("checked", true);
    }
}