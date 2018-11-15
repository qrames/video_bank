

$(document).ready(function() {
     // Stuff to do as soon as the DOM is ready
    $('iframe').each(function(index, el) {
        //YOUTUBE iframe corrector:
        //https://www.youtube.com/watch?v=cTeGOKHS0K0
        // to :
        //"https://www.youtube.com/embed/cTeGOKHS0K0"

        var src = $(this).attr('src');
        var position = src.indexOf("https://www.youtube.com/watch?v=" );
        if (position === 0 ){
            src = src.slice(32);
            console.log(src);
            src = "https://www.youtube.com/embed/" + src;
            $(this).attr('src', src);
        }
    });



    $('#rented').click(function(event) {
        // $("#rended_form").submit();
        // dont work!
    });
});
