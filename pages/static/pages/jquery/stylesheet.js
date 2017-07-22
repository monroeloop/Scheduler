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
            // console.log($(ui.selected).data('time'));
        }
    });

    function createChildDialog(starttime, endtime) {
        console.log(starttime)
        console.log(endtime)
        $('#childDialog').dialog({
            autoOpen: false,
            maxWidth: 700,
            maxHeight: 600,
            height: 500,
            width: 550,
            resizable: true,
            modal: false
        });
    }

    // $(".rowthree").on("click", function () {
    //     $("#childDialog").dialog("open");
    // });
    var day;
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
                    var selectedlist = $(".ui-selected");
                    var starttime = $(selectedlist[0]).data("time").split(':');
                    if (day.toString().length < 2) {
                        day = '0' + day
                    }
                    console.log($('#yearHidden').text())
                    console.log($('#monthHidden').text())
                    // console.log(day)
                    var starttime = new Date($('#yearHidden').text(), $('#monthHidden').text() - 1, day, starttime[0], starttime[1])
                    //
                    // console.log(date);
                    // var endtime = parseInt($(selectedlist[selectedlist.length - 1]).data("time")) + 15
                    // var checkendtime = endtime.toString().split("");
                    // if (checkendtime.slice(2,3)[0]==="6"){
                    //     checkendtime[0] = parseInt(checkendtime[0]) + 1
                    //     checkendtime[2] = "0"
                    // }
                    // endtime = parseInt(checkendtime.join(""));
                    //
                    // createChildDialog(starttime,endtime);
                    $("#childDialog").dialog("open");
                    // console.log($(".ui-selected"))
                }
            }
        });

        var weekdays = "td[class=mon], td[class=tue], td[class=wed], td[class=thu], td[class=fri], td[class=sat], td[class=sun]";
        $(weekdays).on("click", function () {
            day = $(this).text()
            $("#dialog").dialog("open");
        });
    }


    createChildDialog();
    createParentDialog();

});