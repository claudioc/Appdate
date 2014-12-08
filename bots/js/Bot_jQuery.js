var Bot = require('./Bot'),
    sprintf = require('util').format
;

var results = {
    currentVersion: '',
    releaseNotesUrl: '',
    releaseDate: '',
    downloadUrl: ''
};

Bot.open('https://github.com/jquery/jquery/releases')

    .then(function (response) {

        var $tags = response.$('.release-timeline-tags > li');

        var $r1 = $tags.eq(0);
        var $r2 = $tags.eq(1);

        results.releaseDate = $r1.find('time').attr('datetime');
        results.currentVersion = $r1.find('h3 > a > .tag-name').text();
        results.downloadUrl = sprintf('http://code.jquery.com/jquery-%s.js', results.currentVersion);
        results.downloadPage = "http://jquery.com/download/";

        /* Version 2 */
        // console.log($r2.find('time').attr('datetime'));
        // console.log($r2.find('h3 > a > .tag-name').text());
        // console.log($r2.find('h3 > a').attr('href'));

        return Bot.open('http://jquery.com/download/');
    })

    .then(function (response) {

        var $rn1 = response.$(sprintf('a:contains("jQuery %s release notes")', results.currentVersion));

        results.releaseNotesUrl = $rn1.attr('href');
    })

    .then(function () {
        console.log(results);
    })

    .catch(function (err) {
        console.log(err);
    });
