const trends = require('google-trends-api');
const Promise = require('bluebird');
const fs = Promise.promisifyAll(require('fs'));

const words = process.argv.slice(2);
const file = words[0] + '.json';

trends.interestOverTime({ keyword: words })
	.then(results => {
		return fs.writeFile(file, results.trim());
	})
	.then(() => {
		console.log(file);
	})
	.catch(error => {
		console.error('Error:', error);
	});