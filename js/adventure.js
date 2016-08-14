var Adventures = {};
//currentAdventure is used for the adventure we're currently on (id). This should be determined at the beginning of the program
Adventures.currentAdventure = 0; //todo keep track from db
//currentStep is used for the step we're currently on (id). This should be determined at every crossroad, depending on what the user chose
Adventures.currentStep = 0;//todo keep track from db
Adventures.currentUser = 0;//todo keep track from db


//TODO: remove for production
Adventures.debugMode = true;
Adventures.DEFAULT_IMG = "./images/choice.jpg";


//Handle Ajax Error, animation error and speech support
Adventures.bindErrorHandlers = function () {
    //Handle ajax error, if the server is not found or experienced an error
    $(document).ajaxError(function (event, jqxhr, settings, thrownError) {
        Adventures.handleServerError(thrownError);
    });

    //Making sure that we don't receive an animation that does not exist
    $("#situation-image").error(function () {
        Adventures.debugPrint("Failed to load img: " + $("#situation-image").attr("src"));
        Adventures.setImage(Adventures.DEFAULT_IMG);
    });
};


//The core function of the app, sends the user's choice and then parses the results to the server and handling the response
Adventures.chooseOption = function(){
    var self = $(this);
    Adventures.currentStep = self.val();
    console.log($(this));
    $.ajax("/story",{
        type: "POST",
        data: {
            "user": Adventures.currentUser,
            "adventure": Adventures.currentAdventure,
            "next": Adventures.currentStep,
            "energy_change" : self.attr('energy_change'),
            "bodytemp_change": self.attr('bodytemp_change')
        },
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
            $(".greeting-text").hide();
            console.log(data);
            console.log('data');
            Adventures.write(data);
            Adventures.setEnergy(data["energy_total"]);
            Adventures.setBodyTemp(data["bodytemp_total"]);
        }
    });
};

Adventures.setEnergy = function(energy_total){
        if (energy_total== undefined){
        energy_total = 100;
    }
    $(".user-energy").text("Total Energy: "+ energy_total);
    console.log('sup');
}

Adventures.setBodyTemp = function(bodytemp_total){
    if (bodytemp_total == undefined){
        bodytemp_total = 100;
    }
    $(".user-bodytemperature").text("Total Body Temperature: "+bodytemp_total);
    console.log('dude');
}

Adventures.write = function (message) {
    //Writing new choices and image to screen
    $(".situation-text").text(message["text"]).show();
    for(var i=0;i<message['options'].length;i++){
        var opt = $("#option_" + (i+1));
        opt.text(message['options'][i]['text_ans']);
        opt.prop("value", message['options'][i]['next_q']);
        opt.attr('energy_change',message['options'][i]['energy_change'] );
        opt.attr('bodytemp_change',message['options'][i]['bodytemp_change'] );
    }
    Adventures.setImage(message["image"]);
    Adventures.setEnergy(message['energy_total']);
    Adventures.setBodyTemp(message["bodytemp_total"]);
};


Adventures.start = function(){
    $(document).ready(function () {
        $(".game-option").click(Adventures.chooseOption);
        $("#nameField").keyup(Adventures.checkName);
        $(".adventure-button").click(Adventures.initAdventure);
        $(".adventure").hide();
        $(".welcome-screen").show();
    });
};

//Setting the relevant image according to the server response
Adventures.setImage = function (img_name) {
    $("#situation-image").attr("src", "./images/" + img_name);
};

Adventures.checkName = function(){
    if($(this).val() !== undefined && $(this).val() !== null && $(this).val() !== ""){
        $(".adventure-button").prop("disabled", false);
    }
    else{
        $(".adventure-button").prop("disabled", true);
    }
};


Adventures.initAdventure = function(){

    $.ajax("/start",{
        type: "POST",
        data: {
            "user": $("#nameField").val(),
            "adventure_id": $(this).val()
        },
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
            Adventures.write(data);
            $(".adventure").show();
            $(".welcome-screen").hide();
            Adventures.currentAdventure = data['adventure'];
            Adventures.currentStep = data['current'];
            Adventures.currentUser = data['user'];

        }
    });
};

Adventures.handleServerError = function (errorThrown) {
    Adventures.debugPrint("Server Error: " + errorThrown);
    var actualError = "";
    if (Adventures.debugMode) {
        actualError = " ( " + errorThrown + " ) ";
    }
    Adventures.write("Sorry, there seems to be an error on the server. Let's talk later. " + actualError);

};

Adventures.debugPrint = function (msg) {
    if (Adventures.debugMode) {
        console.log("Adventures DEBUG: " + msg)
    }
};

Adventures.start();

