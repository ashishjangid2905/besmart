$(document).ready(function () {
    $(".tab_head").click(function () {
        if ($(this).next().hasClass('expand')) {
            $(this).next().removeClass('expand');
        } 
        
        else if($(this).next().siblings().hasClass('expand')) {
            $(this).next().siblings().removeClass('expand');
            $(this).next().addClass('expand');
        }
        
        else {
            $(this).next().addClass('expand');
        }
    });
});
