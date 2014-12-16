var Bot = require('appdate-bot').Bot,
    sprintf = require('util').format
;

var bot = new Bot({
    group: 'jQuery',
    name: 'jQuery 1.x',
    description: 'The jQuery library, version 1.x',
    website: 'http://www.jquery.com/',
    repository: 'https://github.com/jquery/jquery'
});

bot.fetch('https://github.com/jquery/jquery/releases')

    .then(function (response) {

        var $tags = response.$('.release-timeline-tags > li');

        var $r1 = $tags.eq(0);

        bot.set('releaseDate', $r1.find('time').attr('datetime'));
        bot.set('currentVersion', $r1.find('h3 > a > .tag-name').text());
        bot.set('downloadUrl', sprintf('http://code.jquery.com/jquery-%s.js', bot.get('currentVersion')));
        bot.set('downloadPage', 'http://jquery.com/download/');

        return bot.open('http://jquery.com/download/');
    })

    .then(function (response) {

        var $rn1 = response.$(sprintf('a:contains("jQuery %s release notes")', bot.get('currentVersion')));

        bot.set('releaseNotesUrl', $rn1.attr('href'));
    })

    .then(function () {
        bot.end();
    })

    .catch(function (err) {
        bot.abort(err);
    });
