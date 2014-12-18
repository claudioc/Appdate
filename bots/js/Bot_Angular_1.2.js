
var appdateBot = require('appdate-bot');

var Bot = appdateBot.Bot_Github,
    utils = appdateBot.utils,
    sprintf = require('util').format,
    _ = appdateBot.lodash;

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

//bot.fetchTags('angular', 'angular.js', /^v(1\.2\.\d+)$/)
bot.fetchTags('angular', 'angular.js', /^v(\d+\.\d+\.\d+)$/)

    .then(function (tags) {
        
        // Find the biggest version among the returned ones
        var max = utils.maxVersion(_.pluck(tags, 'tag'), '1.2.x');

        // Select the data for the highest version
        var latest = _.find(tags, { tag: max });

        bot.set('currentVersion', latest.tag);
        bot.set('releaseDate', latest.date);
    })

    .then(function () {
        bot.end();
    })

    .catch(function (err) {
        bot.abort(err);
    });
