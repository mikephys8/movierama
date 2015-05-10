$(document).ready(function () {
    var order;
    console.log('content loaded');
    var like_button = $('#like');
    var hate_button = $('#hate');

    $('.like').click(function (e) {
        action_calls.action(e.target.id, 0)
            .done(function (res) {
                document.location.reload(true);
                //document.getElementById('like'+e.target.id).style.display = 'none';
                //document.getElementById('hate'+e.target.id).style.display = 'none';
                //document.getElementById('unlike'+e.target.id).style.display = '';
                console.log(res);
                // Reload the current page, without using the cache
                //document.location.reload(true);
            });
    });
    $('.hate').click(function (e) {
        action_calls.action(e.target.id, 1)
            .done(function (res) {
                document.location.reload(true);
                //document.getElementById('hate'+e.target.id).style.display = 'none';
                //document.getElementById('like'+e.target.id).style.display = 'none';
                //document.getElementById('unhate'+e.target.id).style.display = '';
                console.log(res);
                // Reload the current page, without using the cache
                //document.location.reload(true);
            });
    });
    $('.undo').click(function (e) {
        console.log(e.target.id);
        action_calls.deleteAction(e.target.id)
            .done(function (res) {
                document.location.reload(true);
                //document.getElementById('hate'+e.target.id).style.display = '';
                //document.getElementById('like'+e.target.id).style.display = '';
                //document.getElementById('unhate'+e.target.id).style.display = 'none';
                //document.getElementById('unlike'+e.target.id).style.display = 'none';
                console.log(res);
                // Reload the current page, without using the cache
                //document.location.reload(true);
            });
    });
    $('#sortByLikes').click(function (e) {
        e.preventDefault();
        tinysort('#movielist>div', { selector:'.movie_likes' });
        tinysort.defaults.order = tinysort.defaults.order == 'asc'? 'desc' : 'asc';
        console.log('epe3e');
    });
    $('#sortByHates').click(function (e) {
        e.preventDefault();
        tinysort('#movielist>div', { selector:'.movie_hates' });
        tinysort.defaults.order = tinysort.defaults.order == 'asc'? 'desc' : 'asc';
        console.log('epe3e');
    });
    $('#sortByDate').click(function (e) {
        e.preventDefault();
        tinysort('#movielist>div', { selector:'.movie_date' });
        tinysort.defaults.order = tinysort.defaults.order == 'asc'? 'desc' : 'asc';
        console.log('epe3e');
    })
});