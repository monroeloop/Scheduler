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
      maxWidth:800,
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
      }
    });

    $( "td[class=mon], td[class=tue], td[class=wed]," +
        "td[class=thu], td[class=fri], td[class=sat], td[class=sun]" ).on( "click", function() {
      $( "#dialog" ).dialog( "open" );
    });
  });

$( function() {
    $( "#columnthree" ).selectable({
        selected: function( event, ui ) {
            console.log($(ui.selected).data('time'))
        }});

  } );
//
// $("#dialog").ready(function() {
//     $( "#rowthree" ).dialog({
//       autoOpen: false,
//       maxWidth: 1000,
//       maxHeight: 1000,
//       width: 500,
//       height: 250,
//       resizable: true,
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
//     $( ".ui-selected" ).on( "click", function() {
//       $( "#columnthree" ).dialog( "open" );
//     });
//   });