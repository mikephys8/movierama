(function (window) {
    var host = '/movierama_app/api/action/';
    var calls = {
        action: function (movie_id, action_id) {
           return $.get(host + movie_id + '/' + action_id)
        },
        deleteAction: function (movie_id) {
            return $.get(host + 'delete/' + movie_id)
        }
    };
    window.action_calls = calls
})(window);