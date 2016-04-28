// Script to go here

$(function () {
    $('a#twitter').bind('click', function () {
        $.getJSON('/GetTwitterData', {},
            function (data) {
            $("#result").text(data.result);
        });
        return false;
    });
});