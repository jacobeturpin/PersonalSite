// Script to go here

$(function () {
    $('a#twittertest').bind('click', function () {
        $.getJSON('/GetTwitterData', {},
            function (data) {
                console.log('Test')
                $("p#result").text(JSON.stringify(data));
        });
        return false;
    });
});