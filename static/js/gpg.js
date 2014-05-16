;(function() {
    var $pages = $('.page');
    var pages = {};
    var hashes = ['home', 'about', 'playing_the_game', 'current_playing', 'cards', 'contact', 'links'];
    var all_pages = hashes;
    var nav = $('.navbar li');
    var nav_collapse = $('.navbar-collapse');
    var error_page = $('#error');
    var error = $('.error', error_page);
    $.map(all_pages, function(hash) { pages[hash] = $('#' + hash); });
     
    var routing = Davis(function() {
        var self = this;
        $.map(_.union([''], hashes), function(page) {
            self.get('/' + page, function() {
                if (page == '')
                    page = 'home';
                set_page(page);
            });
        });
    });
    routing.configure(function(config) {
        config.linkSelector = 'a[class!=picture]';
        config.formSelector = '_form';
    })
    routing.start();
    var noop = function() {};
    //routing.logger = { info: noop, warning: noop, error: noop };
})();