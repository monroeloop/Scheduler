/**
 * Created by adria on 7/10/2017.
 */

$(document).ready(function () {
    $(".menubutton").click(function () {
        $("#bar1").slideDown("750");
        $("#bar2").fadeToggle("500");
        $("#bar3").fadeToggle("500");
        $("#panel1").slideToggle("750");
        $("#panel2").slideToggle("750");
        $("#panel3").slideToggle("750");
    });
});

$(document).ready(function() {
    $( "#dialog" ).dialog({
      autoOpen: false,
      show: {
        effect: "blind",
        duration: 1000
      },
      hide: {
        effect: "fade",
        duration: 1000
      }
    });

    $( ".rowone" ).on( "click", function() {
      $( "#dialog" ).dialog( "open" );
    });
  });