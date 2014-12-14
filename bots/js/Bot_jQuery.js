var Bot = require('appdate-bot').Bot,
    sprintf = require('util').format
;

var bot = new Bot();

bot.open('https://github.com/jquery/jquery/releases')

    .then(function (response) {

        var $tags = response.$('.release-timeline-tags > li');

        var $r1 = $tags.eq(0);
        var $r2 = $tags.eq(1);

        bot.set('releaseDate', $r1.find('time').attr('datetime'));
        bot.set('currentVersion', $r1.find('h3 > a > .tag-name').text());
        bot.set('downloadUrl', sprintf('http://code.jquery.com/jquery-%s.js', bot.get('currentVersion')));
        bot.set('downloadPage', 'http://jquery.com/download/');

        /* Version 2 */
        // console.log($r2.find('time').attr('datetime'));
        // console.log($r2.find('h3 > a > .tag-name').text());
        // console.log($r2.find('h3 > a').attr('href'));

        return bot.open('http://jquery.com/download/');
    })

    .then(function (response) {

        var $rn1 = response.$(sprintf('a:contains("jQuery %s release notes")', bot.get('currentVersion')));

        bot.set('releaseNotesUrl', $rn1.attr('href'));
    })

    .then(function () {
        console.log(bot.results);
    })

    .catch(function (err) {
        console.log(err);
    });
