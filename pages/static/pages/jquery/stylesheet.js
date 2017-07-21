/**
 * Created by adria on 7/10/2017.
 */

$(document).ready(function () {
    // ready func

    $(".menubutton").click(function () {
        $("#bar1").slideDown("750");
        $("#bar2").fadeToggle("500");
        $("#bar3").fadeToggle("500");
        $("#panel1").slideToggle("750");
        $("#panel2").slideToggle("750");
        $("#panel3").slideToggle("750");
    });


    // $(document).ready(function() {
    //     $( "#dialog" ).dialog({
    //       autoOpen: false,
    //       maxWidth:800,
    //       maxHeight: 2000,
    //       width: 500,
    //       height: 700,
    //       resizable: true,
    //       stack: true,
    //       show: {
    //         effect: "blind",
    //         duration: 800
    //       },
    //       hide: {
    //         effect: "fade",
    //         duration: 800
    //       }
    //     });
    //
    //     $( "td[class=mon], td[class=tue], td[class=wed]," +
    //         "td[class=thu], td[class=fri], td[class=sat], td[class=sun]" ).on( "click", function() {
    //       $( "#dialog" ).dialog( "open" );
    //     });
    //   });

    $("#columnthree").selectable({
        selected: function (event, ui) {
            console.log($(ui.selected).data('time'));
        }
    });

    function createChildDialog() {
        $('#childDialog').dialog({
            autoOpen: false,
            maxWidth: 500,
            maxHeight: 600,
            height: 500,
            width: 400,
            resizable: true,
            modal: false
        });
    }

    // $(".rowthree").on("click", function () {
    //     $("#childDialog").dialog("open");
    // });

    function createParentDialog() {

        $('#dialog').dialog({
            autoOpen: false,
            maxWidth: 800,
            maxHeight: 2000,
            width: 500,
            height: 700,
            resizable: true,
            stack: true,
            show: {
                effect: "blind",
                duration: 800
            },
            hide: {
                effect: "fade",
                duration: 800
            },
                buttons: {
                    "Close": function () {
                        $(this).dialog("close");
                    },
                    "Select Times": function () {
                        createChildDialog();
                        $("#childDialog").dialog("open");
                    }
                }
            });

            var weekdays = "td[class=mon], td[class=tue], td[class=wed], td[class=thu], td[class=fri], td[class=sat], td[class=sun]";
            $(weekdays).on("click", function () {
                $("#dialog").dialog("open");
            });
    }


    createChildDialog();
    createParentDialog();

});