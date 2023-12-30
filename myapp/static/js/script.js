$(document).ready(function () {
    $(".tab_head").click(function () {
        var col = $('.tab_head').length;
        var active = $(this);
        var t = active.length
        var b;
        active.next().toggleClass('expand');
        console.log(col);
        console.log(t);

        for (let i = 0; i < col.length; i++) {
            b = i;
        }
        console.log(b);
    });
});
