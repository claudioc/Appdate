var Bot = require('appdate-bot').Bot_Github,
    sprintf = require('util').format
;

var bot = new Bot({
    group: 'Angularjs',
    name: 'Angularjs 1.2.x',
    description: 'The Angular Framework, version 1.2.x',
    website: 'http://angularjs.org/',
    repository: 'https://github.com/angular/angular.js'
});

// Strategy:
//  - get the info from the github release page
//  - find the first 1.2.x version

bot.fetchTags('angular', 'angular.js', /^v\d+\.\d+\.\d+$/)

    .then(function (tags) {

        console.log(tags);

    })

    .then(function (response) {

        //var $rn1 = response.$(sprintf('a:contains("jQuery %s release notes")', bot.get('currentVersion')));

        //bot.set('releaseNotesUrl', $rn1.attr('href'));
    })

    .then(function () {
        bot.end();
    })

    .catch(function (err) {
        bot.abort(err);
    });
